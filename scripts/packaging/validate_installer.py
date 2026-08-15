#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Self-test for make_windows_installer.py that needs no Windows build.

Compiling Mixar for Windows needs MSVC, tens of GB of Blender libraries and
hours of CPU. Packaging is ordinary file work plus one call to makensis - and
makensis has a native POSIX build. So the packaging step can be exercised on
any machine against a throwaway payload that mimics ``build/<env>/bin``:

    python3 scripts/packaging/validate_installer.py              # logic only
    python3 scripts/packaging/validate_installer.py --with-nsis   # + compile the .nsi

``--with-nsis`` is the cheap way to catch a syntax error in
installer/windows/mixar.nsi, minutes instead of a six-hour build. Install NSIS
with ``sudo apt-get install nsis`` (Debian/Ubuntu), ``brew install makensis``
(macOS) or ``choco install nsis`` (Windows).

The installer produced here is real but wraps a stub executable: it proves the
script compiles and the safety checks fire, never that Mixar runs.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
PACKAGER = HERE / "make_windows_installer.py"
REPO_ROOT = HERE.parents[1]

STUB_VERSION = "9.9.9"
RESOURCE_DIR = "5.2"

# The files this fork adds to the bundle. Keep in sync with OVERLAY_MARKERS in
# make_windows_installer.py: the packager refuses to package a tree that is
# missing them, and the stub payload below has to look like a real overlay.
OVERLAY_FILES = (
    "scripts/mixar/modules/byok/core/base_url.py",
    "scripts/mixar/modules/byok/ui/operators/byok_base_url_ops.py",
)

PASSES: list[str] = []
FAILURES: list[str] = []
SKIPS: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    if ok:
        PASSES.append(name)
        print(f"  PASS  {name}")
    else:
        FAILURES.append(name)
        print(f"  FAIL  {name}" + (f"\n        {detail}" if detail else ""))


def skip(name: str, why: str) -> None:
    SKIPS.append(name)
    print(f"  SKIP  {name} ({why})")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def make_payload(
    root: Path,
    *,
    env: str = "Prod",
    resource: str = RESOURCE_DIR,
    dev_bypass: bool = False,
    overlay: bool = True,
    exe: bool = True,
) -> Path:
    """Create a fake build/<env> tree. Returns that directory."""
    build_env = root / "build" / env
    payload = build_env / "bin"
    if exe:
        write(payload / "mixar.exe", "MZ stub executable\n")
    # Build leftovers that must never reach an artifact.
    write(payload / "mixar.pdb", "debug symbols\n")
    write(payload / "CMakeFiles" / "junk.txt", "cmake noise\n")

    resources = payload / resource
    config = {
        "environment": env,
        "log_level": "INFO",
        "backend_url": "https://api.mixar.app",
        "frontend_url": "https://www.mixar.app",
        "app_info": {"version": STUB_VERSION},
    }
    if dev_bypass:
        config["dev_bypass"] = {"email": "dev@example.com", "password": "hunter2"}
    write(resources / "config" / "mixar.json", json.dumps(config, indent=2))
    write(resources / "datafiles" / "fonts" / "stub.ttf", "font\n")
    write(resources / "scripts" / "mixar" / "__pycache__" / "stub.pyc", "bytecode\n")
    if overlay:
        for rel in OVERLAY_FILES:
            write(resources / rel, "# stub module\n")
    return build_env


def clean_env() -> dict[str, str]:
    env = {k: v for k, v in os.environ.items() if not k.startswith("MIXAR_")}
    env["BLENDER_VERSION"] = RESOURCE_DIR
    return env


def run_packager(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(PACKAGER), *args],
        capture_output=True,
        text=True,
        env=clean_env(),
        cwd=str(REPO_ROOT),
    )


