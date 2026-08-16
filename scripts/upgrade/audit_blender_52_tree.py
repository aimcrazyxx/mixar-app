# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later

"""Fast static preflight for the Mixar Blender 5.2 overlay.

The goal is to catch deterministic source problems before a multi-thousand-file
Windows compile: stale Blender UI APIs, merge markers, unbalanced C/C++
preprocessor conditionals, and Python syntax errors.

Two modes are supported:

* normal (default): scan the final, already-patched ``source`` tree and require
  every compatibility migration to be complete.
* ``--repository-mode``: scan ``src`` immediately after checkout. The known
  compatibility fragments intentionally rewritten by patch_blender_52_build.py
  are treated as migration debt; everything else is held to the same rules.
  The known malformed toolbar block is normalized in memory so the structural
  checker can continue looking for unrelated preprocessor damage.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from pathlib import Path
import re
import sys


CPP_SUFFIXES = {".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx", ".inl"}
TEXT_SUFFIXES = CPP_SUFFIXES | {".cmake", ".txt"}

KNOWN_MIGRATION_FILES = {
    "source/blender/editors/interface/interface_layout.cc",
    "source/blender/editors/interface/interface_mixar_section.cc",
    "source/blender/editors/interface/interface_mixar_section.hh",
    "source/blender/editors/interface/interface_widgets.cc",
    "source/blender/editors/space_agent_bubble/space_agent_bubble.cc",
}

# Patterns already encountered during the 5.2 migration plus the broader API
# families that were removed/renamed between the fork's old Blender base and
# Blender 5.2. Keep these intentionally explicit: a hit should be actionable.
STALE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("legacy uiLayout type", re.compile(r"\buiLayout\b")),
    ("legacy uiBut type", re.compile(r"\buiBut\b")),
    ("legacy uiBlock type", re.compile(r"\buiBlock\b")),
    ("legacy ButType enum", re.compile(r"\bButType::")),
    ("legacy uiTextEdit type", re.compile(r"\buiTextEdit\b")),
    ("legacy uiWidgetStateInfo type", re.compile(r"\buiWidgetStateInfo\b")),
    ("legacy but_placeholder_get", re.compile(r"\bbut_placeholder_get\b")),
    ("legacy UI_style_get", re.compile(r"\bUI_style_get\b")),
    ("legacy ui_fontscale", re.compile(r"\bui_fontscale\b")),
    ("legacy UI_fontstyle_set", re.compile(r"\bUI_fontstyle_set\b")),
    ("legacy ui_block_to_window", re.compile(r"\bui_block_to_window(?:_fl)?\b")),
    ("legacy ui_window_to_block", re.compile(r"\bui_window_to_block(?:_fl)?\b")),
    ("legacy ui_but_text_password_hide", re.compile(r"\bui_but_text_password_hide\b")),
    ("legacy UI_draw_roundbox_corner_set", re.compile(r"\bUI_draw_roundbox_corner_set\b")),
    ("legacy UI_draw_roundbox_4fv", re.compile(r"\bUI_draw_roundbox_4fv\b")),
    ("legacy UI_widgetbase_draw_cache_flush", re.compile(r"\bUI_widgetbase_draw_cache_flush\b")),
    ("legacy UI_CNR constant", re.compile(r"\bUI_CNR_[A-Z0-9_]+\b")),
    ("old WM_operator_properties_create_ptr arity", re.compile(r"WM_operator_properties_create_ptr\s*\(\s*&")),
    ("removed absolute_block call", re.compile(r"\babsolute_block\s*\(")),
    ("obsolete fmtlib target", re.compile(r"\bbf::extern::fmtlib\b")),
    ("direct ghostwin access", re.compile(r"(?<!runtime)->ghostwin\b")),
    ("obsolete typed MEM_callocN", re.compile(r"\bMEM_callocN\s*<")),
    ("legacy uiPopupMenu type", re.compile(r"\buiPopupMenu\b")),
    ("legacy uiPopupBlockHandle type", re.compile(r"\buiPopupBlockHandle\b")),
    ("uppercase legacy UI block/button/popup API", re.compile(r"\bUI_(?:block|but|popup)_[A-Za-z0-9_]+\b")),
    ("old UI button constant", re.compile(r"\bUI_BUT_[A-Z0-9_]+\b")),
    ("old UI block constant", re.compile(r"\bUI_BLOCK_[A-Z0-9_]+\b")),
    ("old Block::buttons access", re.compile(r"\bblock->buttons(?:\.|\[)")),
    ("old tooltip drawflag helper", re.compile(r"\bbut_drawflag_enable\s*\(")),
    ("old UI_GetTheme accessor", re.compile(r"\bUI_GetTheme\s*\(")),
    ("old region uiblocks aspect path", re.compile(r"BLI_listbase_is_empty\s*\(\s*&region->runtime->uiblocks")),
)

MERGE_MARKER = re.compile(r"^\s*(?:<<<<<<<\s|=======\s*$|>>>>>>>\s)")
DIRECTIVE = re.compile(r"^\s*#\s*(if|ifdef|ifndef|elif|else|endif)\b")

MALFORMED_WIDGETS = """#ifdef USE_UI_TOOLBAR_HACK
        else if ((but->icon != ICON_NONE) && but_is_tool(but)) {
          wt = widget_type(WidgetStyle::ToolbarItem);
        }
