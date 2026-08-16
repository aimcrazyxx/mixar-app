<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Latest Blender 5.2 repair workflow

```json
{"conclusion":"failure","createdAt":"2026-08-16T11:53:51Z","databaseId":31945573705,"headSha":"125a2fac24006f6af15396933fecb3d56d16fcfb","jobs":[{"completedAt":"2026-08-16T11:54:02Z","conclusion":"failure","databaseId":95160901709,"name":"repair","startedAt":"2026-08-16T11:53:55Z","status":"completed","steps":[{"completedAt":"2026-08-16T11:53:57Z","conclusion":"success","name":"Set up job","number":1,"startedAt":"2026-08-16T11:53:56Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"success","name":"Run actions/checkout@v4","number":2,"startedAt":"2026-08-16T11:53:57Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"success","name":"Synchronize main before editing","number":3,"startedAt":"2026-08-16T11:54:00Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"failure","name":"Port Mixar widgets and explicit custom-space handling","number":4,"startedAt":"2026-08-16T11:54:00Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"skipped","name":"Commit repairs to main","number":5,"startedAt":"2026-08-16T11:54:00Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"skipped","name":"Run the complete stale-API audit","number":6,"startedAt":"2026-08-16T11:54:00Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"success","name":"Post Run actions/checkout@v4","number":12,"startedAt":"2026-08-16T11:54:00Z","status":"completed"},{"completedAt":"2026-08-16T11:54:00Z","conclusion":"success","name":"Complete job","number":13,"startedAt":"2026-08-16T11:54:00Z","status":"completed"}],"url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31945573705/job/95160901709"}],"status":"completed","updatedAt":"2026-08-16T11:54:03Z","url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31945573705"}
```

