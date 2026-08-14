<!--
SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited

SPDX-License-Identifier: GPL-3.0-or-later
-->

# Windows installer (.exe)

Upstream Mixar has no packaging target: `build.bat` produces a runnable tree in
`build\<MIXAR_ENV>\bin` and stops there. This fork adds a packaging step that
turns that tree into two artifacts:

| Artifact | What it is |
| --- | --- |
| `dist\Mixar-<version>-windows-x64-setup.exe` | NSIS installer: Program Files install, shortcuts, Add/Remove Programs entry, uninstaller |
| `dist\Mixar-<version>-windows-x64.zip` | Portable build - unzip and run `mixar.exe` |
| `dist\SHA256SUMS.txt` | SHA-256 of everything produced |

## Prerequisites

- Windows 10/11 x64
- Visual Studio 2022 with the **Desktop development with C++** workload
- CMake 3.16+ (Ninja optional but much faster; VS ships one)
- Git with Git LFS
- [NSIS 3](https://nsis.sourceforge.io) for the installer
  (`winget install NSIS.NSIS` or `choco install nsis -y`)
- **~60 GB free disk** and a few hours for the first build. Blender's
  precompiled library set alone is tens of GB.

## Build and package

```bat
git clone --recurse-submodules https://github.com/aimcrazyxx/mixar-app.git
cd mixar-app
git checkout feat/custom-endpoints

REM Blender 5.2.0 for the upstream tree
git -C upstream fetch --tags origin v5.2.0
git -C upstream checkout --force --detach v5.2.0

copy .env.example .env
scripts\windows\init.bat      REM submodule + Blender libraries (slow)
scripts\windows\build.bat     REM compile (slow)
scripts\windows\install.bat   REM overlay Mixar scripts into the bundle
scripts\windows\package.bat   REM -> dist\
```

`init.bat` re-checks out the submodule at the revision recorded in the parent
repo, so run it **before** pinning `upstream` to `v5.2.0` (or re-pin and rerun
`make update` inside `upstream` afterwards).

## Packaging options

`scripts\windows\package.bat` forwards everything to
`scripts/packaging/make_windows_installer.py`:

| Flag | Effect |
| --- | --- |
| `--suffix a1b2c3d` | Tag artifact names, e.g. with a commit sha |
| `--backend-url URL` | Regenerate the bundled `config\mixar.json` for another backend before packaging |
| `--no-zip` / `--no-installer` | Produce only one of the two artifacts |
| `--payload-dir DIR` | Package a tree from a non-default location |
| `--allow-missing-nsis` | Produce the zip and warn instead of failing when NSIS is absent |
| `--skip-overlay-check` | Package even if this fork's modules are missing from the bundle |
| `--sign --pfx cert.pfx` | Sign payload and installer with `signtool` (password read from `MIXAR_SIGN_PASSWORD`, never from the command line) |

Safety checks that run every time:

- the executable and the `<X.Y>` resource directory must exist;
- `config\mixar.json` is reported (environment, version, backend URL);
- packaging **aborts** if that config carries a `dev_bypass` block, so a Dev
  build with plaintext credentials cannot be shipped by accident;
- `endpoints.py` and the BYOK `base_url` modules must be present, so an
  installer can never silently ship without the custom base URL feature.

## CI

`.github/workflows/build-windows.yml` does all of the above on a Windows runner
and uploads the artifacts. GitHub-hosted runners have roughly 14 GB of free
disk, which is not enough for a Blender build, so register a self-hosted
Windows runner and pass its label in the `runner` input.

## Signing and SmartScreen

An unsigned installer triggers *Windows protected your PC*: click **More info ->
Run anyway**. To avoid it, sign with a real code-signing certificate
(`--sign --pfx`); reputation still takes time to build up with a fresh
certificate.

## Uninstalling

Settings -> Apps, or `"C:\Program Files\Mixar\Uninstall.exe"`. Silent:
`Uninstall.exe /S`. The uninstaller refuses to recurse into a directory that
does not contain `mixar.exe`, and asks before deleting your settings in
`%APPDATA%\Mixar` (custom endpoints and BYOK base URL live there).
