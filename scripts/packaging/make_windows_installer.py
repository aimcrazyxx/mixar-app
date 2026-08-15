#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Package a built Mixar tree into a Windows installer (.exe) plus a portable zip.

scripts/windows/build.bat leaves a runnable tree in ``build/<MIXAR_ENV>/bin``
but the repository has no packaging step, so there is nothing to hand to a
user. This script closes that gap and is safe to re-run:

    scripts\\windows\\package.bat
    python scripts/packaging/make_windows_installer.py --env Prod

Compiling Mixar needs Windows and MSVC; packaging does not. makensis has a
native POSIX build, so given a payload from a Windows build (or from the CI
artifact) this also runs on Linux and macOS:

    sudo apt-get install nsis
    python3 scripts/packaging/make_windows_installer.py --payload-dir ./bin

Run scripts/packaging/validate_installer.py to self-test all of this without a
Windows build at all.

Steps
  1. Locate the built tree (``build/<env>/bin``, ``bin/Release``, ``bin/Debug``).
  2. Verify it: the executable, the ``<X.Y>`` resource directory, the generated
     ``config/mixar.json`` and this fork's BYOK provider modules.
  3. Refuse to package a bundle that carries dev bypass credentials.
  4. Optionally regenerate ``config/mixar.json`` with a different backend URL.
  5. Write ``dist/<name>.zip`` (portable, nothing to install).
  6. Run makensis on ``installer/windows/mixar.nsi`` -> ``dist/<name>-setup.exe``.
  7. Optionally sign payload + installer with signtool.
  8. Write ``dist/SHA256SUMS.txt``.

Stdlib only, no third-party imports.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_NSI = REPO_ROOT / "installer" / "windows" / "mixar.nsi"
DEFAULT_OUT_DIR = REPO_ROOT / "dist"

# Never ship these. Keep in sync with the /x flags in installer/windows/mixar.nsi.
EXCLUDE_NAMES = {"__pycache__", ".git", ".gitignore", ".gitattributes", "CMakeFiles"}
EXCLUDE_SUFFIXES = (".pdb", ".ilk", ".exp", ".obj", ".log", ".tmp")

# Proof that install.bat overlaid this fork's work into the bundle. Without
# these files the artifact is just vanilla Mixar: the custom base URL and the
# custom provider option would both be silently missing. Keep this list in sync
# with OVERLAY_FILES in validate_installer.py - the fork owns exactly these
# four modules.
OVERLAY_MARKERS = (
    Path("scripts/mixar/modules/byok/core/base_url.py"),
    Path("scripts/mixar/modules/byok/core/custom_provider.py"),
    Path("scripts/mixar/modules/byok/ui/operators/byok_base_url_ops.py"),
    Path("scripts/mixar/modules/byok/ui/operators/byok_custom_provider_ops.py"),
)

VERSION_DIR_RE = re.compile(r"^\d+\.\d+$")


def log(msg: str) -> None:
    print(f"[package] {msg}", flush=True)


def die(msg: str) -> None:
    print(f"[package] ERROR: {msg}", file=sys.stderr, flush=True)
    raise SystemExit(1)


def mib(size: int) -> str:
    return f"{size / (1024 * 1024):.1f} MiB"


def read_version(explicit: str | None) -> str:
    if explicit:
        return explicit.strip()
    env_version = os.environ.get("MIXAR_VERSION", "").strip()
    if env_version:
        return env_version
    version_file = REPO_ROOT / "VERSION"
    if version_file.is_file():
        text = version_file.read_text(encoding="utf-8").strip()
        if text:
            return text
    log("WARNING: no VERSION file and no MIXAR_VERSION, using 0.0.0")
    return "0.0.0"


def four_part_version(version: str) -> str:
    """NSIS VIProductVersion demands exactly four numeric fields."""
    parts = re.findall(r"\d+", version)[:4]
    parts += ["0"] * (4 - len(parts))
    return ".".join(parts)


def locate_exe(directory: Path) -> Path | None:
    configured = os.environ.get("MIXAR_EXECUTABLE_NAME", "mixar")
    for name in (f"{configured}.exe", "mixar.exe", "blender.exe"):
        candidate = directory / name
        if candidate.is_file():
            return candidate
    return None


