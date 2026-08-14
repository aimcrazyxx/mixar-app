# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Runtime-configurable Mixar endpoints (custom base URL support).

Upstream Mixar bakes ``backend_url`` / ``frontend_url`` into the bundled
``config/mixar.json`` at build time, so pointing the app at a different
backend means rebuilding the whole Blender fork. This module resolves the
endpoints at runtime instead, with an explicit precedence chain:

1. Process environment (``MIXAR_BACKEND_URL``, ``MIXAR_FRONTEND_URL``,
   ``MIXAR_WS_URL``) - highest priority, handy for one-off launches and CI.
2. User overrides written from the UI, stored *outside* the app bundle so
   they survive app updates and never touch a signed .app payload.
3. Build-time values from the bundled ``config/mixar.json``.
4. Hard-coded upstream defaults.

Every value is validated and normalised once, then cached behind a lock so
hot paths (per-request URL building) do not re-read JSON or re-parse URLs.
"""

from __future__ import annotations

import ipaddress
import json
import os
import threading
from collections import namedtuple
from functools import lru_cache
from urllib.parse import urlsplit, urlunsplit

from .logging_config import get_logger

logger = get_logger(__name__)

DEFAULT_BACKEND_URL = "https://api.mixar.app"
DEFAULT_FRONTEND_URL = "https://www.mixar.app"

ENV_BACKEND = "MIXAR_BACKEND_URL"
ENV_FRONTEND = "MIXAR_FRONTEND_URL"
ENV_WS = "MIXAR_WS_URL"
ENV_ALLOW_INSECURE = "MIXAR_ALLOW_INSECURE_ENDPOINTS"
ENV_USER_CONFIG_DIR = "MIXAR_USER_CONFIG_DIR"

OVERRIDES_FILENAME = "endpoints.json"

#: Resolved endpoint bundle. ``source`` records which layer won, which makes
#: "why is it still talking to prod?" answerable from a bug report.
Endpoints = namedtuple(
    "Endpoints",
    ("backend", "frontend", "ws", "source", "allow_insecure"),
)

_LOCK = threading.RLock()
_CACHE = None
_OVERRIDES = None

_PRIVATE_HOST_NAMES = frozenset(
    {"localhost", "127.0.0.1", "::1", "0.0.0.0", "host.docker.internal"}
)
_PRIVATE_HOST_SUFFIXES = (".local", ".localhost", ".internal", ".test", ".lan")


class EndpointError(ValueError):
    """Raised when a user-supplied endpoint cannot be used."""


def _env_flag(name: str, default: bool = False) -> bool:
    raw = os.environ.get(name)
    if raw is None:
        return default
    value = raw.strip().lower()
    if value in ("1", "true", "yes", "on"):
        return True
    if value in ("0", "false", "no", "off", ""):
        return False
    logger.warning("Ignoring unrecognised boolean for %s: %r", name, raw)
    return default


def _is_private_host(host: str) -> bool:
    """True for loopback/LAN style hosts, where plain http:// is acceptable."""
    candidate = (host or "").strip().strip("[]").lower()
    if not candidate:
        return False
    if candidate in _PRIVATE_HOST_NAMES or candidate.endswith(_PRIVATE_HOST_SUFFIXES):
        return True
    try:
        address = ipaddress.ip_address(candidate)
    except ValueError:
        return False
    return address.is_private or address.is_loopback


@lru_cache(maxsize=128)
def normalize_url(url, allow_insecure=False, label="URL"):
    """Validate and canonicalise an http(s) base URL.

    Accepts bare hosts (``api.example.com`` -> ``https://api.example.com``),
    strips trailing slashes, query strings and fragments, and refuses plain
    http:// for public hosts unless explicitly allowed.
    """
    if not isinstance(url, str):
        raise EndpointError("{0} must be a string".format(label))

    candidate = url.strip()
    if not candidate:
        raise EndpointError("{0} is empty".format(label))
    if any(char.isspace() for char in candidate):
        raise EndpointError("{0} must not contain whitespace".format(label))
    if "://" not in candidate:
        candidate = "https://" + candidate

    parts = urlsplit(candidate)
    scheme = parts.scheme.lower()
    if scheme not in ("http", "https"):
        raise EndpointError(
            "{0} must use http:// or https:// (got {1!r})".format(label, parts.scheme)
        )
    if not parts.hostname:
        raise EndpointError("{0} is missing a host name".format(label))
    if scheme == "http" and not (allow_insecure or _is_private_host(parts.hostname)):
        raise EndpointError(
            "{0} uses plain http:// on a public host; enable "
            "'Allow insecure endpoints' if that is intentional".format(label)
        )

    return urlunsplit((scheme, parts.netloc, parts.path.rstrip("/"), "", ""))


