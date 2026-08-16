# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

# This file is loaded *before* any project() call.
# Keep CI-safe defaults here; scripts/windows/build.bat exports CUDA/OptiX
# environment variables before CMake is invoked when those SDKs are available.

# Only set CMP0167 policy if it's available (CMake 3.30+).
if(POLICY CMP0167)
  cmake_policy(SET CMP0167 OLD)
endif()

# Windows/MSVC: base compiler flags.
if(CMAKE_HOST_WIN32)
  set(CMAKE_CXX_FLAGS "/DWIN32 /D_WINDOWS /W3 /GR /EHsc" CACHE STRING "C++ compiler flags" FORCE)
  set(CMAKE_C_FLAGS "/DWIN32 /D_WINDOWS /W3" CACHE STRING "C compiler flags" FORCE)
endif()

# CUDA must never be forced ON on a machine without nvcc. Forcing
# WITH_CYCLES_CUDA_BINARIES=ON with an empty CUDA_VERSION makes Blender's
# Cycles CMake logic evaluate an invalid expression such as `if(EQUAL 8.0)`.
set(_MIXAR_HAS_CUDA OFF)
if(DEFINED ENV{CUDA_PATH} AND EXISTS "$ENV{CUDA_PATH}/bin/nvcc.exe")
  set(_MIXAR_HAS_CUDA ON)
endif()

if(_MIXAR_HAS_CUDA)
  message(STATUS "Mixar: CUDA toolkit detected at $ENV{CUDA_PATH}")
  set(WITH_CYCLES_DEVICE_CUDA ON CACHE BOOL "Enable Cycles NVIDIA CUDA compute support" FORCE)
  set(WITH_CYCLES_CUDA_BINARIES ON CACHE BOOL "Build Cycles NVIDIA CUDA binaries" FORCE)
  set(WITH_CUDA_DYNLOAD ON CACHE BOOL "Dynamically load CUDA libraries at runtime" FORCE)
else()
  message(STATUS "Mixar: CUDA toolkit not detected; disabling CUDA binaries for this build")
  set(WITH_CYCLES_DEVICE_CUDA OFF CACHE BOOL "Enable Cycles NVIDIA CUDA compute support" FORCE)
  set(WITH_CYCLES_CUDA_BINARIES OFF CACHE BOOL "Build Cycles NVIDIA CUDA binaries" FORCE)
  set(WITH_CUDA_DYNLOAD ON CACHE BOOL "Dynamically load CUDA libraries at runtime" FORCE)
endif()

# OptiX SDK is optional as well. Only enable it when build.bat has exported a
# valid OPTIX_ROOT_DIR containing the SDK header.
if(DEFINED ENV{OPTIX_ROOT_DIR} AND EXISTS "$ENV{OPTIX_ROOT_DIR}/include/optix.h")
  message(STATUS "Mixar: OptiX SDK detected at $ENV{OPTIX_ROOT_DIR}")
  set(WITH_CYCLES_DEVICE_OPTIX ON CACHE BOOL "Enable Cycles NVIDIA OptiX support" FORCE)
else()
  message(STATUS "Mixar: OptiX SDK not detected; disabling OptiX for this build")
  set(WITH_CYCLES_DEVICE_OPTIX OFF CACHE BOOL "Enable Cycles NVIDIA OptiX support" FORCE)
endif()

unset(_MIXAR_HAS_CUDA)

# sccache compiler launcher - auto-enabled when sccache is on PATH.
# On Windows, Blender's platform_win32.cmake handles /Z7 and compiler launcher
# when WITH_WINDOWS_SCCACHE is ON. On other platforms, set the launcher directly.
find_program(SCCACHE_PROGRAM sccache)
if(SCCACHE_PROGRAM)
  message(STATUS "sccache found: ${SCCACHE_PROGRAM}")
  if(CMAKE_HOST_WIN32)
    set(WITH_WINDOWS_SCCACHE ON CACHE BOOL "" FORCE)
  else()
    set(CMAKE_C_COMPILER_LAUNCHER "${SCCACHE_PROGRAM}" CACHE STRING "" FORCE)
    set(CMAKE_CXX_COMPILER_LAUNCHER "${SCCACHE_PROGRAM}" CACHE STRING "" FORCE)
  endif()
else()
  message(STATUS "sccache not found - building without compiler cache")
endif()
