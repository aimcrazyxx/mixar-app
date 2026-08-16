<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Latest Blender 5.2 Windows build

Requested commit: `92935261748f97dd9f266a3fa4cb2ec614e95369`

## Result

```json
{"conclusion":"failure","createdAt":"2026-08-16T18:31:27Z","databaseId":31964847354,"headSha":"92935261748f97dd9f266a3fa4cb2ec614e95369","jobs":[{"completedAt":"2026-08-16T19:07:16Z","conclusion":"failure","databaseId":95208326005,"name":"Prod / Blender 5.2","startedAt":"2026-08-16T18:31:30Z","status":"completed","steps":[{"completedAt":"2026-08-16T18:31:32Z","conclusion":"success","name":"Set up job","number":1,"startedAt":"2026-08-16T18:31:31Z","status":"completed"},{"completedAt":"2026-08-16T18:31:33Z","conclusion":"success","name":"Configure git and derive short sha","number":2,"startedAt":"2026-08-16T18:31:32Z","status":"completed"},{"completedAt":"2026-08-16T18:31:40Z","conclusion":"success","name":"Checkout fork","number":3,"startedAt":"2026-08-16T18:31:33Z","status":"completed"},{"completedAt":"2026-08-16T18:31:40Z","conclusion":"success","name":"Verify batch files use CRLF","number":4,"startedAt":"2026-08-16T18:31:40Z","status":"completed"},{"completedAt":"2026-08-16T18:31:41Z","conclusion":"success","name":"Start the disk ledger","number":5,"startedAt":"2026-08-16T18:31:40Z","status":"completed"},{"completedAt":"2026-08-16T18:31:44Z","conclusion":"success","name":"Report runner state","number":6,"startedAt":"2026-08-16T18:31:41Z","status":"completed"},{"completedAt":"2026-08-16T18:31:44Z","conclusion":"success","name":"Tune build parallelism","number":7,"startedAt":"2026-08-16T18:31:44Z","status":"completed"},{"completedAt":"2026-08-16T18:39:08Z","conclusion":"success","name":"Reclaim disk space (hosted runners only)","number":8,"startedAt":"2026-08-16T18:31:44Z","status":"completed"},{"completedAt":"2026-08-16T18:39:30Z","conclusion":"success","name":"Install NSIS, Ninja and sccache if missing","number":9,"startedAt":"2026-08-16T18:39:08Z","status":"completed"},{"completedAt":"2026-08-16T18:39:31Z","conclusion":"success","name":"Restore compiler cache","number":10,"startedAt":"2026-08-16T18:39:30Z","status":"completed"},{"completedAt":"2026-08-16T18:43:55Z","conclusion":"success","name":"Pin upstream to the requested Blender revision","number":11,"startedAt":"2026-08-16T18:39:31Z","status":"completed"},{"completedAt":"2026-08-16T18:43:55Z","conclusion":"success","name":"Check the resource version matches the pinned tag","number":12,"startedAt":"2026-08-16T18:43:55Z","status":"completed"},{"completedAt":"2026-08-16T18:47:59Z","conclusion":"success","name":"Fetch Blender precompiled libraries","number":13,"startedAt":"2026-08-16T18:43:55Z","status":"completed"},{"completedAt":"2026-08-16T18:48:08Z","conclusion":"success","name":"Measure what the libraries cost","number":14,"startedAt":"2026-08-16T18:47:59Z","status":"completed"},{"completedAt":"2026-08-16T18:48:08Z","conclusion":"skipped","name":"Apply backend URL override","number":15,"startedAt":"2026-08-16T18:48:08Z","status":"completed"},{"completedAt":"2026-08-16T18:48:08Z","conclusion":"success","name":"Prepare .env","number":16,"startedAt":"2026-08-16T18:48:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:06Z","conclusion":"failure","name":"Build Mixar","number":17,"startedAt":"2026-08-16T18:48:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:06Z","conclusion":"success","name":"Compiler cache statistics","number":18,"startedAt":"2026-08-16T19:07:06Z","status":"completed"},{"completedAt":"2026-08-16T19:07:08Z","conclusion":"success","name":"Save compiler cache","number":19,"startedAt":"2026-08-16T19:07:06Z","status":"completed"},{"completedAt":"2026-08-16T19:07:08Z","conclusion":"skipped","name":"Overlay Mixar scripts into the bundle","number":20,"startedAt":"2026-08-16T19:07:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:08Z","conclusion":"skipped","name":"Package installer and portable zip","number":21,"startedAt":"2026-08-16T19:07:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:08Z","conclusion":"skipped","name":"Summarize artifacts","number":22,"startedAt":"2026-08-16T19:07:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:08Z","conclusion":"skipped","name":"Upload installer and portable build","number":23,"startedAt":"2026-08-16T19:07:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:10Z","conclusion":"success","name":"Publish the failure report","number":24,"startedAt":"2026-08-16T19:07:08Z","status":"completed"},{"completedAt":"2026-08-16T19:07:11Z","conclusion":"success","name":"Failure diagnostics","number":25,"startedAt":"2026-08-16T19:07:10Z","status":"completed"},{"completedAt":"2026-08-16T19:07:12Z","conclusion":"success","name":"Upload logs","number":26,"startedAt":"2026-08-16T19:07:11Z","status":"completed"},{"completedAt":"2026-08-16T19:07:14Z","conclusion":"success","name":"Post Checkout fork","number":52,"startedAt":"2026-08-16T19:07:12Z","status":"completed"},{"completedAt":"2026-08-16T19:07:14Z","conclusion":"success","name":"Complete job","number":53,"startedAt":"2026-08-16T19:07:14Z","status":"completed"}],"url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31964847354/job/95208326005"}],"status":"completed","updatedAt":"2026-08-16T19:07:16Z","url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31964847354"}
```

## Failed log