def find_payload_dir(args: argparse.Namespace, env: str) -> tuple[Path, Path]:
    candidates: list[Path] = []
    if args.payload_dir:
        candidates.append(Path(args.payload_dir))
    bases = [Path(args.build_dir)] if args.build_dir else [REPO_ROOT / "build" / env]
    for base in bases:
        candidates += [base / "bin", base / "bin" / "Release", base / "bin" / "Debug", base]
    for candidate in candidates:
        candidate = candidate.expanduser()
        if not candidate.is_dir():
            continue
        exe = locate_exe(candidate)
        if exe:
            return candidate.resolve(), exe
    tried = "\n  ".join(str(c) for c in candidates)
    die(
        "could not find a built Mixar tree (no mixar.exe). Run "
        f"scripts\\windows\\build.bat first.\nLooked in:\n  {tried}"
    )
    raise AssertionError("unreachable")


def find_resource_dir(payload: Path, blender_version: str) -> Path:
    exact = payload / blender_version
    if exact.is_dir():
        return exact
    found = sorted(p for p in payload.iterdir() if p.is_dir() and VERSION_DIR_RE.match(p.name))
    if not found:
        die(
            f"no Blender resource directory (expected '{blender_version}') inside {payload}. "
            "The build did not finish installing."
        )
    picked = found[-1]
    log(f"WARNING: expected resource dir '{blender_version}', found '{picked.name}' - using it")
    return picked


def check_bundle(resource_dir: Path, skip_overlay_check: bool) -> None:
    config_path = resource_dir / "config" / "mixar.json"
    if config_path.is_file():
        try:
            data = json.loads(config_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            die(f"bundled config/mixar.json is unreadable: {exc}")
        app_info = data.get("app_info") or {}
        log(
            "bundled config: environment={} version={} backend_url={}".format(
                data.get("environment"), app_info.get("version"), data.get("backend_url")
            )
        )
        if data.get("dev_bypass"):
            die(
                "bundled config/mixar.json contains a dev_bypass block - refusing to "
                "package plaintext credentials. Rebuild with MIXAR_ENV=Prod."
            )
    else:
        log(f"WARNING: {config_path} is missing; the app will fall back to built-in defaults")

    missing = [str(marker) for marker in OVERLAY_MARKERS if not (resource_dir / marker).is_file()]
    if not missing:
        log("BYOK base URL modules present in the bundle")
        return
    message = "the bundle is missing this fork's modules:\n  " + "\n  ".join(missing)
    if skip_overlay_check:
        log(f"WARNING: {message}")
    else:
        die(f"{message}\nRun scripts\\windows\\install.bat, or pass --skip-overlay-check.")


def regenerate_config(resource_dir: Path, env: str, backend_url: str | None, frontend_url: str | None) -> None:
    script = REPO_ROOT / "scripts" / "generate_config.py"
    if not script.is_file():
        die(f"cannot regenerate config, {script} not found")
    output = resource_dir / "config" / "mixar.json"
    child_env = os.environ.copy()
    child_env["MIXAR_ENV"] = env
    if backend_url:
        child_env["MIXAR_BACKEND_URL"] = backend_url
    if frontend_url:
        child_env["MIXAR_FRONTEND_URL"] = frontend_url
    log(f"regenerating {output}")
    result = subprocess.run(
        [sys.executable, str(script), "--output", str(output)], env=child_env, check=False
    )
    if result.returncode != 0:
        die("generate_config.py failed")


def iter_payload_files(payload: Path):
    for dirpath, dirnames, filenames in os.walk(payload):
        dirnames[:] = sorted(d for d in dirnames if d not in EXCLUDE_NAMES)
        for name in sorted(filenames):
            if name in EXCLUDE_NAMES or name.lower().endswith(EXCLUDE_SUFFIXES):
                continue
            path = Path(dirpath) / name
            yield path, path.relative_to(payload)


def make_zip(payload: Path, dest: Path, top_dir: str) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        dest.unlink()
    count = 0
    raw = 0
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED, allowZip64=True, compresslevel=6) as archive:
        for path, rel in iter_payload_files(payload):
            archive.write(path, f"{top_dir}/{rel.as_posix()}")
            count += 1
            raw += path.stat().st_size
    log(f"portable zip: {dest.name} ({count} files, {mib(raw)} -> {mib(dest.stat().st_size)})")
    return dest


