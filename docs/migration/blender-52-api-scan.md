<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 API scan

## Applied ports

- `uiLayout` → `blender::ui::Layout`: **0**
- `uiBut` → `blender::ui::Button`: **0**
- `uiBlock` → `blender::ui::Block`: **0**
- `absolute_block()` → `absolute(false).block()`: **0**
- `wmWindow::ghostwin` → `wmWindow::runtime->ghostwin`: **0**
- `MEM_callocN<T>` → `MEM_new_zeroed<T>`: **0**
- Renamed UI function calls: **15**

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

## remaining uppercase UI API

Count: **71**

- `src/source/blender/editors/interface/interface_widgets.cc:1457` — `const bool mixar_is_tool_icon = (but->icon != ICON_NONE) && UI_but_is_tool(but);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:143` — `UI_but_flag_enable(button, UI_BUT_DISABLED);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:264` — `UI_but_flag_enable(explore, UI_BUT_ACTIVE_DEFAULT);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:345` — `UI_block_theme_style_set(block, UI_BLOCK_THEME_STYLE_POPUP);`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:351` — `UI_block_draw(C, block);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay_frame.cc:178` — `UI_but_flag_enable(navigate, UI_BUT_ACTIVE_DEFAULT);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:126` — `RNA_int_set(UI_but_operator_ptr_ensure(row), "index", index);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:372` — `RNA_enum_set_identifier(C, UI_but_operator_ptr_ensure(left), "preset", pair.left_identifier);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_shot.cc:384` — `RNA_enum_set_identifier(C, UI_but_operator_ptr_ensure(right), "preset", pair.right_identifier);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:105` — `UI_but_flag_enable(toggle, UI_BUT_DISABLED);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:121` — `UI_block_flag_enable(block, UI_BLOCK_KEEP_OPEN);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:172` — `UI_but_func_set(export_stills, render_popup_close, block, nullptr);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:196` — `UI_but_flag_enable(resolution, UI_BUT_DISABLED);`
- `src/source/blender/editors/space_view3d/view3d_director_popup_render.cc:245` — `UI_but_func_set(render, render_popup_close, block, nullptr);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:224` — `UI_but_flag_enable(auto_key, UI_BUT_ACTIVE_DEFAULT);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:306` — `UI_but_flag_enable(button, UI_BUT_DISABLED);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:324` — `UI_block_theme_style_set(block, UI_BLOCK_THEME_STYLE_POPUP);`
- `src/source/blender/editors/space_view3d/view3d_director_overlay.cc:336` — `UI_block_draw(C, block);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:58` — `UI_block_theme_style_set(block, UI_BLOCK_THEME_STYLE_POPUP);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:64` — `UI_block_direction_set(block, UI_DIR_DOWN);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:65` — `UI_block_bounds_set_normal(block, int(0.4f * UI_UNIT_X));`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:71` — `UI_but_flag_enable(but, UI_BUT_ACTIVE_DEFAULT);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:74` — `UI_but_flag_enable(but, UI_BUT_DISABLED);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:154` — `C, UI_but_operator_ptr_ensure(but), "lens_type", types[index].identifier);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:183` — `RNA_int_set(UI_but_operator_ptr_ensure(but), "lens_mm", preset.mm);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:273` — `C, UI_but_operator_ptr_ensure(but), "preset", preset.identifier);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:332` — `C, UI_but_operator_ptr_ensure(left), "move", pair.left_identifier);`
- `src/source/blender/editors/space_view3d/view3d_director_popup.cc:344` — `C, UI_but_operator_ptr_ensure(right), "move", pair.right_identifier);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:271` — `UI_but_placeholder_set(input_but, mixie_chat_footer_next_placeholder(input_is_empty));`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:274` — `UI_but_flag2_enable(input_but, UI_BUT2_ACTIVATE_ON_INIT_NO_SELECT);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:280` — `* NOTE: Do NOT use UI_but_func_set here - that callback fires on focus loss too. */`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:281` — `UI_but_flag_enable(input_but, UI_BUT_TEXTEDIT_UPDATE);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:400` — `UI_block_emboss_set(block, blender::ui::EmbossType::None);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:550` — `UI_block_emboss_set(block, blender::ui::EmbossType::Emboss);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer.cc:554` — `UI_block_draw(C, block);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:361` — `UI_but_placeholder_set(comment_but, "Add a comment (optional) \xe2\x80\x94 press Enter to send");`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:362` — `UI_but_flag_enable(comment_but, UI_BUT_TEXTEDIT_UPDATE);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_feedback.cc:367` — `UI_block_draw(C, block);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:231` — `RNA_int_set(UI_but_operator_ptr_ensure(remove_but), "index", index);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_footer_draw.cc:238` — `UI_block_draw(C, remove_block);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:53` — `UI_block_flag_enable(block, UI_BLOCK_LOOP | UI_BLOCK_KEEP_OPEN | UI_BLOCK_NO_WIN_CLIP);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:54` — `UI_block_theme_style_set(block, UI_BLOCK_THEME_STYLE_POPUP);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:87` — `UI_block_bounds_set_centered(block, 6 * UI_SCALE_FAC);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:102` — `UI_popup_block_invoke(C, mixie_chat_block_agent_bubble_create, nullptr, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:162` — `UI_block_func_handle_set(block, mixar_uv_redo_cb, op);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:337` — `UI_block_func_handle_set(move_block, do_mixar_uvedit_transform, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:349` — `UI_but_number_step_size_set(but, step);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:350` — `UI_but_number_precision_set(but, digits);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:358` — `UI_but_number_step_size_set(but, step);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:359` — `UI_but_number_precision_set(but, digits);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:379` — `UI_block_func_handle_set(angle_block, do_mixar_uvedit_transform, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:391` — `UI_but_number_step_size_set(angle_but, 1);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:392` — `UI_but_number_precision_set(angle_but, 3);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:399` — `UI_block_func_handle_set(scale_block, do_mixar_uvedit_transform, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:410` — `UI_but_number_step_size_set(but, 1);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:411` — `UI_but_number_precision_set(but, 3);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:419` — `UI_but_number_step_size_set(but, 1);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:420` — `UI_but_number_precision_set(but, 3);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:457` — `UI_block_func_handle_set(apply_move_block, do_mixar_uvedit_transform, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:480` — `UI_block_func_handle_set(cursor_block, do_mixar_uvedit_transform, nullptr);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:497` — `UI_but_number_step_size_set(but, step);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:498` — `UI_but_number_precision_set(but, digits);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:504` — `UI_but_number_step_size_set(but, step);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:505` — `UI_but_number_precision_set(but, digits);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:154` — `UI_but_disable(button, "Settings are locked while this generation is running");`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:308` — `RNA_string_set(UI_but_operator_ptr_ensure(reset), "node_id", reset_node_id);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:342` — `UI_but_placeholder_set(prompt, "Describe what you want to create...");`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:343` — `UI_but_flag_enable(prompt, UI_BUT_TEXTEDIT_UPDATE);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:361` — `RNA_string_set(UI_but_operator_ptr_ensure(generate), "node_id", node_id);`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:363` — `UI_but_disable(generate, "Generation is already running");`
- `src/source/blender/editors/space_mixie/mixie_draw_moodboard_node_ui.cc:465` — `UI_block_draw(C, block);`

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