def zip_names(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as archive:
        return archive.namelist()


def case_happy_path(root: Path) -> None:
    print("\n[1] a normal Prod tree produces a portable zip")
    build_env = make_payload(root)
    out = root / "dist-happy"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--blender-version", RESOURCE_DIR, "--no-installer",
    )
    check("exit code 0", result.returncode == 0, result.stderr.strip())
    archive = out / f"Mixar-{STUB_VERSION}-windows-x64.zip"
    check("portable zip written", archive.is_file(), f"missing {archive}")
    if archive.is_file():
        names = zip_names(archive)
        top = f"Mixar-{STUB_VERSION}-windows-x64"
        check("zip has a single top-level dir", all(n.startswith(f"{top}/") for n in names))
        check("executable inside zip", f"{top}/mixar.exe" in names)
        check("resource dir inside zip", f"{top}/{RESOURCE_DIR}/config/mixar.json" in names)
        check(".pdb excluded", not any(n.endswith(".pdb") for n in names))
        check("__pycache__ excluded", not any("__pycache__" in n for n in names))
        check("CMakeFiles excluded", not any("CMakeFiles" in n for n in names))
    sums = out / "SHA256SUMS.txt"
    check("SHA256SUMS written", sums.is_file())
    if sums.is_file():
        lines = [line for line in sums.read_text(encoding="utf-8").splitlines() if line.strip()]
        check("SHA256SUMS has one entry", len(lines) == 1, repr(lines))
        check("SHA256SUMS hash length", bool(lines) and len(lines[0].split()[0]) == 64)
    check("reports the overlay modules", "BYOK base URL modules present" in result.stdout)


def case_dev_bypass(root: Path) -> None:
    print("\n[2] a bundle carrying dev_bypass credentials is refused")
    build_env = make_payload(root, env="Dev", dev_bypass=True)
    result = run_packager(
        "--env", "Dev", "--build-dir", str(build_env), "--out-dir", str(root / "dist-dev"),
        "--version", STUB_VERSION, "--no-installer",
    )
    check("non-zero exit", result.returncode != 0)
    check("explains why", "dev_bypass" in result.stderr)
    check("nothing written", not (root / "dist-dev" / f"Mixar-{STUB_VERSION}-windows-x64-dev.zip").exists())


def case_missing_overlay(root: Path) -> None:
    print("\n[3] a vanilla bundle without this fork's modules is refused")
    build_env = make_payload(root, overlay=False)
    out = root / "dist-vanilla"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--no-installer",
    )
    check("non-zero exit", result.returncode != 0)
    check("names the missing files", "base_url.py" in result.stderr)
    forced = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--no-installer", "--skip-overlay-check",
    )
    check("--skip-overlay-check overrides it", forced.returncode == 0, forced.stderr.strip())


def case_no_build(root: Path) -> None:
    print("\n[4] no built tree at all fails with a useful message")
    build_env = make_payload(root, exe=False)
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(root / "dist-none"),
        "--version", STUB_VERSION, "--no-installer",
    )
    check("non-zero exit", result.returncode != 0)
    check("points at build.bat", "build.bat" in result.stderr)


def case_resource_mismatch(root: Path) -> None:
    print("\n[5] a resource dir from another Blender version warns, does not crash")
    build_env = make_payload(root, resource="5.1")
    out = root / "dist-mismatch"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--blender-version", "5.2", "--no-installer",
    )
    check("exit code 0", result.returncode == 0, result.stderr.strip())
    check("warns about the version", "expected resource dir '5.2'" in result.stdout)


def case_naming(root: Path) -> None:
    print("\n[6] env and commit suffix land in the artifact name")
    build_env = make_payload(root, env="UAT")
    out = root / "dist-uat"
    result = run_packager(
        "--env", "UAT", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--suffix", "abc1234", "--no-installer",
    )
    check("exit code 0", result.returncode == 0, result.stderr.strip())
    expected = out / f"Mixar-{STUB_VERSION}-windows-x64-uat-abc1234.zip"
    check("name carries env + suffix", expected.is_file(), f"missing {expected.name}")


