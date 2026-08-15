#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later
"""Run one named function from finalize_blender_52.py."""
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
if name not in {"sync_python", "wire_provider", "port_cpp", "fix_checks", "guidance"}:
    raise SystemExit(f"unsupported stage: {name}")
getattr(module, name)()
print(f"completed {name}")
