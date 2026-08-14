# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Shared, pooled HTTP session for Mixar backend calls.

Creating a fresh ``requests`` connection (and a fresh TLS handshake) per call
is the single cheapest thing to fix in a chat/generation client that fires
many small requests. This module provides one lazily-created session with:

* keep-alive connection pooling,
* bounded retries with exponential backoff on idempotent verbs and 429/5xx,
* default connect/read timeouts so a hung backend can never freeze the UI,
* automatic rebuild when the resolved base URL changes (custom endpoints).

It is intentionally additive: existing call sites keep working, and can be
migrated to ``request()``/``get()``/``post()`` incrementally.
"""

from __future__ import annotations

import os
import threading

from .endpoints import api_url, get_endpoints
from .logging_config import get_logger

logger = get_logger(__name__)

_LOCK = threading.RLock()
_SESSION = None
_SESSION_KEY = None


def _env_float(name: str, default: float) -> float:
    raw = os.environ.get(name)
    if not raw:
        return default
    try:
        return float(raw)
    except ValueError:
        logger.warning("Ignoring invalid %s=%r", name, raw)
        return default


def _env_int(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if not raw:
        return default
    try:
        return int(raw)
    except ValueError:
        logger.warning("Ignoring invalid %s=%r", name, raw)
        return default


def connect_timeout() -> float:
    return _env_float("MIXAR_HTTP_CONNECT_TIMEOUT", 5.0)


def read_timeout() -> float:
    return _env_float("MIXAR_HTTP_READ_TIMEOUT", 30.0)


def default_timeout():
    return (connect_timeout(), read_timeout())


def _build_retry():
    try:
        from urllib3.util.retry import Retry
    except ImportError:  # pragma: no cover - very old bundled urllib3
        from requests.packages.urllib3.util.retry import Retry  # type: ignore

    total = _env_int("MIXAR_HTTP_RETRIES", 3)
    kwargs = {
        "total": total,
        "connect": total,
        "read": total,
        "status": total,
        "backoff_factor": _env_float("MIXAR_HTTP_BACKOFF", 0.3),
        "status_forcelist": (408, 429, 500, 502, 503, 504),
        "raise_on_status": False,
        "respect_retry_after_header": True,
    }
    idempotent = frozenset({"GET", "HEAD", "OPTIONS", "PUT", "DELETE", "TRACE"})
    try:
        return Retry(allowed_methods=idempotent, **kwargs)
    except TypeError:  # pragma: no cover - urllib3 < 1.26
        return Retry(method_whitelist=idempotent, **kwargs)


def _build_session():
    import requests
    from requests.adapters import HTTPAdapter

    session = requests.Session()
    adapter = HTTPAdapter(
        pool_connections=_env_int("MIXAR_HTTP_POOL_CONNECTIONS", 8),
        pool_maxsize=_env_int("MIXAR_HTTP_POOL_MAXSIZE", 32),
        max_retries=_build_retry(),
        pool_block=False,
    )
    session.mount("https://", adapter)
    session.mount("http://", adapter)
    session.headers.update({"Connection": "keep-alive"})
    return session


def get_session():
    """Return the shared session, rebuilding it if the base URL changed."""
    global _SESSION, _SESSION_KEY
    key = get_endpoints().backend
    with _LOCK:
        if _SESSION is None or _SESSION_KEY != key:
            close_session()
            _SESSION = _build_session()
            _SESSION_KEY = key
            logger.debug("Created pooled HTTP session for %s", key)
        return _SESSION


def close_session() -> None:
    """Dispose of the shared session (call on unregister/shutdown)."""
    global _SESSION, _SESSION_KEY
    with _LOCK:
        if _SESSION is not None:
            try:
                _SESSION.close()
            except Exception as exc:  # pragma: no cover - best effort
                logger.debug("Error closing HTTP session: %s", exc)
        _SESSION = None
        _SESSION_KEY = None


def request(method: str, path: str = "", **kwargs):
    """Perform a backend request. ``path`` is joined onto the base URL.

    Absolute URLs are passed through unchanged, so this is safe to use for
    pre-signed asset URLs too.
    """
    url = path if "://" in str(path) else api_url(path)
    kwargs.setdefault("timeout", default_timeout())
    return get_session().request(method.upper(), url, **kwargs)


def get(path: str = "", **kwargs):
    return request("GET", path, **kwargs)


def post(path: str = "", **kwargs):
    return request("POST", path, **kwargs)


def probe(path: str = "", timeout=None) -> tuple:
    """Cheap reachability check used by the endpoint settings UI.

    Returns ``(ok, message)``. Any HTTP status below 500 counts as reachable:
    a 401/404 still proves that something is answering at that base URL.
    """
    url = path if "://" in str(path) else api_url(path)
    timeout = timeout or (connect_timeout(), min(read_timeout(), 10.0))
    try:
        response = get_session().get(url, timeout=timeout, allow_redirects=True)
    except Exception as exc:
        return (False, "{0} is unreachable: {1}".format(url, exc))
    if response.status_code >= 500:
        return (
            False,
            "{0} answered HTTP {1}".format(url, response.status_code),
        )
    return (True, "{0} answered HTTP {1}".format(url, response.status_code))
