REM SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
REM
REM SPDX-License-Identifier: GPL-2.0-or-later

@echo off
setlocal enabledelayedexpansion

REM Load all settings from settings.bat
set "SCRIPT_DIR=%~dp0"
call "%SCRIPT_DIR%\settings.bat"
if %errorlevel% neq 0 (
    echo Failed to load settings
    exit /b 1
)

REM Incremental overlay: only copy files newer than destination (preserves timestamps for
REM unchanged files so Ninja skips them). build_clean.bat handles full wipes when needed.
if not exist "%SOURCE_DIR%" mkdir "%SOURCE_DIR%"

REM Multi-threaded robocopy: set ROBOCOPY_THREADS env var to control thread count.
REM Default: 8 threads. CI can set higher (e.g. 32) for faster copies on large instances.
if not defined ROBOCOPY_THREADS set "ROBOCOPY_THREADS=8"

echo Copying upstream to source (threads: %ROBOCOPY_THREADS%)...
REM /E   = copy subdirectories including empty ones
REM /XO  = eXclude Older: skip destination files that are the same age or newer than source
REM /XD  = exclude directories  /XF = exclude files
REM /MT  = multi-threaded copy
REM
REM Do NOT duplicate Blender's multi-GB Windows dependency checkout into source/.
REM It is exposed below through a directory junction instead. This also guarantees that
REM CMake sees the exact pinned LFS checkout at source/lib/windows_x64.
robocopy "%UPSTREAM_DIR%" "%SOURCE_DIR%" /E /XO /MT:%ROBOCOPY_THREADS% ^
    /XD ".git" ".github" ".vscode" ".idea" ".gitea" "%UPSTREAM_DIR%\lib\windows_x64" ^
    /XF ".gitignore" ".gitmodules" ".gitattributes" ".gitkeep" ^
    /R:3 /W:1 /NFL /NDL /NJH /NJS /nc /ns /np

REM robocopy returns 0-7 for success, 8+ for errors
if %errorlevel% geq 8 (
    echo Error copying upstream to source
    exit /b 1
)

REM Blender's Windows CMake files require dependencies specifically at
REM SOURCE_DIR\lib\windows_x64. The dependency repository is intentionally kept under
REM UPSTREAM_DIR so it remains pinned to Blender and is not copied twice.
if not exist "%UPSTREAM_DIR%\lib\windows_x64" (
    echo Error: Blender Windows precompiled libraries are missing at:
    echo   %UPSTREAM_DIR%\lib\windows_x64
    echo Initialize the pinned lib/windows_x64 submodule before running the build.
    exit /b 1
)

if not exist "%SOURCE_DIR%\lib" mkdir "%SOURCE_DIR%\lib"
if not exist "%SOURCE_DIR%\lib\windows_x64" (
    echo Linking Windows precompiled libraries into overlay source...
    mklink /J "%SOURCE_DIR%\lib\windows_x64" "%UPSTREAM_DIR%\lib\windows_x64" >nul
    if !errorlevel! neq 0 (
        echo Error: Failed to create source\lib\windows_x64 junction
        exit /b 1
    )
)

if not exist "%SOURCE_DIR%\lib\windows_x64" (
    echo Error: source\lib\windows_x64 is unavailable after overlay preparation
    exit /b 1
)

echo Windows precompiled libraries ready: %SOURCE_DIR%\lib\windows_x64

echo Overlaying Mixar sources onto source...
REM NO /XO here: Mixar src files must ALWAYS win over upstream, regardless of timestamps.
REM After a git pull, upstream files get newer timestamps than src/ files,
REM so /XO would wrongly skip the Mixar overlay, leaving the raw upstream version.
REM Without /XO, robocopy copies src files when timestamps differ (first run after pull),
REM then skips on subsequent runs when timestamps stabilize (Ninja sees no change).
robocopy "%SRC_DIR%" "%SOURCE_DIR%" /E /MT:%ROBOCOPY_THREADS% /R:3 /W:1 /NFL /NDL /NJH /NJS /nc /ns /np
REM robocopy returns 0-7 for success
if %errorlevel% geq 8 (
    echo Error overlaying Mixar sources
    exit /b 1
)

REM src/ should not replace/remove the dependency junction, but validate again so any
REM future overlay change fails here with a clear message instead of deep inside CMake.
if not exist "%SOURCE_DIR%\lib\windows_x64" (
    echo Error: Mixar overlay removed source\lib\windows_x64
    exit /b 1
)

echo Overlay complete.
exit /b 0
