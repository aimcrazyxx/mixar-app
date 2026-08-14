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

* ``normalize`` — validation shared by the UI, the store and the probe
* ``resolve`` — precedence: ``MIXAR_BYOK_BASE_URL`` env var > stored user
  value > empty (i.e. unchanged upstream behaviour)
* ``set_stored`` / ``get_stored`` — persistence in the writable user config
  layer, so the value survives app updates and never writes inside the bundle
* ``install_patches`` — wraps ``AgentService.save_credentials_all`` so the PUT
  payload carries ``base_url`` **only** when the user set one; with no custom
  value the request is byte-identical to upstream
* ``probe`` — threaded reachability check for the dialog's Test button

Nothing here imports ``bpy`` at module scope, so it can be unit-tested outside
Blender.
"""

import os
import threading
from typing import Callable, Optional, Tuple

from mixar.config.logging_config import get_logger

logger = get_logger(__name__)

# Env var wins over the stored value — handy for CI and for one-off runs.
ENV_VAR = "MIXAR_BYOK_BASE_URL"
# Key inside the user config layer (config/store.py).
CONFIG_KEY = "byok_base_url"
# Opt-in for plain http:// on a public host.
ENV_ALLOW_INSECURE = "MIXAR_ALLOW_INSECURE_ENDPOINTS"

MAX_LENGTH = 512
PROBE_TIMEOUT = 6.0
# Tried in order; the first one that answers below 500 proves reachability.
# A 401/403 counts as reachable — it means something is listening and talking
# HTTP, which is all the Test button claims to verify.
PROBE_PATHS = ("/models", "/v1/models", "/")

_SOURCE_ENV = "env"
_SOURCE_USER = "user"
_SOURCE_DEFAULT = "default"

_LOCAL_HOSTS = ("localhost", "127.0.0.1", "::1", "0.0.0.0", "host.docker.internal")
_LOCAL_SUFFIXES = (".local", ".localhost", ".internal", ".test", ".lan")


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

    Unlike the app's backend-URL normalizer this **keeps the path**, because
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
                "Refusing plain http:// to a public host — use https://, or set "
                "{0}=1 if you really mean it.".format(ENV_ALLOW_INSECURE)
            )

    path = parsed.path.rstrip("/")
    return "{0}://{1}{2}".format(parsed.scheme, parsed.netloc, path)


# ---------------------------------------------------------------------------
# Persistence (writable user layer — never inside the app bundle)
# ---------------------------------------------------------------------------

def get_stored() -> str:
    """Stored value, or ``""``. An unusable stored value is logged and ignored."""
    try:
        from mixar.config import get_config

        config = get_config() or {}
        value = config.get(CONFIG_KEY) or ""
    except Exception as exc:  # noqa: BLE001 — config must never break the dialog
        logger.debug("BYOK base URL: could not read config: %s", exc)
        return ""
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
        BaseUrlError: invalid input (nothing is written).
    """
    normalized = normalize(raw)
    try:
        from mixar.config import add_config

        add_config(CONFIG_KEY, normalized)
    except Exception as exc:  # noqa: BLE001
        logger.error("Could not persist BYOK base URL: %s", exc)
        raise BaseUrlError("Could not save the URL to your config file.") from exc
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
    """True when the env var is what is in effect — the dialog can't override it."""
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
    except Exception:  # noqa: BLE001 — outside Blender (tests)
        callback(*args)
        return

    def _run():
        try:
            callback(*args)
        except Exception as exc:  # noqa: BLE001
            logger.warning("BYOK base URL callback failed: %s", exc, exc_info=True)
        return None

    bpy.app.timers.register(_run, first_interval=0.0)


def _probe_sync(base: str) -> Tuple[bool, str]:
    """Blocking probe. Anything below HTTP 500 proves something is listening."""
    import requests

    last = ""
    for path in PROBE_PATHS:
        target = base + path
        try:
            response = requests.get(target, timeout=PROBE_TIMEOUT)
        except Exception as exc:  # noqa: BLE001 — any transport failure
            last = str(exc) or exc.__class__.__name__
            continue
        if response.status_code < 500:
            return True, "Reachable — HTTP {0} from {1}".format(response.status_code, path)
        last = "HTTP {0} from {1}".format(response.status_code, path)
    return False, last or "No response"


def probe(raw: str, on_done: Callable[[bool, str], None]) -> None:
    """Validate ``raw`` and probe it off the main thread.

    ``on_done(ok, message)`` is always delivered on the main thread.

    Raises:
        BaseUrlError: invalid URL (no thread is started).
    """
    normalized = normalize(raw)
    if not normalized:
        raise BaseUrlError("Enter a URL first.")

    def _thread():
        ok, message = _probe_sync(normalized)
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
    doesn't know the field will reject or ignore it — see docs.
    """
    global _ORIGINAL_SAVE_ALL
    if _ORIGINAL_SAVE_ALL is not None:
        return

    from ...common.api.services import agent_service as agent_service_module

    original = agent_service_module.AgentService.save_credentials_all

    def save_credentials_all(self, provider, model, api_key, base_url=None):
        """PUT /agent/byok, optionally pinning the provider base URL."""
        payload = {
            "provider": provider,
            "model": model,
            "api_key": api_key,
        }
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
