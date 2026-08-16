# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Apply the small Mixar source migrations required by Blender 5.2.

The Windows build overlays ``src`` on top of the pinned Blender checkout in
``source``. This script runs immediately after that overlay and updates only
Mixar-owned compatibility fragments. Every transformation is idempotent and
validated so an upstream API change fails here with a useful message instead
of producing hundreds of compiler errors later.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count == 1:
        return text.replace(old, new)
    if count == 0 and new in text:
        return text
    raise RuntimeError(
        f"{label}: expected one old fragment (or existing replacement), found {count}"
    )


def replace_counted(text: str, old: str, new: str, expected: int, label: str) -> str:
    count = text.count(old)
    if count == expected:
        return text.replace(old, new)
    if count == 0 and text.count(new) >= expected:
        return text
    raise RuntimeError(
        f"{label}: expected {expected} old fragment(s) (or an already-patched file), found {count}"
    )


def patch_layout(root: Path) -> None:
    path = root / "source/blender/editors/interface/interface_layout.cc"
    text = path.read_text(encoding="utf-8")
    old = """  ui::Block *block = layout->block();
  if (!block || block->buttons.is_empty()) {
    return;
  }
  but_drawflag_enable(block->buttons.last().get(), BUT_NO_TOOLTIP);
"""
    new = """  ui::Block *block = layout->block();
  if (!block) {
    return;
  }
  ui::Button *but = block->last_but();
  if (!but) {
    return;
  }
  button_drawflag_enable(but, BUT_NO_TOOLTIP);
"""
    text = replace_once(text, old, new, "interface_layout tooltip helper")
    path.write_text(text, encoding="utf-8")


def patch_mixar_header(root: Path) -> None:
    path = root / "source/blender/editors/interface/interface_mixar_section.hh"
    text = path.read_text(encoding="utf-8")

    # Remove only the obsolete *global* forward declaration before adding the
    # Blender 5.2 namespaced one. Doing this after adding the new declaration
    # would accidentally delete the correct declaration as well.
    global_forward = """/* Custom panel category tab drawing for MIXIE space                     */

struct ARegion;

/**
"""
    namespaced_section = """/* Custom panel category tab drawing for MIXIE space                     */

/**
"""
    if global_forward in text:
        text = text.replace(global_forward, namespaced_section, 1)

    old_namespace = """namespace blender::ui {
struct Layout;
}
"""
    new_namespace = """namespace blender {
struct ARegion;
namespace ui {
struct Layout;
}
}  // namespace blender
"""
    text = replace_once(text, old_namespace, new_namespace, "Mixar header Blender namespace")
    text = replace_once(
        text,
        "void UI_panel_category_draw_all_mixar(ARegion *region, const char *category_id_active);",
        "void UI_panel_category_draw_all_mixar(::blender::ARegion *region, const char *category_id_active);",
        "Mixar panel ARegion signature",
    )
    path.write_text(text, encoding="utf-8")


def patch_mixar_section(root: Path) -> None:
    path = root / "source/blender/editors/interface/interface_mixar_section.cc"
    text = path.read_text(encoding="utf-8")

    anchor = '#include "UI_interface_layout.hh"\n'
    namespace_anchor = anchor + "\nusing namespace blender;\n"
    if namespace_anchor not in text:
        text = replace_once(
            text,
            anchor,
            namespace_anchor,
            "Mixar implementation Blender namespace lookup",
        )

    text = replace_counted(
        text,
        "block->buttons.size()",
        "block->buttons_ptrs.size()",
        5,
        "Blender 5.2 Block button count",
    )
    text = replace_counted(
        text,
        "block->buttons[i].get()",
        "block->buttons_ptrs[i].get()",
        5,
        "Blender 5.2 Block button indexing",
    )

    old_aspect = """  const float aspect = BLI_listbase_is_empty(&region->runtime->uiblocks) ?
                            1.0f :
                            ((::blender::ui::Block *)region->runtime->uiblocks.first)->aspect;
"""
    new_aspect = """  const float aspect = BLI_rctf_size_y(&region->v2d.cur) /
                       (BLI_rcti_size_y(&region->v2d.mask) + 1);
"""
    text = replace_once(text, old_aspect, new_aspect, "Blender 5.2 panel aspect calculation")
    text = replace_once(
        text,
        "const bTheme *btheme = UI_GetTheme();",
        "const bTheme *btheme = ::blender::ui::theme::theme_get();",
        "Blender 5.2 theme accessor",
    )

    path.write_text(text, encoding="utf-8")


