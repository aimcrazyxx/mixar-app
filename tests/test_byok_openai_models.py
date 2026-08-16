# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Pure-Python tests for authenticated OpenAI-compatible model discovery."""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "src/scripts/mixar/modules/byok/core/openai_models.py"
)


def _load_module():
    package_name = "mixar_openai_models_test"
    package = types.ModuleType(package_name)
    package.__path__ = [str(MODULE_PATH.parent)]
    sys.modules[package_name] = package

    base = types.ModuleType(f"{package_name}.base_url")

    def normalize(raw):
        value = (raw or "").strip().rstrip("/")
        if not value:
            return ""
        if not value.startswith(("http://", "https://")):
            value = "https://" + value
        return value

    base.normalize = normalize
    sys.modules[base.__name__] = base

    spec = importlib.util.spec_from_file_location(
        f"{package_name}.openai_models", MODULE_PATH
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


models = _load_module()


def test_models_url_preserves_versioned_base_path():
    assert models.models_url("https://gateway.example/v1/") == (
        "https://gateway.example/v1/models"
    )


def test_parse_openai_shape_deduplicates_and_sorts():
    payload = {
        "object": "list",
        "data": [
            {"id": "z-model", "object": "model"},
            {"id": "a-model"},
            {"id": "z-model"},
            {"id": "  b-model  "},
            {"no_id": True},
        ],
    }
    assert models.parse_model_ids(payload) == ["a-model", "b-model", "z-model"]


@pytest.mark.parametrize("payload", [{}, {"models": []}, {"data": {}}, {"data": []}])
def test_rejects_non_openai_or_empty_payload(payload):
    with pytest.raises(models.ModelDiscoveryError):
        models.parse_model_ids(payload)


def test_fetch_sends_bearer_auth_and_accept_header(monkeypatch):
    captured = {}

    class Response:
        status_code = 200

        @staticmethod
        def json():
            return {"data": [{"id": "gpt-test"}]}

    def get(url, **kwargs):
        captured["url"] = url
        captured.update(kwargs)
        return Response()

    monkeypatch.setitem(sys.modules, "requests", types.SimpleNamespace(get=get))
    assert models.fetch_models_sync("https://api.example/v1", "secret-key") == [
        "gpt-test"
    ]
    assert captured["url"] == "https://api.example/v1/models"
    assert captured["headers"] == {
        "Accept": "application/json",
        "Authorization": "Bearer secret-key",
    }
    assert captured["timeout"] == models.REQUEST_TIMEOUT


def test_auth_failure_does_not_echo_key(monkeypatch):
    class Response:
        status_code = 401

    monkeypatch.setitem(
        sys.modules, "requests", types.SimpleNamespace(get=lambda *a, **k: Response())
    )
    with pytest.raises(models.ModelDiscoveryError) as exc:
        models.fetch_models_sync("https://api.example/v1", "never-print-me")
    assert "401" in str(exc.value)
    assert "never-print-me" not in str(exc.value)


def test_request_exception_does_not_echo_key(monkeypatch):
    def get(*_args, **_kwargs):
        raise RuntimeError("transport failed")

    monkeypatch.setitem(sys.modules, "requests", types.SimpleNamespace(get=get))
    with pytest.raises(models.ModelDiscoveryError) as exc:
        models.fetch_models_sync("https://api.example/v1", "never-print-me")
    assert "never-print-me" not in str(exc.value)
