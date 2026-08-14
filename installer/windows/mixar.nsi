; SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
;
; SPDX-License-Identifier: GPL-3.0-or-later
;
; NSIS installer for Mixar (Windows x64).
;
; This script never hardcodes the build layout: every path, name and version
; arrives as a /D define from scripts/packaging/make_windows_installer.py.
; Build it by hand with:
;
;   makensis /DPAYLOAD_DIR=C:\path\to\build\Prod\bin ^
;            /DOUT_FILE=C:\path\to\dist\Mixar-setup.exe ^
;            /DAPP_VERSION=2.0.0 /DAPP_VERSION_FULL=2.0.0.0 ^
;            installer\windows\mixar.nsi
;
; The POSIX build of makensis (apt-get install nsis) works too - switches take
; a dash there, and PAYLOAD_GLOB has to be passed because a backslash is not a
; path separator on Linux or macOS:
;
;   makensis -DPAYLOAD_DIR=/path/bin -DPAYLOAD_GLOB='/path/bin/*' ... mixar.nsi

Unicode true
ManifestDPIAware true
SetCompressor /SOLID lzma

!include "MUI2.nsh"
!include "LogicLib.nsh"
!include "FileFunc.nsh"
!include "x64.nsh"

; ---------------------------------------------------------------- defines ---

!ifndef PAYLOAD_DIR
  !error "PAYLOAD_DIR is required, e.g. /DPAYLOAD_DIR=build\Prod\bin"
!endif
!ifndef PAYLOAD_GLOB
  ; make_windows_installer.py joins this with the separator of the platform
  ; that runs makensis. The fallback keeps hand-written Windows invocations
  ; working unchanged.
  !define PAYLOAD_GLOB "${PAYLOAD_DIR}\*"
!endif
!ifndef OUT_FILE
  !define OUT_FILE "Mixar-setup.exe"
!endif
!ifndef APP_NAME
  !define APP_NAME "Mixar"
!endif
!ifndef APP_EXE
  !define APP_EXE "mixar.exe"
!endif
!ifndef APP_VERSION
  !define APP_VERSION "0.0.0"
!endif
!ifndef APP_VERSION_FULL
  !define APP_VERSION_FULL "0.0.0.0"
!endif
!ifndef APP_PUBLISHER
  !define APP_PUBLISHER "Mixar"
!endif
!ifndef APP_URL
  !define APP_URL "https://mixar.app"
!endif
!ifndef APP_ENV
  !define APP_ENV "Prod"
!endif
!ifndef UNINST_KEY
  !define UNINST_KEY "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
!endif

Name "${APP_NAME} ${APP_VERSION}"
OutFile "${OUT_FILE}"
InstallDir "$PROGRAMFILES64\${APP_NAME}"
InstallDirRegKey HKLM "Software\${APP_NAME}" "InstallDir"
RequestExecutionLevel admin
BrandingText "${APP_NAME} ${APP_VERSION} (${APP_ENV})"
ShowInstDetails show
ShowUnInstDetails show

VIProductVersion "${APP_VERSION_FULL}"
VIAddVersionKey "ProductName" "${APP_NAME}"
VIAddVersionKey "ProductVersion" "${APP_VERSION}"
VIAddVersionKey "FileVersion" "${APP_VERSION_FULL}"
VIAddVersionKey "FileDescription" "${APP_NAME} setup"
VIAddVersionKey "CompanyName" "${APP_PUBLISHER}"
VIAddVersionKey "LegalCopyright" "${APP_PUBLISHER}"

; ------------------------------------------------------------------- pages ---

!ifdef APP_ICON
  !define MUI_ICON "${APP_ICON}"
  !define MUI_UNICON "${APP_ICON}"
!endif

!define MUI_ABORTWARNING
!define MUI_COMPONENTSPAGE_SMALLDESC
!define MUI_FINISHPAGE_NOAUTOCLOSE
!define MUI_FINISHPAGE_RUN
!define MUI_FINISHPAGE_RUN_FUNCTION LaunchApp
!define MUI_FINISHPAGE_RUN_TEXT "Run ${APP_NAME} now"
!define MUI_FINISHPAGE_LINK "${APP_URL}"
!define MUI_FINISHPAGE_LINK_LOCATION "${APP_URL}"
!define MUI_LANGDLL_REGISTRY_ROOT HKLM
!define MUI_LANGDLL_REGISTRY_KEY "Software\${APP_NAME}"
!define MUI_LANGDLL_REGISTRY_VALUENAME "InstallerLanguage"

!insertmacro MUI_PAGE_WELCOME
!ifdef LICENSE_FILE
  !insertmacro MUI_PAGE_LICENSE "${LICENSE_FILE}"
!endif
!insertmacro MUI_PAGE_COMPONENTS
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"
!insertmacro MUI_LANGUAGE "PortugueseBR"

; ---------------------------------------------------------------- sections ---

