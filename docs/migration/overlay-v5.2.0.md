<!--
SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
SPDX-License-Identifier: GPL-2.0-or-later
-->

# Overlay migration: v5.0.0 to v5.2.0

Produced by .github/workflows/migrate-blender.yml, run 31895909583.

| field | value |
| --- | --- |
| base revision | a37564c4df7a9b604809e5192918400e46a0205f (v5.0.0) |
| target revision | fbe6228777e7d9afefcd61a413844e790ae75db7 (v5.2.0) |
| apply_patch.py exit code | 1 |
| files with conflict markers | 49 |

## Inventory

```
  Upstream-modified files: 116 (will be patched with 3-way merge)
  Custom Mixar files:      1477 (will be preserved as-is)
  Removed from upstream:   20213 (manual review needed)
```

Upstream-modified files were rebased with a 3-way merge. Custom Mixar
files have no upstream counterpart and were carried over untouched.

## Files still carrying conflict markers

- src/CMakeLists.txt
- src/build_files/cmake/platform/platform_apple.cmake
- src/build_files/cmake/platform/platform_win32.cmake
- src/build_files/windows/build_msbuild.cmd
- src/build_files/windows/configure_msbuild.cmd
- src/intern/ghost/intern/GHOST_SystemCocoa.mm
- src/intern/ghost/intern/GHOST_SystemWin32.cc
- src/intern/ghost/intern/GHOST_WindowWin32.cc
- src/intern/ghost/intern/GHOST_XrContext.cc
- src/release/datafiles/userdef/userdef_default_theme.c
- src/release/windows/msix/AppxManifest.xml.template
- src/scripts/startup/bl_ui/space_toolsystem_toolbar.py
- src/source/blender/blendthumb/CMakeLists.txt
- src/source/blender/blenkernel/BKE_appdir.hh
- src/source/blender/blenkernel/BKE_main.hh
- src/source/blender/blenlib/intern/winstuff.cc
- src/source/blender/blenloader/CMakeLists.txt
- src/source/blender/blenloader/intern/versioning_500.cc
- src/source/blender/blenloader/intern/writefile.cc
- src/source/blender/draw/engines/overlay/overlay_grid.hh
- src/source/blender/editors/interface/interface_handlers.cc
- src/source/blender/editors/interface/interface_layout.cc
- src/source/blender/editors/interface/interface_widgets.cc
- src/source/blender/editors/interface/templates/interface_template_id.cc
- src/source/blender/editors/screen/area.cc
- src/source/blender/editors/space_file/file_ops.cc
- src/source/blender/editors/space_image/space_image.cc
- src/source/blender/editors/space_view3d/space_view3d.cc
- src/source/blender/editors/space_view3d/view3d_intern.hh
- src/source/blender/editors/transform/transform_gizmo_2d.cc
- src/source/blender/makesdna/DNA_fileglobal_types.h
- src/source/blender/makesdna/DNA_space_enums.h
- src/source/blender/makesdna/DNA_space_types.h
- src/source/blender/makesdna/DNA_theme_types.h
- src/source/blender/makesrna/intern/makesrna.cc
- src/source/blender/makesrna/intern/rna_main_api.cc
- src/source/blender/makesrna/intern/rna_space.cc
- src/source/blender/makesrna/intern/rna_ui_api.cc
- src/source/blender/makesrna/intern/rna_userdef.cc
- src/source/blender/windowmanager/intern/wm_draw.cc
- src/source/blender/windowmanager/intern/wm_event_system.cc
- src/source/blender/windowmanager/intern/wm_files.cc
- src/source/blender/windowmanager/intern/wm_operator_props.cc
- src/source/blender/windowmanager/intern/wm_splash_screen.cc
- src/source/blender/windowmanager/intern/wm_window.cc
- src/source/creator/CMakeLists.txt
- src/source/creator/creator.cc
- src/tests/python/CMakeLists.txt
- src/tools/check_blender_release/check_static_binaries.py

Markers are diff3 style: the new upstream text first, then the old
upstream ancestor after |||||||, then the Mixar version after =======.

## Follow-up before this branch can build

1. Resolve every file listed above.
2. Flip the pins: BLENDER_REF and BLENDER_VERSION in .github/workflows/build-windows.yml, and BLENDER_VERSION plus PYTHON_VERSION in scripts/windows/settings.bat and scripts/unix/settings.sh.
3. Blender 5.2 ships embedded Python 3.13, so PYTHON_VERSION becomes 3.13. Confirm against the lib/windows_x64/python folder name.
4. Merge into ci/build-windows to trigger the Windows build.
