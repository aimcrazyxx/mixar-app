# SPDX-FileCopyrightText: 2026 Mixar fork contributors
# SPDX-License-Identifier: GPL-3.0-or-later

r"""Remove Python invalid-escape SyntaxWarnings from the generated build tree.

Python historically preserved unknown escapes such as ``\]`` and ``\.`` in
ordinary string literals, but modern Python emits ``SyntaxWarning`` for them
(and future versions may make them errors).  Regex-heavy Blender/Mixar code has
several of these.

The transformation here is semantics-preserving: an unknown source escape
``\]`` is rewritten as ``\\]``.  Both evaluate to the same two runtime
characters (backslash + closing bracket), but the latter is valid Python.

Only ordinary STRING tokens are touched. Raw strings and f-strings are left
alone, and known Python escapes are preserved exactly. The script operates on
the generated ``source/`` tree, so upstream submodules remain untouched.
"""

from __future__ import annotations

import argparse
import io
import re
import sys
import tokenize
import warnings
from pathlib import Path

_STRING_START_RE = re.compile(r"(?is)^([rubf]*)(\"\"\"|'''|\"|')")
_VALID_SINGLE_ESCAPES = frozenset("\\'\"abfnrtv")
_VALID_PREFIX_ESCAPES = frozenset("xuUN")
_VALID_OCTAL = frozenset("01234567")


def _fix_literal(literal: str) -> tuple[str, int]:
    """Return ``(rewritten_literal, invalid_escape_count)``."""
    match = _STRING_START_RE.match(literal)
    if not match:
        return literal, 0

    prefix = match.group(1)
    quote = match.group(2)
    lowered = prefix.lower()
    if "r" in lowered or "f" in lowered:
        return literal, 0

    start = len(prefix) + len(quote)
    if not literal.endswith(quote):
        return literal, 0
    end = len(literal) - len(quote)
    if end < start:
        return literal, 0

    body = literal[start:end]
    out: list[str] = []
    fixed = 0
    index = 0

    while index < len(body):
        char = body[index]
        if char != "\\":
            out.append(char)
            index += 1
            continue

        if index + 1 >= len(body):
            out.append(char)
            index += 1
            continue

        nxt = body[index + 1]
        if (
            nxt in _VALID_SINGLE_ESCAPES
            or nxt in _VALID_OCTAL
            or nxt in _VALID_PREFIX_ESCAPES
        ):
            out.extend(("\\", nxt))
            index += 2
            continue

        # Backslash-newline is a valid line continuation.
        if nxt in "\r\n":
            out.extend(("\\", nxt))
            index += 2
            if nxt == "\r" and index < len(body) and body[index] == "\n":
                out.append("\n")
                index += 1
            continue

        # Unknown escapes are currently preserved by Python at runtime. Doubling
        # only the source backslash keeps that exact runtime value while making
        # the spelling unambiguous to the parser.
        out.extend(("\\\\", nxt))
        fixed += 1
        index += 2

    if not fixed:
        return literal, 0
    return prefix + quote + "".join(out) + quote, fixed


def _line_offsets(text: str) -> list[int]:
    offsets = [0]
    for line in text.splitlines(keepends=True):
        offsets.append(offsets[-1] + len(line))
    return offsets


def _fix_source(text: str, filename: str) -> tuple[str, int, int]:
    """Rewrite invalid escapes in STRING tokens without reformatting the file."""
    offsets = _line_offsets(text)
    replacements: list[tuple[int, int, str]] = []
    literals = 0
    escapes = 0

    try:
        tokens = tokenize.generate_tokens(io.StringIO(text).readline)
        for token in tokens:
            if token.type != tokenize.STRING:
                continue
            rewritten, count = _fix_literal(token.string)
            if not count:
                continue
            start = offsets[token.start[0] - 1] + token.start[1]
            end = offsets[token.end[0] - 1] + token.end[1]
            replacements.append((start, end, rewritten))
            literals += 1
            escapes += count
    except (IndentationError, tokenize.TokenError) as exc:
        raise RuntimeError(f"Could not tokenize {filename}: {exc}") from exc

    for start, end, rewritten in reversed(replacements):
        text = text[:start] + rewritten + text[end:]
    return text, literals, escapes


def _decode_python(path: Path) -> tuple[str, str]:
    data = path.read_bytes()
    try:
        encoding, _ = tokenize.detect_encoding(io.BytesIO(data).readline)
    except SyntaxError as exc:
        raise RuntimeError(f"Could not detect encoding for {path}: {exc}") from exc
    try:
        return data.decode(encoding), encoding
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"Could not decode {path} as {encoding}: {exc}") from exc


def _verify_no_syntax_warning(text: str, path: Path) -> None:
    with warnings.catch_warnings():
        warnings.simplefilter("error", SyntaxWarning)
        compile(text, str(path), "exec", dont_inherit=True)


def fix_tree(root: Path) -> tuple[int, int, int]:
    files_changed = 0
    literals_changed = 0
    escapes_changed = 0

    for path in sorted(root.rglob("*.py")):
        if any(part in {".git", "__pycache__"} for part in path.parts):
            continue
        text, encoding = _decode_python(path)
        rewritten, literals, escapes = _fix_source(text, str(path))
        if not escapes:
            continue

        # Prove the rewritten file parses cleanly before replacing it.
        _verify_no_syntax_warning(rewritten, path)
        path.write_bytes(rewritten.encode(encoding))
        files_changed += 1
        literals_changed += literals
        escapes_changed += escapes
        print(
            f"fixed invalid Python escapes: {path.relative_to(root)} "
            f"({literals} literals, {escapes} escapes)"
        )

    return files_changed, literals_changed, escapes_changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path, help="Generated Blender/Mixar source tree")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        parser.error(f"source root does not exist: {root}")

    try:
        files, literals, escapes = fix_tree(root)
    except Exception as exc:  # noqa: BLE001 - build must fail with context
        print(f"Python invalid-escape cleanup failed: {exc}", file=sys.stderr)
        return 1

    print(
        "Python escape cleanup complete: "
        f"{files} files, {literals} literals, {escapes} invalid escapes fixed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
