# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Blender half of the "Custom (OpenAI-compatible)" provider option.

``core/custom_provider.py`` holds the rules; this file wires them into the BYOK
dialog without touching a single upstream file - the same trick
``byok_base_url_ops.py`` uses for the base URL section, so ``byok_ops.py``,
``byok_props.py`` and ``model_suggestions.py`` stay byte-identical to upstream
and keep merging cleanly.

What it installs (all idempotent, all reverted in ``unregister``):

* ``WindowManager.byok_form_custom_model`` - free text, because a custom
  endpoint has no catalog to pick a model from.
* ``get_provider_items`` wrappers in **two** modules. ``byok_props`` binds that
  function by name at import time, so patching ``model_suggestions`` alone would
  never show the entry in the dropdown; patching ``model_suggestions`` too is
  what makes ``byok_ops._lookup_provider_label`` print
  "Custom (OpenAI-compatible)" instead of the bare id under "Current
  configuration".
* ``MIXAR_BYOK_OT_open_dialog._draw_cloud_fields`` - upstream's ``_draw_form``
  sends everything that is not OpenRouter or Codex there, which is exactly
  where ``custom`` lands. Wrapping this method rather than ``_draw_form`` keeps
  it composable with the base URL wrapper and avoids drawing a second Base URL
  field.
* ``MIXAR_BYOK_OT_save.poll`` / ``.execute`` - a custom save has its own rules
  and sends ``provider='custom'``; the endpoint rides along through the payload
  patch in ``core/base_url.py``.
* ``MIXAR_BYOK_OT_open_dialog.invoke`` - reopening the dialog prefills the
  model that is already active.

The endpoint is never stored twice: it is the value the "Custom endpoint"
section already edits, tests and clears (env var ``MIXAR_BYOK_BASE_URL`` wins
over the stored one), which is why this form shows it read-only instead of
adding a competing field.
"""

from __future__ import annotations

import logging
import sys

import bpy
from bpy.props import StringProperty

from ...core import base_url as base_url_core
from ...core import custom_provider
from ...core import model_suggestions
from . import byok_ops
from .byok_ops import MIXAR_BYOK_OT_open_dialog, MIXAR_BYOK_OT_save

logger = logging.getLogger(__name__)

# The dialog is 640px wide and endpoints are long; enough to recognise the host.
ENDPOINT_DISPLAY_MAXLEN = 62

# Fallback lookup when the relative import cannot run (partially built package).
_PROPS_MODULE_NAME = 'mixar.modules.byok.ui.properties.byok_props'


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _clip(text: str, limit: int = ENDPOINT_DISPLAY_MAXLEN) -> str:
    text = text or ""
    if len(text) <= limit:
        return text
    return text[: max(limit - 3, 1)] + "..."


def _resolved_endpoint() -> str:
    """Base URL a custom save would use, or "" when nothing is configured."""
    try:
        return base_url_core.get_base_url() or ""
    except Exception as exc:  # noqa: BLE001
        logger.debug("Could not resolve the custom endpoint: %s", exc)
        return ""


def _props_module():
    """Module holding the dropdown callback, or None if it is not loaded."""
    try:
        from ..properties import byok_props  # noqa: PLC0415

        return byok_props
    except Exception as exc:  # noqa: BLE001
        logger.debug("byok_props not importable relatively: %s", exc)
        return sys.modules.get(_PROPS_MODULE_NAME)


# ---------------------------------------------------------------------------
# Provider dropdown
# ---------------------------------------------------------------------------

_patched_item_sources = []


def _make_items_wrapper(original):
    def get_provider_items(*args, **kwargs):
        items = original(*args, **kwargs)
        try:
            return custom_provider.with_custom_item(items)
        except Exception as exc:  # noqa: BLE001
            logger.warning("Could not append the custom provider entry: %s", exc)
            return items

    get_provider_items.__mixar_custom_provider_patch__ = True
    get_provider_items.__wrapped__ = original
    return get_provider_items


def _patch_provider_items() -> None:
    """Offer the entry wherever ``get_provider_items`` is resolved."""
    for module in (model_suggestions, _props_module()):
        if module is None:
            continue
        original = getattr(module, 'get_provider_items', None)
        if original is None:
            continue
        if getattr(original, '__mixar_custom_provider_patch__', False):
            continue
        setattr(module, 'get_provider_items', _make_items_wrapper(original))
        _patched_item_sources.append((module, original))


def _unpatch_provider_items() -> None:
    while _patched_item_sources:
        module, original = _patched_item_sources.pop()
        try:
            setattr(module, 'get_provider_items', original)
        except Exception as exc:  # noqa: BLE001
            logger.debug(
                "Could not restore get_provider_items on %s: %s",
                getattr(module, '__name__', module),
                exc,
            )


# ---------------------------------------------------------------------------
# Dialog fields
# ---------------------------------------------------------------------------

def _draw_custom_fields(dialog, box, col, wm) -> None:
    dialog._draw_tall_prop(col, wm, 'byok_form_custom_model', "Model")
    dialog._draw_tall_prop(col, wm, 'byok_form_api_key', "API Key")

    box.separator(factor=0.55)

    endpoint = _resolved_endpoint()
    endpoint_row = box.row()
    if endpoint:
        endpoint_row.enabled = False
        endpoint_row.label(text="Endpoint: " + _clip(endpoint), icon='URL')
    else:
        endpoint_row.alert = True
        endpoint_row.label(
            text="No endpoint yet - fill in Custom endpoint below before saving.",
            icon='ERROR',
        )

    warn = box.row()
    warn.alert = True
    warn.label(
        text="The endpoint must speak OpenAI-compatible tool / function calling.",
        icon='ERROR',
    )

    hint = box.row()
    hint.enabled = False
    hint.label(
        text="Model name exactly as your endpoint serves it, e.g. llama3.1:70b.",
        icon='INFO',
    )
    key_hint = box.row()
    key_hint.enabled = False
    key_hint.label(
        text="Endpoints that ignore auth still need a placeholder key; it is stored encrypted.",
    )


_ORIGINAL_DRAW_CLOUD_FIELDS = None


def _patched_draw_cloud_fields(self, box, col, wm) -> None:
    """Custom form for ``custom``, upstream's catalog form for the rest."""
    try:
        if custom_provider.is_custom(getattr(wm, 'byok_form_provider', '')):
            _draw_custom_fields(self, box, col, wm)
            return
    except Exception as exc:  # noqa: BLE001
        # Never fall through to upstream here: half of our fields may already be
        # on screen, and drawing the catalog form after them would duplicate
        # widgets instead of reporting the problem.
        logger.warning("Custom provider fields failed to draw: %s", exc, exc_info=True)
        failed = box.row()
        failed.alert = True
        failed.label(text="Custom provider fields failed to draw.", icon='ERROR')
        return

    _ORIGINAL_DRAW_CLOUD_FIELDS(self, box, col, wm)


# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------

_ORIGINAL_SAVE_POLL = None
_ORIGINAL_SAVE_EXECUTE = None


def _patched_save_poll(cls, context):
    wm = getattr(context, 'window_manager', None)
    if wm is not None and custom_provider.is_custom(getattr(wm, 'byok_form_provider', '')):
        if getattr(wm, 'byok_dialog_state', '') == 'SAVING':
            return False
        return custom_provider.is_ready(
            getattr(wm, 'byok_form_custom_model', ''),
            getattr(wm, 'byok_form_api_key', ''),
            _resolved_endpoint(),
        )
    return _ORIGINAL_SAVE_POLL(context)


def _execute_custom(operator, wm):
    """Save a free-text model against the endpoint the fork already resolved."""
    model = custom_provider.normalize_model(getattr(wm, 'byok_form_custom_model', ''))
    api_key = (getattr(wm, 'byok_form_api_key', '') or "").strip()
    endpoint = _resolved_endpoint()

    problem = custom_provider.validate(model, api_key, endpoint)
    if problem:
        wm.byok_dialog_state = 'ERROR'
        wm.byok_last_error = problem
        return {'CANCELLED'}

    wm.byok_dialog_state = 'SAVING'
    wm.byok_last_error = ''
    byok_ops._redraw_mixie_chat_areas()

    byok_ops.byok_client.save_credentials(
        provider=custom_provider.PROVIDER_ID,
        model=model,
        api_key=api_key,
        on_done=byok_ops._on_save_done,
    )
    return {'FINISHED'}


def _patched_save_execute(self, context):
    wm = context.window_manager
    if custom_provider.is_custom(getattr(wm, 'byok_form_provider', '')):
        return _execute_custom(self, wm)
    return _ORIGINAL_SAVE_EXECUTE(self, context)


# ---------------------------------------------------------------------------
# Dialog prefill
# ---------------------------------------------------------------------------

_ORIGINAL_INVOKE = None


def _patched_invoke(self, context, event):
    """Upstream invoke, then prefill our model field.

    Runs after the original on purpose: ``invoke_props_dialog`` only schedules
    the dialog, so ``draw`` still sees the value set here.
    """
    result = _ORIGINAL_INVOKE(self, context, event)
    try:
        wm = context.window_manager
        if custom_provider.is_custom(getattr(wm, 'byok_current_provider', '')):
            current_model = getattr(wm, 'byok_current_model', '')
            if current_model:
                wm.byok_form_custom_model = current_model
    except Exception as exc:  # noqa: BLE001
        logger.debug("Could not prefill the custom model: %s", exc)
    return result


