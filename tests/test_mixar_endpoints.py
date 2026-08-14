# SPDX-FileCopyrightText: 2026 Mixar fork contributors
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Tests for runtime endpoint resolution (pure pytest, bpy not required)."""

import json

import pytest

from mixar.config import endpoints


@pytest.fixture(autouse=True)
def isolated_config(tmp_path, monkeypatch):
    """Keep every test away from the real user config and environment."""
    monkeypatch.setenv(endpoints.ENV_USER_CONFIG_DIR, str(tmp_path))
    for name in (
        endpoints.ENV_BACKEND,
        endpoints.ENV_FRONTEND,
        endpoints.ENV_WS,
        endpoints.ENV_ALLOW_INSECURE,
    ):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(endpoints, "_bundled_config", lambda: {})
    endpoints.invalidate()
    yield
    endpoints.invalidate()


def test_defaults_when_nothing_is_configured():
    resolved = endpoints.get_endpoints()
    assert resolved.backend == endpoints.DEFAULT_BACKEND_URL
    assert resolved.frontend == endpoints.DEFAULT_FRONTEND_URL
    assert resolved.ws == "wss://api.mixar.app"
    assert resolved.source == "default"


def test_build_time_config_is_used(monkeypatch):
    monkeypatch.setattr(
        endpoints,
        "_bundled_config",
        lambda: {
            "backend_url": "https://api.staging.example",
            "frontend_url": "https://app.staging.example",
        },
    )
    endpoints.invalidate()
    resolved = endpoints.get_endpoints()
    assert resolved.backend == "https://api.staging.example"
    assert resolved.frontend == "https://app.staging.example"
    assert resolved.source == "build"


def test_user_override_beats_build_time(monkeypatch):
    monkeypatch.setattr(
        endpoints, "_bundled_config", lambda: {"backend_url": "https://api.mixar.app"}
    )
    endpoints.set_custom_endpoints(backend_url="https://api.my-host.example/")
    resolved = endpoints.get_endpoints()
    assert resolved.backend == "https://api.my-host.example"
    assert resolved.source == "user"
    # A custom backend must not keep pointing the SSO flow at hosted Mixar.
    assert resolved.frontend == "https://api.my-host.example"


def test_environment_beats_user_override(monkeypatch):
    endpoints.set_custom_endpoints(backend_url="https://api.my-host.example")
    monkeypatch.setenv(endpoints.ENV_BACKEND, "https://api.from-env.example")
    endpoints.invalidate()
    resolved = endpoints.get_endpoints()
    assert resolved.backend == "https://api.from-env.example"
    assert resolved.source == "env"


def test_overrides_are_persisted_atomically(tmp_path):
    endpoints.set_custom_endpoints(
        backend_url="api.my-host.example", frontend_url="https://app.my-host.example"
    )
    stored = json.loads((tmp_path / endpoints.OVERRIDES_FILENAME).read_text())
    assert stored["enabled"] is True
    assert stored["backend_url"] == "https://api.my-host.example"
    assert stored["frontend_url"] == "https://app.my-host.example"
    assert not list(tmp_path.glob("*.tmp.*"))


def test_clear_returns_to_build_defaults(monkeypatch):
    monkeypatch.setattr(
        endpoints, "_bundled_config", lambda: {"backend_url": "https://api.mixar.app"}
    )
    endpoints.set_custom_endpoints(backend_url="https://api.my-host.example")
    endpoints.clear_custom_endpoints()
    assert endpoints.get_endpoints().backend == "https://api.mixar.app"


@pytest.mark.parametrize(
    "raw,expected",
    (
        ("api.example.com", "https://api.example.com"),
        ("https://api.example.com/", "https://api.example.com"),
        ("https://api.example.com/v2/", "https://api.example.com/v2"),
        ("https://api.example.com?debug=1", "https://api.example.com"),
        ("http://localhost:8000", "http://localhost:8000"),
        ("http://192.168.1.10:8000", "http://192.168.1.10:8000"),
    ),
)
def test_normalize_url_accepts(raw, expected):
    assert endpoints.normalize_url(raw) == expected


@pytest.mark.parametrize(
    "raw",
    (
        "",
        "   ",
        "ftp://api.example.com",
        "https://",
        "http://api.example.com",  # public host over plain http
        "https://api example.com",
    ),
)
def test_normalize_url_rejects(raw):
    with pytest.raises(endpoints.EndpointError):
        endpoints.normalize_url(raw)


def test_public_http_allowed_when_opted_in():
    assert (
        endpoints.normalize_url("http://api.example.com", True)
        == "http://api.example.com"
    )


def test_invalid_url_never_gets_persisted(tmp_path):
    with pytest.raises(endpoints.EndpointError):
        endpoints.set_custom_endpoints(backend_url="not a url at all")
    assert not (tmp_path / endpoints.OVERRIDES_FILENAME).exists()


@pytest.mark.parametrize(
    "raw,expected",
    (
        ("https://api.example.com", "wss://api.example.com"),
        ("http://localhost:8000", "ws://localhost:8000"),
        ("wss://api.example.com/socket", "wss://api.example.com/socket"),
    ),
)
def test_websocket_normalisation(raw, expected):
    assert endpoints.normalize_ws_url(raw) == expected


def test_ws_override_is_used():
    endpoints.set_custom_endpoints(
        backend_url="https://api.my-host.example",
        ws_url="wss://realtime.my-host.example/ws",
    )
    assert endpoints.get_endpoints().ws == "wss://realtime.my-host.example/ws"


def test_corrupt_overrides_file_is_ignored(tmp_path):
    (tmp_path / endpoints.OVERRIDES_FILENAME).write_text("{not json")
    endpoints.invalidate()
    assert endpoints.get_endpoints().backend == endpoints.DEFAULT_BACKEND_URL


def test_invalid_stored_url_falls_back(tmp_path, monkeypatch):
    (tmp_path / endpoints.OVERRIDES_FILENAME).write_text(
        json.dumps({"enabled": True, "backend_url": "gopher://nope"})
    )
    monkeypatch.setattr(
        endpoints, "_bundled_config", lambda: {"backend_url": "https://api.mixar.app"}
    )
    endpoints.invalidate()
    resolved = endpoints.get_endpoints()
    assert resolved.backend == "https://api.mixar.app"
    assert resolved.source == "build"


def test_api_url_joins_paths():
    endpoints.set_custom_endpoints(backend_url="https://api.my-host.example")
    assert endpoints.api_url("/v1/chat") == "https://api.my-host.example/v1/chat"
    assert endpoints.api_url("v1/chat") == "https://api.my-host.example/v1/chat"
    assert endpoints.api_url() == "https://api.my-host.example"


def test_describe_reports_resolution_source():
    endpoints.set_custom_endpoints(backend_url="https://api.my-host.example")
    info = endpoints.describe()
    assert info["resolved_from"] == "user"
    assert info["backend_url"] == "https://api.my-host.example"
    assert info["overrides_path"].endswith(endpoints.OVERRIDES_FILENAME)


def test_resolution_is_cached(monkeypatch):
    calls = []

    def counting_resolve():
        calls.append(1)
        return endpoints.Endpoints(
            endpoints.DEFAULT_BACKEND_URL,
            endpoints.DEFAULT_FRONTEND_URL,
            "wss://api.mixar.app",
            "default",
            False,
        )

    monkeypatch.setattr(endpoints, "_resolve", counting_resolve)
    endpoints.invalidate()
    for _ in range(25):
        endpoints.get_endpoints()
    assert len(calls) == 1