def case_version_file(root: Path) -> None:
    print("\n[7] without --version the repo VERSION file is used")
    version_file = REPO_ROOT / "VERSION"
    if not version_file.is_file():
        skip("VERSION fallback", "no VERSION file in the repo")
        return
    version = version_file.read_text(encoding="utf-8").strip()
    build_env = make_payload(root)
    out = root / "dist-version"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out), "--no-installer",
    )
    check("exit code 0", result.returncode == 0, result.stderr.strip())
    check(f"artifact named after VERSION ({version})",
          (out / f"Mixar-{version}-windows-x64.zip").is_file(),
          f"got {[p.name for p in out.glob('*.zip')]}")


def case_nothing_to_do(root: Path) -> None:
    print("\n[8] --no-zip --no-installer refuses to be a no-op")
    build_env = make_payload(root)
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(root / "dist-noop"),
        "--version", STUB_VERSION, "--no-zip", "--no-installer",
    )
    check("non-zero exit", result.returncode != 0)
    check("says nothing was produced", "nothing was produced" in result.stderr)


def case_missing_nsis_flag(root: Path) -> None:
    print("\n[9] a missing makensis is fatal unless explicitly allowed")
    build_env = make_payload(root)
    out = root / "dist-nonsis"
    # Point at a stub script so this case exercises the makensis lookup rather
    # than the presence of installer/windows/mixar.nsi.
    stub_nsi = root / "stub.nsi"
    write(stub_nsi, "; contents are irrelevant: makensis is missing on purpose\n")
    missing = str(root / "nope" / "makensis")
    fatal = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--nsi", str(stub_nsi), "--makensis", missing,
    )
    check("non-zero exit without NSIS", fatal.returncode != 0)
    check("tells you how to install it", "apt-get install nsis" in fatal.stderr, fatal.stderr.strip())
    tolerated = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--nsi", str(stub_nsi), "--makensis", missing,
        "--allow-missing-nsis",
    )
    check("--allow-missing-nsis keeps the zip", tolerated.returncode == 0, tolerated.stderr.strip())


def case_backend_url(root: Path) -> None:
    print("\n[10] --backend-url regenerates the bundled config")
    generator = REPO_ROOT / "scripts" / "generate_config.py"
    if not generator.is_file():
        skip("--backend-url", "scripts/generate_config.py not present")
        return
    build_env = make_payload(root)
    out = root / "dist-backend"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--no-installer",
        "--backend-url", "https://api.self-hosted.example",
    )
    check("exit code 0", result.returncode == 0, result.stderr.strip())
    config_path = build_env / "bin" / RESOURCE_DIR / "config" / "mixar.json"
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        check("config still valid json", False, str(exc))
        return
    check("backend_url replaced", data.get("backend_url") == "https://api.self-hosted.example",
          repr(data.get("backend_url")))
    check("no dev_bypass leaked in", "dev_bypass" not in data)


def case_nsis(root: Path, keep: Path | None) -> None:
    print("\n[11] makensis compiles installer/windows/mixar.nsi")
    makensis = shutil.which("makensis")
    if not makensis:
        skip("makensis run", "makensis not on PATH; install NSIS to enable")
        return
    nsi = REPO_ROOT / "installer" / "windows" / "mixar.nsi"
    if not nsi.is_file():
        check("mixar.nsi present", False, f"missing {nsi}")
        return
    build_env = make_payload(root)
    out = keep if keep else root / "dist-nsis"
    result = run_packager(
        "--env", "Prod", "--build-dir", str(build_env), "--out-dir", str(out),
        "--version", STUB_VERSION, "--blender-version", RESOURCE_DIR,
        "--makensis", makensis,
    )
    check("exit code 0", result.returncode == 0, (result.stdout + result.stderr).strip()[-2000:])
    installer = out / f"Mixar-{STUB_VERSION}-windows-x64-setup.exe"
    check("installer written", installer.is_file(), f"missing {installer}")
    if installer.is_file():
        size = installer.stat().st_size
        check("installer is not empty", size > 20_000, f"{size} bytes")
        with installer.open("rb") as handle:
            check("installer is a PE binary", handle.read(2) == b"MZ")
    sums = out / "SHA256SUMS.txt"
    if sums.is_file():
        lines = [line for line in sums.read_text(encoding="utf-8").splitlines() if line.strip()]
        check("SHA256SUMS covers zip + installer", len(lines) == 2, repr(lines))


