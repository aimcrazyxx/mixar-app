<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 API scan

## Applied ports

- `uiLayout` → `blender::ui::Layout`: **33**
- `wmWindow::ghostwin` → `wmWindow::runtime->ghostwin`: **77**
- `MEM_callocN<T>` → `MEM_new_zeroed<T>`: **36**

## legacy uiLayout type

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

## legacy uiBut type

Count: **76**

- `src/source/blender/editors/interface/interface_handlers.cc:3292` — `static bool ui_but_is_multiline_text(const uiBut *but)`
- `src/source/blender/editors/interface/interface_handlers.cc:3310` — `static int ui_multiline_get_lines(uiBut *but,`
- `src/source/blender/editors/interface/interface_handlers.cc:3388` — `static void ui_textedit_move_vertical(uiBut *but,`
- `src/source/blender/editors/interface/interface_handlers.cc:3540` — `extern const uiBut *g_multiline_scroll_but;`
- `src/source/blender/editors/interface/interface_mixar_section.cc:51` — `uiBut *but = block->buttons[i].get();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:67` — `uiBut *but = block->buttons[i].get();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:80` — `uiBut *but = block->buttons[i].get();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:93` — `uiBut *but = block->buttons[i].get();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:106` — `uiBut *but = block->buttons[i].get();`
- `src/source/blender/editors/interface/interface_widgets.cc:5571` — `static void widget_mixar_section(uiBut *but,`
- `src/source/blender/editors/interface/interface_widgets.cc:5757` — `static void widget_mixar_action_button(uiBut * /*but*/,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:93` — `uiBut *operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:140` — `void disable_button(uiBut *button, const bool disabled)`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:157` — `uiBut *previous = operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:167` — `uiBut *play = operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:177` — `uiBut *next = operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:253` — `uiBut *explore = operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:304` — `uiBut *capture = operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:154` — `uiBut *lens = uiDefBlockBut(block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:167` — `uiBut *navigate = uiDefButO(block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:182` — `uiBut *aspect = uiDefBlockBut(block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:24` — `struct uiBut;`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:41` — `void director_popup_state(uiBut *but, bool active, bool enabled);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:58` — `uiBut *director_overlay_operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:68` — `void director_overlay_disable_button(uiBut *button, bool disabled);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:74` — `uiBut *add = director_overlay_operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:87` — `uiBut *name = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:117` — `uiBut *row = director_overlay_operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:132` — `uiBut *take = director_overlay_operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:144` — `uiBut *remove = director_overlay_operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:155` — `uiBut *finish = director_overlay_operator_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:197` — `uiBut *prompt = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:213` — `uiBut *adherence = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:232` — `uiBut *fps = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:247` — `uiBut *spacing = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:268` — `uiBut *thirds = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:283` — `uiBut *safe = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:298` — `uiBut *path = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:362` — `uiBut *left = director_overlay_operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:374` — `uiBut *right = director_overlay_operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:391` — `uiBut *seconds = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:89` — `uiBut *toggle = uiDefIconTextButR_prop(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:161` — `uiBut *export_stills = director_overlay_operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:181` — `uiBut *resolution = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:234` — `uiBut *render = director_overlay_operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:108` — `uiBut *button = uiDefIconBlockBut(block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:213` — `uiBut *auto_key = director_overlay_operator_button(`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:268` — `uiBut *director_overlay_operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:303` — `void director_overlay_disable_button(uiBut *button, const bool disabled)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:68` — `void director_popup_state(uiBut *but, const bool active, const bool enabled)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:99` — `uiBut *popup_op_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:144` — `uiBut *but = popup_op_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:174` — `uiBut *but = popup_op_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:187` — `uiBut *slider = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:208` — `uiBut *value = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:263` — `uiBut *but = popup_op_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:322` — `uiBut *left = popup_op_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:334` — `uiBut *right = popup_op_button(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:350` — `uiBut *spacing = uiDefButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:367` — `uiBut *handheld = uiDefIconTextButR(block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:381` — `uiBut *intensity = uiDefButR(block,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:251` — `uiBut *input_but = uiDefButR(block,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:346` — `uiBut *comment_but = uiDefButR(block,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:221` — `uiBut *remove_but = uiDefIconButO(remove_block,`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:339` — `uiBut *but;`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:385` — `uiBut *angle_but = uiDefButF(angle_block, ButType::Num,`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:490` — `uiBut *but;`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:48` — `static uiBut *screen_prop_button(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:88` — `static uiBut *add_parameter_button(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:151` — `static void disable_while_submitted(uiBut *button, const bool submitted)`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:254` — `uiBut *mode = screen_prop_button(block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:268` — `uiBut *model = screen_prop_button(block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:285` — `uiBut *parameter = add_parameter_button(`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:298` — `uiBut *reset = uiDefButO(block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:332` — `uiBut *prompt = screen_prop_button(block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:351` — `uiBut *generate = uiDefButO(block,`

## legacy uiBlock type

Count: **88**

- `src/source/blender/editors/interface/interface_handlers.cc:13599` — `uiBlock *agent_block = static_cast<uiBlock *>(menu->region->runtime->uiblocks.first);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:46` — `uiBlock *block = layout->block();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:63` — `uiBlock *block = layout->block();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:77` — `uiBlock *block = layout->block();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:90` — `uiBlock *block = layout->block();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:103` — `uiBlock *block = layout->block();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:141` — `((uiBlock *)region->runtime->uiblocks.first)->aspect;`
- `src/source/blender/editors/interface/interface_layout.cc:1501` — `* (where uiBlock is opaque) can suppress tooltips on a button it`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:93` — `uiBut *operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:147` — `void draw_transport(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:192` — `void draw_control_row(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:343` — `uiBlock *block = UI_block_begin(`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:122` — `void view3d_director_frame_controls_draw(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:23` — `struct uiBlock;`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:38` — `uiBlock *director_popup_block_begin(bContext *C, ARegion *region, const char *name);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:39` — `void director_popup_block_end(uiBlock *block);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:42` — `void director_popup_section_label(uiBlock *block, const char *text, int y, int width);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:46` — `uiBlock *view3d_director_lens_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:47` — `uiBlock *view3d_director_aspect_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:48` — `uiBlock *view3d_director_moves_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:49` — `uiBlock *view3d_director_shots_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:50` — `uiBlock *view3d_director_camera_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:51` — `uiBlock *view3d_director_animation_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:52` — `uiBlock *view3d_director_render_popup_create(bContext *C, ARegion *region, void *arg);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:58` — `uiBut *director_overlay_operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_intern.hh:71` — `void view3d_director_frame_controls_draw(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:49` — `uiBlock *shots_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:51` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:173` — `uiBlock *camera_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:175` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:322` — `uiBlock *animation_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:324` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:414` — `uiBlock *view3d_director_shots_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:419` — `uiBlock *view3d_director_camera_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:424` — `uiBlock *view3d_director_animation_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:57` — `UI_popup_menu_retval_set(static_cast<uiBlock *>(arg_block), UI_RETURN_OK, true);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:64` — `uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:116` — `uiBlock *render_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:118` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:285` — `uiBlock *view3d_director_render_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:53` — `void draw_tool_rail(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:125` — `void draw_empty_state(uiBlock *block, const ARegion *region, const int unit, const int gap)`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:158` — `void draw_context_actions(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:268` — `uiBut *director_overlay_operator_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:322` — `uiBlock *block = UI_block_begin(`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:55` — `uiBlock *director_popup_block_begin(bContext *C, ARegion *region, const char *name)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:57` — `uiBlock *block = UI_block_begin(C, region, name, blender::ui::EmbossType::Emboss);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:62` — `void director_popup_block_end(uiBlock *block)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:78` — `void director_popup_section_label(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:99` — `uiBut *popup_op_button(uiBlock *block,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:116` — `uiBlock *lens_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:118` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:232` — `uiBlock *aspect_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:234` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:286` — `uiBlock *moves_popup_create(bContext *C, ARegion *region, void * /*arg*/)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:288` — `uiBlock *block = director_popup_block_begin(C, region, __func__);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:403` — `uiBlock *view3d_director_lens_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:408` — `uiBlock *view3d_director_aspect_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:413` — `uiBlock *view3d_director_moves_popup_create(bContext *C, ARegion *region, void *arg)`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:242` — `uiBlock *block = UI_block_begin(C, region, __func__, blender::ui::EmbossType::Emboss);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:332` — `/* uiBlock buttons use region pixel coordinates for rendering and hit testing. */`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:344` — `uiBlock *block = UI_block_begin(C, region, block_name, blender::ui::EmbossType::Emboss);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:208` — `uiBlock *remove_block = UI_block_begin(`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:41` — `static uiBlock *mixie_chat_block_agent_bubble_create(bContext *C,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:47` — `uiBlock *block = UI_block_begin(`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:81` — `* Python menu hasn't loaded yet. Without this, an empty uiBlock`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_main_region.cc:388` — `/* Register uiBlock event handler so embedded text inputs (feedback comment)`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_main_region.cc:391` — `* uiBlock handler first actually makes it run AFTER the chat handler —`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_main_region.cc:395` — `* hit-target ever overlaps a uiBlock button, the click will be stolen from`
- `src/source/blender/editors/space_mixie_chat/space_mixie_chat.cc:316` — `* before the chat handler. main_region_init installs only the uiBlock handler`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:161` — `uiBlock *block = panel->layout->block();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:336` — `uiBlock *move_block = move_wrapper->absolute_block();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:378` — `uiBlock *angle_block = angle_wrapper->absolute_block();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:398` — `uiBlock *scale_block = scale_wrapper->absolute_block();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:456` — `uiBlock *apply_move_block = row->absolute_block();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:479` — `uiBlock *cursor_block = cursor_col->absolute_block();`
- `src/source/blender/editors/include/UI_interface_layout.hh:905` — `* interface_layout.cc where uiBlock is fully visible. */`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:48` — `static uiBut *screen_prop_button(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:88` — `static uiBut *add_parameter_button(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:158` — `static void add_action_toolbar(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:368` — `static void add_selected_media_toolbar(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:452` — `uiBlock *block = UI_block_begin(`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:73` — `static int draw_file_picker_image_section(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:171` — `static int draw_selected_moodboard_image(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:308` — `static int draw_status_section(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:477` — `static int draw_completion_section(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:549` — `static int draw_error_section(uiBlock *block,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:602` — `void draw_tab_scene_recon(const bContext *C, uiBlock *block, const TabContentLayout &layout)`

## legacy uiPopupMenu type

Count: **0**

- None

## legacy uiPopupBlockHandle type

Count: **0**

- None

## merge conflict marker

Count: **0**

- None

## Summary

Blocking stale-pattern hits: **0**
