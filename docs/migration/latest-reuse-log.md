<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# REUSE lint failure

```text
REUSE lint	REUSE Compliance Check	﻿2026-08-15T22:59:09.3307851Z ##[group]Run fsfe/reuse-action@v5
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:09.3308161Z ##[endgroup]
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:09.3399529Z ##[command]/usr/bin/docker run --name a8d0003067ca3cb1c84eba976d46e253c7ce7d_b94098 --label a8d000 --workdir /github/workspace --rm -e "HOME" -e "GITHUB_JOB" -e "GITHUB_REF" -e "GITHUB_SHA" -e "GITHUB_REPOSITORY" -e "GITHUB_REPOSITORY_OWNER" -e "GITHUB_REPOSITORY_OWNER_ID" -e "GITHUB_RUN_ID" -e "GITHUB_RUN_NUMBER" -e "GITHUB_RETENTION_DAYS" -e "GITHUB_RUN_ATTEMPT" -e "GITHUB_ACTOR_ID" -e "GITHUB_ACTOR" -e "GITHUB_WORKFLOW" -e "GITHUB_HEAD_REF" -e "GITHUB_BASE_REF" -e "GITHUB_EVENT_NAME" -e "GITHUB_SERVER_URL" -e "GITHUB_API_URL" -e "GITHUB_GRAPHQL_URL" -e "GITHUB_REF_NAME" -e "GITHUB_REF_PROTECTED" -e "GITHUB_REF_TYPE" -e "GITHUB_WORKFLOW_REF" -e "GITHUB_WORKFLOW_SHA" -e "GITHUB_REPOSITORY_ID" -e "GITHUB_TRIGGERING_ACTOR" -e "GITHUB_WORKSPACE" -e "GITHUB_ACTION" -e "GITHUB_EVENT_PATH" -e "GITHUB_ACTION_REPOSITORY" -e "GITHUB_ACTION_REF" -e "GITHUB_PATH" -e "GITHUB_ENV" -e "GITHUB_STEP_SUMMARY" -e "GITHUB_STATE" -e "GITHUB_OUTPUT" -e "GITHUB_ARTIFACTS" -e "GITHUB_ARTIFACTS_LIST" -e "RUNNER_OS" -e "RUNNER_ARCH" -e "RUNNER_NAME" -e "RUNNER_ENVIRONMENT" -e "RUNNER_TOOL_CACHE" -e "RUNNER_TEMP" -e "RUNNER_WORKSPACE" -e "ACTIONS_RUNTIME_URL" -e "ACTIONS_RUNTIME_TOKEN" -e "ACTIONS_CACHE_URL" -e "ACTIONS_RESULTS_URL" -e "ACTIONS_ORCHESTRATION_ID" -e GITHUB_ACTIONS=true -e CI=true -v "/var/run/docker.sock":"/var/run/docker.sock" -v "/home/runner/work/_temp":"/github/runner_temp" -v "/home/runner/work/_temp/_github_home":"/github/home" -v "/home/runner/work/_temp/_github_workflow":"/github/workflow" -v "/home/runner/work/_temp/_runner_file_commands":"/github/file_commands" -v "/home/runner/work/mixar-app/mixar-app":"/github/workspace" a8d000:3067ca3cb1c84eba976d46e253c7ce7d
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:11.8544488Z reuse.extract - ERROR - Could not parse 'GPL-3.0-or-later\n" + body + "\n"'
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:11.8545895Z reuse.extract - ERROR - '.github/workflows/prepare-blender-workflow-edits.yml' holds an SPDX expression that cannot be parsed, skipping the file
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1447062Z # MISSING COPYRIGHT AND LICENSING INFORMATION
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1447512Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1447826Z The following files have no copyright and licensing information:
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1448488Z * .github/workflows/prepare-blender-workflow-edits.yml
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1448882Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1449084Z The following files have no copyright information:
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1449596Z * .github/action-log-trigger.md
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1451184Z * .github/blender-52-finalize-trigger.md
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1451747Z * .github/prepare-workflow-edits-trigger.md
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1452686Z * .github/workflows/capture-finalizer-log.yml
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1453230Z * .github/workflows/finalize-blender-52.yml
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1453592Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1453722Z # SUMMARY
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1453906Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1454038Z * Bad licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1454398Z * Deprecated licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1454816Z * Licenses without file extension: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1455289Z * Missing licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1455745Z * Unused licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1456379Z * Used licenses: GPL-2.0-or-later, LicenseRef-Mixar-Brand, Apache-2.0, GPL-3.0-or-later
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1457095Z * Read errors: 0
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1457496Z * Files with copyright information: 1771 / 1777
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1458018Z * Files with license information: 1776 / 1777
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1458367Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1458894Z Unfortunately, your project is not compliant with version 3.3 of the REUSE Specification :-(
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1459520Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1459562Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1459974Z # RECOMMENDATIONS
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1460489Z 
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1461132Z * Fix missing copyright/licensing information: For one or more files, the tool
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1462481Z   cannot find copyright and/or licensing information. You typically do this by
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1463731Z   adding 'SPDX-FileCopyrightText' and 'SPDX-License-Identifier' tags to each
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1465212Z   file. The tutorial explains additional ways to do this:
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1466122Z   <https://reuse.software/tutorial/>
REUSE lint	REUSE Compliance Check	2026-08-15T22:59:12.1466660Z 
```