```text
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.4352352Z [3514/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sort_desc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.5353969Z [3515/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sound.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.5406579Z [3516/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sparkle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.5550212Z [3517/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\speaker.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.6509915Z [3518/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sphere.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.6616425Z [3519/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\spherecurve.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.6814498Z [3520/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\split_horizontal.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.8075257Z [3521/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\spreadsheet.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.8134793Z [3522/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\split_vertical.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.8871890Z [3523/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_error.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.9600048Z [3524/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_info.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.9645580Z [3525/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_error_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:14.9883836Z [3526/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_info_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.0782866Z [3527/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_warning.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.0814357Z [3528/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_warning_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.1167072Z [3529/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\statusbar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.1924761Z [3530/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_disable.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.1956953Z [3531/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_loc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.2376363Z [3532/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_vert.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.3113767Z [3533/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\strands.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.3165921Z [3534/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\stroke.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.3584514Z [3535/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\stylus_pressure.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.4375323Z [3536/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.4451563Z [3537/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncircle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.4972783Z [3538/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncurve.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.5696593Z [3539/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncylinder.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.5738932Z [3540/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_nsphere.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.6153117Z [3541/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_nsurface.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.6839487Z [3542/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\syntax_off.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.6892657Z [3543/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ntorus.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.7391807Z [3544/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\syntax_on.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.7985449Z [3545/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tag.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.8066481Z [3546/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\system.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.8580859Z [3547/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\temp.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.9165399Z [3548/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\text.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.9210511Z [3549/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\texture.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:15.9887341Z [3550/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\texture_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.0380976Z [3551/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\three_dots.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.0410523Z [3552/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\time.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.0971605Z [3553/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tool_settings.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.1520233Z [3554/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\topbar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.1557229Z [3555/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.2223532Z [3556/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracker.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.2637918Z [3557/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracker_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.2742508Z [3558/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.3330971Z [3559/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.3908057Z [3560/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_backwards_single.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.4132761Z [3561/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_clear_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.4863329Z [3562/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_clear_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.5655166Z [3563/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.5739371Z [3564/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_forwards_single.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.6341606Z [3565/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_refine_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.6946533Z [3566/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_refine_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.6976515Z [3567/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\transform_origins.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.7535967Z [3568/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\trash.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.8091481Z [3569/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_down.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.8130466Z [3570/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_down_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.8720588Z [3571/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_left.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.9272659Z [3572/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_right.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.9303909Z [3573/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_left_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:16.9934311Z [3574/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_right_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.0422189Z [3575/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_up_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.0460247Z [3576/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_up.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.1309100Z [3577/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uglypackage.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.1631918Z [3578/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unlinked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.1661448Z [3579/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\underline.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.2479655Z [3580/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unlocked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.2776239Z [3581/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unpinned.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.2805081Z [3582/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\url.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.3662248Z [3583/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\usb_drive.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.3921745Z [3584/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\usb_drive_large.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.3974934Z [3585/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\user.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.4788902Z [3586/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.5075530Z [3587/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_edgesel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.5115394Z [3588/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.5958070Z [3589/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_facesel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.6335049Z [3590/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_sync_select.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.6507635Z [3591/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_islandsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.7145930Z [3592/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_vertexsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.7515796Z [3593/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vertexsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.7553570Z [3594/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vertex_crease.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.8323655Z [3595/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view3d.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.8709141Z [3596/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_camera.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.8745213Z [3597/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\viewzoom.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.9447429Z [3598/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_camera_unselected.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.9892235Z [3599/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_ortho.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:17.9929939Z [3600/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_locked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.0632368Z [3601/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_pan.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.1112122Z [3602/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_unlocked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.1149005Z [3603/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_perspective.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.1813998Z [3604/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_zoom.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.2295205Z [3605/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_00.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.2337341Z [3606/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_01.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.2973785Z [3607/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_10.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.3467093Z [3608/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_11.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.3507563Z [3609/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\volume_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.4155268Z [3610/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.4625935Z [3611/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\warning_large.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.4664995Z [3612/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\window.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.5294110Z [3613/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wordwrap_off.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.5767252Z [3614/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\workspace.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.5838496Z [3615/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wordwrap_on.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.6469753Z [3616/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\world.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.7011776Z [3617/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\world_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.7080477Z [3618/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.7685408Z [3619/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\x.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.8209234Z [3620/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\xray.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.8308098Z [3621/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_all.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.8901319Z [3622/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_in.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.9407708Z [3623/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_out.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:18.9467144Z [3624/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_previous.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.0097127Z [3625/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_selected.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.0627213Z [3626/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_blade.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.0780786Z [3627/8229] Building CXX object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\svg_icons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.1273354Z [3628/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_both_handles.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.1799423Z [3629/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_crossc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.2032118Z [3630/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_crosshair.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.2483699Z [3631/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_dot.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.3027853Z [3632/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_e_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.3240520Z [3633/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_eraser.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.3828880Z [3634/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_ew_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.4235956Z [3635/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_eyedropper.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.4509179Z [3636/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.5050687Z [3637/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand_closed.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.5451968Z [3638/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand_point.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.5692648Z [3639/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_h_split.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.6208890Z [3640/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_knife.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.6642475Z [3641/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_left_handle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.6822549Z [3642/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_mute.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.7379176Z [3643/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_n_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.7935900Z [3644/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_nsew_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.8504140Z [3645/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_ns_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.9251862Z [3646/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_paint.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.9553688Z [3647/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pencil.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:19.9789159Z [3648/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pick_area.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.0808913Z [3649/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pointer.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.1033971Z [3650/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_s_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.1084309Z [3651/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_right_handle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.2064820Z [3652/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_slip.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.2171576Z [3653/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_swap_area.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.2215475Z [3654/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_stop.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.3272874Z [3655/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_text_edit.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.3344876Z [3656/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_v_split.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.3383496Z [3657/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_vertex_loop.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.4497999Z [3658/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_wait.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.4648447Z [3659/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_w_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.4680082Z [3660/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_x_move.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.5690954Z [3661/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_y_move.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.5792474Z [3662/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_zoom_out.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:20.5838707Z [3663/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_zoom_in.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.1119712Z [3664/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\preview_grease_pencil.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.1935522Z [3665/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\preview.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.2622752Z [3666/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\splash.png.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.2657393Z [3667/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\startup.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.3528893Z [3668/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\startup.mixar.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.3939235Z [3669/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_41_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.4170941Z [3670/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_40_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.5137899Z [3671/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_39_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.5332369Z [3672/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_38_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.5728025Z [3673/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_37_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.6531787Z [3674/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_36_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.6722735Z [3675/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_35_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.7101945Z [3676/8229] Linking CXX static library lib\bf_editor_datafiles.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.7118381Z [3677/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_34_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.7819646Z [3678/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_33_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.7968026Z [3679/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_32_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.8426980Z [3680/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_31_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.9050230Z [3681/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_30_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.9183848Z [3682/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_29_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:21.9659537Z [3683/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_28_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.0378321Z [3684/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_27_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.0659449Z [3685/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_26_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.1051828Z [3686/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_25_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.1793034Z [3687/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_24_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.2178504Z [3688/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_23_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.2338808Z [3689/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.3132208Z [3690/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.3559981Z [3691/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.3686942Z [3692/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.4444020Z [3693/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.4890494Z [3694/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.5151295Z [3695/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.5920560Z [3696/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.6394971Z [3697/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.6723684Z [3698/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.7311294Z [3699/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.7952790Z [3700/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.8127111Z [3701/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.8971368Z [3702/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.9590671Z [3703/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:22.9775040Z [3704/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.1074008Z [3705/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.1203766Z [3706/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.1576453Z [3707/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.2364669Z [3708/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.2479450Z [3709/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.3176182Z [3710/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.3673469Z [3711/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.3763568Z [3712/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_26_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.4322152Z [3713/8229] Linking C static library lib\bf_draw_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.4664354Z [3714/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_25_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.5221741Z [3715/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_23_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.5250662Z [3716/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_24_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.6068192Z [3717/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.6475330Z [3718/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.6679291Z [3719/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.7521906Z [3720/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.7850261Z [3721/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.7854323Z [3722/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.8838319Z [3723/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.9002357Z [3724/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:23.9174507Z [3725/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.0111379Z [3726/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.0294504Z [3727/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.0455714Z [3728/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.1482786Z [3729/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.1598394Z [3730/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.1743303Z [3731/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.2932286Z [3732/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.2968922Z [3733/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.3299123Z [3734/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.4127133Z [3735/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.4243064Z [3736/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.4581492Z [3737/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.5339331Z [3738/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.5522709Z [3739/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.6001590Z [3740/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_vert.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.6153373Z [3741/8229] Linking C static library lib\bf_gpu_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.6613196Z [3742/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_frag.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.6731516Z [3743/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_lib.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.7190152Z [3744/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_fallback_lib.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.7927160Z [3745/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\intern\ocio_shader_shared.hh.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:24.8412759Z [3746/8229] Linking C static library lib\bf_imbuf_opencolorio_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:25.3295180Z [3747/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\makesrna_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:25.5711163Z [3748/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_define.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:25.6529628Z [3749/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\makesrna.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:26.1024265Z [3750/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ID.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:26.4126497Z [3751/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_action.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:26.4648193Z [3752/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:26.8910222Z [3753/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animviz.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:27.2283248Z [3754/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_annotations.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:27.4925132Z [3755/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_armature.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:27.5119850Z [3756/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_asset.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:28.1326767Z [3757/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_attribute.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:28.2803258Z [3758/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_boid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:28.4641801Z [3759/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_blendfile_import.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:28.9791773Z [3760/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_brush.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:28.9962131Z [3761/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_cachefile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:29.3619253Z [3762/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_camera.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:29.8472429Z [3763/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_cloth.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:29.8520131Z [3764/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_collection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:30.1258612Z [3765/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:30.4963032Z [3766/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:30.6878905Z [3767/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_constraint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:30.9642711Z [3768/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:31.2803217Z [3769/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curveprofile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:31.4886734Z [3770/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curves.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:31.7986886Z [3771/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_depsgraph.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:32.1071340Z [3772/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_dynamicpaint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:32.2654571Z [3773/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fcurve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:32.6349503Z [3774/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fluid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:32.9376194Z [3775/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_grease_pencil.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:33.0985402Z [3776/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_image.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:33.4398603Z [3777/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_key.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:33.6230518Z [3778/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lattice.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:33.8756402Z [3779/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_layer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:34.1492038Z [3780/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_light.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:34.3974912Z [3781/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lightprobe.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:34.7030964Z [3782/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_linestyle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:34.7533696Z [3783/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_main.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:35.1836566Z [3784/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mask.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:35.6054946Z [3785/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_material.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:35.6733643Z [3786/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mesh.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:35.7864410Z [3787/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_meta.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:36.4689001Z [3788/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_movieclip.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:36.5775048Z [3789/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_nla.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:37.1286335Z [3790/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_modifier.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:37.3506670Z [3791/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_node_tree_interface.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:37.4890029Z [3792/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_node_socket.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:38.1942925Z [3793/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:38.2763054Z [3794/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object_force.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:38.2821485Z [3795/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_nodetree.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:38.7739992Z [3796/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_packedfile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:39.0532403Z [3797/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_palette.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:39.1205472Z [3798/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_particle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:39.3766001Z [3799/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pointcloud.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:39.8239623Z [3800/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pose.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:40.1250259Z [3801/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_render.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:40.1824259Z [3802/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_rigidbody.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:40.4418439Z [3803/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_rna.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:41.0379220Z [3804/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_scene.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:41.2052180Z [3805/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_screen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:41.3733480Z [3806/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sculpt_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:41.9182192Z [3807/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sequencer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:41.9677584Z [3808/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sound.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:42.0286776Z [3809/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_shader_fx.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:42.5709305Z [3810/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_speaker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:42.6148960Z [3811/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_test.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:43.0765534Z [3812/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_space.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:43.3420515Z [3813/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_text.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:43.4473591Z [3814/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_texture.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:43.8798000Z [3815/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_timeline.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:44.1478360Z [3816/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_tracking.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:44.4918929Z [3817/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:44.9129349Z [3818/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_vfont.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:45.1076738Z [3819/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_userdef.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:45.2634518Z [3820/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_volume.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:45.8395974Z [3821/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_mixar.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:46.0211049Z [3822/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:46.0422518Z [3823/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:46.5997912Z [3824/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_workspace.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:46.8183346Z [3825/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_world.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:46.8232391Z [3826/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_xr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:47.3816972Z [3827/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_usd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:47.3980484Z [3828/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_action_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:47.5098978Z [3829/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animation_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:47.9677481Z [3830/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_camera_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:47.9720293Z [3831/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_armature_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:48.0771287Z [3832/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curve_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:48.5777122Z [3833/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curves_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:48.7631973Z [3834/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fcurve_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:48.8590564Z [3835/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_grease_pencil_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:49.1910261Z [3836/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_image_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:49.3656147Z [3837/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lattice_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:49.7789930Z [3838/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_material_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:49.8134574Z [3839/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_main_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:49.9573675Z [3840/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mesh_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:50.3968045Z [3841/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_meta_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:50.4885522Z [3842/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:50.5415726Z [3843/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pose_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.1123446Z [3844/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_scene_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.1396417Z [3845/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sound_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.2351491Z [3846/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sequencer_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.7280630Z [3847/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_text_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.7925965Z [3848/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_space_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:51.8322510Z [3849/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_texture_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:52.3988101Z [3850/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_vfont_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:52.5200369Z [3851/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ui_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:52.8574881Z [3852/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.2111367Z [3853/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_gizmo_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.2465034Z [3854/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_workspace_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.3676817Z [3855/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.4940257Z [3856/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.6162603Z [3857/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.7034172Z [3858/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\__\__\__\__\intern\clog\clog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.7409641Z [3859/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.8379863Z [3860/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\__\__\makesdna\intern\dna_parse.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.8726866Z [3861/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:53.8944646Z [3862/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.0015730Z [3863/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.0228353Z [3864/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.0652869Z [3865/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.1410225Z [3866/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.1633778Z [3867/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.2117977Z [3868/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.2544787Z [3869/8229] Linking CXX executable bin\makesrna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.2753681Z [3870/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.2951542Z [3871/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.3436792Z [3872/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.4186749Z [3873/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.4316417Z [3874/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.4761568Z [3875/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.5542709Z [3876/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.5574583Z [3877/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.6040007Z [3878/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.6766417Z [3879/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.6967819Z [3880/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:54.7764163Z [3881/8229] Linking C static library lib\bf_compositor_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:55.4144352Z [3882/8229] Building CXX object intern\clog\CMakeFiles\bf_intern_clog.dir\clog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:55.5820020Z [3883/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\linear_solver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:55.6551581Z [3884/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\eigenvalues.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:55.9233716Z [3885/8229] Building CXX object intern\utfconv\CMakeFiles\bf_intern_utfconv.dir\utfconv.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.3960432Z [3886/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\matrix.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.4988826Z [3887/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\svd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.5661982Z [3888/8229] Building CXX object intern\utfconv\CMakeFiles\bf_intern_utfconv.dir\utf_winfunc.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.6029436Z [3889/8229] Building CXX object intern\uriconvert\CMakeFiles\bf_intern_uriconvert.dir\uri_convert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.6568031Z [3890/8229] Building C object extern\wcwidth\CMakeFiles\extern_wcwidth.dir\wcwidth.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.7924291Z [3891/8229] Building C object extern\xxhash\CMakeFiles\extern_xxhash.dir\xxhash.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:56.8204336Z [3892/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_assert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.1277699Z [3893/8229] Generating rna_ID_gen.cc, rna_action_gen.cc, rna_animation_gen.cc, rna_animviz_gen.cc, rna_annotations_gen.cc, rna_armature_gen.cc, rna_asset_gen.cc, rna_attribute_gen.cc, rna_blendfile_import_gen.cc, rna_boid_gen.cc, rna_brush_gen.cc, rna_cachefile_gen.cc, rna_camera_gen.cc, rna_cloth_gen.cc, rna_collection_gen.cc, rna_color_gen.cc, rna_constraint_gen.cc, rna_context_gen.cc, rna_curve_gen.cc, rna_curveprofile_gen.cc, rna_curves_gen.cc, rna_depsgraph_gen.cc, rna_dynamicpaint_gen.cc, rna_fcurve_gen.cc, rna_fluid_gen.cc, rna_grease_pencil_gen.cc, rna_image_gen.cc, rna_key_gen.cc, rna_lattice_gen.cc, rna_layer_gen.cc, rna_light_gen.cc, rna_lightprobe_gen.cc, rna_linestyle_gen.cc, rna_main_gen.cc, rna_mask_gen.cc, rna_material_gen.cc, rna_mesh_gen.cc, rna_meta_gen.cc, rna_modifier_gen.cc, rna_movieclip_gen.cc, rna_nla_gen.cc, rna_node_socket_gen.cc, rna_node_tree_interface_gen.cc, rna_nodetree_gen.cc, rna_object_gen.cc, rna_object_force_gen.cc, rna_packedfile_gen.cc, rna_palette_gen.cc, rna_particle_gen.cc, rna_pointcloud_gen.cc, rna_pose_gen.cc, rna_render_gen.cc, rna_rigidbody_gen.cc, rna_rna_gen.cc, rna_scene_gen.cc, rna_screen_gen.cc, rna_sculpt_paint_gen.cc, rna_sequencer_gen.cc, rna_shader_fx_gen.cc, rna_sound_gen.cc, rna_space_gen.cc, rna_speaker_gen.cc, rna_test_gen.cc, rna_text_gen.cc, rna_texture_gen.cc, rna_timeline_gen.cc, rna_tracking_gen.cc, rna_ui_gen.cc, rna_userdef_gen.cc, rna_vfont_gen.cc, rna_volume_gen.cc, rna_wm_gen.cc, rna_wm_mixar_gen.cc, rna_wm_gizmo_gen.cc, rna_workspace_gen.cc, rna_world_gen.cc, rna_xr_gen.cc, rna_usd_gen.cc, rna_prototypes_gen.hh, ../RNA_prototypes.hh
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.2121528Z [3894/8229] Linking CXX static library lib\bf_intern_clog.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.2494375Z [3895/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.2691927Z [3896/8229] Linking CXX static library lib\bf_intern_eigen.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.2719480Z [3897/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_dial_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.3326662Z [3898/8229] Linking CXX static library lib\bf_intern_utfconv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.3843664Z [3899/8229] Linking CXX static library lib\bf_intern_uriconvert.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.4048117Z [3900/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_colorspace.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.4502198Z [3901/8229] Linking C static library lib\extern_wcwidth.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:57.4987734Z [3902/8229] Linking C static library lib\extern_xxhash.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:58.1430894Z [3903/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_access_compare_override.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:58.2674757Z [3904/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_define.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:58.4458981Z [3905/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_access.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:58.8857660Z [3906/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_path.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:59.5813375Z [3907/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_ID_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:50:59.6734127Z [3908/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_action_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:00.1341524Z [3909/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_animation_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:00.7536017Z [3910/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_animviz_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:00.7763909Z [3911/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_annotations_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:01.3144135Z [3912/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_armature_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:01.8635571Z [3913/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_asset_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:02.1129846Z [3914/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_attribute_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:02.4582185Z [3915/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_blendfile_import_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:03.0031739Z [3916/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_boid_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:03.2985940Z [3917/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_brush_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:03.6048116Z [3918/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_cachefile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:04.1769378Z [3919/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_camera_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:04.4720484Z [3920/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_cloth_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:04.8357772Z [3921/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_collection_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:05.3840589Z [3922/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_color_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:05.6994947Z [3923/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_constraint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:05.9580285Z [3924/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_context_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:06.5639193Z [3925/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curve_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:06.8389104Z [3926/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curveprofile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:07.1965175Z [3927/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curves_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:07.7147855Z [3928/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_depsgraph_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:08.0152137Z [3929/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_dynamicpaint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:08.3746047Z [3930/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_fcurve_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:08.9583430Z [3931/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_fluid_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:09.3505902Z [3932/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_grease_pencil_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:09.6332511Z [3933/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_image_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:10.1389520Z [3934/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_key_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:10.5832607Z [3935/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_lattice_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:10.8854171Z [3936/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_layer_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:11.3839064Z [3937/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_light_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:11.7097979Z [3938/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_lightprobe_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:12.1510283Z [3939/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_linestyle_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:12.7591927Z [3940/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_main_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:12.9182565Z [3941/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_mask_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:13.5550650Z [3942/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_material_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:14.1339181Z [3943/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_mesh_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:14.1608012Z [3944/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_meta_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:15.3335696Z [3945/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_movieclip_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:15.3469576Z [3946/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_nla_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:15.3812574Z [3947/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_modifier_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:16.6163826Z [3948/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_node_socket_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:16.6652903Z [3949/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_node_tree_interface_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:17.6278512Z [3950/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_nodetree_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:17.8589198Z [3951/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_object_force_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:18.0763468Z [3952/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_object_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:18.7750063Z [3953/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_packedfile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:18.9982974Z [3954/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_palette_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:19.3653367Z [3955/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_particle_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:19.9951461Z [3956/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_pointcloud_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:20.2406399Z [3957/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_pose_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:20.6472580Z [3958/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_render_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:21.1595662Z [3959/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_rigidbody_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:21.3461425Z [3960/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_rna_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:22.1890809Z [3961/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_scene_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:22.4287625Z [3962/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_screen_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:22.6381702Z [3963/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sculpt_paint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:23.4924117Z [3964/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sequencer_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:23.5775176Z [3965/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_shader_fx_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:23.7593298Z [3966/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sound_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:24.6926438Z [3967/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_speaker_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:24.8496564Z [3968/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_test_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:24.9642258Z [3969/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_space_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:25.8312779Z [3970/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_text_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:26.1095187Z [3971/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_texture_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:26.2467472Z [3972/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_timeline_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:26.9988961Z [3973/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_tracking_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:27.4400396Z [3974/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_ui_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:27.9237669Z [3975/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_userdef_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:28.1025005Z [3976/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_vfont_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:28.5873595Z [3977/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_volume_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:29.1769128Z [3978/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_mixar_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:29.1976309Z [3979/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:29.7268266Z [3980/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_gizmo_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:30.3450639Z [3981/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_workspace_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:30.4122834Z [3982/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_world_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:30.8104059Z [3983/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_dynstr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:30.8596746Z [3984/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_xr_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:31.2837977Z [3985/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_ghash.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:31.4877363Z [3986/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_usd_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:31.6827953Z [3987/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_filelist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:31.7124876Z [3988/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_ghash_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.0012490Z [3989/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_heap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.1562838Z [3990/8229] Linking CXX static library lib\bf_rna.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.1855252Z [3991/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_heap_simple.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.3797417Z [3992/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_kdopbvh.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.4913775Z [3993/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_linklist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.7462330Z [3994/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_linklist_lockfree.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.7528773Z [3995/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memarena.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.8484979Z [3996/8229] Generating register_geometry_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:32.9251465Z [3997/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memblock.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.0436418Z [3998/8229] Building CXX object source\blender\nodes\geometry\CMakeFiles\bf_nodes_geometry_generated.dir\register_geometry_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.0985770Z [3999/8229] Linking CXX static library lib\bf_nodes_geometry_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.1689083Z [4000/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memiter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.2444952Z [4001/8229] Generating register_function_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.5103943Z [4002/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_mempool.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.6300826Z [4003/8229] Building CXX object source\blender\nodes\function\CMakeFiles\bf_nodes_functions_generated.dir\register_function_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.6855370Z [4004/8229] Linking CXX static library lib\bf_nodes_functions_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.9473253Z [4005/8229] Generating register_compositor_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.9668686Z [4006/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_mmap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:33.9826143Z [4007/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_timer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:34.3240276Z [4008/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store_rle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:34.4648619Z [4009/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:34.4828911Z [4010/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_subprocess.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:34.6919239Z [4011/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:34.9159198Z [4012/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_utils_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:35.1332426Z [4013/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\astar.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:35.4488588Z [4014/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:35.5971574Z [4015/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_bool_conversion.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:35.8273121Z [4016/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\atomic_disjoint_set.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:35.9002498Z [4017/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_ref.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.0759626Z [4018/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bitmap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.0976240Z [4019/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_span.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.4752332Z [4020/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\boxpack_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.4798180Z [4021/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bitmap_draw_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.6158432Z [4022/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\compression.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:36.6712900Z [4023/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cache_mutex.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:37.1094177Z [4024/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\compute_context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:37.2005474Z [4025/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\convexhull_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:37.2448111Z [4026/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cpp_type.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:37.8536687Z [4027/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cpp_types.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:37.9649441Z [4028/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\delaunay_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.1475192Z [4029/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\csv_parse.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.1587016Z [4030/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\easing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.3234649Z [4031/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\endian_switch.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.4466238Z [4032/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\dot_export.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.6795861Z [4033/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\expr_pylike_eval.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:38.9726961Z [4034/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fftw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:39.0176784Z [4035/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fileops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:39.6429845Z [4036/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_gzip.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:39.6738013Z [4037/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_file.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:39.9357197Z [4038/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fileops_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:40.0666014Z [4039/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fnmatch.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:40.5136217Z [4040/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_memory.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:40.5429624Z [4041/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_zstd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:40.7613877Z [4042/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_vector_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.1335937Z [4043/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\gsqueue.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.2226356Z [4044/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_virtual_vector_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.2911796Z [4045/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_virtual_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.3363500Z [4046/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_md5.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.3652657Z [4047/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_mm2a.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.4436879Z [4048/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_mm3.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.7793910Z [4049/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\implicit_sharing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:41.8609252Z [4050/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_tables.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:42.3619505Z [4051/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_range.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:42.4967549Z [4052/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_mask.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:42.7402679Z [4053/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_mask_expression.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:42.7449426Z [4054/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\jitter_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.0476495Z [4055/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\lasso_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.2056601Z [4056/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\lazy_threading.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.3941419Z [4057/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.4298507Z [4058/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\length_parameterize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.4453028Z [4059/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\listbase.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:43.9533104Z [4060/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_basis_types.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.0105187Z [4061/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.0619639Z [4062/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_boolean.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.1450111Z [4063/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.4750701Z [4064/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_half.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.4951453Z [4065/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.7171407Z [4066/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_interp.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:44.9285378Z [4067/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_matrix_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.1710870Z [4068/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_rotation_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.3340034Z [4069/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_rotation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.5485467Z [4070/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_solvers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.5629310Z [4071/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_matrix.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.7224973Z [4072/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_statistics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:45.7422659Z [4073/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_time.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:46.1461195Z [4074/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_vector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:46.1512496Z [4075/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_vec.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:46.3364736Z [4076/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_cache.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:46.6669527Z [4077/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_counter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:46.7981072Z [4078/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_cache_file_load.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:47.0900353Z [4079/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\mesh_boolean.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:47.3759403Z [4080/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\noise.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:47.4345667Z [4081/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\mesh_intersect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:47.5023579Z [4082/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\noise_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:47.9883358Z [4083/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\ordered_edge.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:48.3437229Z [4084/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\offset_indices.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:48.4134769Z [4085/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\polyfill_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:48.6447172Z [4086/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\quadric.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:48.7252714Z [4087/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\polyfill_2d_beautify.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:48.7447077Z [4088/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\path_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.2263974Z [4089/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\radial_tiling_wrapper.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.3865984Z [4090/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\rct.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.4038531Z [4091/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\rand.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.8099926Z [4092/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\resource_scope.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.8486131Z [4093/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\scanfill.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:49.9682583Z [4094/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\scanfill_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.1910883Z [4095/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\smaa_textures.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.3476322Z [4096/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\sort.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.4750065Z [4097/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\sort_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.6459611Z [4098/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\serialize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.6645375Z [4099/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\session_uid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:50.8423921Z [4100/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\stack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:51.1301292Z [4101/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:51.2324140Z [4102/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_cursor_utf8.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:51.6658934Z [4103/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\storage.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:51.6995796Z [4104/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_ref.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:51.8325526Z [4105/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_search.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:52.1186509Z [4106/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_utf8.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:52.2664081Z [4107/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:52.6333649Z [4108/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\system.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:52.6650749Z [4109/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_iterator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:52.6837452Z [4110/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_graph.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:53.1831114Z [4111/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_scheduler.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:53.2043125Z [4112/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_pool.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:53.5340104Z [4113/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_range.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:53.5679706Z [4114/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\tempfile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.0057898Z [4115/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\timecode.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.0397754Z [4116/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\threads.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.3576870Z [4117/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\time.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.6332921Z [4118/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\timeit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.7602889Z [4119/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\ustring.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:54.9409114Z [4120/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\uuid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:55.1042225Z [4121/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\voxel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:55.1826052Z [4122/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\vector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:55.4541263Z [4123/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\virtual_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:55.8010329Z [4124/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff_dir.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:56.2315203Z [4125/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_args.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:56.3716249Z [4126/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:56.8803963Z [4127/8229] Building CXX object source\blender\blentranslation\msgfmt\CMakeFiles\msgfmt.dir\msgfmt.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:56.9867575Z [4128/8229] Building CXX object source\blender\nodes\composite\CMakeFiles\bf_nodes_compositor_generated.dir\register_compositor_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.1071152Z [4129/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff_registration.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.1252007Z [4130/8229] Linking CXX static library lib\bf_nodes_compositor_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.2539311Z [4131/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\system_win32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.3777575Z [4132/8229] Linking CXX static library lib\bf_blenlib.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.7582753Z [4133/8229] Linking CXX executable bin\msgfmt.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.7902724Z [4134/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Buttons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:57.8703254Z [4135/8229] Generating ab.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.0056933Z [4136/8229] Generating ar.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.1008350Z [4137/8229] Generating be.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.2454538Z [4138/8229] Generating bg.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.3490293Z [4139/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_CallbackEventConsumer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.5716056Z [4140/8229] Generating ca.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.7440906Z [4141/8229] Generating cs.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:58.8469309Z [4142/8229] Generating da.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:59.0067279Z [4143/8229] Generating de.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:59.1002876Z [4144/8229] Generating el.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:59.4376467Z [4145/8229] Generating en_GB.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:59.4617788Z [4146/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:51:59.6839458Z [4147/8229] Generating eo.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.1416696Z [4148/8229] Generating es.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.1783971Z [4149/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextNone.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.2553025Z [4150/8229] Generating eu.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.3790764Z [4151/8229] Generating fa.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.5074110Z [4152/8229] Generating fi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.8667152Z [4153/8229] Generating fr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:00.8883802Z [4154/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_EventManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.0151638Z [4155/8229] Building CXX object source\blender\freestyle\CMakeFiles\bf_freestyle.dir\cmake_pch.cxx.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.0394353Z [4156/8229] Generating he.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.1385664Z [4157/8229] Generating hi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.2399365Z [4158/8229] Generating hr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.3514254Z [4159/8229] Generating hu.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.5100057Z [4160/8229] Generating id.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.8604592Z [4161/8229] Generating it.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:01.9387414Z [4162/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ISystemPaths.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:02.1566597Z [4163/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ISystem.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:02.4868850Z [4164/8229] Generating ja.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:02.5982665Z [4165/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ModifierKeys.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:02.7369618Z [4166/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_PathUtils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:02.8996652Z [4167/8229] Generating ka.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.1546157Z [4168/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Rect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.2207929Z [4169/8229] Generating ko.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.3165811Z [4170/8229] Generating ky.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.3439275Z [4171/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_System.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.4135984Z [4172/8229] Generating lt.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.5078403Z [4173/8229] Generating ml.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.6162667Z [4174/8229] Generating nb.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.7360447Z [4175/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_TimerManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.7497099Z [4176/8229] Generating nl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:03.9628136Z [4177/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Window.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:04.0918649Z [4178/8229] Generating pl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:04.3855144Z [4179/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_WindowManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:04.4048265Z [4180/8229] Generating pt.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:04.5833212Z [4181/8229] Generating pt_BR.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:04.6799858Z [4182/8229] Generating ro.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.0626873Z [4183/8229] Generating ru.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.0896224Z [4184/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_NDOFManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.2441059Z [4185/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextVK.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.4385685Z [4186/8229] Generating sk.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.6177197Z [4187/8229] Generating sl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.7324241Z [4188/8229] Generating sr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:05.8863867Z [4189/8229] Generating sr@latin.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:06.2266520Z [4190/8229] Generating sv.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:06.4398616Z [4191/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextD3D.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:06.6454846Z [4192/8229] Generating sw.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:06.7444950Z [4193/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_DropTargetWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.0065665Z [4194/8229] Generating ta.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.1038170Z [4195/8229] Generating th.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.3397065Z [4196/8229] Generating tr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.5573542Z [4197/8229] Generating uk.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.8421134Z [4198/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_TrackpadWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:07.8469324Z [4199/8229] Generating ur.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:08.2461381Z [4200/8229] Generating vi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:08.2544298Z [4201/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_SystemWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:08.5797551Z [4202/8229] Generating zh_HANS.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:08.8126736Z [4203/8229] Generating zh_HANT.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:09.1335587Z [4204/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Wintab.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:09.5070608Z [4205/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_WindowWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:10.0078374Z [4206/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextWGL.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:10.5751134Z [4207/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_NDOFManagerWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:10.6536932Z [4208/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ImeWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:11.6538311Z [4209/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Xr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:11.6811207Z [4210/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_SystemPathsWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:12.6849530Z [4211/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrAction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:12.8454099Z [4212/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrContext.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:13.8759038Z [4213/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrEvent.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:14.4203489Z [4214/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrControllerModel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:15.1589075Z [4215/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBinding.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:15.7156223Z [4216/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrSession.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:16.2025129Z [4217/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrSwapchain.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:16.9862595Z [4218/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBindingD3D.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:17.4483806Z [4219/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBindingVulkan.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:17.5441494Z [4220/8229] Linking CXX static library lib\bf_intern_ghost.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:17.9353799Z [4221/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\autotrack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:18.4287648Z [4222/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\camera_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:18.6975509Z [4223/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\detector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:19.3946733Z [4224/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\frame_accessor.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:19.6252843Z [4225/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\homography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:20.1016258Z [4226/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:20.3703859Z [4227/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\image.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:21.1387485Z [4228/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:21.3679417Z [4229/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\track_region.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:21.8548401Z [4230/8229] Building CXX object source\blender\io\usd\CMakeFiles\bf_io_usd.dir\cmake_pch.cxx.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:22.1496887Z [4231/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:22.3556899Z [4232/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\tracksN.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:22.8445771Z [4233/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\autotrack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:23.1380485Z [4234/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\predict_tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:23.3119971Z [4235/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\base\aligned_malloc.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:23.3423101Z [4236/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:23.6212521Z [4237/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\image\array_nd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:24.2598919Z [4238/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\image\convolve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:24.2929036Z [4239/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\conditioning.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:24.5946841Z [4240/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\euclidean_resection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:25.4528999Z [4241/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\fundamental.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:25.5250527Z [4242/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\homography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:25.5902107Z [4243/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\panography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:26.4594747Z [4244/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\panography_kernel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:26.4655042Z [4245/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\projection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:26.5188810Z [4246/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\triangulation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:26.5799903Z [4247/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\numeric\poly.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:27.4111394Z [4248/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\numeric\numeric.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:27.5588904Z [4249/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\camera_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:27.7636091Z [4250/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\bundle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:28.4206751Z [4251/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\detect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:28.5419413Z [4252/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\distortion_models.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:28.7204957Z [4253/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\initialize_reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:29.6327805Z [4254/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\intersect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:29.7687107Z [4255/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\keyframe_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:29.9642388Z [4256/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\packed_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:29.9891708Z [4257/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\modal_solver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:30.7849586Z [4258/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\pipeline.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:30.9407275Z [4259/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:30.9463994Z [4260/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\reconstruction_scale.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:31.7476085Z [4261/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\resect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:31.8831873Z [4262/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:31.9174860Z [4263/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\brute_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:32.7409779Z [4264/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\hybrid_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:32.8693852Z [4265/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\klt_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:32.8754203Z [4266/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\pyramid_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:33.1320022Z [4267/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\retrack_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:33.5203159Z [4268/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_CacheLimiterC-Api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:33.6424618Z [4269/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_RefCountedC-Api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:33.8337247Z [4270/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\trklt_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:33.9519079Z [4271/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\opensubdiv_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.0835929Z [4272/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_alloc_string_storage.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.0987363Z [4273/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\type_convert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.1227972Z [4274/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\track_region.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.1656895Z [4275/8229] Linking CXX static library lib\bf_intern_memutil.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.2443809Z [4276/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output_cpu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.2498350Z [4277/8229] Linking CXX static library lib\bf_intern_libmv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.4796315Z [4278/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\util.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:34.8614946Z [4279/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:35.0331488Z [4280/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output_gpu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:35.2248386Z [4281/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_cache_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:35.3642956Z [4282/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:35.7840085Z [4283/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.1060450Z [4284/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\gpu_compute_evaluator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.1207034Z [4285/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\gpu_patch_table.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.2939176Z [4286/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\patch_map.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.4959668Z [4287/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\mesh_topology.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.5909484Z [4288/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\mesh_topology_compare.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.7676694Z [4289/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_factory.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:36.9452294Z [4290/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.0646342Z [4291/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_impl_compare.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.1579867Z [4292/8229] Linking CXX static library lib\bf_intern_opensubdiv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.2705404Z [4293/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_hosek.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.3033414Z [4294/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_single_scattering.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.4382190Z [4295/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\manifold_table.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.4749248Z [4296/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_multiple_scattering.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.5408112Z [4297/8229] Linking CXX static library lib\bf_intern_sky.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:37.5753653Z [4298/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\marching_cubes_table.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.0121909Z [4299/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\Projections.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.0291800Z [4300/8229] Building CXX object intern\openvdb\CMakeFiles\bf_intern_openvdb.dir\openvdb_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.0991349Z [4301/8229] Linking CXX static library lib\bf_intern_openvdb.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.4591175Z [4302/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\octree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.4751034Z [4303/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\dualcon_c_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.5510454Z [4304/8229] Linking CXX static library lib\bf_intern_dualcon.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:38.8479984Z [4305/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QJacobian.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:39.2651262Z [4306/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QJacobianSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:39.2773180Z [4307/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QSegment.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:39.6604908Z [4308/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QTask.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.0122864Z [4309/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.0395877Z [4310/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_Solver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.0653112Z [4311/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Armature.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.1176974Z [4312/8229] Linking CXX static library lib\bf_intern_iksolver.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.7435119Z [4313/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\ConstraintSet.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.8121244Z [4314/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\ControlledObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:40.8338896Z [4315/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\CopyPose.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:41.5145821Z [4316/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Distance.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:41.5855442Z [4317/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\FixedObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:41.6007703Z [4318/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\MovingFrame.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:42.2583050Z [4319/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Scene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:42.3325121Z [4320/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\UncontrolledObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:42.3650914Z [4321/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WDLSSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.0146994Z [4322/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WSDLSSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.0540063Z [4323/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WorldObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.1006131Z [4324/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\eigen_types.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.7693307Z [4325/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chain.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.8054827Z [4326/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chainfksolverpos_recursive.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.8336183Z [4327/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chainjnttojacsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.9573869Z [4328/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frameacc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:43.9989135Z [4329/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frames.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.1542692Z [4330/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\framevel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.2704978Z [4331/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frames_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.3511214Z [4332/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jacobian.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.4606046Z [4333/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.5568769Z [4334/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarrayacc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.6639813Z [4335/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarrayvel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.7238612Z [4336/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\inertia.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:44.9330936Z [4337/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\joint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:45.4328914Z [4338/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\kinfam_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:45.4526048Z [4339/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\segment.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:45.6632921Z [4340/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\tree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.1359970Z [4341/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\error_stack.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.1872924Z [4342/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\treejnttojacsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.2079591Z [4343/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\treefksolverpos_recursive.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.3160724Z [4344/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\utility.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.6127667Z [4345/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\utility_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:46.6841559Z [4346/8229] Linking CXX static library lib\bf_intern_itasc.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:52.7506348Z [4347/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\display_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:56.8173024Z [4348/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:57.9585096Z [4349/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\implicit_sharing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:52:59.0809181Z [4350/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\camera.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:08.8593962Z [4351/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\light.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:11.4779484Z [4352/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\light_linking.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:23.5664289Z [4353/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\image.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:27.9676928Z [4354/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:29.7296136Z [4355/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\geometry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:34.9626464Z [4356/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\output_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:38.4030378Z [4357/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\object_cull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:38.7674170Z [4358/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\object.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:45.4917021Z [4359/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\particles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:48.8998993Z [4360/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\logging.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:54.3075298Z [4361/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\pointcloud.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:53:56.2549052Z [4362/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\curves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:02.9169226Z [4363/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\python.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:05.9600234Z [4364/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\session.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:10.8374399Z [4365/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\texture_cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:16.6779913Z [4366/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\sync.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:20.7603719Z [4367/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\viewport.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:37.0190927Z [4368/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\shader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:41.0142272Z [4369/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\bvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:48.3805478Z [4370/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\bvh2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:50.6556452Z [4371/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:50.7350081Z [4372/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\octree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:50.7381388Z [4373/8229] Linking CXX static library lib\bf_intern_cycles.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:50.7412386Z [4374/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\binning.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:50.8746725Z [4375/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\hiprt.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:52.3218310Z [4376/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\multi.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:57.0076614Z [4377/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\node.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:57.1452428Z [4378/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\optix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:57.5134806Z [4379/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\embree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:54:59.3471938Z [4380/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\build.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:02.4052819Z [4381/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\sort.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:05.0894314Z [4382/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\split.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:05.9799960Z [4383/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\unaligned.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:06.0657159Z [4384/8229] Linking CXX static library lib\cycles_bvh.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:06.5754710Z [4385/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:08.7707131Z [4386/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:10.1604380Z [4387/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\denoise.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:10.7755430Z [4388/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:13.3586552Z [4389/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\memory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:14.7283944Z [4390/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:16.2213396Z [4391/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:17.4924175Z [4392/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:17.6268565Z [4393/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:17.7795768Z [4394/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:17.9232024Z [4395/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:18.0488694Z [4396/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:18.1850823Z [4397/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\util.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:20.5941517Z [4398/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:21.2164816Z [4399/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:24.0476276Z [4400/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:26.6967053Z [4401/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:27.1633965Z [4402/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:29.2886777Z [4403/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:29.4317115Z [4404/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hiprt\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:29.5482709Z [4405/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hiprt\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:31.6715576Z [4406/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:32.2038992Z [4407/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\util.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:34.3986691Z [4408/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\dummy\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:34.5267570Z [4409/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:34.6584609Z [4410/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:38.4126725Z [4411/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:38.4720891Z [4412/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\multi\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:38.5481434Z [4413/8229] Linking CXX static library lib\cycles_device.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:40.0390656Z [4414/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:40.5960949Z [4415/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\adaptive_sampling.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:43.9667186Z [4416/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node_type.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:44.0444797Z [4417/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node_xml.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:44.0995408Z [4418/8229] Linking CXX static library lib\cycles_graph.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:46.0755132Z [4419/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:49.2619153Z [4420/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:49.4283925Z [4421/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:49.5811624Z [4422/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_optix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:51.1621835Z [4423/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn_base.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:54.4448703Z [4424/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:54.7590580Z [4425/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:55:58.9086537Z [4426/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:00.0792282Z [4427/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:01.1941801Z [4428/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor_cpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:03.8482513Z [4429/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:04.9884558Z [4430/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_display.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:06.2476542Z [4431/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:10.4168628Z [4432/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:13.0018258Z [4433/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work_cpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:15.1953864Z [4434/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:16.1318653Z [4435/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\work_balancer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:18.1834443Z [4436/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\render_scheduler.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:20.1296776Z [4437/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\shader_eval.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:21.3411523Z [4438/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\work_tile_scheduler.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:21.4210705Z [4439/8229] Linking CXX static library lib\cycles_integrator.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:25.6348387Z [4440/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\globals.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:27.4615904Z [4441/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\closures.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:56:34.5973262Z [4442/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\globals.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:57:26.5323413Z [4443/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\services.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:57:28.3840851Z [4444/8229] Linking CXX static library lib\cycles_kernel_osl.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:57:42.1830562Z [4445/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\attribute.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:58:00.7826313Z [4446/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\background.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:58:15.7228493Z [4447/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\bake.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:58:47.0433408Z [4448/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\camera.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:58:51.5324660Z [4449/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\constant_fold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:58:55.7916668Z [4450/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\devicescene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:03.1874201Z [4451/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\film.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:07.1445384Z [4452/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\kernel_avx2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:09.8461676Z [4453/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:09.9060714Z [4454/8229] Linking CXX static library lib\cycles_kernel_cpu.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:15.7744997Z [4455/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_attributes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:18.3905729Z [4456/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_bvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:24.4660771Z [4457/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:25.3830971Z [4458/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\hair.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:35.6346564Z [4459/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:35.7765969Z [4460/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:40.7382325Z [4461/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_loader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:50.4532212Z [4462/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_oiio.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T18:59:55.8636230Z [4463/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_sky.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:12.9222918Z [4464/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:20.1260261Z [4465/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\scene_attributes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:28.4288195Z [4466/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\integrator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:38.2715866Z [4467/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:47.0156856Z [4468/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light_tree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:00:54.1487800Z [4469/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light_tree_debug.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:00.9619558Z [4470/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_vdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:04.1812646Z [4471/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:06.1817122Z [4472/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh_displace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:10.8538780Z [4473/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh_subdivision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:12.0711842Z [4474/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\procedural.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:14.2319901Z [4475/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\pointcloud.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:21.6562124Z [4476/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\particles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:25.4413520Z [4477/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\osl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:26.6483518Z [4478/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\curves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:28.4582331Z [4479/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\pass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:45.0930948Z [4480/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\object.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:01:56.7221667Z [4481/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader_graph.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:05.2515926Z [4482/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:05.5691028Z [4483/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\scene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:16.0368848Z [4484/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader_nodes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:18.6345991Z [4485/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\stats.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:20.0243903Z [4486/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\tabulated_sobol.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:21.1335011Z [4487/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\svm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:24.6461853Z [4488/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\tables.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:27.2654349Z [4489/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\buffers.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:28.7999130Z [4490/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\cache_eviction.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:30.2722699Z [4491/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\display_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:35.9919142Z [4492/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\denoising.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:38.7347363Z [4493/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\merge.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:45.6629696Z [4494/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\session.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:47.5461201Z [4495/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:47.8165263Z [4496/8229] Linking CXX static library lib\cycles_session.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:55.1428527Z [4497/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\dice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:02:59.0200519Z [4498/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\interpolation.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:00.3462934Z [4499/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\patch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:05.6101357Z [4500/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\osd.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:06.4694145Z [4501/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\aligned_malloc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:09.2629016Z [4502/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\split.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:11.3525493Z [4503/8229] Linking CXX static library lib\cycles_subd.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:18.5497837Z [4504/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\debug.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:18.6064729Z [4505/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\colorspace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:22.9555781Z [4506/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\guarded_allocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:28.3013493Z [4507/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\ies.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:34.5203960Z [4508/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\image_maketx.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:35.0993729Z [4509/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\implicit_sharing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:37.9759015Z [4510/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\image_metadata.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:40.4610098Z [4511/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\math_cdf.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:41.6230288Z [4512/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\log.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:43.1321948Z [4513/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\murmurhash.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:03:46.9414524Z [4514/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\md5.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:14.7136559Z [4515/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:14.9985545Z [4516/8229] Linking CXX static library lib\cycles_scene.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:21.9583008Z [4517/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\path.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:27.6932298Z [4518/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\profiling.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:34.5870098Z [4519/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\string.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:35.6639813Z [4520/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\openvdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:41.5205603Z [4521/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\system.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:43.5708122Z [4522/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\task.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:44.5683778Z [4523/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\thread.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:46.8572071Z [4524/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\transform.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:49.0176843Z [4525/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\transform_avx2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:50.0274439Z [4526/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\time.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:50.5984636Z [4527/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\windows.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:50.8165315Z [4528/8229] Building CXX object intern\rigidbody\CMakeFiles\bf_intern_rigidbody.dir\rb_bullet_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:51.1410948Z [4529/8229] Building CXX object intern\rigidbody\CMakeFiles\bf_intern_rigidbody.dir\rb_convex_hull_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:51.9395626Z [4530/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\manta_python_API.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:51.9673537Z [4531/8229] Linking CXX static library lib\bf_intern_rigidbody.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:51.9952183Z [4532/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\manta_fluid_API.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:53.1996311Z [4533/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\MANTA_main.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:53.4450394Z [4534/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\area_compensation.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:53.7502414Z [4535/8229] Linking CXX static library lib\bf_intern_mantaflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:54.8426206Z [4536/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\geometry_data_retrieval.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:54.9540596Z [4537/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\least_squares_relocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:56.3846697Z [4538/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim_matrix_transfer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:56.4497194Z [4539/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:57.8333034Z [4540/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\uv_initializer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:57.9287355Z [4541/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim_parametrizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:58.3145666Z [4542/8229] Linking CXX static library lib\bf_intern_slim.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:58.3898909Z [4543/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_cubic.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:58.9185108Z [4544/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_cubic_refit.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:59.4300786Z [4545/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_corners_detect.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:59.5487292Z [4546/8229] Building CXX object intern\quadriflow\CMakeFiles\bf_intern_quadriflow.dir\quadriflow_capi.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:04:59.7417417Z [4547/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\generic_heap.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.0517207Z [4548/8229] Linking CXX static library lib\bf_intern_quadriflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.1722363Z [4549/8229] Building C object extern\rangetree\CMakeFiles\extern_rangetree.dir\intern\range_tree.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.2518113Z [4550/8229] Building C object extern\ufbx\CMakeFiles\extern_ufbx.dir\ufbx.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.5589305Z [4551/8229] Linking C static library lib\extern_curve_fit_nd.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.5634403Z [4552/8229] Building C object extern\nanosvg\CMakeFiles\extern_nanosvg.dir\blender_raster.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.5895823Z [4553/8229] Building C object extern\nanosvg\CMakeFiles\extern_nanosvg.dir\blender_nanosvg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:00.9655315Z [4554/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btBroadphaseProxy.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.0727472Z [4555/8229] Linking C static library lib\extern_ufbx.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.1392921Z [4556/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btAxisSweep3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.4494435Z [4557/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.4705415Z [4558/8229] Linking C static library lib\extern_rangetree.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.6437865Z [4559/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDbvt.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.9558619Z [4560/8229] Linking C static library lib\extern_nanosvg.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:01.9589792Z [4561/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDbvtBroadphase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:02.1068719Z [4562/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDispatcher.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:02.4217976Z [4563/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btOverlappingPairCache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:02.7882047Z [4564/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btQuantizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:02.9288426Z [4565/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btSimpleBroadphase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:03.2580220Z [4566/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\SphereTriangleDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:03.3717881Z [4567/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btActivatingCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:03.8193073Z [4568/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBox2dBox2dCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:03.8465173Z [4569/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBoxBoxCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:04.3383872Z [4570/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBoxBoxDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:04.3534331Z [4571/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionDispatcher.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:04.9859383Z [4572/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:05.0545034Z [4573/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:05.5811433Z [4574/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCompoundCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:05.7275399Z [4575/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionWorldImporter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:06.1125868Z [4576/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCompoundCompoundCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:06.2713538Z [4577/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvex2dConvex2dAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:06.6251734Z [4578/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexConcaveCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:06.8304397Z [4579/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexConvexAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:07.1173505Z [4580/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexPlaneCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:07.2805194Z [4581/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btDefaultCollisionConfiguration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:07.5599622Z [4582/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btEmptyCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:07.8654276Z [4583/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btGhostObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:08.0046281Z [4584/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btHashedSimplePairCache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:08.5846348Z [4585/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btManifoldResult.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:08.6302347Z [4586/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btInternalEdgeUtility.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.0158487Z [4587/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereBoxCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.0849173Z [4588/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSimulationIslandManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.4323386Z [4589/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereTriangleCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.5317123Z [4590/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereSphereCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.8108878Z [4591/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btUnionFind.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:09.9984180Z [4592/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBox2dShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:10.3290058Z [4593/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBoxShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:10.6885293Z [4594/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBvhTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:10.8883289Z [4595/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCapsuleShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:11.5032342Z [4596/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCollisionShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:11.5263408Z [4597/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCompoundShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:11.8961584Z [4598/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConeShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:11.9439815Z [4599/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConcaveShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:12.3427262Z [4600/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvex2dShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:12.6493038Z [4601/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexHullShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:12.8269225Z [4602/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexInternalShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:13.3055705Z [4603/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexPointCloudShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:13.4166782Z [4604/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexPolyhedron.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:13.7744744Z [4605/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:13.9073287Z [4606/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:14.2187996Z [4607/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCylinderShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:14.3603939Z [4608/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btEmptyShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:14.6654204Z [4609/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btHeightfieldTerrainShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:14.8238181Z [4610/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMiniSDF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:15.2668633Z [4611/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMinkowskiSumShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:15.5165644Z [4612/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMultiSphereShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:15.9284732Z [4613/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMultimaterialTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:15.9447269Z [4614/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btOptimizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.1502722Z [4615/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btPolyhedralConvexShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.3033782Z [4616/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btScaledBvhTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.3629081Z [4617/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btSdfCollisionShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.5155795Z [4618/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btShapeHull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.5438732Z [4619/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btSphereShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.6882550Z [4620/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btStaticPlaneShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.8651690Z [4621/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTetrahedronShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:16.8839035Z [4622/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btStridingMeshInterface.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.0324943Z [4623/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleCallback.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.0360130Z [4624/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.2219729Z [4625/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleIndexVertexMaterialArray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.2320406Z [4626/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleIndexVertexArray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.3983921Z [4627/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.4231942Z [4628/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleMesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.4882722Z [4629/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\nanovdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.5871666Z [4630/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btUniformScalingShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.6622291Z [4631/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btContactProcessing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.7061197Z [4632/8229] Linking CXX static library lib\cycles_util.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.7311429Z [4633/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.8428501Z [4634/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.8948236Z [4635/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactQuantizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:17.9691802Z [4636/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.0387410Z [4637/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGenericPoolAllocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.1105455Z [4638/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btTriangleShapeEx.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.1710741Z [4639/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_box_set.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.2355989Z [4640/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_contact.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.2687369Z [4641/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_memory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.3570019Z [4642/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_tri_collision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.4199831Z [4643/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btContinuousConvexCollision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.4513341Z [4644/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.5437544Z [4645/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.6126699Z [4646/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkEpa2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.6375525Z [4647/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkEpaPenetrationDepthSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.7309348Z [4648/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkPairDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.7988562Z [4649/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btMinkowskiPenetrationDepthSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.9403832Z [4650/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btPolyhedralContactClipping.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.9858860Z [4651/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btRaycastCallback.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:18.9904213Z [4652/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btPersistentManifold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.1280245Z [4653/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btSubSimplexConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.1470921Z [4654/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btVoronoiSimplexSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.2169644Z [4655/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Character\btKinematicCharacterController.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.3569372Z [4656/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btContactConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.3604264Z [4657/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btConeTwistConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.4300315Z [4658/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btFixedConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.5669773Z [4659/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGearConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.5823453Z [4660/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.6554728Z [4661/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofSpring2Constraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.7743137Z [4662/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofSpringConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.8111248Z [4663/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btHinge2Constraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.8776593Z [4664/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btHingeConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:19.9937863Z [4665/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btNNCGConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.0281929Z [4666/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btPoint2PointConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.1184087Z [4667/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSequentialImpulseConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.2285162Z [4668/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSliderConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.2627546Z [4669/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSolve2LinearConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.4426409Z [4670/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btUniversalConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.4825782Z [4671/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btTypedConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.6502088Z [4672/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btDiscreteDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.7101043Z [4673/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btSimpleDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.8057407Z [4674/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btRigidBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:20.9400098Z [4675/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.0337464Z [4676/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.1910526Z [4677/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.3516051Z [4678/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.4155561Z [4679/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyJointLimitConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.5611340Z [4680/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyJointMotor.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.6188530Z [4681/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btDantzigLCP.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.7062748Z [4682/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyPoint2Point.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.8576568Z [4683/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btMLCPSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.9122427Z [4684/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btLemkeAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:21.9380298Z [4685/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Vehicle\btRaycastVehicle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.0556221Z [4686/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Vehicle\btWheelInfo.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.3076277Z [4687/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btDefaultSoftBodySolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.4355693Z [4688/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.4675300Z [4689/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyConcaveCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.7996438Z [4690/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyRigidBodyCollisionConfiguration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.8526991Z [4691/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyHelpers.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.8560145Z [4692/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftRigidCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:22.9973167Z [4693/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btAlignedAllocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.1819453Z [4694/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btConvexHull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.2562264Z [4695/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftSoftCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.2926146Z [4696/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftRigidDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.3662069Z [4697/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btConvexHullComputer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.4289080Z [4698/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btGeometryUtil.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.4686970Z [4699/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btPolarDecomposition.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.5539839Z [4700/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btSerializer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.5992018Z [4701/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btSerializer64.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.7071339Z [4702/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btVector3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.7868337Z [4703/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btQuickprof.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:23.8977447Z [4704/8229] Linking CXX static library lib\extern_bullet.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.0460801Z [4705/8229] Building C object extern\hipew\CMakeFiles\extern_hipew.dir\src\hipew.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.1305071Z [4706/8229] Linking C static library lib\extern_hipew.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.4770924Z [4707/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags_completions.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.4944884Z [4708/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.7485682Z [4709/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags_reporting.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.9185457Z [4710/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\windows_port.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:24.9705157Z [4711/8229] Linking CXX static library lib\extern_gflags.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:25.1940991Z [4712/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\demangle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:25.5164079Z [4713/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:25.6052321Z [4714/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\raw_logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:25.9258057Z [4715/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\signalhandler.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.2751729Z [4716/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\symbolize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.3206974Z [4717/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\utilities.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.6185204Z [4718/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\vlog_is_on.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.7353574Z [4719/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\windows\port.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.7814619Z [4720/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\DeviceManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:26.7949789Z [4721/8229] Linking CXX static library lib\extern_glog.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.0367619Z [4722/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\MixingThreadDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.1515749Z [4723/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\NULLDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.1835052Z [4724/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\ReadDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.5308015Z [4725/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\SoftwareDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.5450696Z [4726/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\ThreadedDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.6159256Z [4727/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\Exception.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.9235254Z [4728/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\FileManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:27.9276766Z [4729/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\File.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.0206626Z [4730/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\FileWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.2798942Z [4731/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Accumulator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.2923125Z [4732/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ADSR.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.3584613Z [4733/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ADSRReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.6100278Z [4734/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BaseIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.6482502Z [4735/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ButterworthCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.7012451Z [4736/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Butterworth.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.9588839Z [4737/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\CallbackIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:28.9974865Z [4738/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Delay.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.0523510Z [4739/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DelayReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.3313479Z [4740/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicIIRFilter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.3685243Z [4741/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.4485146Z [4742/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicMusic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.6847162Z [4743/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Effect.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.7167639Z [4744/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\EffectReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:29.8116744Z [4745/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Envelope.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.0422804Z [4746/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Fader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.0729543Z [4747/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\FaderReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.1608726Z [4748/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\HighpassCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.4141151Z [4749/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Highpass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.4461395Z [4750/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\IIRFilter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.5193758Z [4751/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\IIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.7765148Z [4752/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Limiter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.8416062Z [4753/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LimiterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:30.8720950Z [4754/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Loop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.1282243Z [4755/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LoopReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.1848183Z [4756/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LowpassCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.2198673Z [4757/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Lowpass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.4720442Z [4758/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Modulator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.5709613Z [4759/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\MutableReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.6288312Z [4760/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ModulatorReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.8419944Z [4761/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\MutableSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.9340118Z [4762/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Pitch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:31.9906693Z [4763/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PitchReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.2460215Z [4764/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PlaybackManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.3328653Z [4765/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Reverse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.3387333Z [4766/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PlaybackCategory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.5386322Z [4767/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Source.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.6207244Z [4768/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ReverseReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.8890371Z [4769/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\SoundList.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.9177450Z [4770/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Sum.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:32.9656936Z [4771/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Threshold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.2487815Z [4772/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.2662175Z [4773/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.3379301Z [4774/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.4577868Z [4775/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeStorage.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.6305768Z [4776/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Echo.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.7073275Z [4777/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\EchoReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.7989111Z [4778/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Sawtooth.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.8297653Z [4779/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SawtoothReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:33.9466120Z [4780/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SilenceReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.0461778Z [4781/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Silence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.1404876Z [4782/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SineReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.1664569Z [4783/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Sine.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.3232309Z [4784/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SquareReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.3863003Z [4785/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Square.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.5057343Z [4786/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\TriangleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.5132669Z [4787/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Triangle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.7396519Z [4788/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ChannelMapper.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.8628225Z [4789/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\Converter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.8779170Z [4790/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ConverterFunctions.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:34.9132820Z [4791/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ChannelMapperReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.1975200Z [4792/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ConverterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.2369812Z [4793/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResample.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.5697241Z [4794/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffHigh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.5738014Z [4795/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffLow.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.6275901Z [4796/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffMedium.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.9148238Z [4797/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\LinearResample.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.9879933Z [4798/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:35.9920115Z [4799/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\LinearResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.3093833Z [4800/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\Mixer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.3339465Z [4801/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\SpecsChanger.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.3465311Z [4802/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.6749763Z [4803/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Double.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.6784684Z [4804/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\DoubleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:36.7258382Z [4805/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\AnimateableProperty.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.0266929Z [4806/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\PingPong.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.0928039Z [4807/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Sequence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.1233696Z [4808/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceData.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.4445350Z [4809/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceEntry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.5029026Z [4810/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceHandle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.5616214Z [4811/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.8023188Z [4812/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Superpose.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.9301647Z [4813/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SuperposeReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:37.9596927Z [4814/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\Barrier.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.1594346Z [4815/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\Buffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.2941646Z [4816/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\BufferReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.3360327Z [4817/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\RingBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.5683142Z [4818/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\StreamBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.7491538Z [4819/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEG.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:38.8153558Z [4820/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\ThreadPool.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.0462596Z [4821/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEGReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.1957781Z [4822/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEGWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.3698345Z [4823/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BinauralSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.6151137Z [4824/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BinauralReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.7699817Z [4825/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Convolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:39.9450345Z [4826/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ConvolverReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.1805716Z [4827/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ConvolverSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.3872765Z [4828/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\FFTConvolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.4243670Z [4829/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Equalizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.6458332Z [4830/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\HRTF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.8836009Z [4831/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\FFTPlan.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:40.9042712Z [4832/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ImpulseResponse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.0257841Z [4833/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.2669774Z [4834/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFileWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.2924171Z [4835/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFileReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.5742456Z [4836/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\openal\OpenALDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.6934613Z [4837/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\openal\OpenALReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.6976989Z [4838/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\TimeStretchPitchScale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:41.9669307Z [4839/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\TimeStretchPitchScaleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:42.1214794Z [4840/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\AnimateableTimeStretchPitchScaleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:42.1253459Z [4841/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\AnimateableTimeStretchPitchScale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:42.7612934Z [4842/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\PluginManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:42.8236038Z [4843/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\HRTFLoader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:42.9495176Z [4844/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\wasapi\WASAPIDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.0514516Z [4845/8229] Linking CXX static library lib\audaspace.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.2549817Z [4846/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyAnimateableProperty.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.3553749Z [4847/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyAPI.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.4456510Z [4848/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.7340608Z [4849/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyDynamicMusic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.8417881Z [4850/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyHandle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:43.9468140Z [4851/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyPlaybackManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:44.2420117Z [4852/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySequence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:44.3534133Z [4853/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySequenceEntry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:44.6260969Z [4854/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:44.7129809Z [4855/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySource.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:44.9569096Z [4856/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyThreadPool.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:45.1863969Z [4857/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyHRTF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:45.2482853Z [4858/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyImpulseResponse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:45.3129047Z [4859/8229] Linking CXX static library lib\audaspace-py.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:45.9802350Z [4860/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\adjacent-matrix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:46.2440562Z [4861/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\dedge.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:46.2890831Z [4862/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\hierarchy.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:46.7073491Z [4863/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\loader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:47.0076479Z [4864/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\merge-vertex.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:47.2967695Z [4865/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\localsat.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:47.7668169Z [4866/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\optimizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:48.1077924Z [4867/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:48.3556377Z [4868/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-flip.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:48.8356402Z [4869/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-int.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:49.1632670Z [4870/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:49.4067826Z [4871/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-scale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:49.8617898Z [4872/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-sing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:49.9327976Z [4873/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\arg_parser.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.2295965Z [4874/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\subdivide.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.3814381Z [4875/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.4655801Z [4876/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.7499190Z [4877/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\lp_base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.9087145Z [4878/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\lp_skeleton.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:50.9497741Z [4879/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\random.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:51.4417978Z [4880/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\bits\windows.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:51.5032250Z [4881/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\commonkernels.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:51.5088850Z [4882/8229] Linking CXX static library lib\extern_quadriflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:51.5482341Z [4883/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\conjugategrad.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.0214131Z [4884/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\conjugategrad.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.1116873Z [4885/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\edgecollapse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.1456163Z [4886/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\edgecollapse.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.6050514Z [4887/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fastmarch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.7097144Z [4888/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fastmarch.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:52.7427044Z [4889/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iogrids.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:53.2084330Z [4890/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iomeshes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:53.3231922Z [4891/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\ioparticles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:53.8313393Z [4892/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\mantaio.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:54.0844130Z [4893/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\ioutil.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:54.3567541Z [4894/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\mantaio.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:54.6638893Z [4895/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fluidsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:54.6982998Z [4896/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iovdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:54.8933532Z [4897/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fluidsolver.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:55.1725337Z [4898/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\general.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:55.4936565Z [4899/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:55.7526096Z [4900/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:56.0729839Z [4901/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid4d.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:56.3107251Z [4902/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid4d.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:56.6526270Z [4903/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:56.8658770Z [4904/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\kernel.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:57.2316811Z [4905/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\levelset.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:57.4444682Z [4906/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\levelset.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:57.8546603Z [4907/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:57.8594727Z [4908/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\general.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:58.0614368Z [4909/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\mesh.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:58.4320821Z [4910/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\movingobs.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:58.4607229Z [4911/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\movingobs.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:58.6725051Z [4912/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\multigrid.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.0310353Z [4913/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\multigrid.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.0556368Z [4914/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\noisefield.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.2509049Z [4915/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\noisefield.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.6567833Z [4916/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\particle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.6609018Z [4917/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\particle.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:05:59.8324715Z [4918/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\advection.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:00.2707170Z [4919/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\apic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:00.2859866Z [4920/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\extforces.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:00.4211885Z [4921/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\fire.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:00.8855369Z [4922/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\fluidguiding.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:00.8964040Z [4923/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\flip.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:01.0280475Z [4924/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\initplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:01.5026936Z [4925/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\kepsilon.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:01.5087442Z [4926/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\meshplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:01.6078133Z [4927/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\pressure.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.0853189Z [4928/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\ptsplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.1174232Z [4929/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\secondaryparticles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.2200698Z [4930/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\surfaceturbulence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.7300878Z [4931/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\vortexplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.7749677Z [4932/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\viscosity.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.7990490Z [4933/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\waveletturbulence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:02.9049429Z [4934/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\registration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:03.1400690Z [4935/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\python\defines.py.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:03.3460150Z [4936/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\waves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:03.5133050Z [4937/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\shapes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:03.7364516Z [4938/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\shapes.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:03.9331885Z [4939/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\test.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:04.0436137Z [4940/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\timing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:04.2744330Z [4941/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\timing.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:04.5530382Z [4942/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\turbulencepart.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:04.6540345Z [4943/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\turbulencepart.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:04.8814617Z [4944/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexpart.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:05.1524825Z [4945/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexpart.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:05.2600934Z [4946/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexsheet.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:05.4810230Z [4947/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexsheet.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:05.7556940Z [4948/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pclass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:05.8715534Z [4949/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pconvert.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:06.0942159Z [4950/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pvec3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:06.3783682Z [4951/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\registry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:06.4814103Z [4952/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\simpleimage.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:06.5880147Z [4953/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\vector4d.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:06.8649579Z [4954/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\vectorbase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:07.0874168Z [4955/8229] Building CXX object extern\vulkan_memory_allocator\CMakeFiles\extern_vulkan_memory_allocator.dir\vk_mem_alloc_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:07.2417832Z [4956/8229] Linking CXX static library lib\extern_mantaflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:07.2913226Z [4957/8229] Linking CXX static library lib\extern_vulkan_memory_allocator.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:07.6567039Z [4958/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_asset_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:08.0811813Z [4959/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_channels_defines.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:08.3102327Z [4960/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_channels_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:08.6879853Z [4961/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_deps.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:09.1699831Z [4962/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:09.4058084Z [4963/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:09.7048751Z [4964/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_ipo_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:10.3264481Z [4965/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_markers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:10.5170170Z [4966/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_motion_paths.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:10.8469075Z [4967/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:11.1551516Z [4968/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\drivers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:11.5756981Z [4969/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\fmodifier_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:11.9404020Z [4970/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:12.1036808Z [4971/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:12.6646657Z [4972/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_general.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:12.8803113Z [4973/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_keylist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:13.2739102Z [4974/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:13.6882824Z [4975/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyingsets.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:13.8311660Z [4976/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\time_scrub_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:13.9491395Z [4977/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\transformable.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:14.0203505Z [4978/8229] Linking CXX static library lib\bf_editor_animation.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:14.7546335Z [4979/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:14.9103442Z [4980/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:15.0180801Z [4981/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_naming.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:15.6821318Z [4982/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:16.0171995Z [4983/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_relations.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:16.0325483Z [4984/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:16.5215193Z [4985/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_skinning.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:16.7363976Z [4986/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:16.8218146Z [4987/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\bone_collections.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:17.3411908Z [4988/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\editarmature_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:17.5902612Z [4989/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\meshlaplacian.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:17.9673608Z [4990/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:18.4484185Z [4991/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_lib_2.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:18.7232527Z [4992/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:19.1275922Z [4993/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_slide.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:19.6540040Z [4994/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_transform.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:19.7784468Z [4995/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:19.8463808Z [4996/8229] Linking CXX static library lib\bf_editor_armature.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:19.9341446Z [4997/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_catalog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:20.3094402Z [4998/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:20.7434997Z [4999/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:20.7652340Z [5000/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_import.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:20.9840983Z [5001/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_file_status.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:21.5132173Z [5002/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_listing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:21.5177272Z [5003/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_listing_v1.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:21.5495331Z [5004/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_library_reference_enum.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:22.2638204Z [5005/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_library_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:22.3147169Z [5006/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_mark_clear.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:22.5052024Z [5007/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_list.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:23.1017531Z [5008/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_menu_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:23.4654812Z [5009/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:23.5309919Z [5010/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:24.1422087Z [5011/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_asset_view.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:24.5050145Z [5012/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_catalog_selector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:24.5882698Z [5013/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_popover.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:24.7128557Z [5014/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_regiondata.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:25.2298762Z [5015/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_temp_id_consumer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:25.2756861Z [5016/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_type.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:25.4650326Z [5017/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_settings.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:26.0027101Z [5018/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_ui_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:26.0719686Z [5019/8229] Linking CXX static library lib\bf_editor_asset.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:26.1957471Z [5020/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\curve_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:26.6283411Z [5021/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:27.0101115Z [5022/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:27.3135219Z [5023/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:27.6451936Z [5024/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:27.7067753Z [5025/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_query.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:28.3360901Z [5026/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:28.4344305Z [5027/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:28.8356111Z [5028/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editfont.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:29.1155644Z [5029/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editfont_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:29.1811100Z [5030/8229] Linking CXX static library lib\bf_editor_curve.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:29.5092770Z [5031/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:29.9744113Z [5032/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_data.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:29.9900406Z [5033/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_attribute_set.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:30.6735831Z [5034/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:30.8474028Z [5035/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:30.8995175Z [5036/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_extrude.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:31.5132277Z [5037/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_masks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:32.0064885Z [5038/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:32.0881796Z [5039/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:32.3659168Z [5040/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:32.8889896Z [5041/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:32.9898281Z [5042/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\join.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:33.2717391Z [5043/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\select_linked_pick.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:33.7947551Z [5044/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\separate.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:33.8653292Z [5045/8229] Linking CXX static library lib\bf_editor_curves.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:34.1186399Z [5046/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_attributes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:34.2733986Z [5047/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:34.5444513Z [5048/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_randomization.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.0409947Z [5049/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_draw_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.2738444Z [5050/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_library_presets.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.4027993Z [5051/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_arrow_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.5233558Z [5052/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_cube_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.6536126Z [5053/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_dial_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.7614721Z [5054/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\node_group_operator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:35.8206894Z [5055/8229] Linking CXX static library lib\bf_editor_geometry.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:36.0575276Z [5056/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_library_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:36.5051059Z [5057/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\blank3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:36.7577777Z [5058/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\arrow3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:36.9535789Z [5059/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\button2d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:37.6015924Z [5060/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\cage2d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:37.7991314Z [5061/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\cage3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:38.0463289Z [5062/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\dial3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:38.6750999Z [5063/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\move3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:38.8366667Z [5064/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\primitive3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:39.0504111Z [5065/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\snap3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:39.1085705Z [5066/8229] Linking CXX static library lib\bf_editor_gizmo_library.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:39.7508644Z [5067/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\annotate_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:39.9940184Z [5068/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\annotate_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:40.0132777Z [5069/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\editaction_gpencil.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:40.5866242Z [5070/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_data.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:40.9498291Z [5071/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:41.1094616Z [5072/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:41.6953336Z [5073/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:41.7619641Z [5074/8229] Linking CXX static library lib\bf_editor_gpencil_legacy.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:42.0703288Z [5075/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:42.2608235Z [5076/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_bake_animation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:43.1728197Z [5077/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_frames.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:43.2089822Z [5078/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:43.6397674Z [5079/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:44.3063831Z [5080/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_image_render.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:44.3391344Z [5081/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_join_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:44.7931787Z [5082/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_layers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:45.4398326Z [5083/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_material.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:45.4919223Z [5084/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_lineart.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:45.8908291Z [5085/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_merge.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:46.5683628Z [5086/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_modes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:46.6077828Z [5087/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:47.0117984Z [5088/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:47.6676071Z [5089/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_randomize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:47.7307959Z [5090/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_primitive.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:48.1018290Z [5091/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_segments_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:48.8592878Z [5092/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_trim.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:49.1243106Z [5093/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:49.1710551Z [5094/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.0425043Z [5095/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.2604319Z [5096/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_vertex_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.3212143Z [5097/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_weight_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.4743768Z [5098/8229] Linking CXX static library lib\bf_editor_grease_pencil.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.7708304Z [5099/8229] Building CXX object source\blender\editors\id_management\CMakeFiles\bf_editor_id_management.dir\ed_id_management.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:50.8331941Z [5100/8229] Linking CXX static library lib\bf_editor_id_management.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:51.3327178Z [5101/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\buttons\interface_textbox.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:51.4158369Z [5102/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_bone.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:51.9814545Z [5103/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:52.2303891Z [5104/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_colorband.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:52.5002672Z [5105/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_datablock.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:53.0542627Z [5106/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_driver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:53.1661098Z [5107/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_depth.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:53.5868990Z [5108/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_grease_pencil_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:54.1369564Z [5109/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\interface_eyedropper.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:54.3803399Z [5110/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:54.3986714Z [5111/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_align.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:54.9705518Z [5112/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_anim.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:55.1694396Z [5113/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_button_group.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:55.4967123Z [5114/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_button_sections.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:55.9708209Z [5115/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_context_path.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:56.1066761Z [5116/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_context_menu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:56.3194252Z [5117/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_drag.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:56.8199094Z [5118/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_drop.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:56.9555162Z [5119/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:57.4132515Z [5120/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_dropboxes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:58.1039484Z [5121/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_handlers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:58.2065069Z [5122/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_icons_event.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:58.2348126Z [5123/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_icons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:06:59.4071198Z [5124/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.0975385Z [5125/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_mixar_section.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.0981762Z FAILED: [code=2] source/blender/editors/interface/CMakeFiles/bf_editor_interface.dir/interface_mixar_section.cc.obj 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1010653Z sccache "C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe"  /nologo /TP -DBLENDER_WIN_APPID=\"mixar.3.3\" -DBLENDER_WIN_APPID_FRIENDLY_NAME="\"Mixar 3.3\"" -DNDEBUG -DNOMINMAX -DWIN32 -DWIN32_LEAN_AND_MEAN -DWITH_ASSERT_ABORT -DWITH_INPUT_IME -DWITH_INPUT_NDOF -DWITH_INTERNATIONAL -DWITH_OPENVDB -DWITH_OPENVDB_BLOSC -DWITH_PYTHON -DWITH_TBB -DWITH_TBB_MALLOC -D_ALLOW_KEYWORD_MACROS -D_CONSOLE -D_CRT_NONSTDC_NO_DEPRECATE -D_CRT_SECURE_NO_DEPRECATE -D_LIB -D_SCL_SECURE_NO_DEPRECATE -D_USE_MATH_DEFINES -D_WIN32_WINNT=0x603 -D__LITTLE_ENDIAN__ -D__MMX__ -D__SSE2__ -D__SSE3__ -D__SSE4_1__ -D__SSE4_2__ -D__SSE__ -ID:\a\mixar-app\mixar-app\source\source\blender\editors\interface -ID:\a\mixar-app\mixar-app\source\source\blender\editors\asset -ID:\a\mixar-app\mixar-app\source\source\blender\editors\include -ID:\a\mixar-app\mixar-app\source\source\blender\animrig -ID:\a\mixar-app\mixar-app\source\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\python -ID:\a\mixar-app\mixar-app\source\intern\ghost -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\asset_system -ID:\a\mixar-app\mixar-app\source\source\blender\blenfont -ID:\a\mixar-app\mixar-app\source\source\blender\blenkernel -ID:\a\mixar-app\mixar-app\source\intern\profile\. -ID:\a\mixar-app\mixar-app\source\intern\openvdb -ID:\a\mixar-app\mixar-app\source\intern\mikktspace\. -ID:\a\mixar-app\mixar-app\source\source\blender\makesdna -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesdna\intern -ID:\a\mixar-app\mixar-app\source\source\blender\blenlib -ID:\a\mixar-app\mixar-app\source\intern\utfconv -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader_core -ID:\a\mixar-app\mixar-app\source\source\blender\blentranslation -ID:\a\mixar-app\mixar-app\source\source\blender\bmesh -ID:\a\mixar-app\mixar-app\source\source\blender\depsgraph -ID:\a\mixar-app\mixar-app\source\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\editors\datafiles -ID:\a\mixar-app\mixar-app\source\source\blender\functions -ID:\a\mixar-app\mixar-app\source\source\blender\gpu -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\compositor -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\imbuf\opencolorio -ID:\a\mixar-app\mixar-app\build\Prod\intern\opensubdiv -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\movie -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\opencolorio\. -ID:\a\mixar-app\mixar-app\source\intern\clog -ID:\a\mixar-app\mixar-app\source\intern\guardedalloc -ID:\a\mixar-app\mixar-app\source\source\blender\nodes -ID:\a\mixar-app\mixar-app\source\source\blender\render -ID:\a\mixar-app\mixar-app\source\source\blender\sequencer -ID:\a\mixar-app\mixar-app\source\source\blender\windowmanager -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\pthreads\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\vulkan\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\openVDB\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\tbb\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\OpenImageIO\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\fmt\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\opencolorio\include -external:W0 /W3 /w34062 /w34100 /w34115 /w34189 /w35038 /wd4018 /wd4146 /wd4065 /wd4127 /wd4181 /wd4200 /wd4244 /wd4267 /wd4305 /wd4800 /wd4828 /wd4996 /wd4661 /we4013 /we4133 /we4431 /we4033 /DWIN32 /D_WINDOWS /W3  /EHsc /nologo /J /Gd /MP /EHsc /bigobj /permissive- /Zc:__cplusplus /Zc:inline /Zc:preprocessor   /O2 /Ob2 /DNDEBUG /MD  -std:c++20 -MD /utf-8 /showIncludes /Fosource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_mixar_section.cc.obj /Fdsource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\bf_editor_interface.pdb /FS -c D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1038151Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(50): error C2228: left of '.size' must have class/struct/union
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1052803Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(51): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1054964Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(51): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1057534Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(67): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1059983Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(67): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1062215Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(80): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1064355Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(80): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1066492Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(93): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1068676Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(93): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1070914Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(106): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1073110Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(106): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1074942Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1077044Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1078832Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C3861: 'eRegion_Alignment': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1081027Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2065: 'RGN_ALIGN_RIGHT': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1082903Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2737: 'is_left': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1084729Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2065: 'View2D': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1086481Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1088224Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1089927Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1092363Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1094812Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1096629Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C2065: 'style': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1098692Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1100800Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1102602Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1104650Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2065: 'style': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1106491Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(136): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1108248Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(137): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1110041Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(137): error C2737: 'fontid': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1111865Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(138): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1113994Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1115731Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1117508Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C3861: 'BLI_listbase_is_empty': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1119363Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(141): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1121036Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1122784Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C2737: 'aspect': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1124825Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(143): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1126609Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(143): error C2737: 'dpi_fac': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1128413Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(144): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1130167Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(144): error C2737: 'px': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1132193Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1133522Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1134496Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C2065: 'btheme': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1135468Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C3861: 'UI_GetTheme': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1136557Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1137667Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1138846Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1139788Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2065: 'btheme': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1140888Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1141917Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1142904Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1143866Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1144815Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1145795Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1146769Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1147719Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1148668Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1149639Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1150603Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1151885Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1153144Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1155038Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1156925Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1159151Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1160972Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1162897Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1164836Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1166689Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1168542Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1170415Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1172326Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1174369Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1176215Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1178103Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1180417Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1182298Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1184120Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1185977Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1187879Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1189765Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1191633Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1193526Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C2065: 'USER_UIFLAG2_PANEL_TABS_COMPACT': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1195782Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1197643Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(177): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1199976Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(177): error C2737: 'tab_v_pad_text': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1201931Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(178): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1203781Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(183): error C2065: 'BLF_ROTATION': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1205615Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(183): error C3861: 'BLF_enable': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1207458Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(184): error C3861: 'BLF_rotation': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1209237Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(186): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1210983Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(186): error C3861: 'BLF_size': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1212758Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1214451Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1216254Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2737: 'rct_xmin': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1218302Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1220438Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1222250Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2737: 'rct_xmax': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1224137Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2065: 'PanelCategoryDyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1225870Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2059: syntax error: ','
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1227582Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2143: syntax error: missing ';' before '{'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1229385Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'rcti': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1231152Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1233029Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'pc_dyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1234786Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(197): error C2065: 'pc_dyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1236608Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(197): error C3861: 'BLT_translate_do_iface': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1238754Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(199): error C3861: 'BLF_width': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1240959Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(198): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1242748Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(201): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1244456Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(202): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1246502Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(203): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1248203Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(203): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1249981Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(204): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1252062Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(204): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1253784Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1255576Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C3861: 'BLI_rcti_size_y': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1257553Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2672: 'std::max': no matching overloaded function found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1259852Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(88): note: could be '_Ty std::max(std::initializer_list<_Elem>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1263403Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): note: '_Ty std::max(std::initializer_list<_Elem>)': expects 1 arguments - 2 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1265665Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(85): note: or       '_Ty std::max(std::initializer_list<_Elem>,_Pr)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1267684Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(77): note: or       'const _Ty &std::max(const _Ty &,const _Ty &) noexcept(<expr>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1269851Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(67): note: or       'const _Ty &std::max(const _Ty &,const _Ty &,_Pr) noexcept(<expr>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1272379Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): note: 'const _Ty &std::max(const _Ty &,const _Ty &,_Pr) noexcept(<expr>)': expects 3 arguments - 2 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1274593Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2737: 'max_scroll': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1276443Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1278151Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1279987Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2672: 'std::clamp': no matching overloaded function found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1282079Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\algorithm(11911): note: could be 'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1285465Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\algorithm(11883): note: or       'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &,_Pr)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1287778Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): note: 'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &,_Pr)': expects 4 arguments - 3 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1289914Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2737: 'scroll': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1292056Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(212): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1293784Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1295607Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): error C2065: 'PanelCategoryDyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1297379Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): error C2059: syntax error: ','
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.1299201Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): fatal error C1003: error count exceeds 100; stopping compilation
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.3950622Z [5126/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_layout.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.3952014Z FAILED: [code=2] source/blender/editors/interface/CMakeFiles/bf_editor_interface.dir/interface_layout.cc.obj 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.3977793Z sccache "C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe"  /nologo /TP -DBLENDER_WIN_APPID=\"mixar.3.3\" -DBLENDER_WIN_APPID_FRIENDLY_NAME="\"Mixar 3.3\"" -DNDEBUG -DNOMINMAX -DWIN32 -DWIN32_LEAN_AND_MEAN -DWITH_ASSERT_ABORT -DWITH_INPUT_IME -DWITH_INPUT_NDOF -DWITH_INTERNATIONAL -DWITH_OPENVDB -DWITH_OPENVDB_BLOSC -DWITH_PYTHON -DWITH_TBB -DWITH_TBB_MALLOC -D_ALLOW_KEYWORD_MACROS -D_CONSOLE -D_CRT_NONSTDC_NO_DEPRECATE -D_CRT_SECURE_NO_DEPRECATE -D_LIB -D_SCL_SECURE_NO_DEPRECATE -D_USE_MATH_DEFINES -D_WIN32_WINNT=0x603 -D__LITTLE_ENDIAN__ -D__MMX__ -D__SSE2__ -D__SSE3__ -D__SSE4_1__ -D__SSE4_2__ -D__SSE__ -ID:\a\mixar-app\mixar-app\source\source\blender\editors\interface -ID:\a\mixar-app\mixar-app\source\source\blender\editors\asset -ID:\a\mixar-app\mixar-app\source\source\blender\editors\include -ID:\a\mixar-app\mixar-app\source\source\blender\animrig -ID:\a\mixar-app\mixar-app\source\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\python -ID:\a\mixar-app\mixar-app\source\intern\ghost -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\asset_system -ID:\a\mixar-app\mixar-app\source\source\blender\blenfont -ID:\a\mixar-app\mixar-app\source\source\blender\blenkernel -ID:\a\mixar-app\mixar-app\source\intern\profile\. -ID:\a\mixar-app\mixar-app\source\intern\openvdb -ID:\a\mixar-app\mixar-app\source\intern\mikktspace\. -ID:\a\mixar-app\mixar-app\source\source\blender\makesdna -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesdna\intern -ID:\a\mixar-app\mixar-app\source\source\blender\blenlib -ID:\a\mixar-app\mixar-app\source\intern\utfconv -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader_core -ID:\a\mixar-app\mixar-app\source\source\blender\blentranslation -ID:\a\mixar-app\mixar-app\source\source\blender\bmesh -ID:\a\mixar-app\mixar-app\source\source\blender\depsgraph -ID:\a\mixar-app\mixar-app\source\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\editors\datafiles -ID:\a\mixar-app\mixar-app\source\source\blender\functions -ID:\a\mixar-app\mixar-app\source\source\blender\gpu -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\compositor -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\imbuf\opencolorio -ID:\a\mixar-app\mixar-app\build\Prod\intern\opensubdiv -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\movie -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\opencolorio\. -ID:\a\mixar-app\mixar-app\source\intern\clog -ID:\a\mixar-app\mixar-app\source\intern\guardedalloc -ID:\a\mixar-app\mixar-app\source\source\blender\nodes -ID:\a\mixar-app\mixar-app\source\source\blender\render -ID:\a\mixar-app\mixar-app\source\source\blender\sequencer -ID:\a\mixar-app\mixar-app\source\source\blender\windowmanager -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\pthreads\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\vulkan\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\openVDB\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\tbb\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\OpenImageIO\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\fmt\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\opencolorio\include -external:W0 /W3 /w34062 /w34100 /w34115 /w34189 /w35038 /wd4018 /wd4146 /wd4065 /wd4127 /wd4181 /wd4200 /wd4244 /wd4267 /wd4305 /wd4800 /wd4828 /wd4996 /wd4661 /we4013 /we4133 /we4431 /we4033 /DWIN32 /D_WINDOWS /W3  /EHsc /nologo /J /Gd /MP /EHsc /bigobj /permissive- /Zc:__cplusplus /Zc:inline /Zc:preprocessor   /O2 /Ob2 /DNDEBUG /MD  -std:c++20 -MD /utf-8 /showIncludes /Fosource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_layout.cc.obj /Fdsource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\bf_editor_interface.pdb /FS -c D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.4009314Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc(1510): error C2228: left of '.is_empty' must have class/struct/union
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:04.4011370Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc(1513): error C3861: 'but_drawflag_enable': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:05.8913958Z [5127/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_ops_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:05.8920071Z ninja: build stopped: subcommand failed.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:05.9070816Z Error: Build failed
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2302422Z ^[[31;1mException: ^[[0mD:\a\_temp\306f9095-4faf-43af-ba64-bb0467cbe84e.ps1:6^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2303149Z ^[[31;1m^[[0m^[[36;1mLine |^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2303812Z ^[[31;1m^[[0m^[[36;1m^[[36;1m   6 | ^[[0m if ($code -ne 0) { ^[[36;1mthrow "build.bat exited with $code"^[[0m }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2304601Z ^[[31;1m^[[0m^[[36;1m^[[36;1m^[[0m^[[36;1m^[[0m^[[36;1m     | ^[[31;1m                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2305375Z ^[[31;1m^[[0m^[[36;1m^[[36;1m^[[0m^[[36;1m^[[0m^[[36;1m^[[31;1m^[[31;1m^[[36;1m     | ^[[31;1mbuild.bat exited with 1^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2646429Z ##[error]Process completed with exit code 1.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2864798Z ##[group]Run if (Get-Command sccache -ErrorAction SilentlyContinue) {
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2865428Z ^[[36;1mif (Get-Command sccache -ErrorAction SilentlyContinue) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2865780Z ^[[36;1m  sccache --show-stats^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2866005Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2973514Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2973848Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2974010Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2974194Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2974389Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2974580Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2974764Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2975190Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2975466Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2975662Z   SHORT_SHA: 9293526
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2975838Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.2976006Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6310486Z Compile requests                   2240
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6312746Z Compile requests executed          2066
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6313712Z Cache hits                         2062
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6315094Z Cache hits (C/C++)                 2062
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6315532Z Cache misses                          2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6316171Z Cache misses (C/C++)                  2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6316438Z Cache hits rate                   99.90 %
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6316693Z Cache hits rate (C/C++)           99.90 %
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6316944Z Cache timeouts                        0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6317185Z Cache read errors                     0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6317418Z Forced recaches                       0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6317669Z Cache write errors                    0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6317893Z Cache errors                          0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6318125Z Compilations                          2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6318366Z Compilation failures                  2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6318619Z Non-cacheable compilations            0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6318862Z Non-cacheable calls                 174
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6319361Z Non-compilation calls                 0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6319840Z Unsupported compiler calls            0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6320095Z Average cache write               0.000 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6320355Z Average compiler                  3.945 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6320692Z Average cache read hit            0.000 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321101Z Failed distributed compilations       0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321276Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321353Z Non-cacheable reasons:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321567Z multiple input files                172
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321820Z /Yc                                   2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6321981Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6322176Z Cache location                  Local disk: "D:\\a\\mixar-app\\mixar-app\\.sccache"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6322567Z Base directories                (none)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6322955Z Use direct/preprocessor mode?   yes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6323588Z Version (client)                0.17.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6324466Z Cache size                           46 MiB
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.6324842Z Max cache size                        5 GiB
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7788978Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7791135Z ##[group]Run actions/cache/save@v4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7791385Z with:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7791588Z   path: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7792022Z   key: sccache-Windows-Prod-v5.2.0-92935261748f97dd9f266a3fa4cb2ec614e95369
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7792424Z   enableCrossOsArchive: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7792649Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7792806Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7792986Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7793174Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7793357Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7793538Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7793787Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7794078Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7794275Z   SHORT_SHA: 9293526
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7794458Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:06.7794631Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:07.3774345Z (node:1992) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:07.3775262Z (Use `node --trace-deprecation ...` to show where the warning was created)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:07.4958320Z [command]"C:\Program Files\Git\usr\bin\tar.exe" --posix -cf cache.tzst --exclude cache.tzst -P -C D:/a/mixar-app/mixar-app --files-from manifest.txt --force-local --use-compress-program "zstd -T0"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.1687126Z (node:1992) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.6949655Z Sent 47770453 of 47770453 (100.0%), 84.8 MBs/sec
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7551236Z Cache saved with key: sccache-Windows-Prod-v5.2.0-92935261748f97dd9f266a3fa4cb2ec614e95369
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7896674Z ##[group]Run $out = New-Object System.Collections.Generic.List[string]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7897269Z ^[[36;1m$out = New-Object System.Collections.Generic.List[string]^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7897790Z ^[[36;1m$out.Add("Run: https://github.com/aimcrazyxx/mixar-app/actions/runs/31964847354")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7898319Z ^[[36;1m$out.Add("Commit: 92935261748f97dd9f266a3fa4cb2ec614e95369")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7898704Z ^[[36;1m$out.Add("Runner: Windows / windows-latest")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7898992Z ^[[36;1m$out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7899247Z ^[[36;1mfunction Add-Block($title, $path, $tail) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7899530Z ^[[36;1m  $out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7899736Z ^[[36;1m  $out.Add("## $title")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7899989Z ^[[36;1m  if (Test-Path $path) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7900224Z ^[[36;1m    $out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7900556Z ^[[36;1m    Get-Content $path -Tail $tail -ErrorAction SilentlyContinue |^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7900985Z ^[[36;1m      ForEach-Object { $out.Add($_) }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7901250Z ^[[36;1m    $out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7901453Z ^[[36;1m  } else {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7901754Z ^[[36;1m    $out.Add("not produced - the job died before this file existed")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7902103Z ^[[36;1m  }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7902274Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7902536Z ^[[36;1mAdd-Block "Free disk after each stage" "logs\disk.log" 40^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7902923Z ^[[36;1mAdd-Block "Directory sizes" "logs\sizes.log" 40^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7903284Z ^[[36;1mAdd-Block "Library fetch (tail)" "logs\libs.log" 100^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7903652Z ^[[36;1mAdd-Block "build.bat (tail)" "logs\build.log" 200^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7904130Z ^[[36;1mAdd-Block "CMakeError.log (tail)" "build\$env:MIXAR_ENV\CMakeFiles\CMakeError.log" 120^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7904551Z ^[[36;1m$out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7904772Z ^[[36;1m$out.Add("## Free space right now")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7905040Z ^[[36;1m$out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7905247Z ^[[36;1m$drive = Get-PSDrive C^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7905618Z ^[[36;1m$out.Add(("free {0:N1} GB, used {1:N1} GB" -f ($drive.Free / 1GB), ($drive.Used / 1GB)))^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7906013Z ^[[36;1m$out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7906339Z ^[[36;1mSet-Content -Path failure-report.md -Value $out -Encoding utf8^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7906861Z ^[[36;1mGet-Content failure-report.md | Add-Content -Path $env:GITHUB_STEP_SUMMARY^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7907551Z ^[[36;1m$pr = gh pr list --repo $env:GITHUB_REPOSITORY --head $env:GITHUB_REF_NAME --state open --json number --jq '.[0].number'^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7908077Z ^[[36;1mif ($pr) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7908411Z ^[[36;1m  gh pr comment $pr --repo $env:GITHUB_REPOSITORY --body-file failure-report.md^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7908858Z ^[[36;1m  Write-Host "reported on pull request #$pr"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7909557Z ^[[36;1m} else {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7909887Z ^[[36;1m  Write-Host "no open pull request for $env:GITHUB_REF_NAME - trying Issues"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7910350Z ^[[36;1m  gh issue create --repo $env:GITHUB_REPOSITORY `^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7910727Z ^[[36;1m    --title "Windows build failed - run 31964847354" `^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7911058Z ^[[36;1m    --body-file failure-report.md^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7911549Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7976697Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977039Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977204Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977402Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977601Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977799Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7977989Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7978219Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7978510Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7978713Z   SHORT_SHA: 9293526
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7978891Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7991404Z   GH_TOKEN: ***
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:08.7991733Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.2901260Z no open pull request for main - trying Issues
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.5990273Z the 'aimcrazyxx/mixar-app' repository has disabled issues
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6642863Z ##[error]Process completed with exit code 1.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6912281Z ##[group]Run Get-PSDrive C | Select-Object Used, Free | Format-List
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6912871Z ^[[36;1mGet-PSDrive C | Select-Object Used, Free | Format-List^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6913318Z ^[[36;1mif (Test-Path logs\disk.log) { Get-Content logs\disk.log }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6913754Z ^[[36;1m$errorLog = "build\$env:MIXAR_ENV\CMakeFiles\CMakeError.log"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6914110Z ^[[36;1mif (Test-Path $errorLog) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6914402Z ^[[36;1m  Write-Host "--- tail of $errorLog ---"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6914704Z ^[[36;1m  Get-Content $errorLog -Tail 200^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6914951Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6915160Z ^[[36;1mif (Test-Path "build\$env:MIXAR_ENV\bin") {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6915633Z ^[[36;1m  Get-ChildItem "build\$env:MIXAR_ENV\bin" | Select-Object Name | Format-Table -AutoSize^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6916049Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6980724Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6981097Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6981274Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6981466Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6981678Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6981872Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6982096Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6982341Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6982629Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6982836Z   SHORT_SHA: 9293526
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6983027Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:10.6983207Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.1799379Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.1828505Z ^[[32;1mUsed : ^[[0m109578547200
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.1829413Z ^[[32;1mFree : ^[[0m50889211904
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.1829716Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2049292Z after checkout                         33.5 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2051685Z after reclaim                          47.4 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2054040Z after libraries                        47.3 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2056560Z after build.bat (exit 1)               47.4 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2162233Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2190005Z ^[[32;1mName^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2190422Z ^[[32;1m----^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2191792Z datatoc.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2192122Z makesdna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2193049Z makesrna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2193367Z msgfmt.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2194337Z shader_tool.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2195907Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2920273Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2922108Z ##[group]Run actions/upload-artifact@v4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2922379Z with:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2922573Z   name: build-logs-31964847354
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2922816Z   path: logs/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2923012Z   if-no-files-found: warn
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2923478Z   retention-days: 14
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2923705Z   compression-level: 6
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2923904Z   overwrite: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2924112Z   include-hidden-files: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2924330Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2924489Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2924673Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2924873Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2925091Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2925282Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2925514Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2925792Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2925990Z   SHORT_SHA: 9293526
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2926169Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.2926341Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.5955370Z (node:8172) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.5956124Z (Use `node --trace-deprecation ...` to show where the warning was created)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.6037561Z With the provided path, there will be 4 files uploaded
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.6043256Z Artifact name is valid!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.6044772Z Root directory input is valid!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.7557408Z Beginning upload of artifact content to blob storage
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.8158341Z (node:8172) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.8447683Z Uploaded bytes 69535
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.8586005Z Finished uploading artifact content to blob storage!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.8587965Z SHA256 digest of uploaded artifact zip is f6e39883aa72ac07a44b959f7eabee58b57fef87eebf6556963ae2a27a30a281
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:11.8590288Z Finalizing artifact upload
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.0021465Z Artifact build-logs-31964847354.zip successfully finalized. Artifact ID 9268650706
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.0022600Z Artifact build-logs-31964847354 has been successfully uploaded! Final size is 69535 bytes. Artifact ID is 9268650706
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.0036287Z Artifact download URL: https://github.com/aimcrazyxx/mixar-app/actions/runs/31964847354/artifacts/9268650706
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.0525749Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.0527096Z Post job cleanup.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.2910327Z [command]"C:\Program Files\Git\bin\git.exe" version
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3190594Z git version 2.55.0.windows.3
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3255045Z Copying 'C:\Users\runneradmin\.gitconfig' to 'D:\a\_temp\01b575ab-68b9-4182-988d-00ea3b83d839\.gitconfig'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3282057Z Temporarily overriding HOME='D:\a\_temp\01b575ab-68b9-4182-988d-00ea3b83d839' before making global git config changes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3283592Z Adding repository directory to the temporary git global config as a safe directory
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3297662Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\mixar-app\mixar-app
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3649156Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.3973844Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:12.9754337Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.0620977Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.1550528Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.1804075Z http.https://github.com/.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.1843985Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.2131589Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.7465938Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.8285281Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.9217595Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:13.9506582Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.4609832Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.4947668Z file:D:/a/mixar-app/mixar-app/.git/modules/upstream/config	remote.origin.url
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.5122980Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.5456127Z file:D:/a/mixar-app/mixar-app/.git/modules/upstream/modules/lib/windows_x64/config	remote.origin.url
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.5741774Z [command]"C:\Program Files\Git\bin\git.exe" config --file D:/a/mixar-app/mixar-app/.git/modules/upstream/config --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.6026462Z [command]"C:\Program Files\Git\bin\git.exe" config --file D:/a/mixar-app/mixar-app/.git/modules/upstream/modules/lib/windows_x64/config --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.6546690Z Cleaning up orphan processes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.6792532Z Terminate orphan process: pid (4928) (vctip)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.6952973Z Terminate orphan process: pid (8896) (sccache)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.7096402Z Terminate orphan process: pid (8572) (conhost)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T19:07:14.7140643Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/cache/restore@v4, actions/cache/save@v4, actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
