# Blender 5.2 finalization failure

```text
Collecting pytest
  Downloading pytest-9.1.1-py3-none-any.whl.metadata (7.6 kB)
Collecting iniconfig>=1.0.1 (from pytest)
  Downloading iniconfig-2.3.0-py3-none-any.whl.metadata (2.5 kB)
Collecting packaging>=22 (from pytest)
  Downloading packaging-26.3-py3-none-any.whl.metadata (3.5 kB)
Collecting pluggy<2,>=1.5 (from pytest)
  Downloading pluggy-1.6.0-py3-none-any.whl.metadata (4.8 kB)
Collecting pygments>=2.7.2 (from pytest)
  Downloading pygments-2.20.0-py3-none-any.whl.metadata (2.5 kB)
Downloading pytest-9.1.1-py3-none-any.whl (386 kB)
Downloading pluggy-1.6.0-py3-none-any.whl (20 kB)
Downloading iniconfig-2.3.0-py3-none-any.whl (7.5 kB)
Downloading packaging-26.3-py3-none-any.whl (129 kB)
Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 70.7 MB/s  0:00:00
Installing collected packages: pygments, pluggy, packaging, iniconfig, pytest

Successfully installed iniconfig-2.3.0 packaging-26.3 pluggy-1.6.0 pygments-2.20.0 pytest-9.1.1
Submodule 'upstream' (https://projects.blender.org/blender/blender.git) registered for path 'upstream'
Cloning into '/home/runner/work/mixar-app/mixar-app/upstream'...
From https://projects.blender.org/blender/blender
 * branch              f52ba4dcdf5f669c1bc57f39a0e056be30d3ab60 -> FETCH_HEAD
Submodule path 'upstream': checked out 'f52ba4dcdf5f669c1bc57f39a0e056be30d3ab60'
From https://projects.blender.org/blender/blender
 * [new tag]           v5.2.0     -> v5.2.0
Warning: you are leaving 1 commit behind, not connected to
any of your branches:

  f52ba4dc Fix #150131: Selection state of edit bone root/tip not preserved

If you want to keep it by creating a new branch, this may be a good time
to do so with:

 git branch <new-branch-name> f52ba4dc

HEAD is now at fbe62287 Release: Bump to 5.2.0 release
Traceback (most recent call last):
  File "/home/runner/work/mixar-app/mixar-app/scripts/upgrade/finalize_blender_52.py", line 199, in <module>
    main()
    ~~~~^^
  File "/home/runner/work/mixar-app/mixar-app/scripts/upgrade/finalize_blender_52.py", line 193, in main
    fix_checks()
    ~~~~~~~~~~^^
  File "/home/runner/work/mixar-app/mixar-app/scripts/upgrade/finalize_blender_52.py", line 145, in fix_checks
    raise RuntimeError(f"Packaging compile anchor missing: {anchor}")
RuntimeError: Packaging compile anchor missing: operators/byok_custom_provider_ops.py
```
