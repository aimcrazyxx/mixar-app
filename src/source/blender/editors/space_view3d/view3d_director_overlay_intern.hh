/* SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
 *
 * SPDX-License-Identifier: GPL-3.0-or-later */

/** \file
 * \ingroup spview3d
 *
 * Shared helpers between the Director overlay implementation files.
 * Not part of the space API.
 */

#pragma once

#include "RNA_types.hh"

#include "view3d_director.hh"

struct ARegion;
struct Camera;
struct Object;
struct bContext;
struct rctf;
namespace blender::ui {
struct Block;
}
namespace blender::ui {
struct Button;
}

/** Everything a Director popup reads, resolved once at block-create time. */
struct DirectorPopupData {
  DirectorViewState state;
  PointerRNA state_ptr = {};
  PointerRNA shot_ptr = {};
  Object *camera_object = nullptr;
  Camera *camera = nullptr;
  PointerRNA camera_data_ptr = {};
  bool editable = false;
};

bool director_popup_data_get(bContext *C, DirectorPopupData *r_data);
::blender::ui::Block *director_popup_block_begin(bContext *C, ARegion *region, const char *name);
void director_popup_block_end(::blender::ui::Block *block);
/** Accent-depress the active choice; grey out what a locked take forbids. */
void director_popup_state(::blender::ui::Button *but, bool active, bool enabled);
void director_popup_section_label(::blender::ui::Block *block, const char *text, int y, int width);

/** Flow-styled popup blocks (view3d_director_popup*.cc); presentation only —
 * every row invokes the Python-owned `mixar.director_*` operators. */
::blender::ui::Block *view3d_director_lens_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_aspect_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_moves_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_shots_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_camera_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_animation_popup_create(bContext *C, ARegion *region, void *arg);
::blender::ui::Block *view3d_director_render_popup_create(bContext *C, ARegion *region, void *arg);

/** Rounded Flow-style panel in the shared Director palette. */
void director_overlay_panel_draw(const rctf &rect, float radius);

/** Icon (+ optional label) button that invokes a Python-owned operator. */
::blender::ui::Button *director_overlay_operator_button(::blender::ui::Block *block,
                                        const char *operator_id,
                                        int icon,
                                        const char *label,
                                        int x,
                                        int y,
                                        int width,
                                        int height,
                                        const char *tooltip);

void director_overlay_disable_button(::blender::ui::Button *button, bool disabled);

/** Lens, navigation, aspect, and frame tools pinned to the camera gate. */
void view3d_director_frame_controls_draw(::blender::ui::Block *block,
                                         const bContext *C,
                                         const ARegion *region,
                                         const DirectorViewState &state,
                                         int unit,
                                         int gap);
