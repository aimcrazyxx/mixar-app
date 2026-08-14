# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Tests for the BYOK custom base URL normalizer.

The module under test lives inside the Blender add-on tree, so it is loaded by
path with lightweight stand-ins for ``bpy`` and ``requests``. If the file or its
imports are unavailable in a bare interpreter the module skips instead of
failing, so this file never turns a green suite red on a machine without a
built bundle.
"""

from __future__ import annotations

import importlib.util
import sys
import types
from pathlib import Path

import pytest

MODULE_PATH = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "scripts"
    / "mixar"
    / "modules"
    / "byok"
    / "core"
    / "base_url.py"
)


def _install_stub(name: str, **attrs) -> None:
    if name in sys.modules:
        return
    module = types.ModuleType(name)
    for key, value in attrs.items():
        setattr(module, key, value)
    sys.modules[name] = module


def _load_module():
    if not MODULE_PATH.is_file():
        pytest.skip(f"{MODULE_PATH} not found", allow_module_level=True)

    _install_stub(
        "bpy",
        app=types.SimpleNamespace(
            timers=types.SimpleNamespace(
                register=lambda *args, **kwargs: None,
                is_registered=lambda *args, **kwargs: False,
            )
        ),
        types=types.SimpleNamespace(),
        utils=types.SimpleNamespace(),
        context=None,
    )
    _install_stub(
        "requests",
        get=lambda *args, **kwargs: None,
        RequestException=Exception,
    )

    spec = importlib.util.spec_from_file_location("byok_base_url_under_test", MODULE_PATH)
    if spec is None or spec.loader is None:
        pytest.skip("cannot build an import spec for base_url.py", allow_module_level=True)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:  # pragma: no cover - environment dependent
        pytest.skip(f"base_url.py not importable standalone: {exc}", allow_module_level=True)
    return module


base_url = _load_module()


@pytest.mark.parametrize(
    "raw, expected",
    [
        ("https://api.example.com", "https://api.example.com"),
        ("https://api.example.com/", "https://api.example.com"),
        ("  https://api.example.com/v1/  ", "https://api.example.com/v1"),
        ("api.example.com", "https://api.example.com"),
        # A path must survive: OpenAI-compatible gateways almost always live
        # under one, and dropping it would break every request.
        ("https://gateway.example.com/openai/v1", "https://gateway.example.com/openai/v1"),
        ("http://localhost:11434/v1", "http://localhost:11434/v1"),
        ("http://127.0.0.1:8000", "http://127.0.0.1:8000"),
    ],
)
def test_normalize_accepts(raw, expected):
    assert base_url.normalize(raw) == expected


@pytest.mark.parametrize(
    "raw",
    [
        "ftp://api.example.com",
        "file:///etc/passwd",
        "https://",
        "https:///v1",
        "https://api.example.com?key=abc",
        "https://api.example.com#fragment",
        "https://api example.com",
        "not a url at all",
    ],
)
def test_normalize_rejects(raw):
    with pytest.raises(base_url.BaseUrlError):
        base_url.normalize(raw)


def test_empty_input_clears_or_is_rejected():
    """Blank means "use the backend default"; either answer is acceptable."""
    try:
        assert not base_url.normalize("")
        assert not base_url.normalize("   ")
    except base_url.BaseUrlError:
        pass


def test_plain_http_on_public_host_needs_opt_in(monkeypatch):
    monkeypatch.delenv(base_url.ENV_ALLOW_INSECURE, raising=False)
    with pytest.raises(base_url.BaseUrlError):
        base_url.normalize("http://api.example.com")

    monkeypatch.setenv(base_url.ENV_ALLOW_INSECURE, "1")
    assert base_url.normalize("http://api.example.com") == "http://api.example.com"


def test_absurdly_long_url_is_rejected():
    too_long = "https://api.example.com/" + "x" * base_url.MAX_LENGTH
    with pytest.raises(base_url.BaseUrlError):
        base_url.normalize(too_long)


def test_env_var_locks_the_field(monkeypatch):
    monkeypatch.delenv(base_url.ENV_VAR, raising=False)
    assert not base_url.is_locked_by_env()

    monkeypatch.setenv(base_url.ENV_VAR, "https://env.example.com")
    assert base_url.is_locked_by_env()
