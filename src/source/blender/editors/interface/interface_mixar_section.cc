/* SPDX-FileCopyrightText: 2025 Mixar Authors
 * SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
 *
 * SPDX-License-Identifier: GPL-3.0-or-later */

/** \file
 * \ingroup edinterface
 *
 * Mixar custom UI widgets — helpers for styled layouts and controls.
 */

#include <algorithm>
#include <cmath>
#include <cstring>

#include "BLI_listbase.h"
#include "BLI_math_base.h"
#include "BLI_math_vector.h"
#include "BLI_rect.h"
#include "BLI_utildefines.h"

#include "BLT_translation.hh"

#include "BLF_api.hh"

#include "DNA_screen_types.h"
#include "DNA_userdef_types.h"

#include "BKE_screen.hh"

#include "GPU_immediate.hh"
#include "GPU_state.hh"

#include "UI_interface_c.hh"
#include "UI_resources.hh"
#include "UI_view2d.hh"

#include "interface_intern.hh"
#include "interface_mixar_section.hh"

#include "UI_interface_layout.hh"

::blender::ui::Layout *UI_layout_mixar_section(::blender::ui::Layout *layout)
{
  ::blender::ui::Layout &box = layout->box();
  ::blender::ui::Block *block = layout->block();

  /* Walk backwards through the block's buttons to find the Roundbox button
   * that was just created by box(). It should be the most recently added. */
  for (int i = int(block->buttons_ptrs.size()) - 1; i >= 0; i--) {
    ::blender::ui::Button *but = block->buttons_ptrs[i].get();
    if (but->type == ::blender::ui::ButtonType::Roundbox) {
      but->flag2 |= UI_BUT2_MIXAR_SECTION;
      break;
    }
  }

  return &box;
}

void UI_layout_mixar_mark_last_dropdown(::blender::ui::Layout *layout)
{
  ::blender::ui::Block *block = layout->block();

  /* Walk backwards to find the most recently created Menu button. */
  for (int i = int(block->buttons_ptrs.size()) - 1; i >= 0; i--) {
    ::blender::ui::Button *but = block->buttons_ptrs[i].get();
    if (ELEM(but->type, ::blender::ui::ButtonType::Menu, ::blender::ui::ButtonType::Block, ::blender::ui::ButtonType::Popover)) {
      but->flag2 |= UI_BUT2_MIXAR_DROPDOWN;
      break;
    }
  }
}

void UI_layout_mixar_mark_last_action(::blender::ui::Layout *layout)
{
  ::blender::ui::Block *block = layout->block();

  for (int i = int(block->buttons_ptrs.size()) - 1; i >= 0; i--) {
    ::blender::ui::Button *but = block->buttons_ptrs[i].get();
    if (but->type == ::blender::ui::ButtonType::But) {
      but->flag2 |= UI_BUT2_MIXAR_ACTION;
      break;
    }
  }
}

void UI_layout_mixar_mark_last_toggle(::blender::ui::Layout *layout)
{
  ::blender::ui::Block *block = layout->block();

  for (int i = int(block->buttons_ptrs.size()) - 1; i >= 0; i--) {
    ::blender::ui::Button *but = block->buttons_ptrs[i].get();
    if (ELEM(but->type, ::blender::ui::ButtonType::Checkbox, ::blender::ui::ButtonType::CheckboxN)) {
      but->flag2 |= UI_BUT2_MIXAR_TOGGLE;
      break;
    }
  }
}

void UI_layout_mixar_mark_last_input(::blender::ui::Layout *layout)
{
  ::blender::ui::Block *block = layout->block();

  for (int i = int(block->buttons_ptrs.size()) - 1; i >= 0; i--) {
    ::blender::ui::Button *but = block->buttons_ptrs[i].get();
    if (but->type == ::blender::ui::ButtonType::Text) {
      but->flag2 |= UI_BUT2_MIXAR_INPUT;
      break;
    }
  }
}
