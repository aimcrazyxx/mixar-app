# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""UI for custom Mixar endpoints (backend / frontend / WebSocket base URLs).

Lives in ``modules/**/ui/`` so the existing bootstrap auto-discovery registers
it. Exposes:

* ``mixar.endpoints_settings`` - properties dialog to set a custom base URL.
* ``mixar.endpoints_test`` - modal, non-blocking reachability check.
* ``mixar.endpoints_reset`` - back to the build-time defaults.

All three are reachable from Blender's operator search (F3) and from the Edit
menu entry appended below.
"""

from __future__ import annotations

import threading

import bpy

try:  # package-relative import (mixar.modules.common.ui -> mixar.config)
    from ....config import endpoints as mixar_endpoints
except (ImportError, ValueError):  # pragma: no cover - flat module loading
    from mixar.config import endpoints as mixar_endpoints

try:
    from ....config import http as mixar_http
except (ImportError, ValueError):  # pragma: no cover
    try:
        from mixar.config import http as mixar_http
    except ImportError:
        mixar_http = None


def _probe(base_url, result):
    """Reachability probe that never raises into the UI thread."""
    if mixar_http is not None:
        try:
            ok, message = mixar_http.probe(base_url)
            result["ok"], result["message"] = ok, message
            return
        except Exception as exc:  # pragma: no cover - fall through to urllib
            result["message"] = "probe failed: {0}".format(exc)

    import urllib.error
    import urllib.request

    try:
        with urllib.request.urlopen(base_url, timeout=8) as response:
            result["ok"] = True
            result["message"] = "{0} answered HTTP {1}".format(
                base_url, response.status
            )
    except urllib.error.HTTPError as exc:
        result["ok"] = exc.code < 500
        result["message"] = "{0} answered HTTP {1}".format(base_url, exc.code)
    except Exception as exc:
        result["ok"] = False
        result["message"] = "{0} is unreachable: {1}".format(base_url, exc)


class MIXAR_OT_endpoints_settings(bpy.types.Operator):
    """Point this Mixar build at a custom backend without rebuilding it"""

    bl_idname = "mixar.endpoints_settings"
    bl_label = "Mixar Endpoint Settings"
    bl_options = {"REGISTER"}

    use_custom: bpy.props.BoolProperty(
        name="Use custom endpoints",
        description="Override the URLs that were baked in at build time",
        default=False,
    )
    backend_url: bpy.props.StringProperty(
        name="Backend base URL",
        description="API base URL, e.g. https://api.my-mixar.example or http://localhost:8000",
        default="",
    )
    frontend_url: bpy.props.StringProperty(
        name="Frontend base URL",
        description="Browser-facing base URL used for SSO login (defaults to the backend URL)",
        default="",
    )
    ws_url: bpy.props.StringProperty(
        name="WebSocket URL",
        description="Optional. Derived from the backend URL when left empty",
        default="",
    )
    allow_insecure: bpy.props.BoolProperty(
        name="Allow plain http:// on public hosts",
        description="Off by default. http:// is always allowed for localhost and LAN hosts",
        default=False,
    )

    def invoke(self, context, event):
        overrides = mixar_endpoints.load_overrides(refresh=True)
        resolved = mixar_endpoints.get_endpoints(refresh=True)
        self.use_custom = bool(overrides.get("enabled"))
        self.backend_url = overrides.get("backend_url") or resolved.backend
        self.frontend_url = overrides.get("frontend_url") or ""
        self.ws_url = overrides.get("ws_url") or ""
        self.allow_insecure = bool(overrides.get("allow_insecure"))
        return context.window_manager.invoke_props_dialog(self, width=520)

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.prop(self, "use_custom")

        column = layout.column()
        column.enabled = self.use_custom
        column.prop(self, "backend_url")
        column.prop(self, "frontend_url")
        column.prop(self, "ws_url")
        column.prop(self, "allow_insecure")

        info = mixar_endpoints.describe()
        box = layout.box()
        box.label(text="Currently in use", icon="URL")
        box.label(text="Backend: {0}".format(info["backend_url"]))
        box.label(text="Frontend: {0}".format(info["frontend_url"]))
        box.label(text="WebSocket: {0}".format(info["ws_url"]))
        box.label(text="Resolved from: {0}".format(info["resolved_from"]))
        if info["env_overrides"]:
            box.label(
                text="Environment overrides active: {0}".format(
                    ", ".join(sorted(info["env_overrides"]))
                ),
                icon="INFO",
            )

        row = layout.row(align=True)
        row.operator("mixar.endpoints_test", icon="WORLD")
        row.operator("mixar.endpoints_reset", icon="LOOP_BACK")

    def execute(self, context):
        try:
            if self.use_custom:
                resolved = mixar_endpoints.set_custom_endpoints(
                    backend_url=self.backend_url,
                    frontend_url=self.frontend_url,
                    ws_url=self.ws_url,
                    enabled=True,
                    allow_insecure=self.allow_insecure,
                )
            else:
                resolved = mixar_endpoints.clear_custom_endpoints()
        except mixar_endpoints.EndpointError as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}

        if mixar_http is not None:
            mixar_http.close_session()

        self.report(
            {"INFO"},
            "Mixar backend: {0} (sign out and back in to refresh your session)".format(
                resolved.backend
            ),
        )
        return {"FINISHED"}


class MIXAR_OT_endpoints_test(bpy.types.Operator):
    """Check that the configured backend answers, without freezing the UI"""

    bl_idname = "mixar.endpoints_test"
    bl_label = "Test Connection"
    bl_options = {"REGISTER"}

    _timer = None
    _thread = None
    _result = None

    def invoke(self, context, event):
        base_url = mixar_endpoints.get_endpoints().backend
        self._result = {"ok": False, "message": "timed out"}
        self._thread = threading.Thread(
            target=_probe, args=(base_url, self._result), daemon=True
        )
        self._thread.start()
        window_manager = context.window_manager
        self._timer = window_manager.event_timer_add(0.2, window=context.window)
        window_manager.modal_handler_add(self)
        return {"RUNNING_MODAL"}

    def modal(self, context, event):
        if event.type != "TIMER":
            return {"PASS_THROUGH"}
        if self._thread is not None and self._thread.is_alive():
            return {"PASS_THROUGH"}

        self._cleanup(context)
        ok = bool(self._result.get("ok"))
        self.report(
            {"INFO"} if ok else {"WARNING"}, self._result.get("message", "")
        )
        return {"FINISHED"}

    def cancel(self, context):
        self._cleanup(context)

    def _cleanup(self, context):
        if self._timer is not None:
            context.window_manager.event_timer_remove(self._timer)
            self._timer = None


class MIXAR_OT_endpoints_reset(bpy.types.Operator):
    """Forget custom endpoints and use the values baked in at build time"""

    bl_idname = "mixar.endpoints_reset"
    bl_label = "Reset To Defaults"
    bl_options = {"REGISTER"}

    def execute(self, context):
        resolved = mixar_endpoints.clear_custom_endpoints()
        if mixar_http is not None:
            mixar_http.close_session()
        self.report({"INFO"}, "Mixar backend: {0}".format(resolved.backend))
        return {"FINISHED"}


def _draw_menu_entry(self, context):
    self.layout.operator(
        MIXAR_OT_endpoints_settings.bl_idname, text="Mixar Endpoint Settings..."
    )


classes = (
    MIXAR_OT_endpoints_settings,
    MIXAR_OT_endpoints_test,
    MIXAR_OT_endpoints_reset,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    menu = getattr(bpy.types, "TOPBAR_MT_edit", None)
    if menu is not None:
        menu.append(_draw_menu_entry)


def unregister():
    menu = getattr(bpy.types, "TOPBAR_MT_edit", None)
    if menu is not None:
        try:
            menu.remove(_draw_menu_entry)
        except Exception:  # pragma: no cover - already removed
            pass
    for cls in reversed(classes):
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:  # pragma: no cover - not registered
            pass
