<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Latest Blender 5.2 Windows build

Requested commit: `5b6f0e19ed2b294a0dfda59b8fb1b7c34b1fe229`

## Result

```json
{"conclusion":"failure","createdAt":"2026-08-16T12:10:24Z","databaseId":31946334651,"headSha":"5b6f0e19ed2b294a0dfda59b8fb1b7c34b1fe229","jobs":[{"completedAt":"2026-08-16T13:04:59Z","conclusion":"failure","databaseId":95162812080,"name":"Prod / Blender 5.2","startedAt":"2026-08-16T12:10:28Z","status":"completed","steps":[{"completedAt":"2026-08-16T12:10:29Z","conclusion":"success","name":"Set up job","number":1,"startedAt":"2026-08-16T12:10:28Z","status":"completed"},{"completedAt":"2026-08-16T12:10:30Z","conclusion":"success","name":"Configure git and derive short sha","number":2,"startedAt":"2026-08-16T12:10:29Z","status":"completed"},{"completedAt":"2026-08-16T12:10:38Z","conclusion":"success","name":"Checkout fork","number":3,"startedAt":"2026-08-16T12:10:30Z","status":"completed"},{"completedAt":"2026-08-16T12:10:38Z","conclusion":"success","name":"Verify batch files use CRLF","number":4,"startedAt":"2026-08-16T12:10:38Z","status":"completed"},{"completedAt":"2026-08-16T12:10:39Z","conclusion":"success","name":"Start the disk ledger","number":5,"startedAt":"2026-08-16T12:10:38Z","status":"completed"},{"completedAt":"2026-08-16T12:10:42Z","conclusion":"success","name":"Report runner state","number":6,"startedAt":"2026-08-16T12:10:39Z","status":"completed"},{"completedAt":"2026-08-16T12:10:42Z","conclusion":"success","name":"Tune build parallelism","number":7,"startedAt":"2026-08-16T12:10:42Z","status":"completed"},{"completedAt":"2026-08-16T12:18:20Z","conclusion":"success","name":"Reclaim disk space (hosted runners only)","number":8,"startedAt":"2026-08-16T12:10:42Z","status":"completed"},{"completedAt":"2026-08-16T12:18:51Z","conclusion":"success","name":"Install NSIS, Ninja and sccache if missing","number":9,"startedAt":"2026-08-16T12:18:20Z","status":"completed"},{"completedAt":"2026-08-16T12:18:51Z","conclusion":"success","name":"Restore compiler cache","number":10,"startedAt":"2026-08-16T12:18:51Z","status":"completed"},{"completedAt":"2026-08-16T12:24:13Z","conclusion":"success","name":"Pin upstream to the requested Blender revision","number":11,"startedAt":"2026-08-16T12:18:51Z","status":"completed"},{"completedAt":"2026-08-16T12:24:13Z","conclusion":"success","name":"Check the resource version matches the pinned tag","number":12,"startedAt":"2026-08-16T12:24:13Z","status":"completed"},{"completedAt":"2026-08-16T12:28:34Z","conclusion":"success","name":"Fetch Blender precompiled libraries","number":13,"startedAt":"2026-08-16T12:24:13Z","status":"completed"},{"completedAt":"2026-08-16T12:28:41Z","conclusion":"success","name":"Measure what the libraries cost","number":14,"startedAt":"2026-08-16T12:28:34Z","status":"completed"},{"completedAt":"2026-08-16T12:28:41Z","conclusion":"skipped","name":"Apply backend URL override","number":15,"startedAt":"2026-08-16T12:28:41Z","status":"completed"},{"completedAt":"2026-08-16T12:28:41Z","conclusion":"success","name":"Prepare .env","number":16,"startedAt":"2026-08-16T12:28:41Z","status":"completed"},{"completedAt":"2026-08-16T13:04:49Z","conclusion":"failure","name":"Build Mixar","number":17,"startedAt":"2026-08-16T12:28:41Z","status":"completed"},{"completedAt":"2026-08-16T13:04:49Z","conclusion":"success","name":"Compiler cache statistics","number":18,"startedAt":"2026-08-16T13:04:49Z","status":"completed"},{"completedAt":"2026-08-16T13:04:52Z","conclusion":"success","name":"Save compiler cache","number":19,"startedAt":"2026-08-16T13:04:49Z","status":"completed"},{"completedAt":"2026-08-16T13:04:52Z","conclusion":"skipped","name":"Overlay Mixar scripts into the bundle","number":20,"startedAt":"2026-08-16T13:04:52Z","status":"completed"},{"completedAt":"2026-08-16T13:04:52Z","conclusion":"skipped","name":"Package installer and portable zip","number":21,"startedAt":"2026-08-16T13:04:52Z","status":"completed"},{"completedAt":"2026-08-16T13:04:52Z","conclusion":"skipped","name":"Summarize artifacts","number":22,"startedAt":"2026-08-16T13:04:52Z","status":"completed"},{"completedAt":"2026-08-16T13:04:52Z","conclusion":"skipped","name":"Upload installer and portable build","number":23,"startedAt":"2026-08-16T13:04:52Z","status":"completed"},{"completedAt":"2026-08-16T13:04:54Z","conclusion":"success","name":"Publish the failure report","number":24,"startedAt":"2026-08-16T13:04:52Z","status":"completed"},{"completedAt":"2026-08-16T13:04:54Z","conclusion":"success","name":"Failure diagnostics","number":25,"startedAt":"2026-08-16T13:04:54Z","status":"completed"},{"completedAt":"2026-08-16T13:04:55Z","conclusion":"success","name":"Upload logs","number":26,"startedAt":"2026-08-16T13:04:54Z","status":"completed"},{"completedAt":"2026-08-16T13:04:58Z","conclusion":"success","name":"Post Checkout fork","number":52,"startedAt":"2026-08-16T13:04:55Z","status":"completed"},{"completedAt":"2026-08-16T13:04:58Z","conclusion":"success","name":"Complete job","number":53,"startedAt":"2026-08-16T13:04:58Z","status":"completed"}],"url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31946334651/job/95162812080"}],"status":"completed","updatedAt":"2026-08-16T13:05:00Z","url":"https://github.com/aimcrazyxx/mixar-app/actions/runs/31946334651"}
```

## Failed log

