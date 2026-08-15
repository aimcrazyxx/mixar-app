# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Custom base URL for BYOK provider requests.

Upstream keeps the provider endpoint on the server: the AI Provider Settings
dialog sends ``{provider, model, api_key}`` to ``PUT /agent/byok`` and the
backend decides which URL to call (see the note in ``byok/constants.py``:
"the base_url is fixed server-side (not user-entered)"). That makes it
impossible to aim the agent at an OpenAI-compatible endpoint of your own.

This module supplies the missing piece without touching any upstream file:

* ``normalize`` - validation shared by the UI, the store and the probe
* ``resolve`` - precedence: ``MIXAR_BYOK_BASE_URL`` env var > stored user
  value > empty (i.e. unchanged upstream behaviour)
* ``set_stored`` / ``get_stored`` - persistence in this module's own JSON file
* ``install_patches`` - wraps ``AgentService.save_credentials_all`` so the PUT
  payload carries ``base_url`` **only** when the user set one; with no custom
  value the request is byte-identical to upstream
* ``probe`` - threaded reachability check for the dialog's Test button

Scope: the *provider* endpoint, nothing else. The Mixar backend itself is
whatever the build shipped (``https://api.mixar.app``) and this fork
deliberately does not override it.

Why a store of its own instead of ``mixar.config.add_config``: that helper
rewrites ``config/mixar.json`` *inside* the installed application directory,
which needs administrator rights under Program Files, is wiped by every
update and invalidates the macOS code signature. The value is kept next to
Blender's other user config instead, and written atomically so a crash
mid-save cannot truncate it.

Nothing here imports ``bpy`` at module scope, so it can be unit-tested outside
Blender.
"""

import json
import os
import sys
import threading
from typing import Callable, Optional, Tuple

from mixar.config.logging_config import get_logger

logger = get_logger(__name__)

# Env var wins over the stored value - handy for CI and for one-off runs.
ENV_VAR = "MIXAR_BYOK_BASE_URL"
# Key inside this module's JSON store.
CONFIG_KEY = "byok_base_url"
# Overrides where that store lives (tests, portable installs).
ENV_CONFIG_DIR = "MIXAR_USER_CONFIG_DIR"
STORE_FILENAME = "byok.json"
# Opt-in for plain http:// on a public host.
ENV_ALLOW_INSECURE = "MIXAR_ALLOW_INSECURE_ENDPOINTS"

MAX_LENGTH = 512
PROBE_TIMEOUT = 6.0
# Tried in order; the first one that answers below 500 proves reachability.
# A 401/403 counts as reachable - it means something is listening and talking
# HTTP, which is all the Test button claims to verify.
PROBE_PATHS = ("/models", "/v1/models", "/")

_SOURCE_ENV = "env"
_SOURCE_USER = "user"
_SOURCE_DEFAULT = "default"

_LOCAL_HOSTS = ("localhost", "127.0.0.1", "::1", "0.0.0.0", "host.docker.internal")
_LOCAL_SUFFIXES = (".local", ".localhost", ".internal", ".test", ".lan")

_STORE_LOCK = threading.RLock()

# Parsed store, cached. The dialog's Base URL field is RNA get/set backed, so
# every redraw asks for the effective value: without this, one dialog frame
# opens and JSON-parses the file several times. Keyed by path plus
# (mtime_ns, size) and dropped after every write, so a file edited by hand
# outside the app is still picked up.
_STORE_CACHE = {"path": None, "stamp": None, "data": {}}


class BaseUrlError(ValueError):
    """The supplied base URL cannot be used. Message is user-facing."""


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def _is_local_host(host: str) -> bool:
    """True for loopback, private ranges and local-only TLDs."""
    name = (host or "").split(":")[0].strip("[]").lower()
    if not name:
        return False
    if name in _LOCAL_HOSTS or name.endswith(_LOCAL_SUFFIXES):
        return True
    if name.startswith(("10.", "192.168.", "127.", "169.254.")):
        return True
    if name.startswith("172."):
        parts = name.split(".")
        if len(parts) > 1 and parts[1].isdigit() and 16 <= int(parts[1]) <= 31:
            return True
    return False


def normalize(raw: Optional[str]) -> str:
    """Return a canonical base URL, or ``""`` for empty input.

    Unlike a backend-URL normalizer this **keeps the path**, because
    OpenAI-compatible gateways are routinely mounted on one
    (``https://gw.example.com/openai/v1``). Only the trailing slash is dropped
    so callers can concatenate ``/chat/completions`` safely.

    Raises:
        BaseUrlError: with a message meant to be shown in the dialog.
    """
    value = (raw or "").strip()
    if not value:
        return ""
    if len(value) > MAX_LENGTH:
        raise BaseUrlError(
            "URL is too long ({0} characters, maximum {1}).".format(len(value), MAX_LENGTH)
        )
    if any(char.isspace() for char in value):
        raise BaseUrlError("URL must not contain spaces.")

    # A bare host is the most common paste; assume https rather than reject.
    if "://" not in value:
        value = "https://" + value

    from urllib.parse import urlparse

    parsed = urlparse(value)
    if parsed.scheme not in ("http", "https"):
        raise BaseUrlError("Use an http:// or https:// URL.")
    if not parsed.netloc:
        raise BaseUrlError("Missing host name.")
    if parsed.query or parsed.fragment:
        raise BaseUrlError("Base URL must not contain a query string or fragment.")
    if parsed.scheme == "http" and not _is_local_host(parsed.netloc):
        if (os.environ.get(ENV_ALLOW_INSECURE) or "").strip() not in ("1", "true", "yes", "on"):
            raise BaseUrlError(
                "Refusing plain http:// to a public host - use https://, or set "
                "{0}=1 if you really mean it.".format(ENV_ALLOW_INSECURE)
            )

    path = parsed.path.rstrip("/")
    return "{0}://{1}{2}".format(parsed.scheme, parsed.netloc, path)


# ---------------------------------------------------------------------------
# Persistence (own file, in the writable user config directory)
# ---------------------------------------------------------------------------

def user_config_dir() -> str:
    """Directory holding this module's settings file.

    ``MIXAR_USER_CONFIG_DIR`` wins, then Blender's own user config directory,
    then the platform default. Never a path inside the application bundle.
    """
    override = (os.environ.get(ENV_CONFIG_DIR) or "").strip()
    if override:
        return os.path.expanduser(override)

    try:
        import bpy

        blender_config = bpy.utils.user_resource("CONFIG")
        if blender_config:
            return os.path.join(blender_config, "mixar")
    except Exception as exc:  # noqa: BLE001 - outside Blender (tests, tooling)
        logger.debug("Using a platform config directory instead of Blender's: %s", exc)

    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA") or os.path.expanduser("~")
    elif sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Application Support")
    else:
        base = os.environ.get("XDG_CONFIG_HOME") or os.path.expanduser("~/.config")
    return os.path.join(base, "mixar")


def store_path() -> str:
    """Full path of the settings file."""
    return os.path.join(user_config_dir(), STORE_FILENAME)


def _store_stamp(path: str):
    """``(mtime_ns, size)`` for the store, or ``None`` when it does not exist."""
    try:
        info = os.stat(path)
    except OSError:
        return None
    return (info.st_mtime_ns, info.st_size)


def _forget_cache() -> None:
    _STORE_CACHE["path"] = None
    _STORE_CACHE["stamp"] = None
    _STORE_CACHE["data"] = {}


def _read_store() -> dict:
    """Parsed store, or ``{}``. Unreadable or corrupt content is ignored.

    Returns a copy: ``set_stored`` mutates the result, and the cache must not
    follow it.
    """
    path = store_path()
    stamp = _store_stamp(path)
    if _STORE_CACHE["path"] == path and _STORE_CACHE["stamp"] == stamp:
        return dict(_STORE_CACHE["data"])

    data = {}
    if stamp is not None:
        try:
            with open(path, "r", encoding="utf-8") as handle:
                loaded = json.load(handle)
        except FileNotFoundError:
            loaded = {}
        except (OSError, ValueError) as exc:
            logger.warning("Ignoring unreadable BYOK settings at %s: %s", path, exc)
            loaded = {}
        if isinstance(loaded, dict):
            data = loaded

    _STORE_CACHE["path"] = path
    _STORE_CACHE["stamp"] = stamp
    _STORE_CACHE["data"] = data
    return dict(data)


def _write_store(data: dict) -> None:
    """Atomic write: a crash mid-save can never leave a truncated file.

    Raises:
        OSError: the caller turns this into a user-facing message.
    """
    path = store_path()
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    temp_path = path + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except OSError:
        # Never leave a half-written .tmp behind for the next run to trip over.
        try:
            os.remove(temp_path)
        except OSError:
            pass
        raise
    finally:
        _forget_cache()


def get_stored() -> str:
    """Stored value, or ``""``. An unusable stored value is logged and ignored."""
    with _STORE_LOCK:
        value = _read_store().get(CONFIG_KEY) or ""
    if not isinstance(value, str):
        return ""
    try:
        return normalize(value)
    except BaseUrlError as exc:
        logger.warning("Ignoring stored BYOK base URL %r: %s", value, exc)
        return ""


def set_stored(raw: Optional[str]) -> str:
    """Validate and persist. Pass an empty value to clear.

    Returns the normalized value that was stored.

    Raises:
        BaseUrlError: invalid input, or the file could not be written. Nothing
            is written in either case.
    """
    normalized = normalize(raw)
    with _STORE_LOCK:
        data = _read_store()
        if normalized:
            data[CONFIG_KEY] = normalized
        else:
            data.pop(CONFIG_KEY, None)
        try:
            _write_store(data)
        except OSError as exc:
            logger.error("Could not persist BYOK base URL: %s", exc)
            raise BaseUrlError(
                "Could not save the URL to {0}.".format(store_path())
            ) from exc
    logger.info("BYOK base URL set to %s", normalized or "<default>")
    return normalized


def resolve() -> Tuple[str, str]:
    """Return ``(base_url, source)`` where source is env / user / default."""
    env_value = (os.environ.get(ENV_VAR) or "").strip()
    if env_value:
        try:
            return normalize(env_value), _SOURCE_ENV
        except BaseUrlError as exc:
            logger.warning("Ignoring %s=%r: %s", ENV_VAR, env_value, exc)
    stored = get_stored()
    if stored:
        return stored, _SOURCE_USER
    return "", _SOURCE_DEFAULT


def get_base_url() -> str:
    """Effective base URL, or ``""`` when the backend default should be used."""
    return resolve()[0]


def is_locked_by_env() -> bool:
    """True when the env var is what is in effect - the dialog can't override it."""
    return resolve()[1] == _SOURCE_ENV


def describe() -> str:
    """One-line summary for the dialog."""
    value, source = resolve()
    if not value:
        return "Using the provider endpoint chosen by the Mixar backend"
    if source == _SOURCE_ENV:
        return "{0} (from {1})".format(value, ENV_VAR)
    return "{0} (saved)".format(value)


# ---------------------------------------------------------------------------
# Reachability probe
# ---------------------------------------------------------------------------

def _schedule_on_main(callback: Callable[..., None], *args) -> None:
    """Run ``callback(*args)`` on Blender's main thread (zero-delay timer)."""
    try:
        import bpy
    except Exception:  # noqa: BLE001 - outside Blender (tests)
        callback(*args)
        return

    def _run():
        try:
            callback(*args)
        except Exception as exc:  # noqa: BLE001
            logger.warning("BYOK base URL callback failed: %s", exc, exc_info=True)
        return None

    try:
        bpy.app.timers.register(_run, first_interval=0.0)
    except Exception as exc:  # noqa: BLE001 - losing the result is worse
        logger.debug("Could not schedule on the main thread (%s); calling直接", exc)
        _run()


def _probe_sync(base: str) -> Tuple[bool, str]:
    """Blocking probe. Anything below HTTP 500 proves something is listening."""
    try:
        import requests
    except ImportError:
        return False, "no HTTP client available in this build"

    last = ""
    for path in PROBE_PATHS:
        target = base + path
        try:
            response = requests.get(target, timeout=PROBE_TIMEOUT)
        except Exception as exc:  # noqa: BLE001 - any transport failure
            last = str(exc) or exc.__class__.__name__
            continue
        if response.status_code < 500:
            return True, "Reachable - HTTP {0} from {1}".format(response.status_code, path)
        last = "HTTP {0} from {1}".format(response.status_code, path)
    return False, last or "No response"


def probe(raw: str, on_done: Callable[[bool, str], None]) -> None:
    """Validate ``raw`` and probe it off the main thread.

    ``on_done(ok, message)`` is always delivered on the main thread, including
    when the probe itself blows up - a thread that dies quietly would leave the
    dialog saying "Testing..." for the rest of the session.

    Raises:
        BaseUrlError: invalid URL (no thread is started).
    """
    normalized = normalize(raw)
    if not normalized:
        raise BaseUrlError("Enter a URL first.")

    def _thread():
        try:
            ok, message = _probe_sync(normalized)
        except Exception as exc:  # noqa: BLE001 - the UI must never hang
            logger.warning("BYOK base URL probe crashed: %s", exc, exc_info=True)
            ok, message = False, str(exc) or exc.__class__.__name__
        _schedule_on_main(on_done, ok, message)

    threading.Thread(target=_thread, daemon=True, name="MixarBYOKBaseUrlProbe").start()


# ---------------------------------------------------------------------------
# Payload patch
# ---------------------------------------------------------------------------

_ORIGINAL_SAVE_ALL = None


def install_patches() -> None:
    """Make ``PUT /agent/byok`` carry ``base_url`` when one is configured.

    Idempotent. With no custom value configured the payload is exactly what
    upstream sends, so a hosted-backend save cannot regress. A backend that
    doesn't know the field will reject or ignore it - see docs.
    """
    global _ORIGINAL_SAVE_ALL
    if _ORIGINAL_SAVE_ALL is not None:
        return

    from ...common.api.services import agent_service as agent_service_module

    original = agent_service_module.AgentService.save_credentials_all

    def save_credentials_all(self, provider, model, api_key, base_url=None, **extra):
        """PUT /agent/byok, optionally pinning the provider base URL.

        ``**extra`` is forwarded rather than dropped: if upstream grows a
        parameter, its own callers keep working instead of hitting a TypeError
        raised by this patch.
        """
        payload = {
            "provider": provider,
            "model": model,
            "api_key": api_key,
        }
        for key, value in extra.items():
            if value is not None:
                payload[key] = value
        resolved = base_url if base_url is not None else get_base_url()
        if resolved:
            payload["base_url"] = resolved
            logger.info("BYOK save: provider=%s via custom base URL %s", provider, resolved)
        return self.put("byok", json=payload)

    save_credentials_all.__doc__ = (original.__doc__ or "") + (
        "\n\nFork addition: sends `base_url` when the user configured a custom "
        "endpoint (see byok/core/base_url.py)."
    )

    agent_service_module.AgentService.save_credentials_all = save_credentials_all
    _ORIGINAL_SAVE_ALL = original
    logger.debug("BYOK base URL: payload patch installed")


def remove_patches() -> None:
    """Restore the untouched upstream method. Idempotent."""
    global _ORIGINAL_SAVE_ALL
    if _ORIGINAL_SAVE_ALL is None:
        return
    try:
        from ...common.api.services import agent_service as agent_service_module

        agent_service_module.AgentService.save_credentials_all = _ORIGINAL_SAVE_ALL
    except Exception as exc:  # noqa: BLE001
        logger.debug("BYOK base URL: could not restore payload patch: %s", exc)
    _ORIGINAL_SAVE_ALL = None
