# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

""""Custom endpoint" section for the AI Provider Settings dialog.

Adds a Base URL field (+ Test and Clear) to the existing dialog by wrapping
its own ``_draw_form`` helper, so ``byok_ops.py`` stays byte-identical to
upstream and rebases cleanly.

The field is backed by RNA ``get``/``set`` callbacks that read and write the
store in ``core/base_url.py``. Consequences worth knowing:

* it always shows the value actually in effect — no prefill, no stale state
* editing persists immediately (no need to press Save), which is also how the
  value reaches ``PUT /agent/byok`` on the next save
* while ``MIXAR_BYOK_BASE_URL`` is set, the field is read-only and says so

Registration is defensive on purpose: the properties and the payload patch are
installed at import time *and* from ``register()``, both idempotent, so the
section works regardless of which auto-discovery hook the bootstrap uses for
this folder.
"""

import bpy
from bpy.props import StringProperty
from bpy.types import Operator

from mixar.config.logging_config import get_logger

from ...core import base_url as base_url_core
from .byok_ops import MIXAR_BYOK_OT_open_dialog

logger = get_logger(__name__)

# Holds text the user typed that did not validate, so the field doesn't snap
# back to the stored value mid-edit and the error stays on screen.
_draft = {"value": None}


# ---------------------------------------------------------------------------
# RNA property backing
# ---------------------------------------------------------------------------

def _get_base_url(self) -> str:
    if _draft["value"] is not None:
        return _draft["value"]
    try:
        return base_url_core.resolve()[0]
    except Exception as exc:  # noqa: BLE001
        logger.debug("BYOK base URL read failed: %s", exc)
        return ""


def _set_base_url(self, value) -> None:
    text = value or ""
    if base_url_core.is_locked_by_env():
        self.byok_base_url_status = "Locked by {0}".format(base_url_core.ENV_VAR)
        return
    try:
        stored = base_url_core.set_stored(text)
    except base_url_core.BaseUrlError as exc:
        _draft["value"] = text
        self.byok_base_url_status = str(exc)
        return
    except Exception as exc:  # noqa: BLE001
        _draft["value"] = text
        self.byok_base_url_status = "Could not save: {0}".format(exc)
        return
    _draft["value"] = None
    self.byok_base_url_status = "Saved" if stored else "Cleared — using the default endpoint"


# ---------------------------------------------------------------------------
# Operators
# ---------------------------------------------------------------------------

class MIXAR_BYOK_OT_base_url_test(Operator):
    """Check that the custom base URL answers (401/403 still counts as reachable)"""
    bl_idname = "mixar_byok.base_url_test"
    bl_label = "Test Endpoint"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        wm = context.window_manager
        return bool((getattr(wm, 'byok_form_base_url', '') or '').strip())

    def execute(self, context):
        wm = context.window_manager
        wm.byok_base_url_status = "Testing..."
        try:
            base_url_core.probe(wm.byok_form_base_url, _on_probe_done)
        except base_url_core.BaseUrlError as exc:
            wm.byok_base_url_status = str(exc)
            self.report({'ERROR'}, str(exc))
            return {'CANCELLED'}
        _redraw()
        return {'FINISHED'}


class MIXAR_BYOK_OT_base_url_clear(Operator):
    """Forget the custom base URL and use the endpoint the backend picks"""
    bl_idname = "mixar_byok.base_url_clear"
    bl_label = "Clear"
    bl_options = {'INTERNAL'}

    @classmethod
    def poll(cls, context):
        return not base_url_core.is_locked_by_env()

    def execute(self, context):
        wm = context.window_manager
        _draft["value"] = None
        try:
            base_url_core.set_stored("")
        except Exception as exc:  # noqa: BLE001
            self.report({'ERROR'}, "Could not clear: {0}".format(exc))
            return {'CANCELLED'}
        wm.byok_base_url_status = "Cleared — using the default endpoint"
        _redraw()
        return {'FINISHED'}


def _on_probe_done(ok: bool, message: str) -> None:
    """Main-thread probe callback."""
    try:
        wm = bpy.context.window_manager
        wm.byok_base_url_status = message if ok else "Unreachable — {0}".format(message)
        _redraw()
    except Exception as exc:  # noqa: BLE001
        logger.debug("BYOK base URL probe callback failed: %s", exc)


def _redraw() -> None:
    try:
        for window in bpy.context.window_manager.windows:
            for area in window.screen.areas:
                area.tag_redraw()
                for region in area.regions:
                    region.tag_redraw()
    except Exception as exc:  # noqa: BLE001
        logger.debug("BYOK base URL redraw failed: %s", exc)


# ---------------------------------------------------------------------------
# Dialog section
# ---------------------------------------------------------------------------