def ws_url_from_http(url: str) -> str:
    """Derive the WebSocket base URL from an http(s) base URL."""
    parts = urlsplit(url)
    scheme = "wss" if parts.scheme.lower() == "https" else "ws"
    return urlunsplit((scheme, parts.netloc, parts.path.rstrip("/"), "", ""))


def normalize_ws_url(url, allow_insecure=False):
    """Validate a ws(s) URL, accepting an http(s) URL and converting it."""
    if not isinstance(url, str) or not url.strip():
        raise EndpointError("WebSocket URL is empty")

    candidate = url.strip()
    if "://" not in candidate:
        candidate = "wss://" + candidate

    scheme = urlsplit(candidate).scheme.lower()
    if scheme in ("http", "https"):
        return ws_url_from_http(
            normalize_url(candidate, allow_insecure, "WebSocket URL")
        )

    parts = urlsplit(candidate)
    if scheme not in ("ws", "wss"):
        raise EndpointError(
            "WebSocket URL must use ws:// or wss:// (got {0!r})".format(parts.scheme)
        )
    if not parts.hostname:
        raise EndpointError("WebSocket URL is missing a host name")
    if scheme == "ws" and not (allow_insecure or _is_private_host(parts.hostname)):
        raise EndpointError(
            "WebSocket URL uses plain ws:// on a public host; enable "
            "'Allow insecure endpoints' if that is intentional"
        )
    return urlunsplit((scheme, parts.netloc, parts.path.rstrip("/"), "", ""))


def user_config_dir() -> str:
    """Writable, update-safe directory for user-scoped Mixar settings."""
    override = os.environ.get(ENV_USER_CONFIG_DIR)
    if override:
        return override
    try:
        import bpy  # noqa: WPS433 - Blender-only import

        path = bpy.utils.user_resource("CONFIG", path="mixar", create=True)
        if path:
            return path
    except Exception as exc:  # pragma: no cover - non-Blender / stubbed bpy
        logger.debug("bpy user_resource unavailable (%s), using home fallback", exc)
    return os.path.join(os.path.expanduser("~"), ".mixar")


def overrides_path() -> str:
    return os.path.join(user_config_dir(), OVERRIDES_FILENAME)


def atomic_write_json(path: str, payload: dict) -> None:
    """Write JSON without ever leaving a truncated file behind."""
    directory = os.path.dirname(os.path.abspath(path))
    os.makedirs(directory, exist_ok=True)
    tmp_path = "{0}.tmp.{1}".format(path, os.getpid())
    try:
        with open(tmp_path, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, sort_keys=True)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp_path, path)
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:  # pragma: no cover - best effort cleanup
                pass


def load_overrides(refresh: bool = False) -> dict:
    """Read user endpoint overrides (cached, tolerant of corrupt files)."""
    global _OVERRIDES
    with _LOCK:
        if _OVERRIDES is not None and not refresh:
            return dict(_OVERRIDES)

        data = {}
        path = overrides_path()
        try:
            with open(path, "r", encoding="utf-8") as handle:
                loaded = json.load(handle)
            if isinstance(loaded, dict):
                data = loaded
            else:
                logger.warning("Ignoring %s: expected a JSON object", path)
        except FileNotFoundError:
            pass
        except (OSError, ValueError) as exc:
            logger.warning("Ignoring unreadable endpoint overrides at %s: %s", path, exc)

        _OVERRIDES = data
        return dict(data)


def _bundled_config() -> dict:
    """Build-time config values, imported lazily to avoid an import cycle."""
    try:
        from .config import get_config

        config = get_config()
        return dict(config) if config else {}
    except Exception as exc:  # pragma: no cover - config layer is optional here
        logger.debug("Bundled config unavailable: %s", exc)
        return {}


def _first_valid(candidates, allow_insecure, label):
    for raw_value, source in candidates:
        if not raw_value:
            continue
        try:
            return normalize_url(raw_value, allow_insecure, label), source
        except EndpointError as exc:
            logger.warning("Ignoring %s from %s (%r): %s", label, source, raw_value, exc)
    raise EndpointError("No usable {0} configured".format(label))


