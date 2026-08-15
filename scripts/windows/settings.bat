REM SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
REM
REM SPDX-License-Identifier: GPL-2.0-or-later

@echo off
REM Mixar Application Settings for Windows
REM Source this file in batch scripts that need these settings
REM
REM Configuration priority:
REM   1. Environment variables (already set, e.g. from CI)
REM   2. .env file in repo root (local dev overrides)
REM   3. Hardcoded defaults below

REM Get the root directory relative to this settings.bat script
for %%i in ("%~dp0..\..") do set "ROOT_DIR=%%~fi"

REM Load .env if it exists (local dev overrides)
if exist "%ROOT_DIR%\.env" (
    for /f "usebackq eol=# tokens=1,* delims==" %%a in ("%ROOT_DIR%\.env") do (
        if not "%%a"=="" if not "%%b"=="" (
            REM Only set if not already defined (env vars take priority)
            if not defined %%a set "%%a=%%b"
        )
    )
)

REM Version always comes from VERSION file (canonical source)
if not defined MIXAR_VERSION (
    if exist "%ROOT_DIR%\VERSION" (
        set /p MIXAR_VERSION=<"%ROOT_DIR%\VERSION"
    ) else (
        set "MIXAR_VERSION=0.0.0"
    )
)

REM Core environment settings (env var > .env > default)
if not defined MIXAR_ENV set "MIXAR_ENV=Prod"
if not defined MIXAR_BACKEND_URL set "MIXAR_BACKEND_URL=https://api.mixar.app"
if not defined MIXAR_FRONTEND_URL set "MIXAR_FRONTEND_URL=https://www.mixar.app"

REM App info (constants)
if not defined MIXAR_VERSION_PATCH set "MIXAR_VERSION_PATCH=0"
if not defined MIXAR_APP_NAME set "MIXAR_APP_NAME=Mixar"
if not defined MIXAR_EXECUTABLE_NAME set "MIXAR_EXECUTABLE_NAME=mixar"
if not defined MIXAR_DESCRIPTION set "MIXAR_DESCRIPTION=AI Native 3D Content Creation Software"
if not defined MIXAR_VENDOR set "MIXAR_VENDOR=Mixar"
if not defined MIXAR_WEBSITE set "MIXAR_WEBSITE=https://mixar.app"

REM Bundle settings (constants)
if not defined MIXAR_BUNDLE_IDENTIFIER set "MIXAR_BUNDLE_IDENTIFIER=com.mixar.mixar"
if not defined MIXAR_BUNDLE_COPYRIGHT set "MIXAR_BUNDLE_COPYRIGHT=© 2025 Mixar"

REM Build settings (constants)
REM Keep BLENDER_VERSION in sync with the pinned upstream\ submodule revision.
REM Use scripts/upgrade/set_blender_version.sh to change both at once.
if not defined BLENDER_VERSION set "BLENDER_VERSION=5.2"
if not defined PYTHON_VERSION set "PYTHON_VERSION=3.11"
if not defined REQUIRED_CMAKE_VERSION set "REQUIRED_CMAKE_VERSION=3.16"

REM Windows-specific build settings
set "BLENDER_BUILD_TYPE=Release"

REM Directory Structure
set "BUILD_DIR=%ROOT_DIR%\build"
set "SOURCE_DIR=%ROOT_DIR%\source"
set "SRC_DIR=%ROOT_DIR%\src"
set "CMAKE_DIR=%ROOT_DIR%\cmake"

REM Upstream Blender tree (multi-GB, gitignored). Linked git worktrees don't
REM carry ignored files, so fall back to the main checkout's upstream\ (the
REM overlay only reads from it). Mirrors scripts/unix/settings.sh.
if defined MIXAR_UPSTREAM_DIR (
    set "UPSTREAM_DIR=%MIXAR_UPSTREAM_DIR%"
) else (
    set "UPSTREAM_DIR=%ROOT_DIR%\upstream"
    if not exist "%ROOT_DIR%\upstream\CMakeLists.txt" (
        for /f "usebackq delims=" %%g in (`git -C "%ROOT_DIR%" rev-parse --path-format=absolute --git-common-dir 2^>nul`) do (
            for %%m in ("%%g\..") do (
                if exist "%%~fm\upstream\CMakeLists.txt" (
                    set "UPSTREAM_DIR=%%~fm\upstream"
                    echo Worktree checkout: sharing upstream from main checkout: %%~fm\upstream 1>&2
                )
            )
        )
    )
)

REM Platform-specific settings
set "PLATFORM=Windows"

REM Get number of CPU cores (Windows) - Reserve 2 cores for system
set /a "DEFAULT_CORES=%NUMBER_OF_PROCESSORS%-2"
if %DEFAULT_CORES% LEQ 2 set "DEFAULT_CORES=2"

REM Build optimization - Use BUILD_CORES if set, otherwise use DEFAULT_CORES
if not defined BUILD_CORES (
    set "BUILD_CORES=%DEFAULT_CORES%"
) else (
    echo Using custom BUILD_CORES: %BUILD_CORES%
)

REM Normalize BUILD_WITH_NINJA before anything branches on it.
REM
REM Every script here asks `if defined BUILD_WITH_NINJA`, and `if defined` is
REM true for the string "0" - so passing BUILD_WITH_NINJA=0 (what CI sends for
REM use_ninja=false) selected Ninja anyway and the Visual Studio path was
REM unreachable. Clearing the variable for the falsey spellings makes all of
REM those existing checks correct without having to touch each script.
if /i "%BUILD_WITH_NINJA%"=="0" set "BUILD_WITH_NINJA="
if /i "%BUILD_WITH_NINJA%"=="false" set "BUILD_WITH_NINJA="
if /i "%BUILD_WITH_NINJA%"=="no" set "BUILD_WITH_NINJA="
if /i "%BUILD_WITH_NINJA%"=="off" set "BUILD_WITH_NINJA="

REM Windows-specific build settings - Select generator based on BUILD_WITH_NINJA
if defined BUILD_WITH_NINJA (
    set "CMAKE_GENERATOR_ARGS=-G Ninja"
    set "BUILD_ARGS=--parallel %BUILD_CORES%"
    goto :generator_selected
)

REM Visual Studio generator - multi-config, creates Debug/Release folders.
REM The version used to be hardcoded to "Visual Studio 17 2022", which fails
REM immediately on a machine that only has a newer Visual Studio installed -
REM including the CI runner, which ships VS2026. Ask vswhere what is actually
REM there and map its major version to the matching generator name.
set "VS_GENERATOR=Visual Studio 17 2022"
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "%VSWHERE%" call :detect_vs_generator
set "CMAKE_GENERATOR_ARGS=-G "%VS_GENERATOR%" -A x64"
set "BUILD_ARGS=--parallel %BUILD_CORES% --verbose -- /m:%BUILD_CORES%"

:generator_selected
exit /b 0

REM Kept as a subroutine on purpose: settings.bat is called by scripts that run
REM with delayed expansion disabled, so a value read inside a parenthesised
REM block cannot be used within that same block. A subroutine sidesteps it.
:detect_vs_generator
for /f "usebackq tokens=1 delims=." %%v in (`"%VSWHERE%" -latest -products * -property catalog_productDisplayVersion 2^>nul`) do (
    if "%%v"=="18" set "VS_GENERATOR=Visual Studio 18 2026"
    if "%%v"=="17" set "VS_GENERATOR=Visual Studio 17 2022"
    if "%%v"=="16" set "VS_GENERATOR=Visual Studio 16 2019"
)
exit /b 0