; Keep the exclusion list in sync with EXCLUDE_NAMES / EXCLUDE_SUFFIXES in
; scripts/packaging/make_windows_installer.py so the zip and the installer
; ship exactly the same files.
Section "${APP_NAME} (required)" SecCore
  SectionIn RO
  SetOutPath "$INSTDIR"
  SetOverwrite on
  File /r /x "*.pdb" /x "*.ilk" /x "*.exp" /x "*.obj" /x "__pycache__" /x "CMakeFiles" "${PAYLOAD_GLOB}"

  WriteRegStr HKLM "Software\${APP_NAME}" "InstallDir" "$INSTDIR"
  WriteRegStr HKLM "Software\${APP_NAME}" "Version" "${APP_VERSION}"
  WriteRegStr HKLM "Software\${APP_NAME}" "Environment" "${APP_ENV}"

  WriteUninstaller "$INSTDIR\Uninstall.exe"

  WriteRegStr HKLM "${UNINST_KEY}" "DisplayName" "${APP_NAME} ${APP_VERSION}"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayVersion" "${APP_VERSION}"
  WriteRegStr HKLM "${UNINST_KEY}" "DisplayIcon" "$INSTDIR\${APP_EXE},0"
  WriteRegStr HKLM "${UNINST_KEY}" "Publisher" "${APP_PUBLISHER}"
  WriteRegStr HKLM "${UNINST_KEY}" "URLInfoAbout" "${APP_URL}"
  WriteRegStr HKLM "${UNINST_KEY}" "InstallLocation" "$INSTDIR"
  WriteRegStr HKLM "${UNINST_KEY}" "UninstallString" "$\"$INSTDIR\Uninstall.exe$\""
  WriteRegStr HKLM "${UNINST_KEY}" "QuietUninstallString" "$\"$INSTDIR\Uninstall.exe$\" /S"
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoModify" 1
  WriteRegDWORD HKLM "${UNINST_KEY}" "NoRepair" 1

  ${GetSize} "$INSTDIR" "/S=0K" $0 $1 $2
  IntFmt $0 "0x%08X" $0
  WriteRegDWORD HKLM "${UNINST_KEY}" "EstimatedSize" "$0"
SectionEnd

Section "Start Menu shortcut" SecStartMenu
  CreateDirectory "$SMPROGRAMS\${APP_NAME}"
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}" "" "$INSTDIR\${APP_EXE}" 0
  CreateShortCut "$SMPROGRAMS\${APP_NAME}\Uninstall ${APP_NAME}.lnk" "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Desktop shortcut" SecDesktop
  CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${APP_EXE}" "" "$INSTDIR\${APP_EXE}" 0
SectionEnd

!insertmacro MUI_FUNCTION_DESCRIPTION_BEGIN
  !insertmacro MUI_DESCRIPTION_TEXT ${SecCore} "${APP_NAME} ${APP_VERSION} and its runtime files (required)."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecStartMenu} "Add ${APP_NAME} to the Start Menu."
  !insertmacro MUI_DESCRIPTION_TEXT ${SecDesktop} "Add a ${APP_NAME} shortcut to the Desktop."
!insertmacro MUI_FUNCTION_DESCRIPTION_END

; --------------------------------------------------------------- functions ---

Function LaunchApp
  ; Launch through explorer.exe so the app runs as the logged-in user instead
  ; of inheriting the installer's elevated token.
  Exec '"$WINDIR\explorer.exe" "$INSTDIR\${APP_EXE}"'
FunctionEnd

Function .onInit
  ${IfNot} ${RunningX64}
    MessageBox MB_OK|MB_ICONSTOP "${APP_NAME} requires 64-bit Windows."
    Abort
  ${EndIf}
  SetRegView 64

  !insertmacro MUI_LANGDLL_DISPLAY

  ReadRegStr $R0 HKLM "${UNINST_KEY}" "UninstallString"
  ${If} $R0 != ""
  ${AndIfNot} ${Silent}
    MessageBox MB_YESNO|MB_ICONQUESTION \
      "Another ${APP_NAME} installation was found.$\n$\nRemove it before installing ${APP_VERSION}?" \
      IDNO skip_previous
    ReadRegStr $R1 HKLM "Software\${APP_NAME}" "InstallDir"
    ${If} $R1 == ""
      StrCpy $R1 "$INSTDIR"
    ${EndIf}
    ExecWait '$R0 /S _?=$R1'
    skip_previous:
  ${EndIf}
FunctionEnd

Function un.onInit
  SetRegView 64
  !insertmacro MUI_UNGETLANGUAGE
FunctionEnd

Section "Uninstall"
  SetRegView 64

  Delete "$DESKTOP\${APP_NAME}.lnk"
  Delete "$SMPROGRAMS\${APP_NAME}\${APP_NAME}.lnk"
  Delete "$SMPROGRAMS\${APP_NAME}\Uninstall ${APP_NAME}.lnk"
  RMDir "$SMPROGRAMS\${APP_NAME}"

  ; Only ever recurse into a directory that actually looks like a Mixar
  ; install, so a bad InstallDir value can't take a user's data with it.
  ${If} ${FileExists} "$INSTDIR\${APP_EXE}"
    Delete "$INSTDIR\Uninstall.exe"
    RMDir /r "$INSTDIR"
  ${Else}
    MessageBox MB_OK|MB_ICONEXCLAMATION \
      "$INSTDIR does not look like a ${APP_NAME} installation, so no files were removed."
  ${EndIf}

  DeleteRegKey HKLM "${UNINST_KEY}"
  DeleteRegKey HKLM "Software\${APP_NAME}"

  ${IfNot} ${Silent}
    MessageBox MB_YESNO|MB_ICONQUESTION \
      "Also delete your ${APP_NAME} settings and custom endpoints?" \
      IDNO keep_user_data
    RMDir /r "$APPDATA\${APP_NAME}"
    keep_user_data:
  ${EndIf}
SectionEnd