def _resolve() -> Endpoints:
    overrides = load_overrides()
    enabled = bool(overrides.get("enabled"))
    allow_insecure = _env_flag(
        ENV_ALLOW_INSECURE, bool(overrides.get("allow_insecure"))
    )
    bundled = _bundled_config()

    backend, backend_source = _first_valid(
        (
            (os.environ.get(ENV_BACKEND), "env"),
            (overrides.get("backend_url") if enabled else None, "user"),
            (bundled.get("backend_url"), "build"),
            (DEFAULT_BACKEND_URL, "default"),
        ),
        allow_insecure,
        "Backend URL",
    )

    frontend_candidates = [
        (os.environ.get(ENV_FRONTEND), "env"),
        (overrides.get("frontend_url") if enabled else None, "user"),
    ]
    if backend_source in ("env", "user"):
        # A custom backend must not silently keep sending the browser SSO flow
        # to the hosted Mixar frontend.
        frontend_candidates.append((backend, backend_source))
    frontend_candidates.extend(
        (
            (bundled.get("frontend_url"), "build"),
            (DEFAULT_FRONTEND_URL, "default"),
        )
    )
    frontend, _ = _first_valid(frontend_candidates, allow_insecure, "Frontend URL")

    ws_raw = (
        os.environ.get(ENV_WS)
        or (overrides.get("ws_url") if enabled else None)
        or bundled.get("ws_url")
    )
    if ws_raw:
        try:
            ws = normalize_ws_url(ws_raw, allow_insecure)
        except EndpointError as exc:
            logger.warning("Ignoring invalid WebSocket URL %r: %s", ws_raw, exc)
            ws = ws_url_from_http(backend)
    else:
        ws = ws_url_from_http(backend)

    resolved = Endpoints(backend, frontend, ws, backend_source, allow_insecure)
    logger.info(
        "Mixar endpoints resolved from %s: backend=%s frontend=%s ws=%s",
        backend_source,
        backend,
        frontend,
        ws,
    )
    return resolved


def get_endpoints(refresh: bool = False) -> Endpoints:
    """Return the cached resolved endpoints, resolving on first use."""
    global _CACHE
    with _LOCK:
        if _CACHE is None or refresh:
            _CACHE = _resolve()
        return _CACHE


def invalidate() -> None:
    """Drop cached endpoints, overrides and URL parsing results."""
    global _CACHE, _OVERRIDES
    with _LOCK:
        _CACHE = None
        _OVERRIDES = None
        normalize_url.cache_clear()


def get_server_url() -> str:
    """Backend API base URL (drop-in replacement for the build-time value)."""
    return get_endpoints().backend


def get_frontend_url() -> str:
    """Frontend base URL used for browser-facing pages such as SSO login."""
    return get_endpoints().frontend


def get_ws_url() -> str:
    """WebSocket base URL, derived from the backend URL unless overridden."""
    return get_endpoints().ws


def join_url(base: str, path: str = "") -> str:
    if not path:
        return base
    return "{0}/{1}".format(base.rstrip("/"), str(path).lstrip("/"))


def api_url(path: str = "") -> str:
    """Absolute backend URL for ``path``."""
    return join_url(get_endpoints().backend, path)


def frontend_url(path: str = "") -> str:
    """Absolute frontend URL for ``path``."""
    return join_url(get_endpoints().frontend, path)


def set_custom_endpoints(
    backend_url=None,
    frontend_url=None,
    ws_url=None,
    enabled=True,
    allow_insecure=False,
    persist=True,
):
    """Validate and store custom endpoints, then refresh the resolved cache.

    Raises :class:`EndpointError` before writing anything if a value is bad,
    so a typo can never leave the app pointing at an unusable backend.
    """
    payload = {"enabled": bool(enabled), "allow_insecure": bool(allow_insecure)}

    if enabled:
        if not backend_url or not str(backend_url).strip():
            raise EndpointError(
                "A backend base URL is required when custom endpoints are enabled"
            )
        payload["backend_url"] = normalize_url(
            backend_url, bool(allow_insecure), "Backend URL"
        )
        payload["frontend_url"] = (
            normalize_url(frontend_url, bool(allow_insecure), "Frontend URL")
            if frontend_url and str(frontend_url).strip()
            else payload["backend_url"]
        )
        if ws_url and str(ws_url).strip():
            payload["ws_url"] = normalize_ws_url(ws_url, bool(allow_insecure))

    with _LOCK:
        if persist:
            atomic_write_json(overrides_path(), payload)
        global _OVERRIDES
        _OVERRIDES = payload
        global _CACHE
        _CACHE = None
        normalize_url.cache_clear()

    return get_endpoints()


def clear_custom_endpoints(persist: bool = True) -> Endpoints:
    """Disable custom endpoints and fall back to the build-time values."""
    return set_custom_endpoints(enabled=False, persist=persist)


def describe() -> dict:
    """Diagnostics payload for the UI and for bug reports."""
    resolved = get_endpoints()
    env_overrides = {
        name: os.environ[name]
        for name in (ENV_BACKEND, ENV_FRONTEND, ENV_WS)
        if os.environ.get(name)
    }
    return {
        "backend_url": resolved.backend,
        "frontend_url": resolved.frontend,
        "ws_url": resolved.ws,
        "resolved_from": resolved.source,
        "allow_insecure": resolved.allow_insecure,
        "overrides_path": overrides_path(),
        "env_overrides": env_overrides,
    }
