#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Finish the Mixar overlay on Blender 5.2.0. Safe to run more than once."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def replace(path, old, new):
    text = read(path)
    if new in text:
        return
    if text.count(old) != 1:
        raise RuntimeError(f"{path}: expected exactly one migration anchor")
    write(path, text.replace(old, new, 1))


def append(path, marker, addition):
    text = read(path)
    if marker not in text:
        write(path, text.rstrip() + "\n\n" + addition.strip() + "\n")


def sync_python():
    for path in ("scripts/windows/settings.bat", "scripts/unix/settings.sh"):
        text = read(path).replace("PYTHON_VERSION=3.11", "PYTHON_VERSION=3.13")
        write(path, text.replace("PYTHON_VERSION:-3.11", "PYTHON_VERSION:-3.13"))
    path = ".github/workflows/build-windows.yml"
    write(path, read(path).replace(r"python\311\include\Python.h", r"python\313\include\Python.h"))


def wire_provider():
    append(
        "src/scripts/mixar/modules/byok/ui/operators/byok_custom_provider_ops.py",
        "byok_custom_models_ops as _byok_custom_models_ops",
        """# Install transient authenticated OpenAI-compatible /models discovery.
from . import byok_custom_models_ops as _byok_custom_models_ops  # noqa: E402,F401""",
    )
    path = "src/scripts/mixar/modules/space_mixie_chat/ui/operators/auth_ops.py"
    replace(
        path,
        """        ('byok_form_codex_bundle', ''),
        ('byok_dialog_state', 'IDLE'),""",
        """        ('byok_form_codex_bundle', ''),
        ('byok_form_custom_model', ''),
        ('byok_form_custom_model_choice', '__MIXAR_NO_DISCOVERED_MODEL__'),
        ('byok_custom_models_status', ''),
        ('byok_dialog_state', 'IDLE'),""",
    )
    replace(
        path,
        """    except Exception as e:
        logger.debug(\"Failed clearing models-catalog cache on logout: %s\", e)


def _schedule_apply_login""",
        """    except Exception as e:
        logger.debug(\"Failed clearing models-catalog cache on logout: %s\", e)

    try:
        from mixar.modules.byok.ui.operators import byok_custom_models_ops
        byok_custom_models_ops.clear_discovered_models(wm)
    except Exception as e:
        logger.debug(\"Failed clearing custom model discovery on logout: %s\", e)


def _schedule_apply_login""",
    )


def port_cpp():
    replace(
        "src/source/blender/blenloader_core/intern/blo_core_blend_header.cc",
        """  if (!STREQLEN(header_bytes, \"BLENDER\", 7)) {
    return BlenderHeaderInvalid{};
  }""",
        """  const bool is_blender_header = STREQLEN(header_bytes, \"BLENDER\", 7);
  const bool is_mixar_header = STREQLEN(header_bytes, \"MIXAR\", 5);
  if (!is_blender_header && !is_mixar_header) {
    return BlenderHeaderInvalid{};
  }""",
    )
    replace(
        "src/source/blender/editors/space_file/file_intern.hh",
        "void FILE_OT_view_selected(wmOperatorType *ot);",
        "void FILE_OT_view_selected(wmOperatorType *ot);\nvoid FILE_OT_open_blend(wmOperatorType *ot);",
    )
    replace(
        "src/source/blender/editors/space_file/space_file.cc",
        "  WM_operatortype_append(FILE_OT_external_operation);\n}",
        "  WM_operatortype_append(FILE_OT_external_operation);\n  WM_operatortype_append(FILE_OT_open_blend);\n}",
    )
    replace(
        "src/source/blender/windowmanager/intern/wm_files.cc",
        "if (win->ghostwin != nullptr || !wm_window_contains_agent_bubble_space(win)) {",
        "if (win->runtime->ghostwin != nullptr || !wm_window_contains_agent_bubble_space(win)) {",
    )
    replace(
        "src/source/blender/windowmanager/intern/wm_window.cc",
        "void *ghostwin_freed = win->ghostwin;",
        "void *ghostwin_freed = win->runtime->ghostwin;",
    )
    replace(
        "src/source/blender/windowmanager/intern/wm_window.cc",
        "void wm_window_close(bContext *C, wmWindowManager *wm, wmWindow *win)\nstatic bool wm_window_is_last_main_window",
        "static bool wm_window_is_last_main_window",
    )
    path = "src/source/blender/editors/space_image/space_image.cc"
    write(path, read(path).replace("MEM_callocN<ARegionType>", "MEM_new_zeroed<ARegionType>"))


