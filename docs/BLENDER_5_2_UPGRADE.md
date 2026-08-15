<!--
SPDX-FileCopyrightText: 2026 Mixar fork contributors
SPDX-License-Identifier: GPL-3.0-or-later
-->

# Moving this fork to Blender 5.2

This fork builds on **Blender 5.0**, and moving it to 5.2 is a source migration,
not a version-string change.

## How the tree is actually assembled

An earlier revision of this document said the Blender tree is a submodule and is
"not vendored as files". The submodule half is true; the second half is not, and
it is worth being precise because the difference is what breaks the build.

`upstream/` is a submodule pinned to a Blender revision. But `src/` holds **whole
copies of Blender files**, and the overlay step copies them on top of `upstream/`
with no `/XO`, commented in `scripts/windows/overlay.bat` as "Mixar src files must
ALWAYS win over upstream, regardless of timestamps". So the Blender code that
really compiles is whichever revision `src/` was forked from — the submodule pin
only supplies the files `src/` does not carry.

The overlay is Blender 5.0. `src/source/blender/blenkernel/BKE_blender_version.h`
reads:

```c
#define BLENDER_VERSION 500
```

and the vendored files match 5.0 byte for byte, plus Mixar's edits:

| file | in `src/` | Blender 5.0 | Blender 5.2 |
| --- | --- | --- | --- |
| `CMakeLists.txt` | 113,052 | 112,965 | 93,556 |
| `build_files/cmake/platform/platform_win32.cmake` | 51,230 | 51,182 | 44,913 |
| `source/creator/CMakeLists.txt` | 72,275 | 68,171 | — |
| `source/creator/creator.cc` | 16,858 | 16,077 | — |

## Why pinning 5.2 without migrating fails

Setting `BLENDER_REF=v5.2.0` while `src/` is 5.0 mixes two releases. Between 5.0
and 5.1, Blender moved Windows dependency handling out of `platform_win32.cmake`
and into `dependency_targets.cmake`, which grew from 3,596 to 20,758 bytes. The
overlay replaces `platform_win32.cmake` with 5.0's copy, but it does not carry
`dependency_targets.cmake` at all, so 5.2's version survives from upstream and
asks for imported targets that only 5.2's `platform_win32.cmake` creates:

```
add_library cannot create ALIAS target "bf::dependencies::opencolorio"
because target "OpenColorIO::OpenColorIO" does not already exist.
```

The same 5.0 file hardcodes Python 3.11, which produces the other half of the
failure even though the 5.2 libraries ship `python/313`:

```
Missing: ".../source/lib/windows_x64/python/311/include/Python.h"
```

Both messages are one defect. They are not a library problem: the precompiled set
downloads correctly at 6.5 GB with every dependency present.

`.github/workflows/build-windows.yml` now compares `BLENDER_VERSION` in `src/`
against `upstream/` before configuring, so this mismatch fails in seconds with a
named cause instead of 25 minutes into CMake.

## Doing the migration

`scripts/upgrade/` already implements the rebase:

- `generate_diff.py` splits `src/` into *upstream-modified* files (recorded as a
  unified diff against the current `upstream/`, with the base commit written into
  the patch header) and *custom* Mixar files that have no upstream counterpart.
- `apply_patch.py` checks out nothing itself; it replays that patch onto whatever
  `upstream/` now points at, per file, with `git merge-file -p --diff3` using the
  recorded base commit as the ancestor. Custom files are preserved as-is and
  `src/` is backed up to `src_backup_<timestamp>/` first.
- `migrate_upstream.py` chains the two interactively. It takes `--fuzzy` but never
  forwards it, so that flag currently does nothing.

Run it in CI with **Actions to Migrate Blender upstream**, which needs no
compiler and no precompiled libraries:

```
base_ref:     v5.0.0
target_ref:   v5.2.0
push_branch:  migration/blender-5.2
```

It publishes the merged tree and commits `docs/migration/overlay-v5.2.0.md`,
listing every file left with conflict markers. Or run the same thing locally:

```bash
git clone --recurse-submodules https://github.com/<you>/mixar-app.git
cd mixar-app
git -C upstream checkout v5.0.0
python scripts/upgrade/generate_diff.py --output /tmp/overlay.patch \
  --custom-files-output /tmp/custom_files.json
git -C upstream checkout v5.2.0
python scripts/upgrade/apply_patch.py /tmp/overlay.patch \
  --custom-files /tmp/custom_files.json --report /tmp/conflicts.json
```

## What still has to be decided by hand

1. **Conflicts.** Every vendored file whose upstream counterpart changed between
   5.0 and 5.2 has to be reviewed. The large ones are `CMakeLists.txt`,
   `build_files/cmake/macros.cmake`, `platform_win32.cmake`,
   `blenkernel/intern/blendfile.cc` and
   `blenkernel/intern/grease_pencil_convert_legacy.cc`.
2. **DNA and RNA.** `src/source/blender/makesdna/` carries `DNA_space_types.h`,
   `DNA_space_enums.h`, `DNA_theme_types.h` and `DNA_fileglobal_types.h` for the
   eight Mixar editor spaces (`space_mixie`, `space_mixie_chat`,
   `space_agent_bubble`, `space_baking`, `space_mixar_assets`,
   `space_mixar_layers`, `space_mixar_properties`, `space_texture_sets`). Struct
   changes affect the file format, so check `BLENDER_FILE_SUBVERSION` and the
   versioning code in `blenloader` after merging.
3. **Version constants.** `BKE_blender_version.h` should end up at `502`, and
   `BLENDER_VERSION` in both settings files must match, since it names the runtime
   resource folder and the embedded Python path used by `package.bat`.
4. **`PYTHON_VERSION`.** Set by upstream, not by us. 5.0 ships 3.11 and 5.2 ships
   3.13; confirm against the `lib/windows_x64/python/<version>` folder name rather
   than assuming.
5. **Python API drift.** `bpy` changes between 5.0 and 5.2 hit
   `src/scripts/mixar/**`. Run `pytest`, then start the app and read the console
   for registration errors.
6. **Mixar's own version.** `VERSION` is independent of `BLENDER_VERSION`; bump it
   separately if you ship this.

## The custom endpoint work is independent

The runtime endpoint and custom provider support only touch
`src/scripts/mixar/**`, so they apply on 5.0 and on 5.2 alike. Shipping on 5.0
today and migrating separately is a valid order.
