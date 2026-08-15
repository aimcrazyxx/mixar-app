<!--
SPDX-FileCopyrightText: 2026 Mixar fork contributors
SPDX-License-Identifier: GPL-3.0-or-later
-->

# Moving this fork to Blender 5.2

Upstream Mixar 2.0.0 builds on **Blender 5.0**. The Blender tree is not vendored
as files — it is a git **submodule** (`upstream/` →
`https://projects.blender.org/blender/blender.git`), and the exact revision is
pinned per branch as a gitlink.

## What this branch already changed

| Change | File |
|---|---|
| `BLENDER_VERSION` default `5.0` → `5.2` | `scripts/unix/settings.sh` |
| `BLENDER_VERSION` default `5.0` → `5.2` | `scripts/windows/settings.bat` |
| Removed 7 hardcoded `5.0` path segments, now derived from `$BLENDER_VERSION` | `scripts/unix/generate_default_theme.sh` |
| One-step submodule + constant bump helper | `scripts/upgrade/set_blender_version.sh` |

`BLENDER_VERSION` is what names the runtime resource folder
(`Mixar.app/Contents/Resources/5.2/...`, `~/.config/mixar/5.2/...`), so it has
to match the pinned upstream revision or the embedded Python and the user
preferences are looked up in the wrong place.

## What still has to happen locally

The submodule pin itself **cannot** be changed through the GitHub API or web UI:
a submodule pointer is a gitlink, and the contents API only writes file blobs.
Run this in a local clone:

```bash
git clone --recurse-submodules https://github.com/<you>/mixar-app.git
cd mixar-app
git checkout feat/custom-endpoints

# option A — the helper added by this branch (fetch + checkout + version sync)
bash scripts/upgrade/set_blender_version.sh 5.2 v5.2.0

# option B — upstream's own tool, then just sync the constants
python scripts/upgrade/checkout_upstream.py blender-v5.2-release
SKIP_CHECKOUT=1 bash scripts/upgrade/set_blender_version.sh 5.2

git commit -m "build: bump upstream Blender to 5.2"
make init && make build
```

Verified target revision (Blender release tag `v5.2.0`):

```
fbe6228777e7d9afefcd61a413844e790ae75db7
```

If you prefer to track the release branch instead of the exact tag, use
`blender-v5.2-release`.

## Expect to fix things

This is a two-minor-version jump of a 5M-line C++ codebase, so treat it as a
migration, not a version string edit:

1. **Overlay conflicts.** This repo builds by overlaying `src/` on top of
   `upstream/` (`scripts/unix/overlay.sh`). Any Mixar-patched Blender file whose
   upstream counterpart changed between 5.0 and 5.2 has to be re-based —
   `scripts/upgrade/migrate_upstream.py blender-v5.2-release` walks these
   interactively, and `scripts/upgrade/apply_patch.py` handles the patch set.
2. **Python API drift.** `bpy` breaking changes between 5.0 and 5.2 hit
   `src/scripts/mixar/**` (operators, UI classes, keymaps, gpu module). Run
   `pytest` first, then start the app and check the console for registration
   errors.
3. **`PYTHON_VERSION`.** Blender's embedded Python version is set by upstream,
   not by us. Confirm it against
   `upstream/build_files/build_environment/cmake/versions.cmake` and update
   `PYTHON_VERSION` in both settings files if 5.2 moved off 3.11 — otherwise the
   `site-packages` path in `generate_default_theme.sh` misses.
4. **Precompiled libraries.** `make init` pulls the platform libs matching the
   pinned revision. Do not mix 5.0 libs with a 5.2 tree; wipe `build/` on the
   first build after the bump.
5. **Version metadata.** Mixar's own product version lives in `VERSION` and is
   independent of `BLENDER_VERSION`; bump it separately if you ship this.

## Custom endpoints and the bump are independent

The runtime endpoint overlay (`docs/CUSTOM_ENDPOINTS.md`) only touches
`src/scripts/mixar/**`, so it applies cleanly on 5.0 and on 5.2. If the 5.2
migration turns out to be a long job, you can ship the custom base URL support
on 5.0 today and bump Blender separately.