def fix_checks():
    path = ".github/workflows/validate-packaging.yml"
    text = read(path).replace('python-version: "3.11"', 'python-version: "3.13"')
    if '      - "tests/test_byok_openai_models.py"' not in text:
        text = text.replace(
            '      - "tests/test_byok_base_url.py"\n',
            '      - "tests/test_byok_base_url.py"\n'
            '      - "tests/test_byok_custom_provider.py"\n'
            '      - "tests/test_byok_openai_models.py"\n',
        )
    insertions = (
        ("core/custom_provider.py", "core/openai_models.py"),
        ("ui/operators/byok_custom_provider_ops.py", "ui/operators/byok_custom_models_ops.py"),
        ("tests/test_byok_custom_provider.py", "tests/test_byok_openai_models.py"),
    )
    for anchor, item in insertions:
        old = f"            src/scripts/mixar/modules/byok/{anchor} \\\n" if not anchor.startswith("tests/") else f"            {anchor} \\\n"
        new = f"            src/scripts/mixar/modules/byok/{item} \\\n" if not item.startswith("tests/") else f"            {item} \\\n"
        if new not in text:
            if old not in text:
                raise RuntimeError(f"Packaging compile anchor missing: {anchor}")
            text = text.replace(old, old + new, 1)
    text = text.replace(
        "for t in tests/test_byok_base_url.py tests/test_provider_errors.py; do",
        "for t in tests/test_byok_base_url.py tests/test_byok_custom_provider.py "
        "tests/test_byok_openai_models.py tests/test_provider_errors.py; do",
    )
    text = text.replace(
        "            tests/test_byok_base_url.py tests/test_provider_errors.py",
        "            tests/test_byok_base_url.py tests/test_byok_custom_provider.py \\\n"
        "            tests/test_byok_openai_models.py tests/test_provider_errors.py",
    )
    required = (
        'python-version: "3.13"',
        "core/openai_models.py",
        "operators/byok_custom_models_ops.py",
        "tests/test_byok_openai_models.py",
    )
    if not all(item in text for item in required):
        raise RuntimeError("Packaging workflow finalization incomplete")
    write(path, text)

    path = "REUSE.toml"
    text = read(path)
    if '"scripts/upgrade/resolutions.json"' not in text:
        if '  "VERSION",\n' not in text:
            raise RuntimeError("REUSE annotation anchor missing")
        text = text.replace('  "VERSION",\n', '  "VERSION",\n  "scripts/upgrade/resolutions.json",\n', 1)
        write(path, text)


def guidance():
    append(
        "CLAUDE.md",
        "## Custom OpenAI-compatible provider (Blender 5.2)",
        """## Custom OpenAI-compatible provider (Blender 5.2)

- `custom` accepts a Base URL, API key, and free-text model ID.
- `/models` discovery uses Bearer auth and accepts OpenAI `data[].id` only.
- IDs are transient and endpoint-scoped; manual Model text is authoritative.
- Blender 5.2 uses Python 3.13 in Unix, Windows, and CI tooling.""",
    )


def main():
    sync_python()
    wire_provider()
    port_cpp()
    fix_checks()
    guidance()
    print("Blender 5.2 finalization applied")


if __name__ == "__main__":
    main()
