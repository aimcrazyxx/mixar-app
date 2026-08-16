/* SPDX-FileCopyrightText: 2025 Mixar Authors
 * SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
 *
 * SPDX-License-Identifier: GPL-3.0-or-later */

/** \file
 * \ingroup edinterface
 *
 * Mixar custom UI widgets — styled containers and controls for moodboard panels.
 */

#pragma once

namespace blender {
struct ARegion;

namespace ui {
struct Layout;
}
}  // namespace blender

/* -------------------------------------------------------------------- */
/* Custom flag2 bits — checked in interface_widgets.cc widget dispatch.  */

/** Marks a Roundbox button as a Mixar section (styled box container). */
#define UI_BUT2_MIXAR_SECTION (1 << 2)
/** Marks a Menu button as a Mixar dropdown (styled enum selector). */
#define UI_BUT2_MIXAR_DROPDOWN (1 << 3)
/** Marks a But (operator) button as a Mixar action button (accent CTA). */
#define UI_BUT2_MIXAR_ACTION (1 << 4)
/** Marks a Checkbox button as a Mixar toggle switch (pill-shaped). */
#define UI_BUT2_MIXAR_TOGGLE (1 << 5)
/** Marks a Text button as a Mixar styled input (visible border + focus glow). */
#define UI_BUT2_MIXAR_INPUT (1 << 6)

/* -------------------------------------------------------------------- */
/* Layout helpers                                                        */

/**
 * Create a styled section box layout.
 * \return Sub-layout to place items in, identical API to layout.box().
 */
::blender::ui::Layout *UI_layout_mixar_section(::blender::ui::Layout *layout);

/** Mark the most recently created Menu/Block/Popover button. */
void UI_layout_mixar_mark_last_dropdown(::blender::ui::Layout *layout);
/** Mark the most recently created operator button. */
void UI_layout_mixar_mark_last_action(::blender::ui::Layout *layout);
/** Mark the most recently created Checkbox button. */
void UI_layout_mixar_mark_last_toggle(::blender::ui::Layout *layout);
/** Mark the most recently created Text button. */
void UI_layout_mixar_mark_last_input(::blender::ui::Layout *layout);

/* -------------------------------------------------------------------- */
/* Custom panel category tab drawing for MIXIE space                     */

void UI_panel_category_draw_all_mixar(::blender::ARegion *region, const char *category_id_active);
