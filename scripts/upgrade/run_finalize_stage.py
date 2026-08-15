#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later
"""Run one finalizer stage while leaving workflow edits to the GitHub API."""
import importlib.util
import sys
from pathlib import Path

path = Path(__file__).with_name("finalize_blender_52.py")
text = path.read_text(encoding="utf-8")
old = '("operators/byok_custom_provider_ops.py", "operators/byok_custom_models_ops.py")'
new = '("ui/operators/byok_custom_provider_ops.py", "ui/operators/byok_custom_models_ops.py")'
if old not in text and new not in text:
    raise RuntimeError("BYOK packaging path tuple was not found")
path.write_text(text.replace(old, new), encoding="utf-8")
spec = importlib.util.spec_from_file_location("finalize_blender_52", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
name = sys.argv[1]

if name == "sync_python":
    for relative in ("scripts/windows/settings.bat", "scripts/unix/settings.sh"):
        target = module.ROOT / relative
        value = target.read_text(encoding="utf-8")
        value = value.replace("PYTHON_VERSION=3.11", "PYTHON_VERSION=3.13")
        value = value.replace("PYTHON_VERSION:-3.11", "PYTHON_VERSION:-3.13")
        target.write_text(value, encoding="utf-8")
elif name == "fix_checks":
    target = module.ROOT / "REUSE.toml"
    value = target.read_text(encoding="utf-8")
    if '"scripts/upgrade/resolutions.json"' not in value:
        anchor = '  "VERSION",\n'
        if anchor not in value:
            raise RuntimeError("REUSE annotation anchor missing")
        target.write_text(
            value.replace(anchor, anchor + '  "scripts/upgrade/resolutions.json",\n', 1),
            encoding="utf-8",
        )
elif name in {"wire_provider", "port_cpp", "guidance"}:
    getattr(module, name)()
else:
    raise SystemExit(f"unsupported stage: {name}")
print(f"completed {name}")
