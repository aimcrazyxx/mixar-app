<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 API scan

Scanned commit: `e0f49e1fb12e3a0ae8b5afe7e428479c6ac89550`

The audit is report-only; it never rewrites source files.

## legacy uiLayout type

Count: **0**

- None

## legacy uiBut type

Count: **0**

- None

## legacy uiBlock type

Count: **0**

- None

## legacy ButType enum

Count: **87**

- `src/source/blender/editors/interface/interface_mixar_section.cc:52` — `if (but->type == ButType::Roundbox) {`
- `src/source/blender/editors/interface/interface_mixar_section.cc:68` — `if (ELEM(but->type, ButType::Menu, ButType::Block, ButType::Popover)) {`
- `src/source/blender/editors/interface/interface_mixar_section.cc:81` — `if (but->type == ButType::But) {`
- `src/source/blender/editors/interface/interface_mixar_section.cc:94` — `if (ELEM(but->type, ButType::Checkbox, ButType::CheckboxN)) {`
- `src/source/blender/editors/interface/interface_mixar_section.cc:107` — `if (but->type == ButType::Text) {`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:341` — `uiDefBut(move_block, ButType::Label, 0, IFACE_("Move"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:343` — `uiDefBut(move_block, ButType::Label, 0, IFACE_("X"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:346` — `but = uiDefButF(move_block, ButType::Num, B_MIXAR_UVEDIT_VERTEX, "",`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:351` — `uiDefBut(move_block, ButType::Label, 0, IFACE_("Y"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:354` — `but = uiDefButF(move_block, ButType::Num, B_MIXAR_UVEDIT_VERTEX, "",`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:382` — `uiDefBut(angle_block, ButType::Label, 0, IFACE_("Rotation Angle"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:385` — `::blender::ui::Button *angle_but = uiDefButF(angle_block, ButType::Num,`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:402` — `uiDefBut(scale_block, ButType::Label, 0, IFACE_("Scale"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:404` — `uiDefBut(scale_block, ButType::Label, 0, IFACE_("X"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:407` — `but = uiDefButF(scale_block, ButType::Num, B_MIXAR_UVEDIT_SCALE, "",`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:412` — `uiDefBut(scale_block, ButType::Label, 0, IFACE_("Y"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:415` — `but = uiDefButF(scale_block, ButType::Num, B_MIXAR_UVEDIT_SCALE, "",`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:458` — `uiDefBut(apply_move_block, ButType::But, B_MIXAR_UVEDIT_MOVE_AXIS,`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:492` — `uiDefBut(cursor_block, ButType::Label, 0, IFACE_("X"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:494` — `but = uiDefButF(cursor_block, ButType::Num, B_MIXAR_UVEDIT_CURSOR, "",`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:499` — `uiDefBut(cursor_block, ButType::Label, 0, IFACE_("Y"),`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:501` — `but = uiDefButF(cursor_block, ButType::Num, B_MIXAR_UVEDIT_CURSOR, "",`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:99` — `ButType button_type = ButType::Text;`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:113` — `button_type = ButType::Num;`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:117` — `button_type = ButType::Checkbox;`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:121` — `button_type = ButType::Menu;`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:131` — `if (button_type == ButType::Menu) {`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:135` — `else if (ELEM(button_type, ButType::Num, ButType::NumSlider, ButType::Text)) {`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:258` — `ButType::Menu,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:272` — `ButType::Menu,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:299` — `ButType::But,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:336` — `ButType::Text,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:352` — `ButType::But,`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:421` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:104` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:121` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:135` — `ButType::But,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:151` — `ButType::But,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:231` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:246` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:265` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:283` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:372` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:391` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:413` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:436` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:455` — `ButType::But,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:511` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:526` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:570` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:583` — `ButType::Label,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:726` — `ButType::Num,`
- `src/source/blender/editors/space_mixie/mixie_moodboard_sidebar_tabs/tab_scene_recon.cc:803` — `ButType::Text,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:347` — `ButType::Text,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:252` — `ButType::Text,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:325` — `ButType::Menu,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:379` — `ButType::Menu,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:410` — `ButType::But,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:436` — `ButType::But,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:514` — `ButType::But,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:526` — `ButType::But,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:538` — `ButType::But,`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:222` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:280` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:292` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:168` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:84` — `ButType::Label,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:188` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:209` — `ortho ? ButType::NumSlider : ButType::Menu,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:351` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:368` — `ButType::Toggle,`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:382` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:90` — `ButType::Row,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:182` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:266` — `ButType::Label,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:88` — `ButType::Text,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:198` — `ButType::Text,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:214` — `ButType::Menu,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:233` — `ButType::Num,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:248` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:269` — `ButType::Toggle,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:284` — `ButType::Toggle,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:299` — `ButType::Toggle,`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:392` — `ButType::NumSlider,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:106` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:117` — `ButType::But,`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:129` — `ButType::But,`

## legacy uiTextEdit type

Count: **0**

- None

## legacy uiWidgetStateInfo type

Count: **0**

- None

## legacy but_placeholder_get

Count: **0**

- None

## legacy UI_style_get

Count: **4**

- `src/source/blender/editors/interface/interface_mixar_section.cc:134` — `const uiStyle *style = UI_style_get();`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:52` — `uiFontStyle fstyle = UI_style_get()->widget;`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_layout.cc:66` — `*   font = UI_style_get()->widget with points * 1.2f */`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_layout.cc:67` — `uiFontStyle fstyle = UI_style_get()->widget;`

## legacy ui_fontscale

Count: **1**

- `src/source/blender/editors/interface/interface_mixar_section.cc:185` — `ui_fontscale(&fstyle_points, aspect);`

## legacy UI_fontstyle_set

Count: **3**

- `src/source/blender/editors/interface/interface_mixar_section.cc:136` — `UI_fontstyle_set(fstyle);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:53` — `UI_fontstyle_set(&fstyle);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_layout.cc:69` — `UI_fontstyle_set(&fstyle);`

## legacy ui_block_to_window

Count: **0**

- None

## legacy ui_window_to_block

Count: **0**

- None

## legacy ui_but_text_password_hide

Count: **0**

- None

## legacy UI_draw_roundbox_corner_set

Count: **15**

- `src/source/blender/editors/interface/interface_mixar_section.cc:229` — `UI_draw_roundbox_corner_set(UI_CNR_NONE);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:282` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:290` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard.cc:229` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:98` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:112` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:83` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:61` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:126` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:146` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_thumbnails.cc:227` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:264` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:223` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:88` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_draw.cc:61` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`

## legacy UI_draw_roundbox_4fv

Count: **20**

- `src/source/blender/editors/interface/interface_mixar_section.cc:230` — `UI_draw_roundbox_4fv(&bg_rect, true, 0.0f, col_strip_bg);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:244` — `UI_draw_roundbox_4fv(&edge_rect, true, 0.0f, edge_color);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:283` — `UI_draw_roundbox_4fv(&tab_rect, true, tab_radius, active_bg);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:286` — `UI_draw_roundbox_4fv(&tab_rect, false, tab_radius, active_outline);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:291` — `UI_draw_roundbox_4fv(&tab_rect, true, tab_radius, col_inactive);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:295` — `UI_draw_roundbox_4fv(&tab_rect, false, tab_radius, outline_color);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard.cc:230` — `UI_draw_roundbox_4fv(&frame, true, MOODBOARD_MEDIA_FRAME_RADIUS, background);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard.cc:231` — `UI_draw_roundbox_4fv(&frame, false, MOODBOARD_MEDIA_FRAME_RADIUS, border);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:99` — `UI_draw_roundbox_4fv(&rect, true, 22.0f, background);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:100` — `UI_draw_roundbox_4fv(&rect, false, 22.0f, border);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:119` — `UI_draw_roundbox_4fv(&halo, false, 25.0f, halo_color);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:121` — `UI_draw_roundbox_4fv(&rect, false, 22.0f, border);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:84` — `UI_draw_roundbox_4fv(&rect, true, 16.0f, background);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:85` — `UI_draw_roundbox_4fv(&rect, false, 16.0f, border);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:62` — `UI_draw_roundbox_4fv(&gr, true, (float(pos.btn_size) + gp * 2.0f) * 0.5f, gc);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:127` — `UI_draw_roundbox_4fv(&track_rect, true, float(switch_track_h) * 0.5f, track_color);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:147` — `UI_draw_roundbox_4fv(&knob_rect, true, float(knob_diameter) * 0.5f, knob_color);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_thumbnails.cc:230` — `UI_draw_roundbox_4fv(&rect, false, border_radius, color);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:224` — `UI_draw_roundbox_4fv(&active_dot, true, dot_size * 0.5f, active_color);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_draw.cc:62` — `UI_draw_roundbox_4fv(&rect, true, radius, color);`

## legacy UI_widgetbase_draw_cache_flush

Count: **0**

- None

## legacy UI_CNR constant

Count: **15**

- `src/source/blender/editors/interface/interface_mixar_section.cc:229` — `UI_draw_roundbox_corner_set(UI_CNR_NONE);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:282` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/interface/interface_mixar_section.cc:290` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard.cc:229` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:98` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_graph.cc:112` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:83` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:61` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:126` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:146` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_thumbnails.cc:227` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:264` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:223` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:88` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_draw.cc:61` — `UI_draw_roundbox_corner_set(UI_CNR_ALL);`

## old WM_operator_properties_create_ptr arity

Count: **19**

- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_graph.cc:115` — `WM_operator_properties_create_ptr(&props, ot);`
- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_graph.cc:133` — `WM_operator_properties_create_ptr(&props, ot);`
- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_graph.cc:155` — `WM_operator_properties_create_ptr(&props, menu_type);`
- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_graph.cc:433` — `WM_operator_properties_create_ptr(&props, menu_type);`
- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_select.cc:270` — `WM_operator_properties_create_ptr(&ptr, ot);`
- `src/source/blender/editors/space_mixie/mixie_moodboard_ops_select.cc:317` — `WM_operator_properties_create_ptr(&ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:438` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:458` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_history_util.cc:138` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_hit_testing.cc:340` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_hit_testing.cc:392` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_hit_testing.cc:478` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_main_region.cc:330` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_rules_util.cc:138` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_interaction.cc:76` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_interaction.cc:92` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_interaction.cc:115` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline_interaction.cc:135` — `WM_operator_properties_create_ptr(&op_ptr, ot);`
- `src/source/blender/editors/space_view3d/view3d_toast_click.cc:66` — `WM_operator_properties_create_ptr(&op_ptr, ot);`

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

## remaining uppercase UI block/button/popup API

Count: **0**

- None

## remaining old UI button constant

Count: **0**

- None

## remaining old UI block constant

Count: **0**

- None

## UString in Mixar Window RNA

Count: **1**

- `src/source/blender/makesrna/intern/rna_wm_mixar.cc:65` — `* exact key type from rna_internal_types.hh rather than the post-5.2 UString API. */`

## merge conflict marker

Count: **0**

- None

## Custom-space switch coverage

`anim_filter.cc` explicitly handles `SPACE_AGENT_BUBBLE`: **True**

## Intentional compatibility symbol

`UI_layout_disable_last_button_tooltip` is retained with the Blender 5.2 `blender::ui::Layout *` signature.

## Summary

Blocking stale-pattern hits: **165**