def patch_widgets(root: Path) -> None:
    path = root / "source/blender/editors/interface/interface_widgets.cc"
    text = path.read_text(encoding="utf-8")

    # Mixar inserted an action-button branch into Blender's ButtonType::But
    # dispatch, but an obsolete fallback #else/#endif from an older toolbar
    # conditional was left behind. MSVC stops immediately with C1019
    # (unexpected #else). Keep the Blender 5.2 structure: the toolbar special
    # case is conditional, while the Exec fallback is an ordinary C++ else.
    malformed = """#ifdef USE_UI_TOOLBAR_HACK
        else if ((but->icon != ICON_NONE) && but_is_tool(but)) {
          wt = widget_type(WidgetStyle::ToolbarItem);
        }
#endif
        else {
          wt = widget_type(WidgetStyle::Exec);
        }
#else
        wt = widget_type(WidgetStyle::Exec);
#endif
"""
    corrected = """#ifdef USE_UI_TOOLBAR_HACK
        else if ((but->icon != ICON_NONE) && but_is_tool(but)) {
          wt = widget_type(WidgetStyle::ToolbarItem);
        }
#endif
        else {
          wt = widget_type(WidgetStyle::Exec);
        }
"""
    text = replace_once(text, malformed, corrected, "interface_widgets toolbar preprocessor block")
    path.write_text(text, encoding="utf-8")


def audit(root: Path) -> None:
    layout = (root / "source/blender/editors/interface/interface_layout.cc").read_text(
        encoding="utf-8"
    )
    mixar = (root / "source/blender/editors/interface/interface_mixar_section.cc").read_text(
        encoding="utf-8"
    )
    widgets = (root / "source/blender/editors/interface/interface_widgets.cc").read_text(
        encoding="utf-8"
    )
    header = (root / "source/blender/editors/interface/interface_mixar_section.hh").read_text(
        encoding="utf-8"
    )

    stale = {
        "Block::buttons member access": "block->buttons.",
        "Block::buttons indexed access": "block->buttons[",
        "old tooltip drawflag helper": "but_drawflag_enable(",
        "old panel aspect ListBase check": "BLI_listbase_is_empty(&region->runtime->uiblocks)",
        "old theme accessor": "UI_GetTheme()",
    }
    combined = layout + "\n" + mixar
    for label, token in stale.items():
        if token in combined:
            raise RuntimeError(f"stale Blender 5.2 API remains: {label}: {token}")

    malformed_widgets_tail = """        else {
          wt = widget_type(WidgetStyle::Exec);
        }
#else
        wt = widget_type(WidgetStyle::Exec);
#endif
"""
    if malformed_widgets_tail in widgets:
        raise RuntimeError("interface_widgets.cc still contains the orphaned #else/#endif block")

    if "namespace blender {\nstruct ARegion;" not in header:
        raise RuntimeError("Mixar header is missing blender::ARegion forward declaration")
    if "void UI_panel_category_draw_all_mixar(::blender::ARegion *region" not in header:
        raise RuntimeError("Mixar panel header still exposes the pre-5.2 global ARegion type")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        type=Path,
        help="Blender overlay root (normally the repository source directory)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    patch_layout(root)
    patch_mixar_header(root)
    patch_mixar_section(root)
    patch_widgets(root)
    audit(root)
    print(f"Blender 5.2 Mixar compatibility patch is clean: {root}")


if __name__ == "__main__":
    main()
