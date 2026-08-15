# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""The "Custom (OpenAI-compatible)" provider option - pure rules half.

Upstream builds the provider dropdown from the backend catalog
(``GET /api/v1/agent/models``) plus two hardcoded client-side entries,
OpenRouter and Codex. All three pin the endpoint server-side, so somebody
running Ollama / vLLM / LM Studio / LiteLLM, or paying for a gateway the Mixar
backend has never heard of, has no way to select it: the fork could already
store a custom base URL (``core/base_url.py``) but there was no provider to
attach it to.

This module adds that provider. It deliberately imports nothing from ``bpy``:
every rule below is exercised by ``tests/test_byok_custom_provider.py`` on a
bare runner, which is the only place this fork's gates run.

Division of labour:

* this file - the dropdown item, the id check, the item-list merge, the save
  rules and their user-facing wording
* ``ui/operators/byok_custom_provider_ops.py`` - the Blender property, the
  dialog fields and the operator patches that call in here

The endpoint is not stored twice: the custom provider uses the same resolved
base URL as the rest of the fork (``MIXAR_BYOK_BASE_URL`` env var > stored user
value), so the "Custom endpoint" section of the dialog stays the single place
it is edited, tested and cleared.
"""

from __future__ import annotations

# The id sent to the backend as ``provider``. Must not collide with a catalog
# id; the backend treats it as "OpenAI-compatible at the base_url I send you".
PROVIDER_ID = "custom"

# EnumProperty item shape Blender expects: (identifier, label, description).
PROVIDER_ITEM = (
    PROVIDER_ID,
    "Custom (OpenAI-compatible)",
    "Any OpenAI-compatible endpoint - you supply the base URL, key and model",
)

# Free text and deliberately empty. A prefilled slug would quietly save a model
# the user's endpoint does not serve, and the failure would surface much later
# as an opaque provider error.
DEFAULT_MODEL = ""

# Long enough for a namespaced name or an Azure-style deployment id, short
# enough that a pasted paragraph is obviously wrong.
MODEL_MAX_LENGTH = 200


def is_custom(provider) -> bool:
    """True when *provider* is this fork's custom-endpoint option."""
    return provider == PROVIDER_ID


def with_custom_item(items):
    """Return *items* with the custom option appended exactly once.

    Mirrors how upstream appends OpenRouter and Codex: the cloud catalog (or
    its "Loading..." / "No providers configured" sentinel) keeps its position at
    the front, and the custom entry is always offered - it has to be selectable
    offline, before login, and when the backend enables nothing at all.

    Returns a list of tuples, the shape a dynamic ``EnumProperty`` callback
    must hand back; ``items`` may be ``None`` or any iterable of item tuples.
    """
    merged = [tuple(item) for item in (items or ())]
    for item in merged:
        if item and item[0] == PROVIDER_ID:
            return merged
    merged.append(PROVIDER_ITEM)
    return merged


def normalize_model(raw) -> str:
    """Trim a user-typed model name without ever rewriting the name itself.

    Endpoints are case- and punctuation-sensitive (``llama3.1:70b``,
    ``Qwen/Qwen2.5-Coder-32B-Instruct``), so surrounding whitespace from a
    paste is the only thing safe to drop.
    """
    if not raw:
        return ""
    return str(raw).strip()


def validate(model, api_key, base_url):
    """Return an error message for a custom save, or ``None`` when it is valid.

    Checked in the order a user runs into them:

    1. an endpoint must be configured. There is no default for this provider,
       and falling back to the platform one would send the user's key to a host
       they never chose.
    2. a model name is required - nothing can infer it.
    3. a key is required. Local endpoints that ignore auth accept any string,
       so asking for one costs nothing and keeps the stored row honest.
    """
    if not (base_url or "").strip():
        return (
            "Set the endpoint in the Custom endpoint section below first - "
            "this provider has no default URL."
        )
    if not normalize_model(model):
        return "Enter the model name your endpoint serves, e.g. llama3.1:70b."
    if not (api_key or "").strip():
        return (
            "Enter an API key. Use any placeholder if your endpoint ignores auth."
        )
    return None


def is_ready(model, api_key, base_url) -> bool:
    """Boolean form of :func:`validate`, for an operator ``poll``."""
    return validate(model, api_key, base_url) is None