def find_makensis(explicit: str | None) -> Path | None:
    if explicit:
        path = Path(explicit)
        return path if path.is_file() else None
    found = shutil.which("makensis")
    if found:
        return Path(found)
    for base in (
        os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)"),
        os.environ.get("ProgramFiles", r"C:\Program Files"),
    ):
        candidate = Path(base) / "NSIS" / "makensis.exe"
        if candidate.is_file():
            return candidate
    return None


def find_icon(resource_dir: Path) -> Path | None:
    candidates = [
        REPO_ROOT / "installer" / "windows" / "mixar.ico",
        REPO_ROOT / "src" / "release" / "windows" / "icons" / "mixar.ico",
        resource_dir / "datafiles" / "mixar.ico",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    search_root = REPO_ROOT / "src"
    if search_root.is_dir():
        for found in sorted(search_root.rglob("*.ico")):
            return found
    return None


def find_signtool(explicit: str | None) -> Path | None:
    if explicit:
        path = Path(explicit)
        return path if path.is_file() else None
    found = shutil.which("signtool")
    if found:
        return Path(found)
    kits = Path(os.environ.get("ProgramFiles(x86)", r"C:\Program Files (x86)")) / "Windows Kits" / "10" / "bin"
    if kits.is_dir():
        matches = sorted(kits.glob("*/x64/signtool.exe"))
        if matches:
            return matches[-1]
    return None


def sign_file(target: Path, args: argparse.Namespace) -> None:
    signtool = find_signtool(args.signtool)
    if not signtool:
        log(f"WARNING: signtool not found, leaving {target.name} unsigned")
        return
    if not args.pfx:
        log(f"WARNING: no --pfx / MIXAR_SIGN_PFX, leaving {target.name} unsigned")
        return
    password = os.environ.get(args.pfx_password_env, "")
    command = [
        str(signtool), "sign", "/fd", "sha256",
        "/tr", args.timestamp_url, "/td", "sha256",
        "/f", args.pfx,
    ]
    if password:
        command += ["/p", password]
    command.append(str(target))
    printable = " ".join("***" if part == password and password else part for part in command)
    log(f"signing {target.name}")
    log(f"  {printable}")
    if subprocess.run(command, check=False).returncode != 0:
        die(f"signtool failed for {target}")


def nsis_switch_prefix(makensis: Path) -> str:
    """NSIS switches are ``/X`` on Windows and ``-X`` on the POSIX builds.

    A POSIX makensis treats ``/V2`` as an input file name, so the whole run
    dies with a confusing "can't open script" instead of building anything.
    """
    if os.name == "nt" or makensis.suffix.lower() == ".exe":
        return "/"
    return "-"


def run_nsis(nsi: Path, defines: dict[str, str], makensis: Path) -> None:
    flag = nsis_switch_prefix(makensis)
    command = [str(makensis), f"{flag}V2"]
    command += [f"{flag}D{key}={value}" for key, value in defines.items()]
    command.append(str(nsi))
    log(f"running {makensis.name} on {nsi.name} ({flag}D switches)")
    if subprocess.run(command, check=False).returncode != 0:
        die("makensis failed")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Package a built Mixar tree into a Windows installer and portable zip."
    )
    parser.add_argument("--env", default=os.environ.get("MIXAR_ENV", "Prod"),
                        help="MIXAR_ENV the tree was built with (default: %(default)s)")
    parser.add_argument("--blender-version", default=os.environ.get("BLENDER_VERSION", "5.2"),
                        help="Blender X.Y resource directory name (default: %(default)s)")
    parser.add_argument("--version", default=None, help="override product version (default: VERSION file)")
    parser.add_argument("--build-dir", default=None, help="build/<env> directory")
    parser.add_argument("--payload-dir", default=None, help="exact directory holding mixar.exe")
    parser.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="where artifacts are written")
    parser.add_argument("--nsi", default=str(DEFAULT_NSI), help="NSIS script path")
    parser.add_argument("--makensis", default=None, help="path to makensis (or makensis.exe)")
    parser.add_argument("--suffix", default="", help="extra artifact name tag, e.g. a short commit sha")
    parser.add_argument("--backend-url", default=None, help="regenerate config/mixar.json with this backend URL")
    parser.add_argument("--frontend-url", default=None, help="regenerate config/mixar.json with this frontend URL")
    parser.add_argument("--no-zip", action="store_true", help="skip the portable zip")
    parser.add_argument("--no-installer", action="store_true", help="skip the NSIS installer")
    parser.add_argument("--allow-missing-nsis", action="store_true",
                        help="warn instead of failing when makensis is unavailable")
    parser.add_argument("--skip-overlay-check", action="store_true",
                        help="package even if this fork's modules are absent from the bundle")
    parser.add_argument("--sign", action="store_true", help="sign payload and installer with signtool")
    parser.add_argument("--signtool", default=None, help="path to signtool.exe")
    parser.add_argument("--pfx", default=os.environ.get("MIXAR_SIGN_PFX"), help="code signing .pfx")
    parser.add_argument("--pfx-password-env", default="MIXAR_SIGN_PASSWORD",
                        help="env var holding the .pfx password (never pass it on the command line)")
    parser.add_argument("--timestamp-url", default="http://timestamp.digicert.com",
                        help="RFC3161 timestamp server (default: %(default)s)")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    env = args.env or "Prod"
    version = read_version(args.version)
    payload, exe = find_payload_dir(args, env)
    resource_dir = find_resource_dir(payload, args.blender_version)

    log(f"repo:      {REPO_ROOT}")
    log(f"payload:   {payload}")
    log(f"executable:{exe.name}")
    log(f"resources: {resource_dir.name}")
    log(f"version:   {version} ({env})")

    if args.backend_url or args.frontend_url:
        regenerate_config(resource_dir, env, args.backend_url, args.frontend_url)
    check_bundle(resource_dir, args.skip_overlay_check)

    name_parts = [os.environ.get("MIXAR_APP_NAME", "Mixar"), version, "windows-x64"]
    if env != "Prod":
        name_parts.append(env.lower())
    if args.suffix:
        name_parts.append(args.suffix)
    base_name = "-".join(part for part in name_parts if part)

    out_dir = Path(args.out_dir).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    artifacts: list[Path] = []

    if args.sign:
        sign_file(exe, args)

    if not args.no_zip:
        artifacts.append(make_zip(payload, out_dir / f"{base_name}.zip", base_name))

    if not args.no_installer:
        nsi = Path(args.nsi).expanduser()
        if not nsi.is_file():
            die(f"NSIS script not found: {nsi}")
        makensis = find_makensis(args.makensis)
        if not makensis:
            message = (
                "makensis not found. Install NSIS (winget install NSIS.NSIS, "
                "choco install nsis, apt-get install nsis, brew install makensis, "
                "or https://nsis.sourceforge.io) or pass --makensis."
            )
            if args.allow_missing_nsis:
                log(f"WARNING: {message} Skipping the installer.")
            else:
                die(message)
        else:
            installer = out_dir / f"{base_name}-setup.exe"
            if installer.exists():
                installer.unlink()
            defines = {
                "PAYLOAD_DIR": str(payload),
                # Joined here so the separator matches the platform running
                # makensis: a POSIX build does not accept backslashes.
                "PAYLOAD_GLOB": os.path.join(str(payload), "*"),
                "OUT_FILE": str(installer),
                "APP_NAME": os.environ.get("MIXAR_APP_NAME", "Mixar"),
                "APP_EXE": exe.name,
                "APP_VERSION": version,
                "APP_VERSION_FULL": four_part_version(version),
                "APP_PUBLISHER": os.environ.get("MIXAR_VENDOR", "Mixar"),
                "APP_URL": os.environ.get("MIXAR_WEBSITE", "https://mixar.app"),
                "APP_ENV": env,
                "BLENDER_VERSION": resource_dir.name,
            }
            license_file = REPO_ROOT / "LICENSE"
            if license_file.is_file():
                defines["LICENSE_FILE"] = str(license_file)
            icon = find_icon(resource_dir)
            if icon:
                defines["APP_ICON"] = str(icon)
                log(f"installer icon: {icon}")
            run_nsis(nsi, defines, makensis)
            if not installer.is_file():
                die(f"makensis reported success but {installer} is missing")
            log(f"installer: {installer.name} ({mib(installer.stat().st_size)})")
            if args.sign:
                sign_file(installer, args)
            artifacts.append(installer)

    if not artifacts:
        die("nothing was produced (both --no-zip and --no-installer?)")

    sums = out_dir / "SHA256SUMS.txt"
    lines = [f"{sha256(artifact)}  {artifact.name}" for artifact in artifacts]
    sums.write_text("\n".join(lines) + "\n", encoding="utf-8")

    log("done:")
    for line in lines:
        log(f"  {line}")
    log(f"  artifacts in {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
