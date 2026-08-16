REM SPDX-FileCopyrightText: 2026 Mixar fork contributors
REM SPDX-License-Identifier: GPL-3.0-or-later

@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo ============================================================
echo Mixar Blender 5.2 Windows C++ preflight
echo ============================================================

set "SCRIPT_DIR=%~dp0"
call "%SCRIPT_DIR%settings.bat"
if errorlevel 1 (
  echo Error: failed to load settings.bat
  exit /b 1
)

REM Keep this build isolated from the production build. The goal is to prove
REM that Mixar-owned C/C++ compiles against the pinned Blender API before a
REM multi-hour full build is allowed to start.
set "PREFLIGHT_BUILD_DIR=%BUILD_DIR%\Preflight-Blender52"

if not defined BUILD_CORES set "BUILD_CORES=2"
if %BUILD_CORES% LSS 2 set "BUILD_CORES=2"

echo Source      : %SOURCE_DIR%
echo Build       : %PREFLIGHT_BUILD_DIR%
echo Parallelism : %BUILD_CORES%
echo.

REM The exact tree CMake will compile must be generated first. overlay.bat also
REM applies the Blender 5.2 compatibility migrations and static source audit.
echo [1/7] Preparing and auditing exact Blender 5.2 overlay...
call "%SCRIPT_DIR%overlay.bat"
if errorlevel 1 (
  echo Error: overlay/static compatibility preflight failed
  exit /b 1
)

REM Initialize the same MSVC x64 environment used by build.bat.
echo [2/7] Initializing Visual Studio C++ toolchain...
set "VCVARSALL="
set "VSWHERE=%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe"
if exist "!VSWHERE!" (
  for /f "usebackq delims=" %%I in (`"!VSWHERE!" -latest -products * -requires Microsoft.VisualStudio.Component.VC.Tools.x86.x64 -property installationPath 2^>nul`) do (
    if exist "%%I\VC\Auxiliary\Build\vcvarsall.bat" set "VCVARSALL=%%I\VC\Auxiliary\Build\vcvarsall.bat"
  )
)
if not defined VCVARSALL (
  for %%Y in (2026 2022) do (
    for %%E in (Community Professional Enterprise BuildTools) do (
      if not defined VCVARSALL if exist "%ProgramFiles%\Microsoft Visual Studio\%%Y\%%E\VC\Auxiliary\Build\vcvarsall.bat" set "VCVARSALL=%ProgramFiles%\Microsoft Visual Studio\%%Y\%%E\VC\Auxiliary\Build\vcvarsall.bat"
      if not defined VCVARSALL if exist "%ProgramFiles(x86)%\Microsoft Visual Studio\%%Y\%%E\VC\Auxiliary\Build\vcvarsall.bat" set "VCVARSALL=%ProgramFiles(x86)%\Microsoft Visual Studio\%%Y\%%E\VC\Auxiliary\Build\vcvarsall.bat"
    )
  )
)
if not defined VCVARSALL (
  echo Error: Visual Studio C++ toolchain not found
  exit /b 1
)
call "!VCVARSALL!" x64
if errorlevel 1 (
  echo Error: vcvarsall failed
  exit /b 1
)

where ninja >nul 2>&1
if errorlevel 1 (
  echo Error: Ninja not found on PATH
  exit /b 1
)

REM Configure a lean validation graph. GPU kernels and the installer are not
REM relevant to C++ API compatibility, so disable Cycles/CUDA/OptiX here.
echo [3/7] Configuring lean Ninja validation graph...
if not exist "%PREFLIGHT_BUILD_DIR%" mkdir "%PREFLIGHT_BUILD_DIR%"
cmake -C "%CMAKE_DIR%\mixar_overrides.cmake" ^
  -G Ninja ^
  -S "%SOURCE_DIR%" ^
  -B "%PREFLIGHT_BUILD_DIR%" ^
  -DCMAKE_BUILD_TYPE=Release ^
  -DWITH_WINDOWS_RELEASE_PDB=OFF ^
  -DCMAKE_EXPORT_COMPILE_COMMANDS=ON ^
  -DWITH_CYCLES=OFF ^
  -DWITH_CYCLES_DEVICE_CUDA=OFF ^
  -DWITH_CYCLES_CUDA_BINARIES=OFF ^
  -DWITH_CYCLES_DEVICE_OPTIX=OFF
if errorlevel 1 (
  echo Error: CMake preflight configure failed
  exit /b 1
)

REM Compile the exact target that has repeatedly failed late first.
echo [4/7] Compiling bf_editor_interface...
cmake --build "%PREFLIGHT_BUILD_DIR%" --target bf_editor_interface -- -j%BUILD_CORES%
if errorlevel 1 (
  echo Error: bf_editor_interface preflight failed
  exit /b 1
)

REM These targets contain additional Mixar overlays in upstream Blender editor
REM subsystems. Run them before the broad space graph so failures stay local.
echo [5/7] Compiling modified core editor targets...
for %%T in (bf_editor_animation bf_editor_screen bf_editor_sculpt_paint) do (
  echo   - %%T
  cmake --build "%PREFLIGHT_BUILD_DIR%" --target %%T -- -j%BUILD_CORES%
  if errorlevel 1 (
    echo Error: %%T preflight failed
    exit /b 1
  )
)

REM bf_editor_space_api links every Mixar custom space (Mixie, Chat, Agent
REM Bubble, Layers, Properties, Assets, Baking and Texture Sets). Building it
REM forces those custom C++ libraries and their shared dependencies to compile.
echo [6/7] Compiling complete Mixar editor-space dependency graph...
cmake --build "%PREFLIGHT_BUILD_DIR%" --target bf_editor_space_api -- -j%BUILD_CORES%
if errorlevel 1 (
  echo Error: bf_editor_space_api preflight failed
  exit /b 1
)

echo [7/7] Windows C++ preflight PASSED.
echo The known Mixar Blender 5.2 C/C++ surface compiled successfully.
exit /b 0
