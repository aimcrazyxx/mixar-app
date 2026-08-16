<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# Blender 5.2 repair trigger

Temporary same-repository pull request used only to dispatch the reviewed main-branch repair workflow. The workflow patches the remaining Mixar widget API mismatches, handles `SPACE_AGENT_BUBBLE` explicitly, runs the expanded stale-API audit, and starts exact-SHA Windows validation.

A follow-up synchronize event captures the repair and audit workflow results so any automation failure can be diagnosed and corrected without waiting for another compiler log.

The source repair is applied on `main`. This synchronization reruns the audit after fixing its commit/rebase ordering, then dispatches the full Windows build if the report has zero blocking hits.