def _draw_base_url_section(layout, wm, disabled: bool) -> None:
    locked = base_url_core.is_locked_by_env()

    box = layout.box()
    heading = box.row()
    heading.scale_y = 1.15
    heading.label(text="Custom endpoint", icon='URL')

    col = box.column(align=True)
    col.enabled = not disabled and not locked
    col.separator(factor=0.35)

    label_row = col.row()
    label_row.enabled = False
    label_row.label(text="Base URL")

    field_row = col.row(align=True)
    field_row.scale_y = 1.45
    field_row.prop(wm, 'byok_form_base_url', text="")
    field_row.operator(MIXAR_BYOK_OT_base_url_test.bl_idname, text="", icon='FILE_REFRESH')
    field_row.operator(MIXAR_BYOK_OT_base_url_clear.bl_idname, text="", icon='X')
    col.separator(factor=0.45)

    status = (wm.byok_base_url_status or "").strip()
    if status:
        status_row = box.row()
        status_row.alert = status.startswith(("Unreachable", "Refusing", "Could not", "Use an", "Missing", "URL", "Base URL", "Enter", "Locked"))
        status_row.label(
            text=status,
            icon='CHECKMARK' if status.startswith(("Reachable", "Saved", "Cleared")) else 'INFO',
        )

    box.separator(factor=0.4)
    for line in (
        base_url_core.describe(),
        "Leave empty to use the endpoint the Mixar backend picks for the provider.",
        "Point it at any OpenAI-compatible gateway, e.g. http://localhost:11434/v1.",
    ):
        row = box.row()
        row.enabled = False
        row.label(text=line, icon='INFO')

    if locked:
        env_row = box.row()
        env_row.enabled = False
        env_row.label(
            text="{0} is set, so this field is read-only.".format(base_url_core.ENV_VAR),
            icon='LOCKED',
        )


_ORIGINAL_DRAW_FORM = None


def _patched_draw_form(self, layout, wm, disabled: bool) -> None:
    """Upstream form, then our section. Never let the addition break the dialog."""
    _ORIGINAL_DRAW_FORM(self, layout, wm, disabled)
    try:
        _draw_base_url_section(layout, wm, disabled)
    except Exception as exc:  # noqa: BLE001
        logger.warning("Custom endpoint section failed to draw: %s", exc, exc_info=True)


# ---------------------------------------------------------------------------
# Install / uninstall
# ---------------------------------------------------------------------------

def _install_properties_and_patches() -> None:
    """Idempotent: WM properties, the payload patch and the draw wrapper."""
    global _ORIGINAL_DRAW_FORM

    WM = bpy.types.WindowManager
    if not hasattr(WM, 'byok_base_url_status'):
        WM.byok_base_url_status = StringProperty(default='', options={'SKIP_SAVE'})
    if not hasattr(WM, 'byok_form_base_url'):
        WM.byok_form_base_url = StringProperty(
            name="Base URL",
            description=(
                "Send agent provider requests to this base URL instead of the one the "
                "Mixar backend picks. Any OpenAI-compatible endpoint works. "
                "Leave empty for the default"
            ),
            maxlen=base_url_core.MAX_LENGTH,
            get=_get_base_url,
            set=_set_base_url,
            options={'SKIP_SAVE'},
        )

    if _ORIGINAL_DRAW_FORM is None:
        _ORIGINAL_DRAW_FORM = MIXAR_BYOK_OT_open_dialog._draw_form
        MIXAR_BYOK_OT_open_dialog._draw_form = _patched_draw_form

    base_url_core.install_patches()


# Exported for `classes`-style auto-discovery.
classes = (
    MIXAR_BYOK_OT_base_url_test,
    MIXAR_BYOK_OT_base_url_clear,
)

_registered_here = []


def register() -> None:
    for cls in classes:
        if not hasattr(bpy.types, cls.__name__):
            bpy.utils.register_class(cls)
            _registered_here.append(cls)
    _install_properties_and_patches()


def unregister() -> None:
    global _ORIGINAL_DRAW_FORM

    if _ORIGINAL_DRAW_FORM is not None:
        MIXAR_BYOK_OT_open_dialog._draw_form = _ORIGINAL_DRAW_FORM
        _ORIGINAL_DRAW_FORM = None
    base_url_core.remove_patches()

    WM = bpy.types.WindowManager
    for attr in ('byok_form_base_url', 'byok_base_url_status'):
        try:
            delattr(WM, attr)
        except AttributeError:
            pass

    while _registered_here:
        cls = _registered_here.pop()
        try:
            bpy.utils.unregister_class(cls)
        except Exception as exc:  # noqa: BLE001
            logger.debug("Could not unregister %s: %s", cls.__name__, exc)


# Import-time safety net: properties + payload patch must exist even if the
# bootstrap only picks up `classes` for this folder. Both calls are idempotent.
try:
    _install_properties_and_patches()
except Exception as exc:  # noqa: BLE001
    logger.debug("Deferred custom endpoint install: %s", exc)
