<!-- SPDX-FileCopyrightText: 2026 Mixar fork contributors -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# REUSE lint failure

```text
REUSE lint	REUSE Compliance Check	﻿2026-08-15T23:01:44.3223495Z ##[group]Run fsfe/reuse-action@v5
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:44.3223799Z ##[endgroup]
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:44.3315736Z ##[command]/usr/bin/docker run --name fecb4edfc9b0047314c378935afdcfe5c1c71_de3f70 --label 4fecb4 --workdir /github/workspace --rm -e "HOME" -e "GITHUB_JOB" -e "GITHUB_REF" -e "GITHUB_SHA" -e "GITHUB_REPOSITORY" -e "GITHUB_REPOSITORY_OWNER" -e "GITHUB_REPOSITORY_OWNER_ID" -e "GITHUB_RUN_ID" -e "GITHUB_RUN_NUMBER" -e "GITHUB_RETENTION_DAYS" -e "GITHUB_RUN_ATTEMPT" -e "GITHUB_ACTOR_ID" -e "GITHUB_ACTOR" -e "GITHUB_WORKFLOW" -e "GITHUB_HEAD_REF" -e "GITHUB_BASE_REF" -e "GITHUB_EVENT_NAME" -e "GITHUB_SERVER_URL" -e "GITHUB_API_URL" -e "GITHUB_GRAPHQL_URL" -e "GITHUB_REF_NAME" -e "GITHUB_REF_PROTECTED" -e "GITHUB_REF_TYPE" -e "GITHUB_WORKFLOW_REF" -e "GITHUB_WORKFLOW_SHA" -e "GITHUB_REPOSITORY_ID" -e "GITHUB_TRIGGERING_ACTOR" -e "GITHUB_WORKSPACE" -e "GITHUB_ACTION" -e "GITHUB_EVENT_PATH" -e "GITHUB_ACTION_REPOSITORY" -e "GITHUB_ACTION_REF" -e "GITHUB_PATH" -e "GITHUB_ENV" -e "GITHUB_STEP_SUMMARY" -e "GITHUB_STATE" -e "GITHUB_OUTPUT" -e "GITHUB_ARTIFACTS" -e "GITHUB_ARTIFACTS_LIST" -e "RUNNER_OS" -e "RUNNER_ARCH" -e "RUNNER_NAME" -e "RUNNER_ENVIRONMENT" -e "RUNNER_TOOL_CACHE" -e "RUNNER_TEMP" -e "RUNNER_WORKSPACE" -e "ACTIONS_RUNTIME_URL" -e "ACTIONS_RUNTIME_TOKEN" -e "ACTIONS_CACHE_URL" -e "ACTIONS_RESULTS_URL" -e "ACTIONS_ORCHESTRATION_ID" -e GITHUB_ACTIONS=true -e CI=true -v "/var/run/docker.sock":"/var/run/docker.sock" -v "/home/runner/work/_temp":"/github/runner_temp" -v "/home/runner/work/_temp/_github_home":"/github/home" -v "/home/runner/work/_temp/_github_workflow":"/github/workflow" -v "/home/runner/work/_temp/_runner_file_commands":"/github/file_commands" -v "/home/runner/work/mixar-app/mixar-app":"/github/workspace" 4fecb4:edfc9b0047314c378935afdcfe5c1c71
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.3874820Z reuse.extract - ERROR - Could not parse 'GPL-3.0-or-later -->'; echo; echo '# REUSE lint failure'; echo; echo '```text'; tail -n 250 /tmp/reuse.log; echo '```'; } > docs/migration/latest-reuse-log.md'
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.3877317Z reuse.extract - ERROR - '.github/workflows/capture-finalizer-log.yml' holds an SPDX expression that cannot be parsed, skipping the file
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6288163Z # MISSING COPYRIGHT AND LICENSING INFORMATION
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6289415Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6289781Z The following files have no copyright and licensing information:
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6290430Z * .github/workflows/capture-finalizer-log.yml
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6290772Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6290890Z # SUMMARY
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6291057Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6291175Z * Bad licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6291483Z * Deprecated licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6292295Z * Licenses without file extension: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6292723Z * Missing licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6293073Z * Unused licenses: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6293683Z * Used licenses: Apache-2.0, GPL-3.0-or-later, GPL-2.0-or-later, LicenseRef-Mixar-Brand
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6294396Z * Read errors: 0
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6294798Z * Files with copyright information: 1773 / 1774
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6295355Z * Files with license information: 1773 / 1774
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6295731Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6296194Z Unfortunately, your project is not compliant with version 3.3 of the REUSE Specification :-(
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6296835Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6296881Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6297035Z # RECOMMENDATIONS
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6297257Z 
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6297641Z * Fix missing copyright/licensing information: For one or more files, the tool
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6299021Z   cannot find copyright and/or licensing information. You typically do this by
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6299980Z   adding 'SPDX-FileCopyrightText' and 'SPDX-License-Identifier' tags to each
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6300826Z   file. The tutorial explains additional ways to do this:
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6301434Z   <https://reuse.software/tutorial/>
REUSE lint	REUSE Compliance Check	2026-08-15T23:01:47.6301766Z 
```