#endif
        else {
          wt = widget_type(WidgetStyle::Exec);
        }
#else
        wt = widget_type(WidgetStyle::Exec);
#endif
"""
CORRECTED_WIDGETS = """#ifdef USE_UI_TOOLBAR_HACK
        else if ((but->icon != ICON_NONE) && but_is_tool(but)) {
          wt = widget_type(WidgetStyle::ToolbarItem);
        }
#endif
        else {
          wt = widget_type(WidgetStyle::Exec);
        }
"""


@dataclass
class Conditional:
    line: int
    kind: str
    seen_else: bool = False


def iter_manifest_paths(root: Path, manifest_root: Path | None) -> list[Path]:
    """Return files to inspect in *root*, optionally limited to overlay-owned paths."""
    if manifest_root is None:
        return sorted(path for path in root.rglob("*") if path.is_file())

    paths: list[Path] = []
    for source_path in manifest_root.rglob("*"):
        if not source_path.is_file():
            continue
        relative = source_path.relative_to(manifest_root)
        candidate = root / relative
        if not candidate.is_file():
            raise RuntimeError(f"overlay lost manifest file: {relative}")
        paths.append(candidate)
    return sorted(paths)


def strip_comments_for_directive(line: str, in_block_comment: bool) -> tuple[str, bool]:
    """Strip comments sufficiently to decide whether a line contains a directive."""
    out: list[str] = []
    i = 0
    while i < len(line):
        if in_block_comment:
            end = line.find("*/", i)
            if end == -1:
                return "".join(out), True
            in_block_comment = False
            i = end + 2
            continue
        if line.startswith("/*", i):
            in_block_comment = True
            i += 2
            continue
        if line.startswith("//", i):
            break
        out.append(line[i])
        i += 1
    return "".join(out), in_block_comment


def normalize_repository_text(relative: str, text: str) -> str:
    if relative == "source/blender/editors/interface/interface_widgets.cc":
        if MALFORMED_WIDGETS in text:
            return text.replace(MALFORMED_WIDGETS, CORRECTED_WIDGETS, 1)
    return text


def check_preprocessor(relative: str, text: str, errors: list[str]) -> None:
    stack: list[Conditional] = []
    in_block_comment = False
    for number, raw_line in enumerate(text.splitlines(), 1):
        line, in_block_comment = strip_comments_for_directive(raw_line, in_block_comment)
        match = DIRECTIVE.match(line)
        if not match:
            continue
        directive = match.group(1)
        if directive in {"if", "ifdef", "ifndef"}:
            stack.append(Conditional(number, directive))
        elif directive == "elif":
            if not stack:
                errors.append(f"{relative}:{number}: orphan #elif")
            elif stack[-1].seen_else:
                errors.append(f"{relative}:{number}: #elif after #else opened at line {stack[-1].line}")
        elif directive == "else":
            if not stack:
                errors.append(f"{relative}:{number}: orphan #else")
            elif stack[-1].seen_else:
                errors.append(f"{relative}:{number}: duplicate #else for conditional opened at line {stack[-1].line}")
            else:
                stack[-1].seen_else = True
        elif directive == "endif":
            if not stack:
                errors.append(f"{relative}:{number}: orphan #endif")
            else:
                stack.pop()
    for item in stack:
        errors.append(f"{relative}:{item.line}: unterminated #{item.kind}")


def check_stale_apis(relative: str, text: str, errors: list[str]) -> None:
    for label, pattern in STALE_PATTERNS:
        for number, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                errors.append(f"{relative}:{number}: {label}: {line.strip()}")


def check_text(relative: str, text: str, errors: list[str]) -> None:
    for number, line in enumerate(text.splitlines(), 1):
        if MERGE_MARKER.match(line):
            errors.append(f"{relative}:{number}: unresolved merge marker: {line.strip()}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="tree containing files to audit")
    parser.add_argument(
        "--manifest-root",
        type=Path,
        help="only audit paths represented by this overlay/manifest tree",
    )
    parser.add_argument(
        "--repository-mode",
        action="store_true",
        help="scan src before the known compatibility patch is applied",
    )
    args = parser.parse_args()

    root = args.root.resolve()
    manifest_root = args.manifest_root.resolve() if args.manifest_root else None
    if not root.is_dir():
        raise SystemExit(f"audit root does not exist: {root}")
    if manifest_root is not None and not manifest_root.is_dir():
        raise SystemExit(f"manifest root does not exist: {manifest_root}")

    errors: list[str] = []
    checked = 0
    cpp_checked = 0
    python_checked = 0

    for path in iter_manifest_paths(root, manifest_root):
        relative = path.relative_to(root).as_posix()
        suffix = path.suffix.lower()
        name = path.name

        if suffix in TEXT_SUFFIXES or name == "CMakeLists.txt":
            text = path.read_text(encoding="utf-8", errors="replace")
            if args.repository_mode:
                text = normalize_repository_text(relative, text)
            check_text(relative, text, errors)
            checked += 1

            if suffix in CPP_SUFFIXES:
                check_preprocessor(relative, text, errors)
                cpp_checked += 1

            skip_known_api_debt = args.repository_mode and relative in KNOWN_MIGRATION_FILES
            if not skip_known_api_debt:
                check_stale_apis(relative, text, errors)

        elif suffix == ".py":
            try:
                ast.parse(path.read_text(encoding="utf-8", errors="strict"), filename=relative)
            except (SyntaxError, UnicodeError) as exc:
                line = getattr(exc, "lineno", "?")
                errors.append(f"{relative}:{line}: Python syntax/encoding error: {exc}")
            python_checked += 1
            checked += 1

    # Project-specific invariants that a regex-only scan can miss.
    anim = root / "source/blender/editors/animation/anim_filter.cc"
    if anim.is_file() and "case SPACE_AGENT_BUBBLE:" not in anim.read_text(encoding="utf-8", errors="replace"):
        errors.append("source/blender/editors/animation/anim_filter.cc: missing SPACE_AGENT_BUBBLE switch coverage")

    if not args.repository_mode:
        header = root / "source/blender/editors/interface/interface_mixar_section.hh"
        if header.is_file():
            header_text = header.read_text(encoding="utf-8", errors="replace")
            if "namespace blender {\nstruct ARegion;" not in header_text:
                errors.append("source/blender/editors/interface/interface_mixar_section.hh: missing blender::ARegion forward declaration")
            if "UI_panel_category_draw_all_mixar(::blender::ARegion *region" not in header_text:
                errors.append("source/blender/editors/interface/interface_mixar_section.hh: stale ARegion function signature")

    print(
        f"Blender 5.2 audit: {checked} files checked "
        f"({cpp_checked} C/C++ preprocessor trees, {python_checked} Python files)"
    )
    if args.repository_mode:
        print(f"Known migration debt exempted in {len(KNOWN_MIGRATION_FILES)} compatibility file(s).")

    if errors:
        print(f"ERROR: {len(errors)} preflight problem(s) found:", file=sys.stderr)
        for error in errors[:300]:
            print(f"  - {error}", file=sys.stderr)
        if len(errors) > 300:
            print(f"  - ... {len(errors) - 300} more", file=sys.stderr)
        return 1

    print("Blender 5.2 audit clean.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