def load_packager_module():
    spec = importlib.util.spec_from_file_location("mixar_packager", PACKAGER)
    if not spec or not spec.loader:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def case_helpers() -> None:
    print("\n[0] version and command-line helpers")
    module = load_packager_module()
    if module is None:
        check("packager importable", False, "could not load the module")
        return
    check("packager importable", True)
    check("four_part_version pads X.Y.Z", module.four_part_version("2.0.0") == "2.0.0.0")
    check("four_part_version pads X.Y", module.four_part_version("2.0") == "2.0.0.0")
    check("four_part_version ignores text", module.four_part_version("v2.1.3-rc4") == "2.1.3.4")
    check("four_part_version truncates", module.four_part_version("1.2.3.4.5") == "1.2.3.4")
    # The two lists that have to agree, or a real package aborts on a bundle
    # that is in fact correct.
    check("marker lists agree",
          tuple(str(p) for p in module.OVERLAY_MARKERS) == OVERLAY_FILES,
          f"{[str(p) for p in module.OVERLAY_MARKERS]} vs {list(OVERLAY_FILES)}")
    # The POSIX build of makensis reads "/V2" as a file name, so the switch
    # prefix has to follow the binary, not the author's habits.
    posix = module.nsis_switch_prefix(Path("/usr/bin/makensis"))
    windows = module.nsis_switch_prefix(Path(r"C:\Program Files (x86)\NSIS\makensis.exe"))
    expected_posix = "/" if os.name == "nt" else "-"
    check(f"posix makensis gets {expected_posix}D switches", posix == expected_posix, repr(posix))
    check("makensis.exe gets /D switches", windows == "/", repr(windows))


def main() -> int:
    parser = argparse.ArgumentParser(description="Self-test the Windows packaging script.")
    parser.add_argument("--with-nsis", action="store_true",
                        help="also compile the NSIS script (requires makensis on PATH)")
    parser.add_argument("--keep-artifacts", default=None,
                        help="directory to keep the generated installer in (implies --with-nsis)")
    args = parser.parse_args()

    if not PACKAGER.is_file():
        print(f"ERROR: {PACKAGER} not found", file=sys.stderr)
        return 1

    keep = None
    if args.keep_artifacts:
        keep = Path(args.keep_artifacts).expanduser().resolve()
        keep.mkdir(parents=True, exist_ok=True)
        args.with_nsis = True

    print(f"packager: {PACKAGER}")
    print(f"repo:     {REPO_ROOT}")
    print(f"python:   {sys.version.split()[0]} on {sys.platform}")
    print(f"makensis: {shutil.which('makensis') or 'not found'}")

    case_helpers()

    with tempfile.TemporaryDirectory(prefix="mixar-pkg-") as tmp:
        root = Path(tmp)
        case_happy_path(root / "c1")
        case_dev_bypass(root / "c2")
        case_missing_overlay(root / "c3")
        case_no_build(root / "c4")
        case_resource_mismatch(root / "c5")
        case_naming(root / "c6")
        case_version_file(root / "c7")
        case_nothing_to_do(root / "c8")
        case_missing_nsis_flag(root / "c9")
        case_backend_url(root / "c10")
        if args.with_nsis:
            case_nsis(root / "c11", keep)
        else:
            skip("makensis run", "pass --with-nsis to compile the installer")

    print(f"\n{len(PASSES)} passed, {len(FAILURES)} failed, {len(SKIPS)} skipped")
    if FAILURES:
        print("failed checks:")
        for name in FAILURES:
            print(f"  - {name}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
