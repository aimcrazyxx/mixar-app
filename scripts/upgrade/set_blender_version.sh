#!/bin/bash
# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Move the pinned upstream Blender submodule to another release and keep the
# BLENDER_VERSION build constant in sync, in one idempotent step.
#
# Usage:
#   bash scripts/upgrade/set_blender_version.sh                 # 5.2 / v5.2.0
#   bash scripts/upgrade/set_blender_version.sh 5.2 v5.2.0      # explicit ref
#   bash scripts/upgrade/set_blender_version.sh 5.2 blender-v5.2-release
#   SKIP_CHECKOUT=1 bash scripts/upgrade/set_blender_version.sh 5.2
#     ^ only sync the version constants (use after
#       scripts/upgrade/checkout_upstream.py has moved upstream/ already)
#
# Why this is a local step: a submodule pointer is a gitlink, and the GitHub
# API can only write file blobs. The pin therefore cannot be changed from a
# web/API-only workflow.

set -euo pipefail

VERSION="${1:-5.2}"
REF="${2:-v${VERSION}.0}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$ROOT_DIR"

if [ "${SKIP_CHECKOUT:-0}" != "1" ]; then
    if [ ! -e upstream/.git ] && [ ! -f upstream/CMakeLists.txt ]; then
        echo "error: upstream/ is not populated yet." >&2
        echo "       run: git submodule update --init upstream" >&2
        exit 1
    fi

    echo "==> Fetching $REF into upstream/"
    git -C upstream fetch --tags origin "$REF" 2>/dev/null \
        || git -C upstream fetch --tags origin

    if git -C upstream rev-parse --verify --quiet "refs/tags/${REF}^{commit}" >/dev/null; then
        TARGET="refs/tags/$REF"
    elif git -C upstream rev-parse --verify --quiet "refs/remotes/origin/${REF}" >/dev/null; then
        TARGET="refs/remotes/origin/$REF"
    elif git -C upstream rev-parse --verify --quiet "${REF}^{commit}" >/dev/null; then
        TARGET="$REF"
    else
        echo "error: could not resolve '$REF' in the upstream Blender remote." >&2
        echo "       try a release branch instead, e.g. blender-v${VERSION}-release" >&2
        exit 1
    fi

    echo "==> Checking out $TARGET"
    git -C upstream checkout --detach "$TARGET"
    git -C upstream submodule update --init --recursive || true
fi

echo "==> Syncing BLENDER_VERSION to $VERSION"
python3 - "$VERSION" <<'PY'
import re
import sys

version = sys.argv[1]
edits = (
    ("scripts/unix/settings.sh", r"(BLENDER_VERSION:-)[0-9]+\.[0-9]+"),
    ("scripts/windows/settings.bat", r"(BLENDER_VERSION=)[0-9]+\.[0-9]+"),
)
for path, pattern in edits:
    with open(path, encoding="utf-8") as handle:
        text = handle.read()
    patched = re.sub(pattern, lambda match: match.group(1) + version, text)
    if patched == text:
        print("    unchanged {0}".format(path))
        continue
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(patched)
    print("    updated   {0}".format(path))
PY

git add scripts/unix/settings.sh scripts/windows/settings.bat
if [ "${SKIP_CHECKOUT:-0}" != "1" ]; then
    git add upstream
fi

PINNED="$(git -C upstream rev-parse HEAD 2>/dev/null || echo unknown)"
echo ""
echo "Staged. upstream/ is now at: $PINNED"
echo "Next steps:"
echo "  git commit -m \"build: bump upstream Blender to ${VERSION}\""
echo "  make init && make build"
echo ""
echo "Reminder: verify PYTHON_VERSION in scripts/unix/settings.sh still matches"
echo "          upstream/build_files/build_environment/cmake/versions.cmake"