```text
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.6447001Z [3512/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sorttime.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.7113604Z [3513/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sort_asc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.7169829Z [3514/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sort_desc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.7701531Z [3515/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sound.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.8404989Z [3516/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sparkle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.8431956Z [3517/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\speaker.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.8943082Z [3518/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sphere.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.9663867Z [3519/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\split_horizontal.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:25.9687554Z [3520/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\spherecurve.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.0219702Z [3521/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\split_vertical.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.0916511Z [3522/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\spreadsheet.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.0956913Z [3523/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_error.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.1619444Z [3524/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_error_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.2208092Z [3525/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_info.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.2324753Z [3526/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_info_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.2837629Z [3527/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_warning.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.3443686Z [3528/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\status_warning_filled.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.3625333Z [3529/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\statusbar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.4129826Z [3530/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_disable.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.4769481Z [3531/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_loc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.4852576Z [3532/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\sticky_uvs_vert.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.5437884Z [3533/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\strands.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.6050333Z [3534/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\stroke.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.6220541Z [3535/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\stylus_pressure.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.7388338Z [3536/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.7646233Z [3537/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncircle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.8133080Z [3538/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncurve.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.8439832Z [3539/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ncylinder.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.8988263Z [3540/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_nsphere.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.9330747Z [3541/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_nsurface.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:26.9698140Z [3542/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\surface_ntorus.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.0260133Z [3543/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\syntax_off.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.0573047Z [3544/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\syntax_on.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.0987558Z [3545/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\system.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.1499853Z [3546/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tag.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.1828493Z [3547/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\temp.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.2212805Z [3548/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\text.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.2827160Z [3549/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\texture.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.3129262Z [3550/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\texture_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.3557238Z [3551/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\three_dots.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.4067535Z [3552/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\time.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.4366496Z [3553/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tool_settings.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.4826065Z [3554/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\topbar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.5340153Z [3555/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.5598284Z [3556/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracker.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.6090656Z [3557/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracker_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.6626403Z [3558/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.6857240Z [3559/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.7332957Z [3560/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_backwards_single.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.7905874Z [3561/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_clear_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.8228844Z [3562/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_clear_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.8684028Z [3563/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.9201912Z [3564/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_forwards_single.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.9471987Z [3565/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_refine_backwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:27.9968051Z [3566/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tracking_refine_forwards.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.0411645Z [3567/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\transform_origins.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.0742235Z [3568/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\trash.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.1211960Z [3569/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_down.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.1688200Z [3570/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_down_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.1990335Z [3571/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_left.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.2459898Z [3572/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_left_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.2925667Z [3573/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_right.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.3236930Z [3574/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_right_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.3808066Z [3575/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_up.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.4401497Z [3576/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\tria_up_bar.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.4678946Z [3577/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uglypackage.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.5248774Z [3578/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\underline.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.5766553Z [3579/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unlinked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.6005890Z [3580/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unlocked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.6535825Z [3581/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\unpinned.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.7063657Z [3582/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\url.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.7174266Z [3583/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\usb_drive.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.7773249Z [3584/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\usb_drive_large.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.8322550Z [3585/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\user.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.8428756Z [3586/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.9095631Z [3587/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.9578423Z [3588/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_edgesel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:28.9793387Z [3589/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_facesel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.0359853Z [3590/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_islandsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.0815597Z [3591/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_sync_select.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.1016802Z [3592/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\uv_vertexsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.1626857Z [3593/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vertexsel.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.2124044Z [3594/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vertex_crease.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.2331729Z [3595/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view3d.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.2872256Z [3596/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\viewzoom.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.3406057Z [3597/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_camera.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.3582064Z [3598/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_camera_unselected.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.4089101Z [3599/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_locked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.4767470Z [3600/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_ortho.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.4853466Z [3601/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_pan.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.5405749Z [3602/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_perspective.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.6018088Z [3603/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_unlocked.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.6080332Z [3604/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\view_zoom.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.6673174Z [3605/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_00.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.7270329Z [3606/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_01.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.7349267Z [3607/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_10.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.7881613Z [3608/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vis_sel_11.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.8554148Z [3609/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\volume_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.8582493Z [3610/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\vpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.9175156Z [3611/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\warning_large.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.9797607Z [3612/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\window.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:29.9821315Z [3613/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wordwrap_off.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.0442545Z [3614/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wordwrap_on.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.1098861Z [3615/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\workspace.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.1121318Z [3616/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\world.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.1725418Z [3617/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\world_data.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.2320809Z [3618/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\wpaint_hlt.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.2342416Z [3619/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\x.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.3075592Z [3620/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\xray.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.3542643Z [3621/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_all.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.3598574Z [3622/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_in.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.4298519Z [3623/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_out.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.4796756Z [3624/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_previous.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.4865249Z [3625/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\icons_svg\zoom_selected.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.6191460Z [3626/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_blade.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.6276898Z [3627/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_both_handles.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.7066900Z [3628/8229] Building CXX object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\svg_icons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.7561571Z [3629/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_crosshair.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.7598635Z [3630/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_crossc.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.8404539Z [3631/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_dot.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.8804188Z [3632/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_e_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.8914539Z [3633/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_eraser.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:30.9700013Z [3634/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_ew_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.0132309Z [3635/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_eyedropper.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.0225830Z [3636/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.1198238Z [3637/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand_closed.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.1523874Z [3638/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_hand_point.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.1563820Z [3639/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_h_split.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.2461601Z [3640/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_knife.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.2894655Z [3641/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_left_handle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.2916278Z [3642/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_mute.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.3830967Z [3643/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_n_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.4190724Z [3644/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_nsew_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.4227293Z [3645/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_ns_scroll.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.5275496Z [3646/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_paint.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.5635618Z [3647/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pick_area.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.5681395Z [3648/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pencil.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.6746388Z [3649/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_pointer.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.6995370Z [3650/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_s_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.7085694Z [3651/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_right_handle.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.8153411Z [3652/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_slip.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.8247664Z [3653/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_stop.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.8412535Z [3654/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_swap_area.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.9459770Z [3655/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_text_edit.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.9595268Z [3656/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_v_split.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:31.9773501Z [3657/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_vertex_loop.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.0743654Z [3658/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_wait.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.0887236Z [3659/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_w_arrow.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.1104498Z [3660/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_x_move.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.2101387Z [3661/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_y_move.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.2375894Z [3662/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_zoom_in.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:32.2561851Z [3663/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\cursors\cursor_zoom_out.svg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:33.7376889Z [3664/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\preview_grease_pencil.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:33.9924304Z [3665/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\startup.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.0238390Z [3666/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\preview.blend.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.1561214Z [3667/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_41_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.1806244Z [3668/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\splash.png.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.2481616Z [3669/8229] Building C object source\blender\editors\datafiles\CMakeFiles\bf_editor_datafiles.dir\__\__\__\__\release\datafiles\startup.mixar.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.3297145Z [3670/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_40_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.3393050Z [3671/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_39_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.4125717Z [3672/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_38_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.4933989Z [3673/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_37_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.5189158Z [3674/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_36_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.5300696Z [3675/8229] Linking CXX static library lib\bf_editor_datafiles.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.5637170Z [3676/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_35_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.6282129Z [3677/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_34_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.6678307Z [3678/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_33_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.7090864Z [3679/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_32_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.7820616Z [3680/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_31_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.8147895Z [3681/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_30_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.8629526Z [3682/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_29_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.9253028Z [3683/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_28_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:34.9553879Z [3684/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_27_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.0577236Z [3685/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_26_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.0827847Z [3686/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_25_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.1480670Z [3687/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_24_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.2342301Z [3688/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.2944239Z [3689/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_23_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.3354494Z [3690/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.4188872Z [3691/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.4337875Z [3692/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.4907321Z [3693/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.6064104Z [3694/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.6328492Z [3695/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.6761628Z [3696/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.8039655Z [3697/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.8580352Z [3698/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:35.8752844Z [3699/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.0344843Z [3700/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.0638453Z [3701/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.1262464Z [3702/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.2749093Z [3703/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.3505300Z [3704/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.4559372Z [3705/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.5286756Z [3706/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.5573057Z [3707/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.6006124Z [3708/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.7186904Z [3709/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.7700741Z [3710/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.8105148Z [3711/8229] Building C object source\blender\draw\CMakeFiles\bf_draw_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.8575586Z [3712/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_26_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.8744517Z [3713/8229] Linking C static library lib\bf_draw_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:36.9168046Z [3714/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_25_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.0025895Z [3715/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_24_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.0146851Z [3716/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_23_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.0976911Z [3717/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.1419052Z [3718/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.2188517Z [3719/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.2508908Z [3720/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.3050800Z [3721/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.3517230Z [3722/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.4019865Z [3723/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.4328223Z [3724/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.5346969Z [3725/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.5551476Z [3726/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.5872377Z [3727/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.6745182Z [3728/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.7280804Z [3729/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.7464111Z [3730/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.8331970Z [3731/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.8864457Z [3732/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:37.9801387Z [3733/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.0364518Z [3734/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.0493176Z [3735/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.1216894Z [3736/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.1829519Z [3737/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.1920557Z [3738/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.2776894Z [3739/8229] Building C object source\blender\gpu\CMakeFiles\bf_gpu_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.3280735Z [3740/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_vert.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.3325153Z [3741/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_frag.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.3513583Z [3742/8229] Linking C static library lib\bf_gpu_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.4107231Z [3743/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_lib.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.4521486Z [3744/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\shaders\gpu_shader_display_transform_fallback_lib.glsl.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.4605322Z [3745/8229] Building C object source\blender\imbuf\opencolorio\CMakeFiles\bf_imbuf_opencolorio_shaders.dir\intern\ocio_shader_shared.hh.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:38.5179244Z [3746/8229] Linking C static library lib\bf_imbuf_opencolorio_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:40.4100953Z [3747/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\makesrna_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:41.7086246Z [3748/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\makesrna.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:42.1988713Z [3749/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_define.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:43.4990901Z [3750/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ID.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:44.7810941Z [3751/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:44.8055608Z [3752/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_action.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:46.2374556Z [3753/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animviz.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:47.5446352Z [3754/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_annotations.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:47.9088586Z [3755/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_asset.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:49.2023036Z [3756/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_armature.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:50.9541389Z [3757/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_attribute.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:51.7881081Z [3758/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_boid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:51.9207623Z [3759/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_blendfile_import.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:54.1284986Z [3760/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_cachefile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:54.1836637Z [3761/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_brush.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:54.5977263Z [3762/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_camera.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:56.6633672Z [3763/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_collection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:56.9601158Z [3764/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_cloth.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:57.3213555Z [3765/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:58.7988421Z [3766/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:31:59.7853676Z [3767/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_constraint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:00.1628894Z [3768/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:01.5070666Z [3769/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curveprofile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:02.4370889Z [3770/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curves.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:02.9360724Z [3771/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_depsgraph.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:04.4719415Z [3772/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_dynamicpaint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:05.0566999Z [3773/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fcurve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:06.1072643Z [3774/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fluid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:07.2709525Z [3775/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_grease_pencil.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:07.7759036Z [3776/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_image.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:08.8873600Z [3777/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_key.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:09.4716244Z [3778/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lattice.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:10.5338250Z [3779/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_layer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:11.1082821Z [3780/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_light.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:12.1160766Z [3781/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lightprobe.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:12.8562462Z [3782/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_main.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:13.3781977Z [3783/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_linestyle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:14.9462315Z [3784/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mask.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:16.0424882Z [3785/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_material.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:16.7176030Z [3786/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_meta.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:16.8364148Z [3787/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mesh.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:19.3118576Z [3788/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_nla.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:19.4411136Z [3789/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_movieclip.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:22.1911699Z [3790/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_node_tree_interface.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:22.6519941Z [3791/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_modifier.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:23.8774567Z [3792/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_node_socket.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:25.5392235Z [3793/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:26.7174807Z [3794/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object_force.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:27.1392883Z [3795/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_packedfile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:28.3355669Z [3796/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_nodetree.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:29.3503863Z [3797/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_palette.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:29.9519018Z [3798/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pointcloud.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:30.3126230Z [3799/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_particle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:32.0786679Z [3800/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pose.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:32.8349588Z [3801/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_rigidbody.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:33.7946684Z [3802/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_rna.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:34.3025957Z [3803/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_render.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:36.4599664Z [3804/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_scene.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:37.8036503Z [3805/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sculpt_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:38.2559149Z [3806/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_screen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:39.4839233Z [3807/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sequencer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:39.9118354Z [3808/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sound.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:40.7391918Z [3809/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_shader_fx.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:41.5538226Z [3810/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_speaker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:42.4040105Z [3811/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_test.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:44.0625094Z [3812/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_text.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:44.8738270Z [3813/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_space.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:45.3322873Z [3814/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_texture.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:46.9719194Z [3815/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_timeline.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:47.8519412Z [3816/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_tracking.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:49.8679881Z [3817/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:50.5170485Z [3818/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_vfont.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:50.5812102Z [3819/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_userdef.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:52.4396508Z [3820/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_volume.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:52.8914945Z [3821/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_mixar.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:55.0176355Z [3822/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:55.0746159Z [3823/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:55.4354079Z [3824/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_workspace.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:57.4539127Z [3825/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_world.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:57.6547390Z [3826/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_xr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:58.0763847Z [3827/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_usd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:59.1616125Z [3828/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_action_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:32:59.6814532Z [3829/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_armature_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:00.1536806Z [3830/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_animation_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:00.8570541Z [3831/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_camera_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:01.3642566Z [3832/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curve_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:01.9638744Z [3833/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_curves_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:03.5086648Z [3834/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_fcurve_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:03.5198234Z [3835/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_image_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:04.2194415Z [3836/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_grease_pencil_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:05.1908887Z [3837/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_lattice_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:05.9263921Z [3838/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_material_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:06.9191830Z [3839/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_mesh_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:07.4085210Z [3840/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_main_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:07.5984117Z [3841/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_meta_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:09.0186758Z [3842/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_pose_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:09.1188893Z [3843/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_object_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:10.0711637Z [3844/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_scene_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:10.7202855Z [3845/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sound_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:11.5543725Z [3846/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_sequencer_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:12.2097752Z [3847/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_space_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:12.3215923Z [3848/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_text_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:13.2553640Z [3849/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_texture_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:14.0184542Z [3850/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_vfont_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:15.0972143Z [3851/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_ui_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:16.6040063Z [3852/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_gizmo_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.3830032Z [3853/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_workspace_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.3873239Z [3854/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\rna_wm_api.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.5165293Z [3855/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_22_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.6580768Z [3856/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_21_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.7898322Z [3857/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_20_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:17.9243394Z [3858/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_19_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.0869239Z [3859/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_18_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.2254576Z [3860/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_17_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.3657483Z [3861/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_16_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.5723464Z [3862/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\__\__\__\__\intern\clog\clog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.5980470Z [3863/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_15_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.7420750Z [3864/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_13_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.7507969Z [3865/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_14_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.8857945Z [3866/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_11_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:18.8890637Z [3867/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_12_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.0246574Z [3868/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_10_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.0271661Z [3869/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_9_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.1633283Z [3870/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_8_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.2025180Z [3871/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_7_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.3142920Z [3872/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_6_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.3442701Z [3873/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_5_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.4765444Z [3874/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_4_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.4855276Z [3875/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_3_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.8124853Z [3876/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_1_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:19.8833811Z [3877/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_2_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:20.1388638Z [3878/8229] Building C object source\blender\compositor\CMakeFiles\bf_compositor_shaders.dir\Unity\unity_0_c.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:20.1906177Z [3879/8229] Linking C static library lib\bf_compositor_shaders.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:20.4834998Z [3880/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\makesrna.dir\__\__\makesdna\intern\dna_parse.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:20.8354902Z [3881/8229] Linking CXX executable bin\makesrna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:22.1372142Z [3882/8229] Generating rna_ID_gen.cc, rna_action_gen.cc, rna_animation_gen.cc, rna_animviz_gen.cc, rna_annotations_gen.cc, rna_armature_gen.cc, rna_asset_gen.cc, rna_attribute_gen.cc, rna_blendfile_import_gen.cc, rna_boid_gen.cc, rna_brush_gen.cc, rna_cachefile_gen.cc, rna_camera_gen.cc, rna_cloth_gen.cc, rna_collection_gen.cc, rna_color_gen.cc, rna_constraint_gen.cc, rna_context_gen.cc, rna_curve_gen.cc, rna_curveprofile_gen.cc, rna_curves_gen.cc, rna_depsgraph_gen.cc, rna_dynamicpaint_gen.cc, rna_fcurve_gen.cc, rna_fluid_gen.cc, rna_grease_pencil_gen.cc, rna_image_gen.cc, rna_key_gen.cc, rna_lattice_gen.cc, rna_layer_gen.cc, rna_light_gen.cc, rna_lightprobe_gen.cc, rna_linestyle_gen.cc, rna_main_gen.cc, rna_mask_gen.cc, rna_material_gen.cc, rna_mesh_gen.cc, rna_meta_gen.cc, rna_modifier_gen.cc, rna_movieclip_gen.cc, rna_nla_gen.cc, rna_node_socket_gen.cc, rna_node_tree_interface_gen.cc, rna_nodetree_gen.cc, rna_object_gen.cc, rna_object_force_gen.cc, rna_packedfile_gen.cc, rna_palette_gen.cc, rna_particle_gen.cc, rna_pointcloud_gen.cc, rna_pose_gen.cc, rna_render_gen.cc, rna_rigidbody_gen.cc, rna_rna_gen.cc, rna_scene_gen.cc, rna_screen_gen.cc, rna_sculpt_paint_gen.cc, rna_sequencer_gen.cc, rna_shader_fx_gen.cc, rna_sound_gen.cc, rna_space_gen.cc, rna_speaker_gen.cc, rna_test_gen.cc, rna_text_gen.cc, rna_texture_gen.cc, rna_timeline_gen.cc, rna_tracking_gen.cc, rna_ui_gen.cc, rna_userdef_gen.cc, rna_vfont_gen.cc, rna_volume_gen.cc, rna_wm_gen.cc, rna_wm_mixar_gen.cc, rna_wm_gizmo_gen.cc, rna_workspace_gen.cc, rna_world_gen.cc, rna_xr_gen.cc, rna_usd_gen.cc, rna_prototypes_gen.hh, ../RNA_prototypes.hh
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:22.1403264Z [3883/8229] Building CXX object intern\clog\CMakeFiles\bf_intern_clog.dir\clog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:22.1822552Z [3884/8229] Linking CXX static library lib\bf_intern_clog.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:28.5152817Z [3885/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_access.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:37.0289410Z [3886/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_access_compare_override.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:39.2191877Z [3887/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\eigenvalues.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:40.3001623Z [3888/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\linear_solver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:42.1618050Z [3889/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_define.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:42.4904217Z [3890/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_path.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:48.1482889Z [3891/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_animation_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:48.9897032Z [3892/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_action_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:51.1802967Z [3893/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_ID_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:52.8444940Z [3894/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_animviz_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:54.2330254Z [3895/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_annotations_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:58.1399158Z [3896/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_asset_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:33:58.9136242Z [3897/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_armature_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:01.5640043Z [3898/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_attribute_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:03.2245029Z [3899/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_blendfile_import_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:04.3710584Z [3900/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_boid_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:08.4875876Z [3901/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_cachefile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:11.8009584Z [3902/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_camera_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:14.9768828Z [3903/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_cloth_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:17.2604029Z [3904/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_collection_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:20.3205654Z [3905/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_color_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:23.8717740Z [3906/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_constraint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:25.1743768Z [3907/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_context_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:29.2381553Z [3908/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curve_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:29.9000520Z [3909/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curveprofile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:35.1404966Z [3910/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_depsgraph_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:35.4444531Z [3911/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_brush_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:35.7632305Z [3912/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_curves_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:41.1627423Z [3913/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_fcurve_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:41.9736516Z [3914/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_dynamicpaint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:48.9995011Z [3915/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_grease_pencil_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:49.6246583Z [3916/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_image_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:53.5649996Z [3917/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_key_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:55.2071734Z [3918/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_lattice_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:34:58.9418612Z [3919/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_fluid_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:00.4493032Z [3920/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_light_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:00.9210588Z [3921/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_layer_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:04.1035430Z [3922/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_lightprobe_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:07.8316305Z [3923/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_linestyle_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:09.9320760Z [3924/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_main_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:10.0762291Z [3925/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_mask_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:14.9520681Z [3926/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_material_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:15.4118597Z [3927/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_meta_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:20.6210091Z [3928/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_mesh_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:21.7560988Z [3929/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_movieclip_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:27.6916109Z [3930/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_nla_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:30.0304731Z [3931/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_modifier_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:30.4086474Z [3932/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_node_socket_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:37.6022595Z [3933/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_node_tree_interface_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:44.3762193Z [3934/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_object_force_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:52.1011274Z [3935/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_packedfile_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:58.7783381Z [3936/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_nodetree_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:35:58.9747566Z [3937/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_palette_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:03.7370531Z [3938/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_pointcloud_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:09.8907222Z [3939/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_object_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:12.2336704Z [3940/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_pose_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:18.1011658Z [3941/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_rigidbody_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:19.6498919Z [3942/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_render_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:22.1950572Z [3943/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_particle_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:23.5406941Z [3944/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_rna_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:27.8732348Z [3945/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_screen_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:31.3963944Z [3946/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sculpt_paint_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:38.0194036Z [3947/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_shader_fx_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:39.1617634Z [3948/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sequencer_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:42.6775308Z [3949/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_sound_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:42.8585809Z [3950/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_scene_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:47.6325414Z [3951/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_test_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:48.0773786Z [3952/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_speaker_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:53.7852214Z [3953/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_text_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:55.2357360Z [3954/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_texture_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:55.3466842Z [3955/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_space_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:36:59.0860798Z [3956/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_timeline_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:01.2032365Z [3957/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_tracking_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:03.5416704Z [3958/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_ui_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:06.2557126Z [3959/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_vfont_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:09.4499017Z [3960/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_volume_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:14.1330228Z [3961/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_userdef_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:15.8225800Z [3962/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_mixar_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:18.4229855Z [3963/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:20.9529821Z [3964/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_workspace_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:21.4176712Z [3965/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_wm_gizmo_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:23.6994177Z [3966/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_world_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:26.0697887Z [3967/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_usd_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:27.5873811Z [3968/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\matrix.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.0114449Z [3969/8229] Building CXX object intern\utfconv\CMakeFiles\bf_intern_utfconv.dir\utfconv.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.3247316Z [3970/8229] Building CXX object source\blender\makesrna\intern\CMakeFiles\bf_rna.dir\rna_xr_gen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.5590423Z [3971/8229] Building CXX object intern\uriconvert\CMakeFiles\bf_intern_uriconvert.dir\uri_convert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.7688978Z [3972/8229] Building C object extern\wcwidth\CMakeFiles\extern_wcwidth.dir\wcwidth.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.8839315Z [3973/8229] Linking CXX static library lib\bf_rna.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:28.8959555Z [3974/8229] Building CXX object intern\utfconv\CMakeFiles\bf_intern_utfconv.dir\utf_winfunc.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.4544142Z [3975/8229] Generating register_geometry_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.4661195Z [3976/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_assert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.4976094Z [3977/8229] Linking CXX static library lib\bf_intern_uriconvert.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.5090363Z [3978/8229] Building C object extern\xxhash\CMakeFiles\extern_xxhash.dir\xxhash.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.5473915Z [3979/8229] Linking CXX static library lib\bf_intern_utfconv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.5814335Z [3980/8229] Linking C static library lib\extern_wcwidth.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.6189821Z [3981/8229] Linking C static library lib\extern_xxhash.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.6253539Z [3982/8229] Building CXX object source\blender\nodes\geometry\CMakeFiles\bf_nodes_geometry_generated.dir\register_geometry_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.6722780Z [3983/8229] Linking CXX static library lib\bf_nodes_geometry_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:29.7813317Z [3984/8229] Generating register_function_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:31.5278864Z [3985/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_colorspace.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:31.6944046Z [3986/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:31.8192207Z [3987/8229] Building CXX object source\blender\nodes\function\CMakeFiles\bf_nodes_functions_generated.dir\register_function_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:31.8657991Z [3988/8229] Linking CXX static library lib\bf_nodes_functions_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:32.0291595Z [3989/8229] Generating register_compositor_nodes.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:32.4829356Z [3990/8229] Building CXX object intern\eigen\CMakeFiles\bf_intern_eigen.dir\intern\svd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:32.5423473Z [3991/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_dial_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:32.5465989Z [3992/8229] Linking CXX static library lib\bf_intern_eigen.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:32.8245879Z [3993/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_dynstr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:33.6986089Z [3994/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_ghash.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:33.7103244Z [3995/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_ghash_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:34.5099711Z [3996/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_filelist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:34.6490654Z [3997/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_heap_simple.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:34.6643663Z [3998/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_heap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:35.3414459Z [3999/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_linklist_lockfree.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:35.5380690Z [4000/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_linklist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:36.1908202Z [4001/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memarena.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:36.5504290Z [4002/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_kdopbvh.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:36.6294943Z [4003/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memblock.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:37.2183364Z [4004/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_memiter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:37.9689543Z [4005/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_mempool.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:38.7236952Z [4006/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_timer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:38.8735433Z [4007/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_mmap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:39.6767030Z [4008/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store_rle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:40.1992131Z [4009/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_subprocess.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:40.6493721Z [4010/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:40.7539091Z [4011/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_store.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:41.5793408Z [4012/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_utils_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:41.7505813Z [4013/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\astar.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:42.7904505Z [4014/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_bool_conversion.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:44.1908921Z [4015/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\array_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:44.3265655Z [4016/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_ref.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:45.0746931Z [4017/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bitmap.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:45.1301153Z [4018/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\atomic_disjoint_set.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:46.0439950Z [4019/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bit_span.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:46.1166170Z [4020/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\boxpack_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:46.2878795Z [4021/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\compression.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:46.9589032Z [4022/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\bitmap_draw_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:47.7826944Z [4023/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cache_mutex.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:48.2774640Z [4024/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\compute_context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:49.0724217Z [4025/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\convexhull_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:49.8549409Z [4026/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cpp_type.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:52.4910916Z [4027/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\csv_parse.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:55.2830449Z [4028/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\cpp_types.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:56.2386058Z [4029/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\easing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:57.5900886Z [4030/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\dot_export.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:57.6038605Z [4031/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\endian_switch.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:57.7608649Z [4032/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\delaunay_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:59.1478595Z [4033/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\expr_pylike_eval.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:59.5150361Z [4034/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fileops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:37:59.9234208Z [4035/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fftw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:00.8426110Z [4036/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_file.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:01.1827431Z [4037/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_gzip.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:01.9041657Z [4038/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fileops_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:02.1032641Z [4039/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\fnmatch.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:02.9580072Z [4040/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_memory.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:03.4110752Z [4041/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\filereader_zstd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:04.5579120Z [4042/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_vector_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:05.3596136Z [4043/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\gsqueue.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:05.6863957Z [4044/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_virtual_vector_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:05.8396818Z [4045/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\generic_virtual_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:05.8978310Z [4046/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_mm2a.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:06.0295876Z [4047/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_mm3.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:06.0640367Z [4048/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_md5.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:07.0700808Z [4049/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\implicit_sharing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:07.4358745Z [4050/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\hash_tables.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:08.7605114Z [4051/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_range.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:09.5969470Z [4052/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\jitter_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:12.6195011Z [4053/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_mask_expression.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:12.8020040Z [4054/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\lasso_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:13.2406763Z [4055/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\index_mask.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:14.1243576Z [4056/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\lazy_threading.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:14.1771150Z [4057/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\listbase.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:14.3935230Z [4058/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:15.2460034Z [4059/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\length_parameterize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:16.0107450Z [4060/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_basis_types.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:16.2887818Z [4061/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:16.8231277Z [4062/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_boolean.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:17.3298654Z [4063/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:18.0341244Z [4064/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_half.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:18.3046359Z [4065/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:19.9179853Z [4066/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_matrix_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:19.9811727Z [4067/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_interp.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:20.6066137Z [4068/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_rotation_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:21.3869945Z [4069/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_solvers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:22.0533551Z [4070/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_rotation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:22.2184042Z [4071/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_statistics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:22.3068062Z [4072/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_time.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:23.2727931Z [4073/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_vector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:24.2572834Z [4074/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_vec.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:25.7739431Z [4075/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_cache.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:28.0176047Z [4076/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_cache_file_load.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:28.5003534Z [4077/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\memory_counter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:30.9877020Z [4078/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\math_matrix.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:34.2067193Z [4079/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\noise.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:37.3161658Z [4080/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\mesh_boolean.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:37.3286945Z [4081/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\noise_c.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:37.6474300Z [4082/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\mesh_intersect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:39.0053153Z [4083/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\ordered_edge.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:40.3601532Z [4084/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\polyfill_2d.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:40.6688014Z [4085/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\offset_indices.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:40.6935199Z [4086/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\path_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:41.0821838Z [4087/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\quadric.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:41.4517904Z [4088/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\polyfill_2d_beautify.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:42.5246976Z [4089/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\radial_tiling_wrapper.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:43.0912533Z [4090/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\rand.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:43.3234409Z [4091/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\rct.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:44.2772207Z [4092/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\resource_scope.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:44.4241214Z [4093/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\scanfill.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:45.2060547Z [4094/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\scanfill_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:45.5956078Z [4095/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\smaa_textures.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:45.8377870Z [4096/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\sort.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:45.9790302Z [4097/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\sort_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:46.3619948Z [4098/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\session_uid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:46.7841004Z [4099/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\stack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:48.1144966Z [4100/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:48.4018025Z [4101/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\storage.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:48.9516509Z [4102/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_cursor_utf8.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:50.8606396Z [4103/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_ref.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:53.4792709Z [4104/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_utf8.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:53.6695486Z [4105/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\serialize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:53.6732690Z [4106/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_search.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:55.2465427Z [4107/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\string_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:55.7683255Z [4108/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\system.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:55.8391392Z [4109/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_graph.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:56.3664388Z [4110/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_iterator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:57.5140218Z [4111/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_pool.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:57.7993172Z [4112/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_scheduler.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:58.6140938Z [4113/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\tempfile.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:58.7785422Z [4114/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\task_range.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:38:59.8591914Z [4115/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\timecode.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:00.1555457Z [4116/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\threads.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:01.3322419Z [4117/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\time.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:02.7043746Z [4118/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\timeit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:03.1482765Z [4119/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\ustring.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:03.3729018Z [4120/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\uuid.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:03.6495582Z [4121/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\voxel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:04.3065418Z [4122/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\vector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:05.5178466Z [4123/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff_dir.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:05.5841331Z [4124/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\virtual_array.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:05.9719820Z [4125/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:06.6950689Z [4126/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\BLI_args.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:08.5580305Z [4127/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\system_win32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:08.7062309Z [4128/8229] Building CXX object source\blender\nodes\composite\CMakeFiles\bf_nodes_compositor_generated.dir\register_compositor_nodes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:08.7556064Z [4129/8229] Linking CXX static library lib\bf_nodes_compositor_generated.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:08.8537854Z [4130/8229] Building CXX object source\blender\blentranslation\msgfmt\CMakeFiles\msgfmt.dir\msgfmt.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:10.3524639Z [4131/8229] Building CXX object source\blender\blenlib\CMakeFiles\bf_blenlib.dir\intern\winstuff_registration.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:10.5447639Z [4132/8229] Linking CXX static library lib\bf_blenlib.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:10.8317039Z [4133/8229] Linking CXX executable bin\msgfmt.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:10.9296501Z [4134/8229] Generating ab.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.0220361Z [4135/8229] Building CXX object source\blender\freestyle\CMakeFiles\bf_freestyle.dir\cmake_pch.cxx.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.0373310Z [4136/8229] Generating ar.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.1211867Z [4137/8229] Generating be.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.1912861Z [4138/8229] Generating bg.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.4428649Z [4139/8229] Generating ca.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.5418201Z [4140/8229] Generating cs.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.6110458Z [4141/8229] Generating da.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.6561788Z [4142/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Buttons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.7201183Z [4143/8229] Generating de.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:11.7884211Z [4144/8229] Generating el.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.0233936Z [4145/8229] Generating en_GB.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.0932527Z [4146/8229] Generating eo.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.3098765Z [4147/8229] Generating es.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.3275059Z [4148/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_CallbackEventConsumer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.3784050Z [4149/8229] Generating eu.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.4410564Z [4150/8229] Generating fa.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.5332124Z [4151/8229] Generating fi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.7769103Z [4152/8229] Generating fr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.8488142Z [4153/8229] Generating he.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.9195379Z [4154/8229] Generating hi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:12.9879395Z [4155/8229] Generating hr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.0954899Z [4156/8229] Generating hu.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.1881592Z [4157/8229] Generating id.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.3126993Z [4158/8229] Generating it.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.5450662Z [4159/8229] Generating ja.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.7444748Z [4160/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextNone.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.8259178Z [4161/8229] Generating ka.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:13.9430404Z [4162/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Context.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.0766855Z [4163/8229] Generating ko.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.1832576Z [4164/8229] Generating ky.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.2583317Z [4165/8229] Generating lt.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.3265655Z [4166/8229] Generating ml.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.3995238Z [4167/8229] Generating nb.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.4745466Z [4168/8229] Generating nl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.7173469Z [4169/8229] Generating pl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:14.9001035Z [4170/8229] Generating pt.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.0285892Z [4171/8229] Generating pt_BR.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.0976113Z [4172/8229] Generating ro.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.3392051Z [4173/8229] Generating ru.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.5596046Z [4174/8229] Generating sk.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.8762664Z [4175/8229] Generating sl.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.9058752Z [4176/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_EventManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:15.9711226Z [4177/8229] Generating sr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:16.0645568Z [4178/8229] Generating sr@latin.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:16.3047893Z [4179/8229] Generating sv.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:16.4954792Z [4180/8229] Generating sw.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:16.8721181Z [4181/8229] Generating ta.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.0018171Z [4182/8229] Generating th.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.0788832Z [4183/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ISystem.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.1811047Z [4184/8229] Generating tr.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.3439828Z [4185/8229] Generating uk.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.5783300Z [4186/8229] Generating ur.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.7873641Z [4187/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ISystemPaths.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:17.8064425Z [4188/8229] Generating vi.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:18.0603549Z [4189/8229] Generating zh_HANS.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:18.2115211Z [4190/8229] Generating zh_HANT.mo
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:18.5463790Z [4191/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ModifierKeys.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:19.2952300Z [4192/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_PathUtils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:19.6496870Z [4193/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Rect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:20.9261414Z [4194/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_System.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:20.9569849Z [4195/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_TimerManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:22.1748004Z [4196/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Window.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:22.6651710Z [4197/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_WindowManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:24.5857389Z [4198/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_NDOFManager.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:26.2304606Z [4199/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextVK.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:26.8688979Z [4200/8229] Building CXX object source\blender\io\usd\CMakeFiles\bf_io_usd.dir\cmake_pch.cxx.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:27.7841581Z [4201/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextD3D.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:29.1806644Z [4202/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_DropTargetWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:30.2858265Z [4203/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_TrackpadWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:32.6093066Z [4204/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Wintab.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:32.6509994Z [4205/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_SystemWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:33.7051410Z [4206/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_WindowWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:34.8862387Z [4207/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ContextWGL.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:35.1883645Z [4208/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_NDOFManagerWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:35.6623937Z [4209/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_ImeWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:37.3829369Z [4210/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_Xr.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:37.5300732Z [4211/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_SystemPathsWin32.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:39.1600410Z [4212/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrAction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:41.3710278Z [4213/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrEvent.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:41.4093229Z [4214/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrContext.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:44.5906436Z [4215/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBinding.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:46.6007714Z [4216/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrSession.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:47.5423747Z [4217/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrSwapchain.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:52.1318605Z [4218/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBindingD3D.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:54.2499967Z [4219/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrGraphicsBindingVulkan.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:59.4863091Z [4220/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\autotrack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:59.6766024Z [4221/8229] Building CXX object intern\ghost\CMakeFiles\bf_intern_ghost.dir\intern\GHOST_XrControllerModel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:39:59.7987431Z [4222/8229] Linking CXX static library lib\bf_intern_ghost.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:00.9819916Z [4223/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\camera_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:02.2265138Z [4224/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\detector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:04.2343644Z [4225/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\frame_accessor.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:05.6064028Z [4226/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:05.6375335Z [4227/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\homography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:06.6802024Z [4228/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\image.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:09.8842808Z [4229/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\track_region.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:10.9532507Z [4230/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:11.4364402Z [4231/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:14.6970602Z [4232/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\intern\tracksN.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:16.3227187Z [4233/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\autotrack.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:17.5563787Z [4234/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\base\aligned_malloc.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:19.4635977Z [4235/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\image\array_nd.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:19.7097267Z [4236/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:26.6429372Z [4237/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\image\convolve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:29.7175622Z [4238/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\autotrack\predict_tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:40:34.8345106Z [4239/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\conditioning.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:41:05.9168959Z [4240/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\homography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:41:34.4629351Z [4241/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\euclidean_resection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:41:54.6305282Z [4242/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\panography.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:41:57.3353776Z [4243/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\fundamental.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:41:58.0440168Z [4244/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\panography_kernel.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:04.8499473Z [4245/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\numeric\numeric.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:05.1981625Z [4246/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\numeric\poly.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:05.8442303Z [4247/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\triangulation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:09.0770941Z [4248/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\multiview\projection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:10.0901507Z [4249/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\camera_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:14.2626164Z [4250/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\detect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:17.0810884Z [4251/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\bundle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:22.9110230Z [4252/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\distortion_models.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:24.5055930Z [4253/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\initialize_reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:33.8534260Z [4254/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\modal_solver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:34.4468138Z [4255/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\packed_intrinsics.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:39.6661161Z [4256/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\pipeline.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:42:47.4659627Z [4257/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\reconstruction.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:00.4639295Z [4258/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\reconstruction_scale.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:03.6077062Z [4259/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\keyframe_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:11.7786243Z [4260/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\tracks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:16.2281537Z [4261/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\brute_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:17.3886077Z [4262/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\intersect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:20.3825141Z [4263/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\hybrid_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:21.4037081Z [4264/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\klt_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:22.2032890Z [4265/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\retrack_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:24.8421718Z [4266/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\pyramid_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:44.9442384Z [4267/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\trklt_region_tracker.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:47.0552547Z [4268/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_CacheLimiterC-Api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:48.5768622Z [4269/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_RefCountedC-Api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:53.6171970Z [4270/8229] Building CXX object intern\memutil\CMakeFiles\bf_intern_memutil.dir\intern\MEM_alloc_string_storage.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:55.5990467Z [4271/8229] Linking CXX static library lib\bf_intern_memutil.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:55.7753019Z [4272/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\opensubdiv_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:43:58.4021876Z [4273/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\type_convert.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:03.0479107Z [4274/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\base\util.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:08.5393330Z [4275/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:09.1972974Z [4276/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output_cpu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:13.5168292Z [4277/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\tracking\track_region.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:13.5908544Z [4278/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\eval_output_gpu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:14.7928121Z [4279/8229] Building CXX object intern\libmv\CMakeFiles\bf_intern_libmv.dir\libmv\simple_pipeline\resect.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:14.8299570Z [4280/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:14.9726331Z [4281/8229] Linking CXX static library lib\bf_intern_libmv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:16.3520872Z [4282/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_cache_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:17.8514655Z [4283/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\evaluator_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:18.7041616Z [4284/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\gpu_compute_evaluator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:19.3750629Z [4285/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\gpu_patch_table.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:19.7842661Z [4286/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\evaluator\patch_map.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:19.8021279Z [4287/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\mesh_topology.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:20.7268646Z [4288/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\mesh_topology_compare.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:20.9081764Z [4289/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:21.2492555Z [4290/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_factory.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:22.0707049Z [4291/8229] Building CXX object intern\opensubdiv\CMakeFiles\bf_intern_opensubdiv.dir\internal\topology\topology_refiner_impl_compare.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:22.1244079Z [4292/8229] Linking CXX static library lib\bf_intern_opensubdiv.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:22.3958629Z [4293/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_hosek.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:22.7483432Z [4294/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_single_scattering.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:22.9047853Z [4295/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\manifold_table.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:23.1904669Z [4296/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\marching_cubes_table.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:23.2215703Z [4297/8229] Building CXX object intern\sky\CMakeFiles\bf_intern_sky.dir\source\sky_multiple_scattering.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:23.2727263Z [4298/8229] Linking CXX static library lib\bf_intern_sky.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:24.2085351Z [4299/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\Projections.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:25.2396647Z [4300/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\dualcon_c_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:32.7578719Z [4301/8229] Building CXX object intern\dualcon\CMakeFiles\bf_intern_dualcon.dir\intern\octree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:32.8076983Z [4302/8229] Linking CXX static library lib\bf_intern_dualcon.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:42.1254767Z [4303/8229] Building CXX object intern\openvdb\CMakeFiles\bf_intern_openvdb.dir\openvdb_capi.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:42.8743755Z [4304/8229] Linking CXX static library lib\bf_intern_openvdb.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:44.2652422Z [4305/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QJacobianSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:46.1786752Z [4306/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QJacobian.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:49.7148210Z [4307/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QTask.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:50.8328555Z [4308/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_Solver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:52.7683367Z [4309/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:54.8897295Z [4310/8229] Building CXX object intern\iksolver\CMakeFiles\bf_intern_iksolver.dir\intern\IK_QSegment.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:54.9645385Z [4311/8229] Linking CXX static library lib\bf_intern_iksolver.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:54.9933514Z [4312/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Armature.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:59.1112564Z [4313/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\ControlledObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:59.7076237Z [4314/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\ConstraintSet.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:44:59.7749676Z [4315/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\CopyPose.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:02.3969607Z [4316/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Distance.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:02.5520868Z [4317/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\FixedObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:02.6481859Z [4318/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\MovingFrame.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:05.3398300Z [4319/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\UncontrolledObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:09.3341052Z [4320/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WDLSSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:14.6503753Z [4321/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WorldObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:14.7663179Z [4322/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\WSDLSSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:16.9283172Z [4323/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\eigen_types.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:17.3029130Z [4324/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chain.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:17.6451496Z [4325/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\Scene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:17.9865942Z [4326/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frameacc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:18.3211799Z [4327/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frames.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:19.6859639Z [4328/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chainfksolverpos_recursive.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:19.7445335Z [4329/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\frames_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:19.9646679Z [4330/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\chainjnttojacsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:20.0557535Z [4331/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\framevel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:20.3803939Z [4332/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jacobian.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:20.3956519Z [4333/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:20.7323026Z [4334/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarrayacc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:20.7856537Z [4335/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\jntarrayvel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:21.7151884Z [4336/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\joint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:22.7617083Z [4337/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\inertia.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:23.6661697Z [4338/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\kinfam_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:24.6911494Z [4339/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\segment.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:25.8672716Z [4340/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\tree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:26.4472526Z [4341/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\treefksolverpos_recursive.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:26.6929533Z [4342/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\utility.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:27.4626293Z [4343/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\error_stack.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:27.5560173Z [4344/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\treejnttojacsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:28.0675925Z [4345/8229] Building CXX object intern\itasc\CMakeFiles\bf_intern_itasc.dir\kdl\utilities\utility_io.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:28.1203254Z [4346/8229] Linking CXX static library lib\bf_intern_itasc.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:32.5094452Z [4347/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\display_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:34.3441193Z [4348/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:35.0191280Z [4349/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\implicit_sharing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:36.0561636Z [4350/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\camera.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:42.6520089Z [4351/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\light.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:44.1728308Z [4352/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\light_linking.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:53.1073639Z [4353/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\image.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:55.6684355Z [4354/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:45:56.6591663Z [4355/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\geometry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:00.2520838Z [4356/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\output_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:02.4734394Z [4357/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\object_cull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:03.6210871Z [4358/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\object.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:07.0769628Z [4359/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\particles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:09.3149312Z [4360/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\logging.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:13.9933813Z [4361/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\pointcloud.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:16.5270293Z [4362/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\curves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:19.0275981Z [4363/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\python.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:22.4537506Z [4364/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\session.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:25.9103404Z [4365/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\texture_cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:28.1322194Z [4366/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\sync.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:32.5681651Z [4367/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\viewport.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:45.8412085Z [4368/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\shader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:48.4732645Z [4369/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\bvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:50.8365456Z [4370/8229] Building CXX object intern\cycles\blender\CMakeFiles\bf_intern_cycles.dir\volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:50.9370666Z [4371/8229] Linking CXX static library lib\bf_intern_cycles.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:52.5459778Z [4372/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\binning.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:52.8757389Z [4373/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\octree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:54.1899647Z [4374/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\bvh2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:54.3014787Z [4375/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\hiprt.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:55.2403729Z [4376/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\multi.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:58.0871924Z [4377/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\embree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:58.2930805Z [4378/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\optix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:58.7231413Z [4379/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\build.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:46:58.8924881Z [4380/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\node.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:01.5442926Z [4381/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\sort.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:03.1958893Z [4382/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\unaligned.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:04.1020213Z [4383/8229] Building CXX object intern\cycles\bvh\CMakeFiles\cycles_bvh.dir\split.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:04.1531803Z [4384/8229] Linking CXX static library lib\cycles_bvh.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:04.4755582Z [4385/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:05.8761855Z [4386/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:06.7968348Z [4387/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\denoise.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:07.3878368Z [4388/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:09.2262704Z [4389/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\memory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:09.6369125Z [4390/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:10.6241351Z [4391/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:11.9207305Z [4392/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:12.0252065Z [4393/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:12.1262869Z [4394/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:12.2284666Z [4395/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:12.3290708Z [4396/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:12.4204163Z [4397/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\util.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:14.3603882Z [4398/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cpu\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:14.3750420Z [4399/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\cuda\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:16.4681888Z [4400/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:17.9578594Z [4401/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\graphics_interop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:18.8286091Z [4402/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:20.1409096Z [4403/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:20.2387576Z [4404/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hiprt\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:20.3403389Z [4405/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hiprt\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:21.6404190Z [4406/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:22.3671734Z [4407/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\hip\util.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:23.7417889Z [4408/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\dummy\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:23.8546615Z [4409/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\device_impl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:23.9569224Z [4410/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\queue.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:26.3600457Z [4411/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\multi\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:26.6778251Z [4412/8229] Building CXX object intern\cycles\device\CMakeFiles\cycles_device.dir\optix\device.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:26.7343008Z [4413/8229] Linking CXX static library lib\cycles_device.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:27.8563769Z [4414/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:28.2920463Z [4415/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\adaptive_sampling.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:29.9117121Z [4416/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node_type.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:30.7018494Z [4417/8229] Building CXX object intern\cycles\graph\CMakeFiles\cycles_graph.dir\node_xml.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:30.7494523Z [4418/8229] Linking CXX static library lib\cycles_graph.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:32.0402009Z [4419/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:33.6973356Z [4420/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:34.5379278Z [4421/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:34.6515217Z [4422/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_optix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:35.6071755Z [4423/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn_base.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:37.1924241Z [4424/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\denoiser_oidn_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:38.0995284Z [4425/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:41.4329085Z [4426/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:41.4649436Z [4427/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:42.5599639Z [4428/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor_cpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:44.8490834Z [4429/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\pass_accessor_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:44.9445359Z [4430/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_display.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:45.8965191Z [4431/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:49.2757519Z [4432/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:50.6325805Z [4433/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work_cpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:52.3221504Z [4434/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\path_trace_work_gpu.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:53.1254262Z [4435/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\work_balancer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:54.7494622Z [4436/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\render_scheduler.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:55.7181869Z [4437/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\shader_eval.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:56.6381504Z [4438/8229] Building CXX object intern\cycles\integrator\CMakeFiles\cycles_integrator.dir\work_tile_scheduler.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:56.7311637Z [4439/8229] Linking CXX static library lib\cycles_integrator.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:47:59.2246881Z [4440/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\globals.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:48:01.2934248Z [4441/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\closures.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:48:05.0067749Z [4442/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\globals.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:48:46.0517854Z [4443/8229] Building CXX object intern\cycles\kernel\osl\CMakeFiles\cycles_kernel_osl.dir\services.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:48:48.1605298Z [4444/8229] Linking CXX static library lib\cycles_kernel_osl.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:48:57.7179450Z [4445/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\attribute.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:49:11.6058653Z [4446/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\background.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:49:22.9030351Z [4447/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\bake.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:49:49.5714510Z [4448/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\camera.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:49:53.1131382Z [4449/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\constant_fold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:49:56.3748229Z [4450/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\devicescene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:01.6150985Z [4451/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\film.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:06.8203824Z [4452/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\kernel_avx2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:10.0922317Z [4453/8229] Building CXX object intern\cycles\kernel\device\cpu\CMakeFiles\cycles_kernel_cpu.dir\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:10.1590057Z [4454/8229] Linking CXX static library lib\cycles_kernel_cpu.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:12.7184924Z [4455/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_attributes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:15.7464170Z [4456/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_bvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:18.4229692Z [4457/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry_mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:20.4352992Z [4458/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\hair.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:23.3744130Z [4459/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\geometry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:26.0429525Z [4460/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_cache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:26.3546761Z [4461/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_loader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:29.8428873Z [4462/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_sky.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:29.8942931Z [4463/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_oiio.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:40.4024302Z [4464/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:44.5712777Z [4465/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\scene_attributes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:47.9845801Z [4466/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\integrator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:52.7776022Z [4467/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:50:56.7883684Z [4468/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light_tree.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:01.3300060Z [4469/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\light_tree_debug.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:07.9809764Z [4470/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:10.0999182Z [4471/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh_displace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:12.6857401Z [4472/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\image_vdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:14.3135581Z [4473/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\mesh_subdivision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:15.3764558Z [4474/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\procedural.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:17.2604733Z [4475/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\pointcloud.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:22.0465775Z [4476/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\particles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:23.3780815Z [4477/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\osl.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:24.0620419Z [4478/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\curves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:26.0713510Z [4479/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\pass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:34.4964133Z [4480/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\object.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:41.1971606Z [4481/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader_graph.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:48.0780146Z [4482/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\scene.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:48.4872306Z [4483/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:53.0047059Z [4484/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\shader_nodes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:55.6129560Z [4485/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\stats.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:56.0491615Z [4486/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\tabulated_sobol.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:57.7108573Z [4487/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\svm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:51:58.4557053Z [4488/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\tables.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:00.8031824Z [4489/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\cache_eviction.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:01.2712889Z [4490/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\buffers.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:02.1662204Z [4491/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\display_driver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:06.4046990Z [4492/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\denoising.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:07.1477134Z [4493/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\merge.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:12.2365448Z [4494/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\tile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:12.2516574Z [4495/8229] Building CXX object intern\cycles\session\CMakeFiles\cycles_session.dir\session.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:12.3113473Z [4496/8229] Linking CXX static library lib\cycles_session.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:17.8657434Z [4497/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\dice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:19.0944507Z [4498/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\interpolation.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:19.9506746Z [4499/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\patch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:23.8635713Z [4500/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\osd.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:24.3409277Z [4501/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\aligned_malloc.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:25.3133982Z [4502/8229] Building CXX object intern\cycles\subd\CMakeFiles\cycles_subd.dir\split.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:25.3643350Z [4503/8229] Linking CXX static library lib\cycles_subd.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:29.5493044Z [4504/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\debug.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:31.3120242Z [4505/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\colorspace.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:31.5840461Z [4506/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\guarded_allocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:36.1811485Z [4507/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\ies.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:39.1489258Z [4508/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\image_maketx.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:39.8713254Z [4509/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\implicit_sharing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:42.8331804Z [4510/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\image_metadata.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:44.4627409Z [4511/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\log.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:44.5762422Z [4512/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\math_cdf.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:45.6288851Z [4513/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\murmurhash.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:52:48.9115102Z [4514/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\md5.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:15.0227025Z [4515/8229] Building CXX object intern\cycles\scene\CMakeFiles\cycles_scene.dir\volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:15.9491066Z [4516/8229] Linking CXX static library lib\cycles_scene.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:22.2723252Z [4517/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\path.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:27.3237802Z [4518/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\profiling.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:30.0993896Z [4519/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\openvdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:33.1945837Z [4520/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\string.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:34.7759866Z [4521/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\system.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:36.9314805Z [4522/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\thread.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:38.6652088Z [4523/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\task.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:40.5569721Z [4524/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\transform.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:41.4644267Z [4525/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\time.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:42.1451464Z [4526/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\transform_avx2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:42.5913696Z [4527/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\windows.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:43.4174238Z [4528/8229] Building CXX object intern\rigidbody\CMakeFiles\bf_intern_rigidbody.dir\rb_convex_hull_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:45.8922962Z [4529/8229] Building CXX object intern\rigidbody\CMakeFiles\bf_intern_rigidbody.dir\rb_bullet_api.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:46.7669722Z [4530/8229] Linking CXX static library lib\bf_intern_rigidbody.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:47.1533463Z [4531/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\manta_python_API.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:48.2204497Z [4532/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\manta_fluid_API.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:53:58.4674994Z [4533/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\area_compensation.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:00.3612663Z [4534/8229] Building CXX object intern\mantaflow\CMakeFiles\bf_intern_mantaflow.dir\intern\MANTA_main.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:01.2960155Z [4535/8229] Linking CXX static library lib\bf_intern_mantaflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:04.5728380Z [4536/8229] Building CXX object intern\cycles\util\CMakeFiles\cycles_util.dir\nanovdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:04.9327825Z [4537/8229] Linking CXX static library lib\cycles_util.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:06.6814307Z [4538/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\geometry_data_retrieval.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:10.4183573Z [4539/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim_matrix_transfer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:15.2556640Z [4540/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim_parametrizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:23.7124683Z [4541/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\slim.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:36.2612085Z [4542/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\least_squares_relocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:36.6467007Z [4543/8229] Building CXX object intern\quadriflow\CMakeFiles\bf_intern_quadriflow.dir\quadriflow_capi.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:37.5055435Z [4544/8229] Linking CXX static library lib\bf_intern_quadriflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:38.0511921Z [4545/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_cubic.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:38.9418694Z [4546/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_cubic_refit.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:39.0871953Z [4547/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\curve_fit_corners_detect.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:39.6000335Z [4548/8229] Building C object extern\curve_fit_nd\CMakeFiles\extern_curve_fit_nd.dir\intern\generic_heap.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:40.6789917Z [4549/8229] Linking C static library lib\extern_curve_fit_nd.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:41.2884271Z [4550/8229] Building C object extern\rangetree\CMakeFiles\extern_rangetree.dir\intern\range_tree.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:43.1338881Z [4551/8229] Linking C static library lib\extern_rangetree.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:43.7090066Z [4552/8229] Building C object extern\nanosvg\CMakeFiles\extern_nanosvg.dir\blender_nanosvg.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.1726756Z [4553/8229] Building C object extern\nanosvg\CMakeFiles\extern_nanosvg.dir\blender_raster.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.1782565Z [4554/8229] Building C object extern\ufbx\CMakeFiles\extern_ufbx.dir\ufbx.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.2290709Z [4555/8229] Linking C static library lib\extern_nanosvg.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.2717317Z [4556/8229] Linking C static library lib\extern_ufbx.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.3716978Z [4557/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btBroadphaseProxy.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.5899827Z [4558/8229] Building CXX object intern\slim\CMakeFiles\bf_intern_slim.dir\intern\uv_initializer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.7949350Z [4559/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.8207184Z [4560/8229] Linking CXX static library lib\bf_intern_slim.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:44.8349595Z [4561/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btAxisSweep3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:45.0196390Z [4562/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDispatcher.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:45.4486883Z [4563/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDbvt.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:45.5077353Z [4564/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btDbvtBroadphase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:45.7676288Z [4565/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btOverlappingPairCache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:46.1015218Z [4566/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btSimpleBroadphase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:46.1847410Z [4567/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\SphereTriangleDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:46.6119431Z [4568/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btActivatingCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:46.9004688Z [4569/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBox2dBox2dCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:46.9523415Z [4570/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\BroadphaseCollision\btQuantizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:47.2438808Z [4571/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBoxBoxCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:47.4447957Z [4572/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionDispatcher.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:47.5963404Z [4573/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btBoxBoxDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:48.2718451Z [4574/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:49.5767259Z [4575/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:49.7358691Z [4576/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCompoundCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:50.0366469Z [4577/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCollisionWorldImporter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:50.3251536Z [4578/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvex2dConvex2dAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:50.7498236Z [4579/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btCompoundCompoundCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:50.8334218Z [4580/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexConcaveCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:51.4180756Z [4581/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btDefaultCollisionConfiguration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:51.5482056Z [4582/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexPlaneCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:51.7694584Z [4583/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btConvexConvexAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:51.8133790Z [4584/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btEmptyCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:52.1092849Z [4585/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btGhostObject.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:52.2843967Z [4586/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btHashedSimplePairCache.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:52.5970398Z [4587/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btManifoldResult.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:52.8301349Z [4588/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSimulationIslandManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.2316865Z [4589/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereBoxCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.4193493Z [4590/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereSphereCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.4729367Z [4591/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btInternalEdgeUtility.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.7065204Z [4592/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btSphereTriangleCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.7662158Z [4593/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionDispatch\btUnionFind.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:53.8078936Z [4594/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBox2dShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:54.0797510Z [4595/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBoxShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:54.1544998Z [4596/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCapsuleShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:54.8345002Z [4597/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btBvhTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.0633067Z [4598/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCollisionShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.2071838Z [4599/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConcaveShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.2617543Z [4600/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCompoundShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.4767149Z [4601/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConeShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.5285132Z [4602/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvex2dShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.8429226Z [4603/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexInternalShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:55.9512137Z [4604/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexPointCloudShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:56.4153820Z [4605/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexHullShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:56.5183080Z [4606/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:56.7906966Z [4607/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:56.9942170Z [4608/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btCylinderShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:57.1325162Z [4609/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btConvexPolyhedron.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:57.1913049Z [4610/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btEmptyShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:57.5482294Z [4611/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btHeightfieldTerrainShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:57.6350844Z [4612/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMinkowskiSumShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:57.9878748Z [4613/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMiniSDF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:58.5002247Z [4614/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btOptimizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:58.6844209Z [4615/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMultiSphereShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:58.7276973Z [4616/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btMultimaterialTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:59.2672102Z [4617/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btSdfCollisionShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:59.3053975Z [4618/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btPolyhedralConvexShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:59.6112404Z [4619/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btSphereShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:54:59.7711074Z [4620/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btScaledBvhTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.0003603Z [4621/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btStaticPlaneShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.3005105Z [4622/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTetrahedronShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.5109596Z [4623/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btShapeHull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.6074634Z [4624/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.7297395Z [4625/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleCallback.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:00.7568438Z [4626/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btStridingMeshInterface.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:01.0603438Z [4627/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleIndexVertexArray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:01.2104975Z [4628/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleIndexVertexMaterialArray.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:01.2598536Z [4629/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleMesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:01.4808009Z [4630/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btTriangleMeshShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:01.5636720Z [4631/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\CollisionShapes\btUniformScalingShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:02.0579594Z [4632/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btContactProcessing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:02.2947521Z [4633/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:02.5708732Z [4634/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.0656178Z [4635/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactQuantizedBvh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.1416378Z [4636/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGImpactShape.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.1699621Z [4637/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btGenericPoolAllocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.5841435Z [4638/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_box_set.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.6229511Z [4639/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_contact.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.7332165Z [4640/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\btTriangleShapeEx.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:03.8041834Z [4641/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_memory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:04.1547008Z [4642/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:04.2840792Z [4643/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btContinuousConvexCollision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:04.5123715Z [4644/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:04.8936091Z [4645/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkEpaPenetrationDepthSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:04.9363594Z [4646/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkEpa2.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:05.4063881Z [4647/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btMinkowskiPenetrationDepthSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:05.5715066Z [4648/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btGjkPairDetector.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:05.5836351Z [4649/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\Gimpact\gim_tri_collision.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:06.0009160Z [4650/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btRaycastCallback.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:06.2272465Z [4651/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btPolyhedralContactClipping.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:06.4566093Z [4652/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btSubSimplexConvexCast.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:06.4837286Z [4653/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btPersistentManifold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:06.6844662Z [4654/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletCollision\NarrowPhaseCollision\btVoronoiSimplexSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:07.3670920Z [4655/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Character\btKinematicCharacterController.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:07.4022058Z [4656/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btContactConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:07.8496153Z [4657/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGearConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:07.8866622Z [4658/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btFixedConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:08.6160704Z [4659/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btConeTwistConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:08.7362026Z [4660/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:08.7618524Z [4661/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofSpring2Constraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:09.3536966Z [4662/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btGeneric6DofSpringConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:09.4567987Z [4663/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btHinge2Constraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:09.6562926Z [4664/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btHingeConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:09.9871045Z [4665/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btPoint2PointConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:10.2987280Z [4666/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btNNCGConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:10.6944763Z [4667/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSequentialImpulseConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:10.9102347Z [4668/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSliderConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:10.9137717Z [4669/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btSolve2LinearConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:11.4933131Z [4670/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btUniversalConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:11.7475450Z [4671/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\ConstraintSolver\btTypedConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:12.5146794Z [4672/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btSimpleDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:12.9458185Z [4673/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btRigidBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:13.0116563Z [4674/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Dynamics\btDiscreteDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:13.9721084Z [4675/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:15.2961995Z [4676/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyConstraintSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:16.4868224Z [4677/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyJointLimitConstraint.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:16.5845014Z [4678/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:17.4427636Z [4679/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyJointMotor.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:17.6054042Z [4680/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBodyPoint2Point.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:18.5601283Z [4681/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Featherstone\btMultiBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:18.6362143Z [4682/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btDantzigLCP.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:18.7589912Z [4683/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btLemkeAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:19.4476293Z [4684/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Vehicle\btWheelInfo.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:19.7053090Z [4685/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\Vehicle\btRaycastVehicle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:19.7081700Z [4686/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletDynamics\MLCPSolvers\btMLCPSolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:20.6354522Z [4687/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btDefaultSoftBodySolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:21.0406775Z [4688/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyConcaveCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:22.5474364Z [4689/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyRigidBodyCollisionConfiguration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:25.4285796Z [4690/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftRigidCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:26.0448213Z [4691/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBodyHelpers.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:27.6806426Z [4692/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftSoftCollisionAlgorithm.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:27.7137351Z [4693/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftRigidDynamicsWorld.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:27.8739978Z [4694/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btAlignedAllocator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:28.6916502Z [4695/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btConvexHull.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:29.0635947Z [4696/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btGeometryUtil.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:29.4945428Z [4697/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btConvexHullComputer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:29.5195876Z [4698/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btPolarDecomposition.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:29.6753817Z [4699/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btSerializer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:29.8287330Z [4700/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btSerializer64.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:30.0011344Z [4701/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btVector3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:30.1363429Z [4702/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\LinearMath\btQuickprof.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:30.6680492Z [4703/8229] Building C object extern\hipew\CMakeFiles\extern_hipew.dir\src\hipew.c.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:30.7183921Z [4704/8229] Linking C static library lib\extern_hipew.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:33.6573044Z [4705/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags_completions.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:33.7284148Z [4706/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:34.3724144Z [4707/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\windows_port.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:35.7912289Z [4708/8229] Building CXX object extern\gflags\CMakeFiles\extern_gflags.dir\src\gflags_reporting.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:35.8414101Z [4709/8229] Linking CXX static library lib\extern_gflags.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:36.0928368Z [4710/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\demangle.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:37.8802595Z [4711/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\raw_logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:38.5692028Z [4712/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\logging.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:39.8102038Z [4713/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\signalhandler.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:40.4111943Z [4714/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\symbolize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:41.6014072Z [4715/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\utilities.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:42.2821432Z [4716/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\vlog_is_on.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:42.3769560Z [4717/8229] Building CXX object extern\glog\CMakeFiles\extern_glog.dir\src\windows\port.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:42.6192255Z [4718/8229] Linking CXX static library lib\extern_glog.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:43.7174780Z [4719/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\MixingThreadDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:44.6045325Z [4720/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\DeviceManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:44.6825842Z [4721/8229] Building CXX object extern\bullet2\CMakeFiles\extern_bullet.dir\src\BulletSoftBody\btSoftBody.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:44.7945682Z [4722/8229] Linking CXX static library lib\extern_bullet.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:45.3868293Z [4723/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\NULLDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:45.7219122Z [4724/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\ReadDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:46.6049829Z [4725/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\SoftwareDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:46.6586491Z [4726/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\devices\ThreadedDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:47.1704613Z [4727/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\Exception.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:47.8169182Z [4728/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\FileManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:47.8528889Z [4729/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\File.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:48.2531358Z [4730/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\file\FileWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:48.6295031Z [4731/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ADSR.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:48.6409602Z [4732/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Accumulator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:49.0538601Z [4733/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ADSRReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:49.4875709Z [4734/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BaseIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:49.4963627Z [4735/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ButterworthCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:49.8997290Z [4736/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Butterworth.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:50.2575105Z [4737/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\CallbackIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:50.3073172Z [4738/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Delay.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:50.6858267Z [4739/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DelayReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:51.1268912Z [4740/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicIIRFilter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:51.1555166Z [4741/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicIIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.0286071Z [4742/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Effect.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.0296938Z [4743/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\EffectReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.0844068Z [4744/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\DynamicMusic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.7905612Z [4745/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Fader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.8287735Z [4746/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\FaderReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:52.8431041Z [4747/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Envelope.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:53.6440893Z [4748/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\HighpassCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:53.6686286Z [4749/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\IIRFilter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:53.6944270Z [4750/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Highpass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:54.4130850Z [4751/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Limiter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:54.5218401Z [4752/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\IIRFilterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:54.6617120Z [4753/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LimiterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:55.1890371Z [4754/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Loop.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:55.3103801Z [4755/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LoopReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:55.5127131Z [4756/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\LowpassCalculator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:56.0417666Z [4757/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Lowpass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:56.1173884Z [4758/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Modulator.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:56.7142025Z [4759/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ModulatorReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:56.8273163Z [4760/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\MutableReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:57.1402759Z [4761/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\MutableSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:57.5318956Z [4762/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Pitch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:57.5958580Z [4763/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PitchReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:58.4090695Z [4764/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Reverse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:58.4625954Z [4765/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PlaybackManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:58.7638305Z [4766/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\PlaybackCategory.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:59.0964151Z [4767/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Source.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:59.5044588Z [4768/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ReverseReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:55:59.9870379Z [4769/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Sum.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:00.2681892Z [4770/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Threshold.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:00.9805345Z [4771/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Volume.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:01.0066024Z [4772/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\SoundList.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:01.0983830Z [4773/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:01.3651808Z [4774/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeStorage.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:01.9185883Z [4775/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Echo.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:01.9843039Z [4776/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\VolumeSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:02.1077286Z [4777/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\EchoReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:02.2910799Z [4778/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SawtoothReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:02.4710368Z [4779/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SilenceReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:02.7728723Z [4780/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Sawtooth.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:02.9082893Z [4781/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Silence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:03.0797202Z [4782/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SineReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:03.2460933Z [4783/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Sine.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:03.3831082Z [4784/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\SquareReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:03.6784916Z [4785/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\TriangleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:03.7240674Z [4786/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Square.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:04.0522876Z [4787/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\generator\Triangle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:04.5077051Z [4788/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ChannelMapper.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:04.7853523Z [4789/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ChannelMapperReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:04.7883141Z [4790/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ConverterFunctions.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:04.8190119Z [4791/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\Converter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:05.5474387Z [4792/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ConverterReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:05.6207481Z [4793/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResample.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:06.2543832Z [4794/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffHigh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:06.2831902Z [4795/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffLow.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:06.4159898Z [4796/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReaderCoeffMedium.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:07.0327535Z [4797/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\LinearResample.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:07.2888641Z [4798/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\LinearResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:07.3763202Z [4799/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\JOSResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:08.0282183Z [4800/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\Mixer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:08.0712382Z [4801/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\ResampleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:08.0833526Z [4802/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\respec\SpecsChanger.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:08.8204195Z [4803/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Double.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:08.8628506Z [4804/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\DoubleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:09.1720820Z [4805/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\AnimateableProperty.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:09.6856909Z [4806/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\PingPong.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:10.0646929Z [4807/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Sequence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:10.3504101Z [4808/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceData.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:10.9334905Z [4809/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceEntry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:11.3078174Z [4810/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceHandle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:11.7966268Z [4811/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\Superpose.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:11.9453927Z [4812/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SequenceReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:12.5631754Z [4813/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\sequence\SuperposeReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:12.7628512Z [4814/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\Buffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:12.7787144Z [4815/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\Barrier.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:13.4182258Z [4816/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\BufferReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:13.5399184Z [4817/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\RingBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:13.7714053Z [4818/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\StreamBuffer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:14.6148392Z [4819/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEG.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:15.0839039Z [4820/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEGReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:15.3352469Z [4821/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\ThreadPool.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:15.9591939Z [4822/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\ffmpeg\FFMPEGWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:17.1398727Z [4823/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BinauralSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:17.9563383Z [4824/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\BinauralReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:18.8078396Z [4825/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Convolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:19.9149338Z [4826/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ConvolverReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:20.4016793Z [4827/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ConvolverSound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:21.2965607Z [4828/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\FFTConvolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:22.0922088Z [4829/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\Equalizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:22.3146829Z [4830/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\HRTF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:23.2263087Z [4831/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\ImpulseResponse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:23.3264435Z [4832/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFile.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:23.5921883Z [4833/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\util\FFTPlan.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:24.2297536Z [4834/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFileWriter.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:24.3712596Z [4835/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\libsndfile\SndFileReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:25.4685179Z [4836/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\TimeStretchPitchScale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:25.5710080Z [4837/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\openal\OpenALReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:26.5689878Z [4838/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\openal\OpenALDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:26.8194993Z [4839/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\TimeStretchPitchScaleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:27.0274321Z [4840/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\AnimateableTimeStretchPitchScale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:27.8598923Z [4841/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\src\fx\AnimateableTimeStretchPitchScaleReader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:28.8549776Z [4842/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\PluginManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:29.1839951Z [4843/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\plugins\wasapi\WASAPIDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:30.1409240Z [4844/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace.dir\HRTFLoader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:30.2503927Z [4845/8229] Linking CXX static library lib\audaspace.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:30.2583662Z [4846/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyAnimateableProperty.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:30.7218266Z [4847/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyAPI.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:31.5392060Z [4848/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyDynamicMusic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:31.5527176Z [4849/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyDevice.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:32.0070036Z [4850/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyHandle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:32.9215851Z [4851/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyPlaybackManager.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:33.0304133Z [4852/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySequence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:33.5540498Z [4853/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySequenceEntry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:34.1571023Z [4854/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySource.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:35.2781248Z [4855/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyThreadPool.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:35.9871440Z [4856/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PySound.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:36.1228455Z [4857/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyHRTF.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:37.2675883Z [4858/8229] Building CXX object extern\audaspace\CMakeFiles\audaspace-py.dir\bindings\python\PyImpulseResponse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:37.3228286Z [4859/8229] Linking CXX static library lib\audaspace-py.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:40.3876979Z [4860/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\adjacent-matrix.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:42.4585347Z [4861/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\dedge.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:44.2308408Z [4862/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\loader.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:48.2988438Z [4863/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\merge-vertex.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:51.1910813Z [4864/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\hierarchy.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:56:53.3677096Z [4865/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\localsat.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:02.3117453Z [4866/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:05.4697494Z [4867/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-flip.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:11.8677778Z [4868/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\optimizer.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:14.3395358Z [4869/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-int.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:16.8910398Z [4870/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:24.3666414Z [4871/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-sing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:24.8802191Z [4872/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\parametrizer-scale.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:27.4613033Z [4873/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:27.5662316Z [4874/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\arg_parser.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:28.7907298Z [4875/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\src\subdivide.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:29.0983984Z [4876/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\lp_base.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:29.1695300Z [4877/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:30.4683563Z [4878/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\lp_skeleton.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:30.5014541Z [4879/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\random.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:30.9732509Z [4880/8229] Building CXX object extern\quadriflow\CMakeFiles\extern_quadriflow.dir\3rd\lemon-1.3.1\lemon\bits\windows.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:31.0457183Z [4881/8229] Linking CXX static library lib\extern_quadriflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:32.7092014Z [4882/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\commonkernels.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:33.1754281Z [4883/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\conjugategrad.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:34.7767866Z [4884/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\conjugategrad.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:36.4161395Z [4885/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\edgecollapse.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:36.6865746Z [4886/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\edgecollapse.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:39.0679258Z [4887/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fastmarch.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:39.1169429Z [4888/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fastmarch.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:41.3320791Z [4889/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iogrids.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:42.5100913Z [4890/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iomeshes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:42.6690912Z [4891/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\ioparticles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:44.8839268Z [4892/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\mantaio.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:46.4380412Z [4893/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\mantaio.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:49.1389407Z [4894/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fluidsolver.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:51.2233547Z [4895/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fluidsolver.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:53.1181860Z [4896/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\general.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:54.3946783Z [4897/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\general.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:57:59.6762641Z [4898/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\ioutil.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:07.7186941Z [4899/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:09.6670890Z [4900/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:22.0879482Z [4901/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid4d.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:23.5479766Z [4902/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\grid4d.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:26.9187655Z [4903/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\kernel.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:27.2398980Z [4904/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\kernel.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:32.9094497Z [4905/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\levelset.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:33.3711145Z [4906/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\levelset.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:47.4977206Z [4907/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\mesh.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:53.4999359Z [4908/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\mesh.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:55.3682586Z [4909/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\movingobs.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:58:59.0437682Z [4910/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\movingobs.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:03.4581434Z [4911/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\multigrid.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:04.3944410Z [4912/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\multigrid.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:07.9654892Z [4913/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\noisefield.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:09.3340785Z [4914/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\noisefield.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:11.3180812Z [4915/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\fileio\iovdb.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:20.0023604Z [4916/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\advection.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:22.3784107Z [4917/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\particle.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:22.7589794Z [4918/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\particle.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:24.2595077Z [4919/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\apic.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:26.1114549Z [4920/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\fire.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:27.7365090Z [4921/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\extforces.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:32.2465926Z [4922/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\flip.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:32.3616913Z [4923/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\fluidguiding.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:35.9801960Z [4924/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\initplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:37.9283082Z [4925/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\kepsilon.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:37.9804082Z [4926/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\meshplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:41.8984292Z [4927/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\pressure.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:42.0827471Z [4928/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\ptsplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:44.5084573Z [4929/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\secondaryparticles.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:48.3126197Z [4930/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\surfaceturbulence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:48.7256334Z [4931/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\viscosity.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:50.4605544Z [4932/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\vortexplugins.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:51.3634856Z [4933/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\python\defines.py.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:51.9316444Z [4934/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\registration.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:53.8585415Z [4935/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\waves.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:53.9982429Z [4936/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\plugin\waveletturbulence.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:57.5870402Z [4937/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\test.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:57.6574550Z [4938/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\shapes.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:58.0275324Z [4939/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\shapes.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:59.7966717Z [4940/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\timing.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T12:59:59.9538044Z [4941/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\timing.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:01.2765128Z [4942/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\turbulencepart.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:03.9026823Z [4943/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexpart.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:04.2649812Z [4944/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\turbulencepart.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:06.1000704Z [4945/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexpart.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:07.1366028Z [4946/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexsheet.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:07.6835804Z [4947/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\preprocessed\vortexsheet.h.reg.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:08.5454958Z [4948/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pclass.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:10.0907586Z [4949/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pconvert.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:10.1308705Z [4950/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\pvec3.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:12.0493551Z [4951/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\vector4d.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:12.2254732Z [4952/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\pwrapper\registry.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:12.9199415Z [4953/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\simpleimage.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:13.6129422Z [4954/8229] Building CXX object extern\mantaflow\CMakeFiles\extern_mantaflow.dir\helper\util\vectorbase.cpp.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:14.5881093Z [4955/8229] Linking CXX static library lib\extern_mantaflow.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:15.7555448Z [4956/8229] Building CXX object extern\vulkan_memory_allocator\CMakeFiles\extern_vulkan_memory_allocator.dir\vk_mem_alloc_impl.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:15.7977235Z [4957/8229] Linking CXX static library lib\extern_vulkan_memory_allocator.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:19.0045649Z [4958/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_asset_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:20.5234564Z [4959/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_channels_defines.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:22.8004349Z [4960/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_channels_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:24.0870554Z [4961/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_deps.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:25.6580285Z [4962/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:28.6131016Z [4963/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_ipo_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:29.5636762Z [4964/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:30.9835054Z [4965/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_markers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:33.8527077Z [4966/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\drivers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:33.9679093Z [4967/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_motion_paths.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:35.1957666Z [4968/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\anim_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:38.3567353Z [4969/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\fmodifier_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:39.0076513Z [4970/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:39.5983656Z [4971/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:43.3123116Z [4972/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_keylist.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:44.4346645Z [4973/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframes_general.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:46.2566266Z [4974/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyframing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:48.2377315Z [4975/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\time_scrub_ui.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:48.3065655Z [4976/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\keyingsets.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:49.2080438Z [4977/8229] Building CXX object source\blender\editors\animation\CMakeFiles\bf_editor_animation.dir\transformable.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:49.2739582Z [4978/8229] Linking CXX static library lib\bf_editor_animation.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:53.5671861Z [4979/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:53.7898389Z [4980/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:54.0191634Z [4981/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_naming.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:57.6857592Z [4982/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:59.2883858Z [4983/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_relations.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:00:59.4178973Z [4984/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:01.7915022Z [4985/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_skinning.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:02.3170265Z [4986/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\armature_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:02.6474433Z [4987/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\bone_collections.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:05.0599512Z [4988/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\editarmature_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:06.4445314Z [4989/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\meshlaplacian.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:08.0870892Z [4990/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:10.5994411Z [4991/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_lib_2.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:12.6970197Z [4992/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:14.0283182Z [4993/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_slide.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:16.3551018Z [4994/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_transform.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:16.8317712Z [4995/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_catalog.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:18.1119123Z [4996/8229] Building CXX object source\blender\editors\armature\CMakeFiles\bf_editor_armature.dir\pose_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:18.1771945Z [4997/8229] Linking CXX static library lib\bf_editor_armature.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:19.2831045Z [4998/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_filter.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:21.3447543Z [4999/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_import.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:22.3581843Z [5000/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:22.5164322Z [5001/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_file_status.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:24.2317247Z [5002/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_library_reference_enum.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:26.2484650Z [5003/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_listing.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:27.3239943Z [5004/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_indexer_remote_listing_v1.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:27.6416194Z [5005/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_library_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:29.8624423Z [5006/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_mark_clear.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:30.4361618Z [5007/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_menu_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:31.8844650Z [5008/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_list.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:35.4982560Z [5009/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:35.5373848Z [5010/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:37.0677937Z [5011/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_asset_view.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:38.6568031Z [5012/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_regiondata.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:40.4289123Z [5013/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_popover.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:40.4588738Z [5014/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_catalog_selector.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:42.0531125Z [5015/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_type.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:42.5063070Z [5016/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_temp_id_consumer.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:43.0576910Z [5017/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_shelf_settings.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:45.1781060Z [5018/8229] Building CXX object source\blender\editors\asset\CMakeFiles\bf_editor_asset.dir\intern\asset_ui_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:45.2479590Z [5019/8229] Linking CXX static library lib\bf_editor_asset.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:46.5788918Z [5020/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\curve_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:50.0885717Z [5021/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:50.1365965Z [5022/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:52.1439514Z [5023/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:52.4084107Z [5024/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_query.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:54.7374789Z [5025/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:55.3569435Z [5026/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:57.2179438Z [5027/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editcurve_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:01:58.1893876Z [5028/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editfont_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:00.1471027Z [5029/8229] Building CXX object source\blender\editors\curve\CMakeFiles\bf_editor_curve.dir\editfont.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:00.2285996Z [5030/8229] Linking CXX static library lib\bf_editor_curve.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:03.0963683Z [5031/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:03.9475683Z [5032/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_data.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:08.9415114Z [5033/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_attribute_set.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:10.0104125Z [5034/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:11.3304947Z [5035/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:13.8969054Z [5036/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_masks.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:14.0851661Z [5037/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_extrude.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:19.5401402Z [5038/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:20.1329458Z [5039/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:21.9497393Z [5040/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:24.1332240Z [5041/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\curves_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:24.7583472Z [5042/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\join.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:25.8510623Z [5043/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\select_linked_pick.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:28.1582310Z [5044/8229] Building CXX object source\blender\editors\curves\CMakeFiles\bf_editor_curves.dir\intern\separate.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:28.2374982Z [5045/8229] Linking CXX static library lib\bf_editor_curves.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:29.9382040Z [5046/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:31.0405289Z [5047/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_randomization.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:31.1528620Z [5048/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\geometry_attributes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:33.4955333Z [5049/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_draw_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:33.7589135Z [5050/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_library_presets.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:33.9072255Z [5051/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_arrow_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:34.0535266Z [5052/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_cube_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:34.2069040Z [5053/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\geometry\geom_dial_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:37.7906282Z [5054/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_library_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:38.6942856Z [5055/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\arrow3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:41.5007820Z [5056/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\blank3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:41.5551595Z [5057/8229] Building CXX object source\blender\editors\geometry\CMakeFiles\bf_editor_geometry.dir\node_group_operator.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:41.6179495Z [5058/8229] Linking CXX static library lib\bf_editor_geometry.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:43.2320177Z [5059/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\button2d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:46.1904607Z [5060/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\cage2d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:46.4998771Z [5061/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\cage3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:48.0489310Z [5062/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\dial3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:50.7618454Z [5063/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\move3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:51.2352030Z [5064/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\primitive3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:52.5266779Z [5065/8229] Building CXX object source\blender\editors\gizmo_library\CMakeFiles\bf_editor_gizmo_library.dir\gizmo_types\snap3d_gizmo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:52.5750091Z [5066/8229] Linking CXX static library lib\bf_editor_gizmo_library.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:55.5650788Z [5067/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\annotate_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:56.5588680Z [5068/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\annotate_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:56.5767544Z [5069/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\editaction_gpencil.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:02:58.7785758Z [5070/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_data.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:00.6465148Z [5071/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:01.7222100Z [5072/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:03.6650303Z [5073/8229] Building CXX object source\blender\editors\gpencil_legacy\CMakeFiles\bf_editor_gpencil_legacy.dir\gpencil_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:03.7077267Z [5074/8229] Linking CXX static library lib\bf_editor_gpencil_legacy.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:07.2016316Z [5075/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_add.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:08.4640642Z [5076/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_bake_animation.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:21.7807055Z [5077/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:22.1889729Z [5078/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_frames.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:23.0557806Z [5079/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_edit.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:29.1066182Z [5080/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_image_render.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:29.4148222Z [5081/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_layers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:29.4810514Z [5082/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_join_selection.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:34.9281988Z [5083/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_lineart.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:34.9574735Z [5084/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_material.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:36.2853364Z [5085/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_merge.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:39.9622378Z [5086/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_modes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:40.7941841Z [5087/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:42.2359130Z [5088/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_pen.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:45.4123182Z [5089/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_randomize.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:48.0527337Z [5090/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_primitive.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:50.2759832Z [5091/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_segments_geom.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:54.8124676Z [5092/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_trim.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:57.2435173Z [5093/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_undo.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:03:57.3417453Z [5094/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_select.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:04.0241507Z [5095/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_vertex_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:06.1638746Z [5096/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_weight_paint.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:06.7079727Z [5097/8229] Building CXX object source\blender\editors\grease_pencil\CMakeFiles\bf_editor_grease_pencil.dir\intern\grease_pencil_utils.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:06.8423902Z [5098/8229] Linking CXX static library lib\bf_editor_grease_pencil.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:08.3046743Z [5099/8229] Building CXX object source\blender\editors\id_management\CMakeFiles\bf_editor_id_management.dir\ed_id_management.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:08.3431093Z [5100/8229] Linking CXX static library lib\bf_editor_id_management.lib
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:11.4495566Z [5101/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\buttons\interface_textbox.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:11.5364278Z [5102/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_bone.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:13.6510010Z [5103/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:14.6601769Z [5104/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_colorband.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:16.1421039Z [5105/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_datablock.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:17.5948628Z [5106/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_driver.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:19.3378662Z [5107/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_depth.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:20.8227651Z [5108/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\eyedropper_grease_pencil_color.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:22.1654807Z [5109/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\eyedroppers\interface_eyedropper.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:23.6689680Z [5110/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_align.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:25.0634197Z [5111/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_anim.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:27.1765915Z [5112/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:27.1902313Z [5113/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_button_group.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:29.7850233Z [5114/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_context_path.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:31.0017931Z [5115/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_button_sections.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:32.8245485Z [5116/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_context_menu.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:32.8694407Z [5117/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_drag.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:35.1774477Z [5118/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_draw.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:35.3842402Z [5119/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_drop.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:37.9100032Z [5120/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_dropboxes.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:40.6867442Z [5121/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_icons_event.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:41.5199139Z [5122/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_icons.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:44.0199705Z [5123/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_handlers.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:45.7651842Z [5124/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_layout.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:45.7653307Z FAILED: [code=2] source/blender/editors/interface/CMakeFiles/bf_editor_interface.dir/interface_layout.cc.obj 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:45.7672030Z sccache "C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe"  /nologo /TP -DBLENDER_WIN_APPID=\"mixar.3.3\" -DBLENDER_WIN_APPID_FRIENDLY_NAME="\"Mixar 3.3\"" -DNDEBUG -DNOMINMAX -DWIN32 -DWIN32_LEAN_AND_MEAN -DWITH_ASSERT_ABORT -DWITH_INPUT_IME -DWITH_INPUT_NDOF -DWITH_INTERNATIONAL -DWITH_OPENVDB -DWITH_OPENVDB_BLOSC -DWITH_PYTHON -DWITH_TBB -DWITH_TBB_MALLOC -D_ALLOW_KEYWORD_MACROS -D_CONSOLE -D_CRT_NONSTDC_NO_DEPRECATE -D_CRT_SECURE_NO_DEPRECATE -D_LIB -D_SCL_SECURE_NO_DEPRECATE -D_USE_MATH_DEFINES -D_WIN32_WINNT=0x603 -D__LITTLE_ENDIAN__ -D__MMX__ -D__SSE2__ -D__SSE3__ -D__SSE4_1__ -D__SSE4_2__ -D__SSE__ -ID:\a\mixar-app\mixar-app\source\source\blender\editors\interface -ID:\a\mixar-app\mixar-app\source\source\blender\editors\asset -ID:\a\mixar-app\mixar-app\source\source\blender\editors\include -ID:\a\mixar-app\mixar-app\source\source\blender\animrig -ID:\a\mixar-app\mixar-app\source\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\python -ID:\a\mixar-app\mixar-app\source\intern\ghost -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\asset_system -ID:\a\mixar-app\mixar-app\source\source\blender\blenfont -ID:\a\mixar-app\mixar-app\source\source\blender\blenkernel -ID:\a\mixar-app\mixar-app\source\intern\profile\. -ID:\a\mixar-app\mixar-app\source\intern\openvdb -ID:\a\mixar-app\mixar-app\source\intern\mikktspace\. -ID:\a\mixar-app\mixar-app\source\source\blender\makesdna -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesdna\intern -ID:\a\mixar-app\mixar-app\source\source\blender\blenlib -ID:\a\mixar-app\mixar-app\source\intern\utfconv -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader_core -ID:\a\mixar-app\mixar-app\source\source\blender\blentranslation -ID:\a\mixar-app\mixar-app\source\source\blender\bmesh -ID:\a\mixar-app\mixar-app\source\source\blender\depsgraph -ID:\a\mixar-app\mixar-app\source\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\editors\datafiles -ID:\a\mixar-app\mixar-app\source\source\blender\functions -ID:\a\mixar-app\mixar-app\source\source\blender\gpu -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\compositor -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\imbuf\opencolorio -ID:\a\mixar-app\mixar-app\build\Prod\intern\opensubdiv -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\movie -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\opencolorio\. -ID:\a\mixar-app\mixar-app\source\intern\clog -ID:\a\mixar-app\mixar-app\source\intern\guardedalloc -ID:\a\mixar-app\mixar-app\source\source\blender\nodes -ID:\a\mixar-app\mixar-app\source\source\blender\render -ID:\a\mixar-app\mixar-app\source\source\blender\sequencer -ID:\a\mixar-app\mixar-app\source\source\blender\windowmanager -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\pthreads\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\vulkan\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\openVDB\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\tbb\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\OpenImageIO\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\fmt\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\opencolorio\include -external:W0 /W3 /w34062 /w34100 /w34115 /w34189 /w35038 /wd4018 /wd4146 /wd4065 /wd4127 /wd4181 /wd4200 /wd4244 /wd4267 /wd4305 /wd4800 /wd4828 /wd4996 /wd4661 /we4013 /we4133 /we4431 /we4033 /DWIN32 /D_WINDOWS /W3  /EHsc /nologo /J /Gd /MP /EHsc /bigobj /permissive- /Zc:__cplusplus /Zc:inline /Zc:preprocessor   /O2 /Ob2 /DNDEBUG /MD  -std:c++20 -MD /utf-8 /showIncludes /Fosource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_layout.cc.obj /Fdsource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\bf_editor_interface.pdb /FS -c D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:45.7683749Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc(1510): error C2228: left of '.is_empty' must have class/struct/union
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:45.7684616Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_layout.cc(1513): error C3861: 'but_drawflag_enable': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3055750Z [5125/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_mixar_section.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3057170Z FAILED: [code=2] source/blender/editors/interface/CMakeFiles/bf_editor_interface.dir/interface_mixar_section.cc.obj 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3072043Z sccache "C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\cl.exe"  /nologo /TP -DBLENDER_WIN_APPID=\"mixar.3.3\" -DBLENDER_WIN_APPID_FRIENDLY_NAME="\"Mixar 3.3\"" -DNDEBUG -DNOMINMAX -DWIN32 -DWIN32_LEAN_AND_MEAN -DWITH_ASSERT_ABORT -DWITH_INPUT_IME -DWITH_INPUT_NDOF -DWITH_INTERNATIONAL -DWITH_OPENVDB -DWITH_OPENVDB_BLOSC -DWITH_PYTHON -DWITH_TBB -DWITH_TBB_MALLOC -D_ALLOW_KEYWORD_MACROS -D_CONSOLE -D_CRT_NONSTDC_NO_DEPRECATE -D_CRT_SECURE_NO_DEPRECATE -D_LIB -D_SCL_SECURE_NO_DEPRECATE -D_USE_MATH_DEFINES -D_WIN32_WINNT=0x603 -D__LITTLE_ENDIAN__ -D__MMX__ -D__SSE2__ -D__SSE3__ -D__SSE4_1__ -D__SSE4_2__ -D__SSE__ -ID:\a\mixar-app\mixar-app\source\source\blender\editors\interface -ID:\a\mixar-app\mixar-app\source\source\blender\editors\asset -ID:\a\mixar-app\mixar-app\source\source\blender\editors\include -ID:\a\mixar-app\mixar-app\source\source\blender\animrig -ID:\a\mixar-app\mixar-app\source\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\python -ID:\a\mixar-app\mixar-app\source\intern\ghost -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesrna -ID:\a\mixar-app\mixar-app\source\source\blender\asset_system -ID:\a\mixar-app\mixar-app\source\source\blender\blenfont -ID:\a\mixar-app\mixar-app\source\source\blender\blenkernel -ID:\a\mixar-app\mixar-app\source\intern\profile\. -ID:\a\mixar-app\mixar-app\source\intern\openvdb -ID:\a\mixar-app\mixar-app\source\intern\mikktspace\. -ID:\a\mixar-app\mixar-app\source\source\blender\makesdna -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\makesdna\intern -ID:\a\mixar-app\mixar-app\source\source\blender\blenlib -ID:\a\mixar-app\mixar-app\source\intern\utfconv -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader -ID:\a\mixar-app\mixar-app\source\source\blender\blenloader_core -ID:\a\mixar-app\mixar-app\source\source\blender\blentranslation -ID:\a\mixar-app\mixar-app\source\source\blender\bmesh -ID:\a\mixar-app\mixar-app\source\source\blender\depsgraph -ID:\a\mixar-app\mixar-app\source\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\editors\datafiles -ID:\a\mixar-app\mixar-app\source\source\blender\functions -ID:\a\mixar-app\mixar-app\source\source\blender\gpu -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\compositor -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\draw -ID:\a\mixar-app\mixar-app\build\Prod\source\blender\imbuf\opencolorio -ID:\a\mixar-app\mixar-app\build\Prod\intern\opensubdiv -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\movie -ID:\a\mixar-app\mixar-app\source\source\blender\imbuf\opencolorio\. -ID:\a\mixar-app\mixar-app\source\intern\clog -ID:\a\mixar-app\mixar-app\source\intern\guardedalloc -ID:\a\mixar-app\mixar-app\source\source\blender\nodes -ID:\a\mixar-app\mixar-app\source\source\blender\render -ID:\a\mixar-app\mixar-app\source\source\blender\sequencer -ID:\a\mixar-app\mixar-app\source\source\blender\windowmanager -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\pthreads\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\vulkan\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\openVDB\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\tbb\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\OpenImageIO\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\fmt\include -external:ID:\a\mixar-app\mixar-app\source\lib\windows_x64\opencolorio\include -external:W0 /W3 /w34062 /w34100 /w34115 /w34189 /w35038 /wd4018 /wd4146 /wd4065 /wd4127 /wd4181 /wd4200 /wd4244 /wd4267 /wd4305 /wd4800 /wd4828 /wd4996 /wd4661 /we4013 /we4133 /we4431 /we4033 /DWIN32 /D_WINDOWS /W3  /EHsc /nologo /J /Gd /MP /EHsc /bigobj /permissive- /Zc:__cplusplus /Zc:inline /Zc:preprocessor   /O2 /Ob2 /DNDEBUG /MD  -std:c++20 -MD /utf-8 /showIncludes /Fosource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_mixar_section.cc.obj /Fdsource\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\bf_editor_interface.pdb /FS -c D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3090727Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(50): error C2228: left of '.size' must have class/struct/union
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3110274Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(51): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3111864Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(51): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3113705Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(67): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3115316Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(67): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3116891Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(80): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3118711Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(80): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3120399Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(93): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3121948Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(93): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3123598Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(106): error C3867: 'blender::ui::Block::buttons': non-standard syntax; use '&' to create a pointer to member
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3125387Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(106): error C2109: subscript requires array or pointer type
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3126746Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3128208Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3129591Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C3861: 'eRegion_Alignment': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3130996Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2065: 'RGN_ALIGN_RIGHT': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3132913Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(132): error C2737: 'is_left': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3134656Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2065: 'View2D': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3136036Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3137561Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(133): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3138950Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3140683Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3142419Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3143825Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(134): error C2065: 'style': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3145741Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3147355Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3148851Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3150304Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(135): error C2065: 'style': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3151646Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(136): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3153099Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(137): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3154650Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(137): error C2737: 'fontid': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3156184Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(138): error C2065: 'fstyle': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3157648Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3159039Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3160386Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C3861: 'BLI_listbase_is_empty': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3161275Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(141): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3162002Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3162743Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(139): error C2737: 'aspect': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3163505Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(143): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3164410Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(143): error C2737: 'dpi_fac': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3165213Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(144): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3165970Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(144): error C2737: 'px': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3166845Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3167735Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3168480Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C2065: 'btheme': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3169247Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(147): error C3861: 'UI_GetTheme': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3170106Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C4430: missing type specifier - int assumed. Note: C++ does not support default-int
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3171323Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2143: syntax error: missing ';' before '*'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3172066Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3172794Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(148): error C2065: 'btheme': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3173528Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3174468Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3175283Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3176067Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(154): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3176873Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3177660Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3178459Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3179228Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(155): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3180005Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3180787Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3181571Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3182423Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(156): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3183192Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3183975Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3184762Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3185533Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(157): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3186330Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3187118Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3187907Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3188749Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(158): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3189515Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3190327Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3191352Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3192131Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(159): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3192885Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3193677Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3194662Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3195436Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(160): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3196206Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): error C2065: 'ts': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3197021Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): error C2660: 'ubyte4_to_float4': function does not take 1 arguments
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3197823Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(118): note: see declaration of 'ubyte4_to_float4'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3198604Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(161): note: while trying to match the argument list '(float [4])'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3199371Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3200171Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C2065: 'USER_UIFLAG2_PANEL_TABS_COMPACT': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3201070Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(176): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3201850Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(177): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3202668Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(177): error C2737: 'tab_v_pad_text': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3203479Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(178): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3204260Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(183): error C2065: 'BLF_ROTATION': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3205039Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(183): error C3861: 'BLF_enable': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3205804Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(184): error C3861: 'BLF_rotation': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3206594Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(186): error C2065: 'U': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3208278Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(186): error C3861: 'BLF_size': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3209056Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3209800Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3210574Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(189): error C2737: 'rct_xmin': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3211544Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3212286Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3213051Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(190): error C2737: 'rct_xmax': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3213850Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2065: 'PanelCategoryDyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3214591Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2059: syntax error: ','
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3215322Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(195): error C2143: syntax error: missing ';' before '{'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3216068Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'rcti': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3216830Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3217571Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(196): error C2065: 'pc_dyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3218312Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(197): error C2065: 'pc_dyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3219096Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(197): error C3861: 'BLT_translate_do_iface': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3220271Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(199): error C3861: 'BLF_width': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3221039Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(198): error C3861: 'round_fl_to_int': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3221793Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(201): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3222518Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(202): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3223248Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(203): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3223972Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(203): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3224694Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(204): error C2065: 'rct': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3225422Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(204): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3226148Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2065: 'v2d': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3227001Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C3861: 'BLI_rcti_size_y': identifier not found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3227849Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2672: 'std::max': no matching overloaded function found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3229170Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(88): note: could be '_Ty std::max(std::initializer_list<_Elem>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3230082Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): note: '_Ty std::max(std::initializer_list<_Elem>)': expects 1 arguments - 2 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3230976Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(85): note: or       '_Ty std::max(std::initializer_list<_Elem>,_Pr)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3231959Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(77): note: or       'const _Ty &std::max(const _Ty &,const _Ty &) noexcept(<expr>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3232844Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\utility(67): note: or       'const _Ty &std::max(const _Ty &,const _Ty &,_Pr) noexcept(<expr>)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3233815Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): note: 'const _Ty &std::max(const _Ty &,const _Ty &,_Pr) noexcept(<expr>)': expects 3 arguments - 2 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3234737Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(210): error C2737: 'max_scroll': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3235521Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3236283Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3237065Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2672: 'std::clamp': no matching overloaded function found
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3237944Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\algorithm(11911): note: could be 'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3238937Z C:\Program Files\Microsoft Visual Studio\18\Enterprise\VC\Tools\MSVC\14.51.36231\include\algorithm(11883): note: or       'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &,_Pr)'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3239928Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): note: 'const _Ty &std::clamp(const _Ty &,const _Ty &,const _Ty &,_Pr)': expects 4 arguments - 3 provided
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3240835Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(211): error C2737: 'scroll': const object must be initialized
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3241597Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(212): error C2027: use of undefined type 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3242327Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.hh(70): note: see declaration of 'ARegion'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3243099Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): error C2065: 'PanelCategoryDyn': undeclared identifier
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3243843Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): error C2059: syntax error: ','
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:46.3244616Z D:\a\mixar-app\mixar-app\source\source\blender\editors\interface\interface_mixar_section.cc(213): fatal error C1003: error count exceeds 100; stopping compilation
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.0385657Z [5126/8229] Building CXX object source\blender\editors\interface\CMakeFiles\bf_editor_interface.dir\interface_ops.cc.obj
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.0389401Z ninja: build stopped: subcommand failed.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.0574015Z Error: Build failed
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3408002Z ^[[31;1mException: ^[[0mD:\a\_temp\3ee8163b-74bd-434c-93d6-cfc1b92a5b9a.ps1:6^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3408524Z ^[[31;1m^[[0m^[[36;1mLine |^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3408995Z ^[[31;1m^[[0m^[[36;1m^[[36;1m   6 | ^[[0m if ($code -ne 0) { ^[[36;1mthrow "build.bat exited with $code"^[[0m }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3409796Z ^[[31;1m^[[0m^[[36;1m^[[36;1m^[[0m^[[36;1m^[[0m^[[36;1m     | ^[[31;1m                    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3410513Z ^[[31;1m^[[0m^[[36;1m^[[36;1m^[[0m^[[36;1m^[[0m^[[36;1m^[[31;1m^[[31;1m^[[36;1m     | ^[[31;1mbuild.bat exited with 1^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.3726938Z ##[error]Process completed with exit code 1.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4242717Z ##[group]Run if (Get-Command sccache -ErrorAction SilentlyContinue) {
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4243327Z ^[[36;1mif (Get-Command sccache -ErrorAction SilentlyContinue) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4243676Z ^[[36;1m  sccache --show-stats^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4243934Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4337176Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4337503Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4337713Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4337935Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4338154Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4338383Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4338595Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4338843Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4339119Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4339361Z   SHORT_SHA: 5b6f0e1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4339614Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.4339863Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7007030Z Compile requests                   2239
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7007552Z Compile requests executed          2065
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7008561Z Cache hits                            0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7009426Z Cache misses                       2063
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7010009Z Cache misses (C/C++)               2063
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7010332Z Cache hits rate                    0.00 %
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7010661Z Cache hits rate (C/C++)            0.00 %
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7010986Z Cache timeouts                        0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7011291Z Cache read errors                     0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7011871Z Forced recaches                       0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7012185Z Cache write errors                    0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7012489Z Cache errors                          0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7013058Z Compilations                       2063
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7013383Z Compilation failures                  2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7013714Z Non-cacheable compilations            0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7014028Z Non-cacheable calls                 174
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7014291Z Non-compilation calls                 0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7014547Z Unsupported compiler calls            0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7014805Z Average cache write               0.000 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7015067Z Average compiler                  1.950 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7015321Z Average cache read hit            0.000 s
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7015578Z Failed distributed compilations       0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7015754Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7015837Z Non-cacheable reasons:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7016059Z multiple input files                172
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7016310Z /Yc                                   2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7016469Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7016644Z Cache location                  Local disk: "D:\\a\\mixar-app\\mixar-app\\.sccache"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7017035Z Base directories                (none)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7017936Z Use direct/preprocessor mode?   yes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7018415Z Version (client)                0.17.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7019160Z Cache size                           46 MiB
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.7019606Z Max cache size                        5 GiB
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8069841Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8071160Z ##[group]Run actions/cache/save@v4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8071643Z with:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8072037Z   path: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8072421Z   key: sccache-Windows-Prod-v5.2.0-5b6f0e19ed2b294a0dfda59b8fb1b7c34b1fe229
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8072803Z   enableCrossOsArchive: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8073037Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8073234Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8073442Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8073661Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8073877Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8074089Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8074425Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8074700Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8074922Z   SHORT_SHA: 5b6f0e1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8075130Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:49.8075328Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:50.3898312Z (node:1404) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:50.3899068Z (Use `node --trace-deprecation ...` to show where the warning was created)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:50.4871996Z [command]"C:\Program Files\Git\usr\bin\tar.exe" --posix -cf cache.tzst --exclude cache.tzst -P -C D:/a/mixar-app/mixar-app --files-from manifest.txt --force-local --use-compress-program "zstd -T0"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:51.1015128Z (node:1404) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.1024745Z Sent 47685294 of 47685294 (100.0%), 44.9 MBs/sec
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4298008Z Cache saved with key: sccache-Windows-Prod-v5.2.0-5b6f0e19ed2b294a0dfda59b8fb1b7c34b1fe229
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4582900Z ##[group]Run $out = New-Object System.Collections.Generic.List[string]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4583498Z ^[[36;1m$out = New-Object System.Collections.Generic.List[string]^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4584005Z ^[[36;1m$out.Add("Run: https://github.com/aimcrazyxx/mixar-app/actions/runs/31946334651")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4584633Z ^[[36;1m$out.Add("Commit: 5b6f0e19ed2b294a0dfda59b8fb1b7c34b1fe229")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4585003Z ^[[36;1m$out.Add("Runner: Windows / windows-latest")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4585296Z ^[[36;1m$out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4585557Z ^[[36;1mfunction Add-Block($title, $path, $tail) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4585847Z ^[[36;1m  $out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4586110Z ^[[36;1m  $out.Add("## $title")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4586365Z ^[[36;1m  if (Test-Path $path) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4586621Z ^[[36;1m    $out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4586939Z ^[[36;1m    Get-Content $path -Tail $tail -ErrorAction SilentlyContinue |^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4587385Z ^[[36;1m      ForEach-Object { $out.Add($_) }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4587652Z ^[[36;1m    $out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4587943Z ^[[36;1m  } else {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4588257Z ^[[36;1m    $out.Add("not produced - the job died before this file existed")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4588640Z ^[[36;1m  }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4588845Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4589129Z ^[[36;1mAdd-Block "Free disk after each stage" "logs\disk.log" 40^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4589496Z ^[[36;1mAdd-Block "Directory sizes" "logs\sizes.log" 40^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4589848Z ^[[36;1mAdd-Block "Library fetch (tail)" "logs\libs.log" 100^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4590204Z ^[[36;1mAdd-Block "build.bat (tail)" "logs\build.log" 200^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4590678Z ^[[36;1mAdd-Block "CMakeError.log (tail)" "build\$env:MIXAR_ENV\CMakeFiles\CMakeError.log" 120^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4591068Z ^[[36;1m$out.Add("")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4591318Z ^[[36;1m$out.Add("## Free space right now")^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4591601Z ^[[36;1m$out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4591843Z ^[[36;1m$drive = Get-PSDrive C^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4592204Z ^[[36;1m$out.Add(("free {0:N1} GB, used {1:N1} GB" -f ($drive.Free / 1GB), ($drive.Used / 1GB)))^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4592607Z ^[[36;1m$out.Add('```')^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4592928Z ^[[36;1mSet-Content -Path failure-report.md -Value $out -Encoding utf8^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4593379Z ^[[36;1mGet-Content failure-report.md | Add-Content -Path $env:GITHUB_STEP_SUMMARY^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4593959Z ^[[36;1m$pr = gh pr list --repo $env:GITHUB_REPOSITORY --head $env:GITHUB_REF_NAME --state open --json number --jq '.[0].number'^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4594423Z ^[[36;1mif ($pr) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4594756Z ^[[36;1m  gh pr comment $pr --repo $env:GITHUB_REPOSITORY --body-file failure-report.md^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4595193Z ^[[36;1m  Write-Host "reported on pull request #$pr"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4595480Z ^[[36;1m} else {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4595798Z ^[[36;1m  Write-Host "no open pull request for $env:GITHUB_REF_NAME - trying Issues"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4596199Z ^[[36;1m  gh issue create --repo $env:GITHUB_REPOSITORY `^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4596545Z ^[[36;1m    --title "Windows build failed - run 31946334651" `^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4596909Z ^[[36;1m    --body-file failure-report.md^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4597173Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4652023Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4652437Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4652739Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4653004Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4653278Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4653558Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4653831Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4654157Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4654514Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4654836Z   SHORT_SHA: 5b6f0e1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4655110Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4682671Z   GH_TOKEN: ***
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:52.4683012Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:53.8078307Z no open pull request for main - trying Issues
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.2323933Z the 'aimcrazyxx/mixar-app' repository has disabled issues
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.2840737Z ##[error]Process completed with exit code 1.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3078794Z ##[group]Run Get-PSDrive C | Select-Object Used, Free | Format-List
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3079338Z ^[[36;1mGet-PSDrive C | Select-Object Used, Free | Format-List^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3079878Z ^[[36;1mif (Test-Path logs\disk.log) { Get-Content logs\disk.log }^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3080337Z ^[[36;1m$errorLog = "build\$env:MIXAR_ENV\CMakeFiles\CMakeError.log"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3080692Z ^[[36;1mif (Test-Path $errorLog) {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3080987Z ^[[36;1m  Write-Host "--- tail of $errorLog ---"^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3081329Z ^[[36;1m  Get-Content $errorLog -Tail 200^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3081604Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3081850Z ^[[36;1mif (Test-Path "build\$env:MIXAR_ENV\bin") {^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3082278Z ^[[36;1m  Get-ChildItem "build\$env:MIXAR_ENV\bin" | Select-Object Name | Format-Table -AutoSize^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3082678Z ^[[36;1m}^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3136199Z shell: C:\Program Files\PowerShell\7\pwsh.EXE -command ". '{0}'"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3136753Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3137009Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3137270Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3137549Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3137818Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3138100Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3138454Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3138802Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3139079Z   SHORT_SHA: 5b6f0e1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3139351Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.3139616Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.6994176Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7017827Z ^[[32;1mUsed : ^[[0m112730451968
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7018655Z ^[[32;1mFree : ^[[0m47737307136
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7019000Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7083293Z after checkout                         30.6 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7085009Z after reclaim                          44.5 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7086000Z after libraries                        44.5 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7087501Z after build.bat (exit 1)               44.5 GB free
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7167620Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7188312Z ^[[32;1mName^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7188840Z ^[[32;1m----^[[0m
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7189924Z datatoc.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7190284Z makesdna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7192597Z makesrna.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7192968Z msgfmt.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7193303Z shader_tool.exe
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7193551Z 
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7740738Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7741891Z ##[group]Run actions/upload-artifact@v4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7742211Z with:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7742443Z   name: build-logs-31946334651
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7742704Z   path: logs/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7742966Z   if-no-files-found: warn
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7743222Z   retention-days: 14
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7743472Z   compression-level: 6
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7743714Z   overwrite: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7743986Z   include-hidden-files: false
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7744249Z env:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7744464Z   MIXAR_ENV: Prod
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7744695Z   BLENDER_VERSION: 5.2
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7744928Z   BLENDER_REF: v5.2.0
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7745274Z   BUILD_WITH_NINJA: 1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7745511Z   MAKE_INSTALLER: true
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7745776Z   SCCACHE_DIR: D:\a\mixar-app\mixar-app\.sccache
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7746082Z   SCCACHE_CACHE_SIZE: 5G
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7746321Z   SHORT_SHA: 5b6f0e1
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7746552Z   BUILD_CORES: 4
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.7746809Z ##[endgroup]
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.9993357Z (node:6388) [DEP0040] DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:54.9994220Z (Use `node --trace-deprecation ...` to show where the warning was created)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.0063798Z With the provided path, there will be 4 files uploaded
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.0068188Z Artifact name is valid!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.0069352Z Root directory input is valid!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.2083449Z Beginning upload of artifact content to blob storage
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.2689427Z (node:6388) [DEP0169] DeprecationWarning: `url.parse()` behavior is not standardized and prone to errors that have security implications. Use the WHATWG URL API instead. CVEs are not issued for `url.parse()` vulnerabilities.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.4649192Z Uploaded bytes 69470
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.5061559Z Finished uploading artifact content to blob storage!
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.5062498Z SHA256 digest of uploaded artifact zip is aeafcdbc9f71d1df01aa5dda9f816cf06634762ecf1229e14d26ac0c5439838a
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.5064264Z Finalizing artifact upload
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.6969117Z Artifact build-logs-31946334651.zip successfully finalized. Artifact ID 9264050297
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.6970142Z Artifact build-logs-31946334651 has been successfully uploaded! Final size is 69470 bytes. Artifact ID is 9264050297
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.6979642Z Artifact download URL: https://github.com/aimcrazyxx/mixar-app/actions/runs/31946334651/artifacts/9264050297
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.7540678Z Node 20 is being deprecated. This workflow is running with Node 24 by default. If you need to temporarily use Node 20, you can set the ACTIONS_ALLOW_USE_UNSECURE_NODE_VERSION=true environment variable. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.7541816Z Post job cleanup.
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9415221Z [command]"C:\Program Files\Git\bin\git.exe" version
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9704371Z git version 2.55.0.windows.3
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9757752Z Copying 'C:\Users\runneradmin\.gitconfig' to 'D:\a\_temp\cd2a887c-14d5-4eb2-af4b-e50215005ac9\.gitconfig'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9777487Z Temporarily overriding HOME='D:\a\_temp\cd2a887c-14d5-4eb2-af4b-e50215005ac9' before making global git config changes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9778996Z Adding repository directory to the temporary git global config as a safe directory
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:55.9789080Z [command]"C:\Program Files\Git\bin\git.exe" config --global --add safe.directory D:\a\mixar-app\mixar-app
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.0069728Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp core\.sshCommand
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.0335069Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'core\.sshCommand' && git config --local --unset-all 'core.sshCommand' || :\""
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.5358834Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.6109115Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.6949160Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp http\.https\:\/\/github\.com\/\.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.7168694Z http.https://github.com/.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.7207614Z [command]"C:\Program Files\Git\bin\git.exe" config --local --unset-all http.https://github.com/.extraheader
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:56.7461886Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "sh -c \"git config --local --name-only --get-regexp 'http\.https\:\/\/github\.com\/\.extraheader' && git config --local --unset-all 'http.https://github.com/.extraheader' || :\""
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.2247587Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.2956270Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.3801387Z [command]"C:\Program Files\Git\bin\git.exe" config --local --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.4070343Z [command]"C:\Program Files\Git\bin\git.exe" submodule foreach --recursive "git config --local --show-origin --name-only --get-regexp remote.origin.url"
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.8818604Z Entering 'upstream'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.9105403Z file:D:/a/mixar-app/mixar-app/.git/modules/upstream/config	remote.origin.url
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.9292734Z Entering 'upstream/lib/windows_x64'
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.9584883Z file:D:/a/mixar-app/mixar-app/.git/modules/upstream/modules/lib/windows_x64/config	remote.origin.url
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:57.9855280Z [command]"C:\Program Files\Git\bin\git.exe" config --file D:/a/mixar-app/mixar-app/.git/modules/upstream/config --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.0132608Z [command]"C:\Program Files\Git\bin\git.exe" config --file D:/a/mixar-app/mixar-app/.git/modules/upstream/modules/lib/windows_x64/config --name-only --get-regexp ^includeIf\.gitdir:
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.0598573Z Cleaning up orphan processes
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.1369173Z Terminate orphan process: pid (2852) (vctip)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.1516085Z Terminate orphan process: pid (6640) (sccache)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.1634461Z Terminate orphan process: pid (2984) (conhost)
Prod / Blender 5.2	UNKNOWN STEP	2026-08-16T13:04:58.1656090Z ##[warning]Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/cache/restore@v4, actions/cache/save@v4, actions/checkout@v4, actions/upload-artifact@v4. For more information see: https://github.blog/changelog/2025-09-19-deprecation-of-node-20-on-github-actions-runners/
```
