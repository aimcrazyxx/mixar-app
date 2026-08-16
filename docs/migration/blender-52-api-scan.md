<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 API scan

## Applied ports

- `uiLayout` → `blender::ui::Layout`: **0**
- `uiBut` → `blender::ui::Button`: **75**
- `uiBlock` → `blender::ui::Block`: **88**
- `absolute_block()` → `absolute(false).block()`: **5**
- `wmWindow::ghostwin` → `wmWindow::runtime->ghostwin`: **0**
- `MEM_callocN<T>` → `MEM_new_zeroed<T>`: **0**

## legacy uiLayout type

Count: **0**

- None

## legacy uiBut type

Count: **0**

- None

## legacy uiBlock type

Count: **0**

- None

## removed absolute_block call

Count: **0**

- None

## obsolete fmtlib target

Count: **0**

- None

## direct ghostwin access

Count: **0**

- None

## obsolete typed MEM_callocN

Count: **0**

- None

## legacy uiPopupMenu type

Count: **0**

- None

## legacy uiPopupBlockHandle type

Count: **0**

- None

## tooltip helper occurrences

Count: **3**

- `src/source/blender/editors/interface/interface_layout.cc:1504` — `void UI_layout_disable_last_button_tooltip(ui::Layout *layout)`
- `src/source/blender/editors/include/UI_interface_layout.hh:906` — `void UI_layout_disable_last_button_tooltip(Layout *layout);`
- `src/source/blender/makesrna/intern/rna_ui_api.cc:522` — `UI_layout_disable_last_button_tooltip(layout);`

## merge conflict marker

Count: **0**

- None

## Summary

Blocking stale-pattern hits: **0**
