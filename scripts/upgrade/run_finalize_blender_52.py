#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later
"""Correct the finalizer's BYOK UI path and execute it."""
from pathlib import Path
import runpy

path = Path(__file__).with_name("finalize_blender_52.py")
text = path.read_text(encoding="utf-8")
old = '("operators/byok_custom_provider_ops.py", "operators/byok_custom_models_ops.py")'
new = '("ui/operators/byok_custom_provider_ops.py", "ui/operators/byok_custom_models_ops.py")'
if old not in text and new not in text:
    raise RuntimeError("BYOK packaging path tuple was not found")
path.write_text(text.replace(old, new), encoding="utf-8")
runpy.run_path(str(path), run_name="__main__")
