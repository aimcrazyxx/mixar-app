<!--
SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
SPDX-License-Identifier: GPL-2.0-or-later
-->

# Migration trigger

Changing this file on `main` starts the `Migrate Blender upstream` workflow.

It exists for one reason: a `workflow_dispatch` run can only be started from the
Run workflow button or the Actions API. Automation that can push commits but has
no Actions API access needs some other way in, and a path filter on a harmless
file is the cheapest one.

The workflow reads nothing out of this file. A push-started run always uses the
defaults declared in `.github/workflows/migrate-blender.yml`; to migrate between
any other pair of tags, use the Run workflow button instead.

## Requested runs

- 2026-08-15 - rebase the `src/` overlay from `v5.0.0` onto `v5.2.0`, publishing
  to `migration/blender-5.2`.
