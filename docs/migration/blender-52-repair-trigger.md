<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 repair trigger

Temporary same-repository pull request used only to dispatch the reviewed main-branch repair workflow. The workflow patches the remaining Mixar widget API mismatches, handles `SPACE_AGENT_BUBBLE` explicitly, runs the expanded stale-API audit, and starts exact-SHA Windows validation.

The expanded report found 165 stale-pattern hits across custom Mixar callers. This synchronization applies the reviewed Blender 5.2 names, fully qualifies UI symbols outside `blender::ui`, migrates all old operator-property creation calls, reruns the report-only audit, and dispatches the full Windows build only when it is clean.
