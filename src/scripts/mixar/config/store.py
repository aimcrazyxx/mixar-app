# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Config store: layered, thread-safe, crash-safe replacement helpers.

Upstream ``config.py`` loads ``<app>/config/mixar.json`` lazily into a module
global and, on ``add_config()``, rewrites that same file inside the installed
application directory. Three problems with that:

* **Lost settings on update** - the bundle's ``config`` folder is regenerated
  by every build/install, so user preferences are wiped.
* **Read-only / signed bundles** - on macOS the app payload is code-signed and
  on Linux/Windows it may be installed root-only, so the write either fails or
  invalidates the signature.
* **Truncated JSON** - the file is opened with ``"w"`` and written in place, so
  a crash mid-write leaves an unparseable config.

This module keeps the exact same public API (``get_config``, ``add_config``,
``load_mixar_config``, ``get_config_path``) but splits storage into two layers:
the read-only bundled defaults, and a writable user layer stored next to the
other Blender user config. Writes are atomic and lock-protected.
"""

from __future__ import annotations

import json
import os
import threading

from .endpoints import atomic_write_json, user_config_dir
from .logging_config import get_logger

logger = get_logger(__name__)

USER_CONFIG_FILENAME = "config.json"

#: Keys that may never be introduced or altered by the writable user layer.
#: ``dev_bypass`` stays gated by the build-time ``_build_env`` module, but we
#: also refuse to let a user-owned file inject it in the first place.
PROTECTED_KEYS = frozenset({"dev_bypass", "environment"})

_LOCK = threading.RLock()
_MERGED = None
_USER_LAYER = None


def get_bundled_config_path() -> str:
    """Path of the build-time config shipped inside the application."""
    import bpy  # noqa: WPS433 - Blender-only import

    return os.path.join(bpy.utils.resource_path("LOCAL"), "config", "mixar.json")


def get_user_config_path() -> str:
    """Path of the writable, update-safe user config layer."""
    return os.path.join(user_config_dir(), USER_CONFIG_FILENAME)


def get_config_path() -> str:
    """Backwards-compatible alias for the bundled config path."""
    try:
        return get_bundled_config_path()
    except Exception as exc:  # pragma: no cover - non-Blender contexts
        logger.debug("Bundled config path unavailable: %s", exc)
        return get_user_config_path()


def _read_json(path: str) -> dict:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except FileNotFoundError:
        return {}
    except (OSError, ValueError) as exc:
        logger.warning("Ignoring unreadable config at %s: %s", path, exc)
        return {}
    if not isinstance(loaded, dict):
        logger.warning("Ignoring %s: expected a JSON object", path)
        return {}
    return loaded


def _read_bundled() -> dict:
    try:
        path = get_bundled_config_path()
    except Exception as exc:  # pragma: no cover - non-Blender contexts
        logger.debug("Bundled config unavailable: %s", exc)
        return {}
    config = _read_json(path)
    if not config:
        logger.warning("No bundled config found at: %s", path)
    return config


def _read_user_layer() -> dict:
    user_layer = _read_json(get_user_config_path())
    rejected = PROTECTED_KEYS.intersection(user_layer)
    for key in rejected:
        logger.warning("Ignoring protected key %r from the user config layer", key)
        user_layer.pop(key, None)
    return user_layer


def load_mixar_config(refresh: bool = True) -> dict:
    """Load and merge the bundled and user config layers."""
    global _MERGED, _USER_LAYER
    with _LOCK:
        if _MERGED is not None and not refresh:
            return _MERGED
        merged = _read_bundled()
        _USER_LAYER = _read_user_layer()
        merged.update(_USER_LAYER)
        _MERGED = merged
        return _MERGED


def get_config() -> dict:
    """Return the merged configuration, loading it on first use."""
    global _MERGED
    with _LOCK:
        if _MERGED is None:
            load_mixar_config(refresh=True)
        return _MERGED


def reload_config() -> dict:
    """Force a re-read of both layers (used after external edits)."""
    return load_mixar_config(refresh=True)


def add_config(key, value) -> bool:
    """Persist ``key`` in the writable user layer. Returns False on failure."""
    if key in PROTECTED_KEYS:
        logger.error("Refusing to write protected config key %r", key)
        return False

    with _LOCK:
        if _MERGED is None:
            load_mixar_config(refresh=True)
        user_layer = dict(_USER_LAYER or {})
        user_layer[key] = value
        try:
            atomic_write_json(get_user_config_path(), user_layer)
        except OSError as exc:
            logger.error("Error saving config: %s", exc)
            return False
        globals()["_USER_LAYER"] = user_layer
        _MERGED[key] = value
        return True
