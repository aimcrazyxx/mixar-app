# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Close the client-side transport loop for Custom (OpenAI-compatible).

The other BYOK tests validate the form rules, base-URL store and /models
parsing separately.  These tests pin the seam that matters in production:
``byok_client.save_credentials('custom', ...)`` must reach ``PUT /agent/byok``
with the resolved custom ``base_url`` in the JSON payload.

The Mixar backend itself is not part of this repository, so this is the
furthest deterministic integration boundary the desktop client can exercise.
"""

from __future__ import annotations

import importlib.util
import logging
import sys
import types
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "src" / "scripts" / "mixar" / "modules" / "byok" / "core"
OPS = (
    ROOT
    / "src"
    / "scripts"
    / "mixar"
    / "modules"
    / "byok"
    / "ui"
    / "operators"
    / "byok_custom_provider_ops.py"
)


def _package(name: str, path: Path | None = None):
    module = types.ModuleType(name)
    if path is not None:
        module.__path__ = [str(path)]
    sys.modules[name] = module
    return module


def _load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def test_custom_save_reaches_byok_put_with_resolved_base_url(monkeypatch, tmp_path):
    """BYOK client -> AgentService patch -> PUT payload, without Blender/network."""
    # Isolated package tree so importing these two production modules cannot
    # pull the rest of Blender/Mixar into the bare pytest process.
    _package("mixar", ROOT / "src" / "scripts" / "mixar")
    _package("mixar.config")
    logging_config = types.ModuleType("mixar.config.logging_config")
    logging_config.get_logger = logging.getLogger
    sys.modules[logging_config.__name__] = logging_config

    _package("mixar.modules")
    _package("mixar.modules.byok")
    _package("mixar.modules.byok.core", CORE)
    _package("mixar.modules.common")
    api = _package("mixar.modules.common.api")
    services = _package("mixar.modules.common.api.services")

    class APIResponse:
        def __init__(self, success=True, data=None, status_code=200):
            self.success = success
            self.data = data
            self.status_code = status_code

    class AgentService:
        def __init__(self):
            self.calls = []

        # This upstream-looking method must be replaced by base_url.install_patches.
        def save_credentials_all(self, provider, model, api_key):
            raise AssertionError("base_url payload patch was not installed")

        def put(self, path, json=None):
            self.calls.append((path, json))
            return APIResponse(
                True,
                {"status": "success", "data": {"saved": True}},
                200,
            )

    agent_service_module = types.ModuleType(
        "mixar.modules.common.api.services.agent_service"
    )
    agent_service_module.AgentService = AgentService
    sys.modules[agent_service_module.__name__] = agent_service_module
    services.agent_service = agent_service_module

    service = AgentService()
    api.APIResponse = APIResponse
    api.get_agent_service = lambda: service

    base_url = _load(
        "mixar.modules.byok.core.base_url",
        CORE / "base_url.py",
    )
    monkeypatch.setenv(base_url.ENV_CONFIG_DIR, str(tmp_path))
    monkeypatch.delenv(base_url.ENV_VAR, raising=False)
    endpoint = base_url.set_stored("http://localhost:11434/v1/")
    assert endpoint == "http://localhost:11434/v1"
    base_url.install_patches()

    byok_client = _load(
        "mixar.modules.byok.core.byok_client",
        CORE / "byok_client.py",
    )

    class InlineThread:
        def __init__(self, target=None, **_kwargs):
            self.target = target

        def start(self):
            self.target()

    monkeypatch.setattr(byok_client.threading, "Thread", InlineThread)
    monkeypatch.setattr(
        byok_client,
        "_schedule_on_main",
        lambda callback, *args: callback(*args),
    )

    callbacks = []
    byok_client.save_credentials(
        provider="custom",
        model="Qwen/Qwen3-Coder",
        api_key="sk-local",
        on_done=lambda *args: callbacks.append(args),
    )

    assert callbacks == [(True, {"saved": True}, None)]
    assert service.calls == [
        (
            "byok",
            {
                "provider": "custom",
                "model": "Qwen/Qwen3-Coder",
                "api_key": "sk-local",
                "base_url": "http://localhost:11434/v1",
            },
        )
    ]


def test_custom_ui_save_is_wired_to_the_transport_contract():
    """Pin the UI -> byok_client link that feeds the runtime test above."""
    source = OPS.read_text(encoding="utf-8")
    assert "byok_ops.byok_client.save_credentials(" in source
    assert "provider=custom_provider.PROVIDER_ID" in source
    assert "model=model" in source
    assert "api_key=api_key" in source
    assert "base_url_core.install_patches()" in source