```text
repair	Port Mixar widgets and explicit custom-space handling	﻿2026-08-16T11:54:00.4252520Z ##[group]Run python3 - <<'PY'
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4252965Z ^[[36;1mpython3 - <<'PY'^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4253262Z ^[[36;1mfrom pathlib import Path^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4253582Z ^[[36;1mimport re^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4253836Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4254265Z ^[[36;1mwidgets_path = Path("src/source/blender/editors/interface/interface_widgets.cc")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4254828Z ^[[36;1mwidgets = widgets_path.read_text(encoding="utf-8")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4255200Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4255534Z ^[[36;1mdef replace_counted(old: str, new: str, expected: int) -> None:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4255971Z ^[[36;1m    global widgets^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4256267Z ^[[36;1m    count = widgets.count(old)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4256588Z ^[[36;1m    if count == expected:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4256929Z ^[[36;1m        widgets = widgets.replace(old, new)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4257263Z ^[[36;1m        return^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4257528Z ^[[36;1m    if count == 0:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4257800Z ^[[36;1m        return^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4258277Z ^[[36;1m    raise RuntimeError(f"expected {expected} or 0 occurrence(s) of {old!r}, found {count}")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4258789Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4259096Z ^[[36;1mdef replace_once(old: str, new: str) -> None:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4259450Z ^[[36;1m    global widgets^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4259744Z ^[[36;1m    count = widgets.count(old)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4260054Z ^[[36;1m    if count == 1:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4260354Z ^[[36;1m        widgets = widgets.replace(old, new)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4260687Z ^[[36;1m        return^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4260963Z ^[[36;1m    if count == 0 and new in widgets:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4261719Z ^[[36;1m        return^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4262187Z ^[[36;1m    raise RuntimeError(f"expected one old fragment or an existing replacement; found {count}")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4262685Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4262981Z ^[[36;1m# Blender 5.2 names used by Mixar-only widget code.^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4263499Z ^[[36;1mreplace_counted("but_placeholder_get(but)", "button_placeholder_get(but)", 1)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4264063Z ^[[36;1mreplace_counted("uiWidgetStateInfo", "WidgetStateInfo", 5)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4264599Z ^[[36;1mreplace_counted("UI_draw_roundbox_corner_set", "draw_roundbox_corner_set", 5)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4265148Z ^[[36;1mreplace_counted("UI_draw_roundbox_4fv", "draw_roundbox_4fv", 8)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4265728Z ^[[36;1mreplace_counted("UI_widgetbase_draw_cache_flush()", "widgetbase_draw_cache_flush()", 1)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4266258Z ^[[36;1mreplace_counted("UI_CNR_ALL", "CNR_ALL", 5)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4266599Z ^[[36;1mreplace_once(^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4267016Z ^[[36;1m    "BLFWrapMode(int(BLFWrapMode::Typographical) | int(BLFWrapMode::HardLimit))",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4267566Z ^[[36;1m    "BLFWrapMode::Typographical | BLFWrapMode::HardLimit",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4267938Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4268162Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4268572Z ^[[36;1m# Keep upstream icon geometry while suppressing the search clear icon in multiline chat.^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4269057Z ^[[36;1mold_icon = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4269431Z ^[[36;1m    "  /* extra icons, e.g. 'x' icon to clear text or icon for eyedropper */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4269931Z ^[[36;1m    "  widget_draw_extra_icons(wcol, but, rect, alpha);\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4270291Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4270520Z ^[[36;1mnew_icon = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4270870Z ^[[36;1m    "  /* Extra icons, e.g. 'x' to clear text or the eyedropper.\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4272081Z ^[[36;1m    "   * Multiline chat input owns the full text rectangle and must not draw them. */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4272657Z ^[[36;1m    "  if (!ui_but_is_multiline_text(but)) {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4273081Z ^[[36;1m    "    widget_draw_extra_icons(wcol, but, rect, alpha);\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4273465Z ^[[36;1m    "  }\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4273710Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4273964Z ^[[36;1mreplace_once(old_icon, new_icon)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4274454Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4274688Z ^[[36;1mold_duplicate_icon = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4274974Z ^[[36;1m    "\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4275340Z ^[[36;1m    "  /* extra icons, e.g. 'x' icon to clear text or icon for eyedropper.\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4275908Z ^[[36;1m    "   * For multiline text buttons, skip extra icons (the VALUE_CLEAR 'x' icon\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4276521Z ^[[36;1m    "   * is auto-added by TEXTEDIT_UPDATE for search fields, not wanted here). */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4277029Z ^[[36;1m    "  if (!ui_but_is_multiline_text(but)) {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4277440Z ^[[36;1m    "    widget_draw_extra_icons(wcol, but, rect, alpha);\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4277805Z ^[[36;1m    "  }\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4278045Z ^[[36;1m    "\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4278412Z ^[[36;1m    "  /* Multi-line text buttons handle their own wrapping and drawing */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4278836Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4279077Z ^[[36;1mnew_multiline_comment = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4279365Z ^[[36;1m    "\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4279728Z ^[[36;1m    "  /* Multi-line text buttons handle their own wrapping and drawing. */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4280154Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4280464Z ^[[36;1mreplace_once(old_duplicate_icon, new_multiline_comment)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4280836Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4281306Z ^[[36;1m# Preserve Blender 5.2's vertical-text clipping bypass.^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4281690Z ^[[36;1mold_clipping = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4281959Z ^[[36;1m    "  else {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4282351Z ^[[36;1m    "    /* clip but->drawstr to fit in available space */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4282765Z ^[[36;1m    "    if (but->editstr && but->pos >= 0) {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4283090Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4283319Z ^[[36;1mnew_clipping = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4283578Z ^[[36;1m    "  else {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4283911Z ^[[36;1m    "    if (but->text_direction != TextDirection::Default) {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4284332Z ^[[36;1m    "      /* Do not clip vertical text. */\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4284652Z ^[[36;1m    "    }\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4284955Z ^[[36;1m    "    else if (but->editstr && but->pos >= 0) {\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4285285Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4285549Z ^[[36;1mreplace_once(old_clipping, new_clipping)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4285872Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4286106Z ^[[36;1mstale_widget_patterns = {^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4286499Z ^[[36;1m    "but_placeholder_get": r"\bbut_placeholder_get\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4286922Z ^[[36;1m    "uiWidgetStateInfo": r"\buiWidgetStateInfo\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4287380Z ^[[36;1m    "UI_draw_roundbox_corner_set": r"\bUI_draw_roundbox_corner_set\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4287845Z ^[[36;1m    "UI_draw_roundbox_4fv": r"\bUI_draw_roundbox_4fv\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4288320Z ^[[36;1m    "UI_widgetbase_draw_cache_flush": r"\bUI_widgetbase_draw_cache_flush\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4288785Z ^[[36;1m    "UI_CNR_*": r"\bUI_CNR_[A-Z0-9_]+\b",^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4289095Z ^[[36;1m}^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4289393Z ^[[36;1mfor label, pattern in stale_widget_patterns.items():^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4289780Z ^[[36;1m    if re.search(pattern, widgets):^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4290215Z ^[[36;1m        raise RuntimeError(f"stale Blender 5.0 widget API remains: {label}")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4354081Z ^[[36;1mif widgets.count("widget_draw_extra_icons(wcol, but, rect, alpha);") != 1:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4354735Z ^[[36;1m    raise RuntimeError("widget_draw_extra_icons must have exactly one call")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4355496Z ^[[36;1mwidgets_path.write_text(widgets, encoding="utf-8")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4355880Z ^[[36;1m^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4356300Z ^[[36;1manim_path = Path("src/source/blender/editors/animation/anim_filter.cc")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4356861Z ^[[36;1manim = anim_path.read_text(encoding="utf-8")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4357231Z ^[[36;1mold = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4357685Z ^[[36;1m    "      case SPACE_MIXAR_ASSETS:\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4358018Z ^[[36;1m    "\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4358272Z ^[[36;1m    "      case SPACE_BAKING:\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4358596Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4358817Z ^[[36;1mnew = (^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4359083Z ^[[36;1m    "      case SPACE_MIXAR_ASSETS:\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4359536Z ^[[36;1m    "      case SPACE_AGENT_BUBBLE:\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4359990Z ^[[36;1m    "\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4360401Z ^[[36;1m    "      case SPACE_BAKING:\n"^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4360923Z ^[[36;1m)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4361330Z ^[[36;1mif old in anim:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4361606Z ^[[36;1m    if anim.count(old) != 1:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4362069Z ^[[36;1m        raise RuntimeError("unexpected custom-space switch shape")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4362577Z ^[[36;1m    anim = anim.replace(old, new)^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4362942Z ^[[36;1melif new not in anim:^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4363465Z ^[[36;1m    raise RuntimeError("could not add SPACE_AGENT_BUBBLE to animation context switch")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4363998Z ^[[36;1manim_path.write_text(anim, encoding="utf-8")^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4364335Z ^[[36;1mPY^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4364571Z ^[[36;1mgit diff --check^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4364885Z ^[[36;1m! git grep -nE '^(<<<<<<<|=======|>>>>>>>)' -- src^[[0m
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4402270Z shell: /usr/bin/bash -e {0}
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.4402583Z ##[endgroup]
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.5792085Z src/release/datafiles/blender_icons_geom.py:11:=============
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.5793405Z src/release/datafiles/blender_icons_geom.py:20:===========
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6666972Z src/scripts/mixar/modules/common/generation_params/core/engine.py:13:=========================================================
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6701528Z src/scripts/mixar/modules/paint/core/element/buffer_pool.py:13:=====================
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6702672Z src/scripts/mixar/modules/paint/core/element/buffer_pool.py:31:=============
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6703704Z src/scripts/mixar/modules/paint/core/element/buffer_pool.py:36:=============
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6704763Z src/scripts/mixar/modules/paint/core/element/buffer_pool.py:52:==============
repair	Port Mixar widgets and explicit custom-space handling	2026-08-16T11:54:00.6880827Z ##[error]Process completed with exit code 1.
```
