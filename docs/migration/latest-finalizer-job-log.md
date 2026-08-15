# Failed Blender finalizer job log

```text
finalize	Run finalizer in durable stages	﻿2026-08-15T22:50:15.0318965Z ##[group]Run set -euo pipefail
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0319660Z ^[[36;1mset -euo pipefail^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0320304Z ^[[36;1mgit config user.name github-actions[bot]^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0321245Z ^[[36;1mgit config user.email 41898282+github-actions[bot]@users.noreply.github.com^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0327178Z ^[[36;1mcheckpoint() {^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0327623Z ^[[36;1m  printf '%s\n' "$1" > docs/migration/finalize-blender-52-stage.txt^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0328064Z ^[[36;1m  git add -A^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0328409Z ^[[36;1m  git commit -m "ci: Blender 5.2 stage - $1" || true^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0329055Z ^[[36;1m  git push origin HEAD:refs/heads/migration/blender-5.2^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0329589Z ^[[36;1m}^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0329843Z ^[[36;1mrun_stage() {^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0330115Z ^[[36;1m  name=$1^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0330395Z ^[[36;1m  set +e^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0330861Z ^[[36;1m  python3 scripts/upgrade/run_finalize_stage.py "$name" > /tmp/stage.log 2>&1^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0331381Z ^[[36;1m  rc=$?^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0332015Z ^[[36;1m  set -e^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0332383Z ^[[36;1m  if [ "$rc" -ne 0 ]; then^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0333653Z ^[[36;1m    { echo '# Blender 5.2 finalization failure'; echo; echo "Run: $GITHUB_RUN_ID"; echo "Stage: $name"; echo '```text'; cat /tmp/stage.log; echo '```'; } > docs/migration/finalize-blender-52-failure.md^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0334572Z ^[[36;1m    checkpoint "$name-failed"^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0335020Z ^[[36;1m    exit "$rc"^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0335287Z ^[[36;1m  fi^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0335537Z ^[[36;1m  checkpoint "$name"^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0335816Z ^[[36;1m}^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0336065Z ^[[36;1mrun_stage sync_python^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0336373Z ^[[36;1mrun_stage wire_provider^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0336684Z ^[[36;1mrun_stage port_cpp^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0336984Z ^[[36;1mrun_stage fix_checks^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0337278Z ^[[36;1mrun_stage guidance^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0337597Z ^[[36;1mpython3 -m pip install -q pytest^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0338243Z ^[[36;1mpython3 -m pytest -q tests/test_byok_base_url.py tests/test_byok_custom_provider.py tests/test_byok_openai_models.py^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0338865Z ^[[36;1m! grep -RIl '^<<<<<<< ' src^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0339424Z ^[[36;1mrm -f docs/migration/finalize-blender-52-failure.md docs/migration/finalize-blender-52-stage.txt^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0340016Z ^[[36;1mcheckpoint tests-passed^[[0m
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0460440Z shell: /usr/bin/bash -e {0}
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0460851Z env:
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0461205Z   pythonLocation: /opt/hostedtoolcache/Python/3.13.15/x64
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0462087Z   PKG_CONFIG_PATH: /opt/hostedtoolcache/Python/3.13.15/x64/lib/pkgconfig
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0462619Z   Python_ROOT_DIR: /opt/hostedtoolcache/Python/3.13.15/x64
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0463078Z   Python2_ROOT_DIR: /opt/hostedtoolcache/Python/3.13.15/x64
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0463529Z   Python3_ROOT_DIR: /opt/hostedtoolcache/Python/3.13.15/x64
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0463981Z   LD_LIBRARY_PATH: /opt/hostedtoolcache/Python/3.13.15/x64/lib
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.0464414Z ##[endgroup]
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.5503642Z warning: in the working copy of 'scripts/windows/settings.bat', LF will be replaced by CRLF the next time Git touches it
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.8417918Z [migration/blender-5.2 8be584f] ci: Blender 5.2 stage - sync_python
finalize	Run finalizer in durable stages	2026-08-15T22:50:15.8419183Z  5 files changed, 5 insertions(+), 5 deletions(-)
finalize	Run finalizer in durable stages	2026-08-15T22:50:16.8228509Z To https://github.com/aimcrazyxx/mixar-app
finalize	Run finalizer in durable stages	2026-08-15T22:50:16.8229887Z  ! [remote rejected] HEAD -> migration/blender-5.2 (refusing to allow a GitHub App to create or update workflow `.github/workflows/build-windows.yml` without `workflows` permission)
finalize	Run finalizer in durable stages	2026-08-15T22:50:16.8231006Z error: failed to push some refs to 'https://github.com/aimcrazyxx/mixar-app'
finalize	Run finalizer in durable stages	2026-08-15T22:50:16.8256048Z ##[error]Process completed with exit code 1.
```
