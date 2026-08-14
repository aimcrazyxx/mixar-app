REM SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
REM
REM SPDX-License-Identifier: GPL-3.0-or-later

@echo off
setlocal enabledelayedexpansion

REM Mixar Packaging Script for Windows
REM Turns the tree built by build.bat + install.bat into:
REM   dist\Mixar-<version>-windows-x64.zip        (portable)
REM   dist\Mixar-<version>-windows-x64-setup.exe  (NSIS installer)
REM
REM Usage:
REM   scripts\windows\package.bat
REM   scripts\windows\package.bat --suffix a1b2c3d --no-zip
REM   scripts\windows\package.bat --backend-url https://api.example.com
REM Extra arguments are forwarded to scripts/packaging/make_windows_installer.py.

set "SCRIPT_DIR=%~dp0"
call "%SCRIPT_DIR%settings.bat"
if %ERRORLEVEL% neq 0 (
    echo Error: Failed to load settings
    exit /b 1
)

set "PACKAGER=%ROOT_DIR%\scripts\packaging\make_windows_installer.py"
if not exist "%PACKAGER%" (
    echo Error: packager not found: %PACKAGER%
    exit /b 1
)

set "COMMON_ARGS=--env "%MIXAR_ENV%" --blender-version "%BLENDER_VERSION%""

REM Prefer the Python that ships inside the build (matches PYTHON_VERSION exactly).
set "EMBEDDED_PY=%BUILD_DIR%\%MIXAR_ENV%\bin\%BLENDER_VERSION%\python\bin\python.exe"

if exist "%EMBEDDED_PY%" (
    echo Using embedded Python: %EMBEDDED_PY%
    "%EMBEDDED_PY%" "%PACKAGER%" %COMMON_ARGS% %*
    goto :finished
)

where py >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo Using launcher Python: py -3
    py -3 "%PACKAGER%" %COMMON_ARGS% %*
    goto :finished
)

where python >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo Using Python from PATH
    python "%PACKAGER%" %COMMON_ARGS% %*
    goto :finished
)

echo Error: no Python interpreter found. Build first ^(scripts\windows\build.bat^)
echo        or install Python 3 from https://www.python.org/downloads/
exit /b 1

:finished
set "RC=%ERRORLEVEL%"
if not "%RC%"=="0" (
    echo Error: packaging failed with exit code %RC%
    exit /b %RC%
)
echo Packaging complete. Artifacts are in: %ROOT_DIR%\dist
exit /b 0
