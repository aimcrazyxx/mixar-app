# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""OpenAI-compatible ``GET /models`` discovery for the custom BYOK provider.

Only the OpenAI response shape is accepted for now::

    {"data": [{"id": "model-id"}, ...]}

The API key is used only in the request header. It is never persisted or
included in logs and error messages.
"""

from __future__ import annotations

import threading
from collections.abc import Callable
from typing import Any

from . import base_url

MAX_MODELS = 500
MAX_MODEL_ID_LENGTH = 200
REQUEST_TIMEOUT = (3.05, 10.0)


class ModelDiscoveryError(ValueError):
    """The endpoint could not return a usable OpenAI model list."""


def models_url(raw_base_url: str) -> str:
    """Return the deterministic OpenAI ``/models`` URL for a base URL."""
    normalized = base_url.normalize(raw_base_url)
    if not normalized:
        raise ModelDiscoveryError("Set a Base URL before loading models")
    return normalized.rstrip("/") + "/models"


def parse_model_ids(payload: Any) -> list[str]:
    """Parse, deduplicate and bound model IDs from an OpenAI response."""
    if not isinstance(payload, dict) or not isinstance(payload.get("data"), list):
        raise ModelDiscoveryError(
            "Expected an OpenAI-compatible response with a data array"
        )

    seen: set[str] = set()
    model_ids: list[str] = []
    for row in payload["data"]:
        if not isinstance(row, dict):
            continue
        model_id = row.get("id")
        if not isinstance(model_id, str):
            continue
        model_id = model_id.strip()
        if not model_id or len(model_id) > MAX_MODEL_ID_LENGTH or model_id in seen:
            continue
        seen.add(model_id)
        model_ids.append(model_id)

    if not model_ids:
        raise ModelDiscoveryError("The endpoint returned no valid OpenAI model IDs")

    model_ids.sort(key=str.casefold)
    return model_ids[:MAX_MODELS]


def fetch_models_sync(raw_base_url: str, api_key: str) -> list[str]:
    """Fetch model IDs with a Bearer token; intended for a worker thread."""
    key = (api_key or "").strip()
    if not key:
        raise ModelDiscoveryError("Enter an API key before loading models")

    target = models_url(raw_base_url)

    try:
        import requests

        response = requests.get(
            target,
            headers={
                "Accept": "application/json",
                "Authorization": f"Bearer {key}",
            },
            timeout=REQUEST_TIMEOUT,
        )
    except Exception as exc:
        # Do not include request objects or headers in the message: they may
        # contain the API key on some requests exception implementations.
        raise ModelDiscoveryError(
            f"Could not reach the models endpoint ({type(exc).__name__})"
        ) from None

    status = int(getattr(response, "status_code", 0) or 0)
    if status in {401, 403}:
        raise ModelDiscoveryError(f"The API key was rejected (HTTP {status})")
    if status < 200 or status >= 300:
        raise ModelDiscoveryError(f"The models endpoint returned HTTP {status}")

    try:
        payload = response.json()
    except Exception:
        raise ModelDiscoveryError("The models endpoint did not return JSON") from None
    return parse_model_ids(payload)


def _schedule_on_main(callback: Callable[..., None], *args: Any) -> None:
    """Schedule a callback on Blender's main thread."""
    import bpy

    def _run() -> None:
        callback(*args)
        return None

    bpy.app.timers.register(_run, first_interval=0.0)


def fetch_models(
    raw_base_url: str,
    api_key: str,
    callback: Callable[[list[str] | None, str | None], None],
) -> None:
    """Fetch models in a daemon thread and return through a main-thread callback."""

    def _worker() -> None:
        try:
            models = fetch_models_sync(raw_base_url, api_key)
        except Exception as exc:
            message = str(exc) or "Model discovery failed"
            _schedule_on_main(callback, None, message)
            return
        _schedule_on_main(callback, models, None)

    threading.Thread(
        target=_worker,
        daemon=True,
        name="MixarOpenAIModels",
    ).start()
