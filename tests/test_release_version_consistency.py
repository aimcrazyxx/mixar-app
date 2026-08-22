# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Keep every release-version surface synchronized with VERSION."""

import importlib.util
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()


def _macro(name: str) -> int:
    header = (ROOT / "src/source/blender/blenkernel/BKE_blender_version.h").read_text(
        encoding="utf-8"
    )
    match = re.search(rf"^#define {name} (\d+)$", header, re.MULTILINE)
    assert match, f"missing numeric {name} macro"
    return int(match.group(1))


def test_release_is_mixar_334_on_blender_52():
    assert VERSION == "3.3.4"
    assert _macro("MIXAR_VERSION") == 303
    assert _macro("MIXAR_VERSION_PATCH") == 4
    assert _macro("BLENDER_VERSION") == 502


def test_runtime_config_uses_version_file_over_stale_environment(monkeypatch, tmp_path):
    module_path = ROOT / "scripts/generate_config.py"
    spec = importlib.util.spec_from_file_location("mixar_generate_config", module_path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    version_file = tmp_path / "VERSION"
    version_file.write_text(VERSION + "\n", encoding="utf-8")
    monkeypatch.setenv("MIXAR_VERSION", "0.0.1")

    config = module.generate_config(str(version_file))

    assert config["app_info"]["version"] == VERSION


def test_platform_settings_derive_the_patch_from_version():
    windows = (ROOT / "scripts/windows/settings.bat").read_text(encoding="utf-8")
    unix = (ROOT / "scripts/unix/settings.sh").read_text(encoding="utf-8")

    assert 'set /p MIXAR_VERSION=<"%ROOT_DIR%\\VERSION"' in windows
    assert 'set "MIXAR_VERSION_PATCH=%%c"' in windows
    assert 'export MIXAR_VERSION_PATCH="${MIXAR_VERSION##*.}"' in unix
