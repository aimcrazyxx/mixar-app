<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 API scan

Exact implementation signatures ported: **0**

## legacy uiLayout type

Count: **32**

- `src/source/blender/editors/interface/interface_mixar_section.cc:43` — `uiLayout *UI_layout_mixar_section(uiLayout *layout)`
- `src/source/blender/editors/interface/interface_mixar_section.cc:45` — `uiLayout &box = layout->box();`
- `src/source/blender/editors/interface/interface_mixar_section.cc:61` — `void UI_layout_mixar_mark_last_dropdown(uiLayout *layout)`
- `src/source/blender/editors/interface/interface_mixar_section.cc:75` — `void UI_layout_mixar_mark_last_action(uiLayout *layout)`
- `src/source/blender/editors/interface/interface_mixar_section.cc:88` — `void UI_layout_mixar_mark_last_toggle(uiLayout *layout)`
- `src/source/blender/editors/interface/interface_mixar_section.cc:101` — `void UI_layout_mixar_mark_last_input(uiLayout *layout)`
- `src/source/blender/editors/interface/interface_mixar_section.hh:14` — `struct uiLayout;`
- `src/source/blender/editors/interface/interface_mixar_section.hh:37` — `uiLayout *UI_layout_mixar_section(uiLayout *layout);`
- `src/source/blender/editors/interface/interface_mixar_section.hh:45` — `void UI_layout_mixar_mark_last_dropdown(uiLayout *layout);`
- `src/source/blender/editors/interface/interface_mixar_section.hh:51` — `void UI_layout_mixar_mark_last_action(uiLayout *layout);`
- `src/source/blender/editors/interface/interface_mixar_section.hh:57` — `void UI_layout_mixar_mark_last_toggle(uiLayout *layout);`
- `src/source/blender/editors/interface/interface_mixar_section.hh:63` — `void UI_layout_mixar_mark_last_input(uiLayout *layout);`
- `src/source/blender/editors/space_mixie_chat/mixie_chat_agent_bubble.cc:62` — `uiLayout &layout = blender::ui::block_layout(block,`
- `src/source/blender/editors/sculpt_paint/paint_image_proj.cc:6930` — `uiLayout *layout = op->layout;`
- `src/source/blender/editors/sculpt_paint/paint_image_proj.cc:6945` — `uiLayout *col = &layout->column(true);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:172` — `uiLayout *col = &panel->layout->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:273` — `uiLayout *xform_box = &panel->layout->box();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:274` — `uiLayout *xform_col = &xform_box->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:334` — `uiLayout *move_wrapper = &xform_col->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:369` — `uiLayout *pivot_split = &xform_col->split(0.4f, false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:376` — `uiLayout *angle_wrapper = &xform_col->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:396` — `uiLayout *scale_wrapper = &xform_col->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:425` — `uiLayout *axis_box = &panel->layout->box();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:426` — `uiLayout *axis_col = &axis_box->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:444` — `uiLayout *sp = &axis_col->split(0.4f, false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:454` — `uiLayout *row = &axis_col->row(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:466` — `uiLayout *cursor_box = &panel->layout->box();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:467` — `uiLayout *cursor_col = &cursor_box->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:510` — `uiLayout *mirror_box = &panel->layout->box();`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:511` — `uiLayout *mirror_col = &mirror_box->column(false);`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:515` — `uiLayout *row = &mirror_col->row(true);`
- `src/source/blender/windowmanager/intern/wm_splash_screen.cc:404` — `uiLayout *row = &layout.row(true);`

## obsolete fmtlib target

Count: **0**

- None

## direct ghostwin access

Count: **74**

- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:317` — `if (w->ghostwin != ghostwin) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:379` — `if (win == nullptr || win->ghostwin == nullptr || win->ghostwin != g_bubble_ghostwin) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:383` — `if (candidate->ghostwin != g_bubble_ghostwin) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:404` — `if (win == nullptr || win->ghostwin == nullptr || win->ghostwin != g_bubble_ghostwin ||`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:412` — `bubble_set_min_content_size(win->ghostwin, height_floor);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:444` — `win->ghostwin, AGENT_BUBBLE_AUTOGROW_TOP_RESERVE);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:453` — `const_cast<bContext *>(C), win->ghostwin, AGENT_BUBBLE_DEFAULT_WIDTH, target_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:454` — `bubble_set_min_content_size(win->ghostwin, height_floor);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:554` — `if (w->ghostwin != g_pill_ghostwin) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:705` — `if (win->ghostwin == nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:729` — `Mixar_WindowMarkAsFloatingDock(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:731` — `Mixar_WindowSetChromeless(win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:732` — `Mixar_WindowSetFloatingLevel(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:733` — `Mixar_WindowSetHidesOnDeactivate(win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:734` — `Mixar_WindowSetCornerRadius(win->ghostwin, AGENT_BUBBLE_CORNER_RADIUS);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:737` — `C, win->ghostwin, AGENT_BUBBLE_DEFAULT_WIDTH, collapsed_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:738` — `bubble_set_min_content_size(win->ghostwin, collapsed_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:741` — `Mixar_WindowSetParentTracked(win->ghostwin, g_host_ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:746` — `Mixar_WindowSetParentPlain(win->ghostwin, g_host_ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:748` — `Mixar_WindowOrderFront(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:755` — `Mixar_WindowSnapToCentreBottomOfWindow(win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:759` — `g_bubble_ghostwin = win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:761` — `repaired_bubble = win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:766` — `Mixar_WindowMarkAsFloatingDock(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:768` — `Mixar_WindowSetBorderless(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:769` — `Mixar_WindowSetFloatingLevel(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:770` — `Mixar_WindowSetHidesOnDeactivate(win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:771` — `Mixar_WindowSetCornerRadius(win->ghostwin, AGENT_BUBBLE_PILL_CORNER_RADIUS);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:772` — `Mixar_WindowSetMinContentSize(win->ghostwin, 40, 20);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:773` — `g_pill_ghostwin = win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:774` — `repaired_pill = win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:907` — `if (first != nullptr && first->ghostwin != nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:908` — `Mixar_WindowMakeKey(first->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1121` — `if (invoker != nullptr && invoker->ghostwin != nullptr &&`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1122` — `invoker->ghostwin != g_bubble_ghostwin &&`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1123` — `invoker->ghostwin != g_pill_ghostwin)`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1125` — `g_host_ghostwin = invoker->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1227` — `if (win->ghostwin != nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1236` — `Mixar_WindowMarkAsFloatingDock(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1243` — `Mixar_WindowBindToParentSpace(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1248` — `Mixar_WindowSetChromeless(win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1256` — `Mixar_WindowSetFloatingLevel(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1263` — `Mixar_WindowSetHidesOnDeactivate(win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1269` — `Mixar_WindowSetCornerRadius(win->ghostwin, AGENT_BUBBLE_CORNER_RADIUS);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1278` — `C, win->ghostwin, AGENT_BUBBLE_DEFAULT_WIDTH, collapsed_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1279` — `bubble_set_min_content_size(win->ghostwin, collapsed_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1293` — `Mixar_WindowSnapToCentreBottomOfWindow(win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1298` — `Mixar_WindowSnapToCentreBottom(win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1304` — `bubble_set_min_content_size(win->ghostwin, collapsed_height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1311` — `g_bubble_ghostwin = win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1358` — `if (!Mixar_WindowHasChildWindow(win->ghostwin)) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1431` — `if (pill_win->ghostwin != nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1436` — `Mixar_WindowMarkAsFloatingDock(pill_win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1442` — `Mixar_WindowBindToParentSpace(pill_win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1452` — `Mixar_WindowSetBorderless(pill_win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1458` — `Mixar_WindowSetFloatingLevel(pill_win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1462` — `Mixar_WindowSetHidesOnDeactivate(pill_win->ghostwin, true);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1467` — `Mixar_WindowSetCornerRadius(pill_win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1473` — `Mixar_WindowSetMinContentSize(pill_win->ghostwin, 40, 20);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1474` — `Mixar_WindowForceSize(pill_win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1479` — `Mixar_WindowPositionAboveParent(pill_win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1480` — `win->ghostwin,`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1486` — `Mixar_WindowSetParent(pill_win->ghostwin, win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1491` — `g_pill_ghostwin = pill_win->ghostwin;`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1654` — `if (win == nullptr || win->ghostwin == nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1662` — `bubble_force_size_and_refresh(C, win->ghostwin, width, height);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1664` — `Mixar_WindowOrderFront(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1722` — `if (w->ghostwin != g_bubble_ghostwin) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1797` — `if (win == nullptr || win->ghostwin == nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1802` — `Mixar_WindowBeginDrag(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1820` — `if (win == nullptr || win->ghostwin == nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1824` — `Mixar_WindowUpdateDrag(win->ghostwin);`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1841` — `if (win == nullptr || win->ghostwin == nullptr) {`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:1845` — `Mixar_WindowEndDrag(win->ghostwin);`

## obsolete typed MEM_callocN

Count: **36**

- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:408` — `ARegionType *art = MEM_callocN<ARegionType>("spacetype view3d director timeline region");`
- `src/source/blender/editors/space_view3d/view3d_director_timeline.cc:423` — `art = MEM_callocN<ARegionType>("spacetype view3d legacy director timeline region");`
- `src/source/blender/editors/space_view3d/view3d_agent_strip_runtime.cc:528` — `ARegionType *art = MEM_callocN<ARegionType>("spacetype view3d agent strip region");`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:956` — `SpaceAgentBubble *sbubble = MEM_callocN<SpaceAgentBubble>("initagentbubble");`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:2311` — `art = MEM_callocN<ARegionType>("spacetype agent_bubble main region");`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:2328` — `art = MEM_callocN<ARegionType>("spacetype agent_bubble header region");`
- `src/source/blender/editors/space_agent_bubble/space_agent_bubble.cc:2352` — `art = MEM_callocN<ARegionType>("spacetype agent_bubble footer region");`
- `src/source/blender/editors/space_mixar_properties/space_mixar_properties.cc:38` — `SpaceMixarProperties *sprops = MEM_callocN<SpaceMixarProperties>("initmixarproperties");`
- `src/source/blender/editors/space_mixar_properties/space_mixar_properties.cc:134` — `ARegionType *art = MEM_callocN<ARegionType>("spacetype mixar_properties main");`
- `src/source/blender/editors/space_mixar_properties/space_mixar_properties.cc:144` — `art = MEM_callocN<ARegionType>("spacetype mixar_properties header");`
- `src/source/blender/editors/space_baking/space_baking.cc:45` — `SpaceBaking *sbaking = MEM_callocN<SpaceBaking>("initbaking");`
- `src/source/blender/editors/space_baking/space_baking.cc:182` — `ARegionType *art = MEM_callocN<ARegionType>("spacetype baking main");`
- `src/source/blender/editors/space_baking/space_baking.cc:192` — `art = MEM_callocN<ARegionType>("spacetype baking header");`
- `src/source/blender/editors/space_mixie_chat/space_mixie_chat.cc:110` — `smixie_chat = MEM_callocN<SpaceMixieChat>("initmixiechat");`
- `src/source/blender/editors/space_mixie_chat/space_mixie_chat.cc:312` — `art = MEM_callocN<ARegionType>("spacetype mixie_chat region");`
- `src/source/blender/editors/space_mixie_chat/space_mixie_chat.cc:335` — `art = MEM_callocN<ARegionType>("spacetype mixie_chat header region");`
- `src/source/blender/editors/space_mixie_chat/space_mixie_chat.cc:347` — `art = MEM_callocN<ARegionType>("spacetype mixie_chat footer region");`
- `src/source/blender/editors/sculpt_paint/paint_image_proj.cc:4471` — `PrepareImageEntry *e = MEM_callocN<PrepareImageEntry>("PrepareImageEntry");`
- `src/source/blender/editors/space_mixar_layers/space_mixar_layers.cc:38` — `SpaceMixarLayers *slayers = MEM_callocN<SpaceMixarLayers>("initmixarlayers");`
- `src/source/blender/editors/space_mixar_layers/space_mixar_layers.cc:183` — `art = MEM_callocN<ARegionType>("spacetype mixar_layers main");`
- `src/source/blender/editors/space_mixar_layers/space_mixar_layers.cc:193` — `art = MEM_callocN<ARegionType>("spacetype mixar_layers topbar");`
- `src/source/blender/editors/space_mixar_layers/space_mixar_layers.cc:203` — `art = MEM_callocN<ARegionType>("spacetype mixar_layers bottombar");`
- `src/source/blender/editors/space_texture_sets/space_texture_sets.cc:53` — `stexture_sets = MEM_callocN<SpaceTextureSets>("inittexturesets");`
- `src/source/blender/editors/space_texture_sets/space_texture_sets.cc:207` — `art = MEM_callocN<ARegionType>("spacetype texture_sets region");`
- `src/source/blender/editors/space_texture_sets/space_texture_sets.cc:219` — `art = MEM_callocN<ARegionType>("spacetype texture_sets header region");`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:183` — `PanelType *pt = MEM_callocN<PanelType>("mixar_uv_redo_panel");`
- `src/source/blender/editors/space_image/image_mixar_uv_panels.cc:536` — `PanelType *pt = MEM_callocN<PanelType>("mixar_uv_transform_panel");`
- `src/source/blender/editors/space_mixar_assets/space_mixar_assets.cc:38` — `SpaceMixarAssets *sassets = MEM_callocN<SpaceMixarAssets>("initmixarassets");`
- `src/source/blender/editors/space_mixar_assets/space_mixar_assets.cc:132` — `ARegionType *art = MEM_callocN<ARegionType>("spacetype mixar_assets main");`
- `src/source/blender/editors/space_mixar_assets/space_mixar_assets.cc:142` — `art = MEM_callocN<ARegionType>("spacetype mixar_assets header");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:87` — `smixie = MEM_callocN<SpaceMixie>("initmixie");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:702` — `art = MEM_callocN<ARegionType>("spacetype mixie region");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:715` — `art = MEM_callocN<ARegionType>("spacetype mixie tools region");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:729` — `art = MEM_callocN<ARegionType>("spacetype mixie footer region");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:741` — `art = MEM_callocN<ARegionType>("spacetype mixie ui region");`
- `src/source/blender/editors/space_mixie/space_mixie.cc:754` — `art = MEM_callocN<ARegionType>("spacetype mixie region");`

## merge conflict marker

Count: **0**

- None

## Summary

Total stale-pattern hits: **142**