# ---------------------------------------------------------------------------
# Install / uninstall
# ---------------------------------------------------------------------------

def _install_properties_and_patches() -> None:
    """Idempotent: the WM property, the dropdown entry and the patches."""
    global _ORIGINAL_DRAW_CLOUD_FIELDS, _ORIGINAL_SAVE_POLL
    global _ORIGINAL_SAVE_EXECUTE, _ORIGINAL_INVOKE

    WM = bpy.types.WindowManager
    if not hasattr(WM, 'byok_form_custom_model'):
        WM.byok_form_custom_model = StringProperty(
            name="Model",
            description=(
                "Model name exactly as your endpoint serves it, "
                "e.g. llama3.1:70b or Qwen/Qwen2.5-Coder-32B-Instruct"
            ),
            default=custom_provider.DEFAULT_MODEL,
            maxlen=custom_provider.MODEL_MAX_LENGTH,
        )

    _patch_provider_items()

    if _ORIGINAL_DRAW_CLOUD_FIELDS is None:
        _ORIGINAL_DRAW_CLOUD_FIELDS = MIXAR_BYOK_OT_open_dialog._draw_cloud_fields
        MIXAR_BYOK_OT_open_dialog._draw_cloud_fields = _patched_draw_cloud_fields

    if _ORIGINAL_INVOKE is None:
        _ORIGINAL_INVOKE = MIXAR_BYOK_OT_open_dialog.invoke
        MIXAR_BYOK_OT_open_dialog.invoke = _patched_invoke

    if _ORIGINAL_SAVE_POLL is None:
        # Bound classmethod: calling it takes only `context`.
        _ORIGINAL_SAVE_POLL = MIXAR_BYOK_OT_save.poll
        MIXAR_BYOK_OT_save.poll = classmethod(_patched_save_poll)

    if _ORIGINAL_SAVE_EXECUTE is None:
        _ORIGINAL_SAVE_EXECUTE = MIXAR_BYOK_OT_save.execute
        MIXAR_BYOK_OT_save.execute = _patched_save_execute

    # The endpoint has to reach the backend, and that patch lives with the
    # base URL module. Idempotent, so installing it from here is safe even when
    # byok_base_url_ops.py already did.
    base_url_core.install_patches()


def _remove_patches() -> None:
    global _ORIGINAL_DRAW_CLOUD_FIELDS, _ORIGINAL_SAVE_POLL
    global _ORIGINAL_SAVE_EXECUTE, _ORIGINAL_INVOKE

    if _ORIGINAL_DRAW_CLOUD_FIELDS is not None:
        MIXAR_BYOK_OT_open_dialog._draw_cloud_fields = _ORIGINAL_DRAW_CLOUD_FIELDS
        _ORIGINAL_DRAW_CLOUD_FIELDS = None

    if _ORIGINAL_INVOKE is not None:
        MIXAR_BYOK_OT_open_dialog.invoke = _ORIGINAL_INVOKE
        _ORIGINAL_INVOKE = None

    if _ORIGINAL_SAVE_POLL is not None:
        original = getattr(_ORIGINAL_SAVE_POLL, '__func__', _ORIGINAL_SAVE_POLL)
        MIXAR_BYOK_OT_save.poll = classmethod(original)
        _ORIGINAL_SAVE_POLL = None

    if _ORIGINAL_SAVE_EXECUTE is not None:
        MIXAR_BYOK_OT_save.execute = _ORIGINAL_SAVE_EXECUTE
        _ORIGINAL_SAVE_EXECUTE = None

    _unpatch_provider_items()


# No new operators: the custom provider reuses mixar_byok.save and the base URL
# operators. Kept for the `classes`-style auto-discovery contract.
classes = ()


def register() -> None:
    _install_properties_and_patches()


def unregister() -> None:
    _remove_patches()

    WM = bpy.types.WindowManager
    try:
        delattr(WM, 'byok_form_custom_model')
    except AttributeError:
        pass


# Import-time safety net: the dropdown entry must exist even if the bootstrap
# only looks at `classes` for this folder (ours is empty). Idempotent.
try:
    _install_properties_and_patches()
except Exception as exc:  # noqa: BLE001
    logger.debug("Deferred custom provider install: %s", exc)

# Install transient authenticated OpenAI-compatible /models discovery.
from . import byok_custom_models_ops as _byok_custom_models_ops  # noqa: E402,F401
