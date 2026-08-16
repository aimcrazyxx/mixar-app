# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Authenticated OpenAI ``/models`` discovery UI for the custom provider.

This module is imported by ``byok_custom_provider_ops``. It deliberately keeps
model IDs in process memory only, tracks the endpoint that produced them, and
leaves the existing free-text Model field as the final override.
"""

from __future__ import annotations

import bpy
from bpy.props import EnumProperty, StringProperty
from bpy.types import Operator, WindowManager

from mixar.config.logging_config import get_logger

from ...core import base_url as base_url_core
from ...core import openai_models
from . import byok_custom_provider_ops as custom_ui

logger = get_logger(__name__)

_NONE = "__MIXAR_NO_DISCOVERED_MODEL__"
_model_items = [(_NONE, "Load models first", "Use /models to discover model IDs")]
_models_endpoint = ""
_request_serial = 0
_original_draw = None
_original_register = None
_original_unregister = None


def _enum_items(_self, _context):
    return _model_items


def _model_selected(wm, _context):
    selected = getattr(wm, "byok_form_custom_model_choice", _NONE)
    if selected != _NONE and hasattr(wm, "byok_form_custom_model"):
        wm.byok_form_custom_model = selected


def _replace_items(model_ids: list[str] | None, placeholder: str) -> None:
    global _model_items
    if model_ids:
        # Keep tuple-owned strings alive for Blender's dynamic enum callback.
        _model_items = [(model_id, model_id, "OpenAI model ID") for model_id in model_ids]
    else:
        _model_items = [(_NONE, placeholder, placeholder)]


def clear_discovered_models(wm=None) -> None:
    """Clear transient model IDs, including during logout or endpoint changes."""
    global _models_endpoint, _request_serial
    _request_serial += 1
    _models_endpoint = ""
    _replace_items(None, "Load models first")
    if wm is not None:
        if hasattr(wm, "byok_form_custom_model_choice"):
            wm.byok_form_custom_model_choice = _NONE
        if hasattr(wm, "byok_custom_models_status"):
            wm.byok_custom_models_status = ""


class MIXAR_BYOK_OT_fetch_custom_models(Operator):
    """Load models from an OpenAI-compatible endpoint"""

    bl_idname = "mixar_byok.fetch_custom_models"
    bl_label = "Load Models"
    bl_description = "Send an authenticated OpenAI-compatible GET request to Base URL + /models"

    @classmethod
    def poll(cls, context):
        wm = getattr(context, "window_manager", None)
        if wm is None or getattr(wm, "byok_form_provider", "") != "custom":
            return False
        return bool(
            base_url_core.get_base_url()
            and getattr(wm, "byok_form_api_key", "").strip()
            and getattr(wm, "byok_dialog_state", "IDLE") != "SAVING"
        )

    def execute(self, context):
        global _models_endpoint, _request_serial

        wm = context.window_manager
        endpoint = base_url_core.get_base_url()
        api_key = getattr(wm, "byok_form_api_key", "")
        try:
            target = openai_models.models_url(endpoint)
        except Exception as exc:
            self.report({'ERROR'}, str(exc))
            return {'CANCELLED'}

        _request_serial += 1
        serial = _request_serial
        _models_endpoint = ""
        _replace_items(None, "Loading models…")
        wm.byok_custom_models_status = f"Loading {target}…"

        def _done(model_ids, error):
            global _models_endpoint
            if serial != _request_serial:
                return
            live_wm = getattr(bpy.context, "window_manager", None)
            if live_wm is None:
                return
            current_endpoint = base_url_core.get_base_url()
            if current_endpoint != endpoint:
                _replace_items(None, "Endpoint changed; load again")
                live_wm.byok_custom_models_status = "Base URL changed — load models again"
                return
            if error:
                _models_endpoint = ""
                _replace_items(None, "Model discovery failed")
                live_wm.byok_custom_models_status = error[:300]
                return

            _models_endpoint = endpoint
            _replace_items(model_ids, "No models returned")
            current_model = getattr(live_wm, "byok_form_custom_model", "").strip()
            selected = current_model if current_model in (model_ids or []) else model_ids[0]
            live_wm.byok_form_custom_model_choice = selected
            live_wm.byok_form_custom_model = selected
            count = len(model_ids)
            live_wm.byok_custom_models_status = (
                f"Loaded {count} model{'s' if count != 1 else ''} from /models"
            )

        openai_models.fetch_models(endpoint, api_key, _done)
        return {'FINISHED'}


def _draw_discovery(box, wm) -> None:
    if getattr(wm, "byok_form_provider", "") != "custom":
        return

    box.separator(factor=0.5)
    row = box.row(align=True)
    row.operator(
        MIXAR_BYOK_OT_fetch_custom_models.bl_idname,
        text="Load Models from /models",
        icon='FILE_REFRESH',
    )

    current_endpoint = base_url_core.get_base_url()
    if _models_endpoint and _models_endpoint == current_endpoint and _model_items[0][0] != _NONE:
        box.prop(wm, "byok_form_custom_model_choice", text="Discovered")
        hint = box.row()
        hint.enabled = False
        hint.label(text="Selection copies into Model above; free text still wins", icon='INFO')
    elif _models_endpoint and _models_endpoint != current_endpoint:
        warning = box.row()
        warning.alert = True
        warning.label(text="Base URL changed — load models again", icon='ERROR')

    status = getattr(wm, "byok_custom_models_status", "")
    if status:
        line = box.row()
        line.enabled = False
        line.label(text=status, icon='INFO')


def _install_properties() -> None:
    if not hasattr(WindowManager, "byok_form_custom_model_choice"):
        WindowManager.byok_form_custom_model_choice = EnumProperty(
            name="Discovered Model",
            description="Model IDs returned by the OpenAI-compatible /models endpoint",
            items=_enum_items,
            update=_model_selected,
            options={'SKIP_SAVE'},
        )
    if not hasattr(WindowManager, "byok_custom_models_status"):
        WindowManager.byok_custom_models_status = StringProperty(
            name="Model discovery status",
            default="",
            maxlen=300,
            options={'SKIP_SAVE'},
        )


def _register_operator() -> None:
    if not hasattr(bpy.types, MIXAR_BYOK_OT_fetch_custom_models.__name__):
        bpy.utils.register_class(MIXAR_BYOK_OT_fetch_custom_models)


def _install_draw() -> None:
    global _original_draw
    if _original_draw is not None:
        return
    _original_draw = custom_ui._draw_custom_fields

    def _wrapped(dialog, box, col, wm):
        _original_draw(dialog, box, col, wm)
        _draw_discovery(box, wm)

    custom_ui._draw_custom_fields = _wrapped


def _install_runtime() -> None:
    _install_properties()
    _register_operator()
    _install_draw()


def _uninstall_runtime() -> None:
    global _original_draw
    clear_discovered_models(getattr(bpy.context, "window_manager", None))
    if _original_draw is not None:
        custom_ui._draw_custom_fields = _original_draw
        _original_draw = None
    if hasattr(bpy.types, MIXAR_BYOK_OT_fetch_custom_models.__name__):
        try:
            bpy.utils.unregister_class(MIXAR_BYOK_OT_fetch_custom_models)
        except Exception:
            pass
    for name in ("byok_form_custom_model_choice", "byok_custom_models_status"):
        if hasattr(WindowManager, name):
            delattr(WindowManager, name)


def _wrap_lifecycle() -> None:
    global _original_register, _original_unregister
    if _original_register is not None:
        return
    _original_register = custom_ui.register
    _original_unregister = custom_ui.unregister

    def _register():
        _original_register()
        _install_runtime()

    def _unregister():
        _uninstall_runtime()
        _original_unregister()

    custom_ui.register = _register
    custom_ui.unregister = _unregister


_wrap_lifecycle()
_install_runtime()
