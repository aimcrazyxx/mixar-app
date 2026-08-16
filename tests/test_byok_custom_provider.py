# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Rules behind the "Custom (OpenAI-compatible)" provider.

``core/custom_provider.py`` imports no ``bpy``, so it loads straight from disk.
``ui/operators/byok_custom_provider_ops.py`` cannot be imported on a bare
runner, so it gets the same treatment as the other UI module in this fork -
CI's compileall gate - plus static checks that the upstream symbols it
monkeypatches still exist. Without those, an upstream rename would disable the
whole feature at runtime with every test still green.
"""

from __future__ import annotations

import ast
import importlib.util
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
BYOK_DIR = REPO_ROOT / "src" / "scripts" / "mixar" / "modules" / "byok"
CORE_PATH = BYOK_DIR / "core" / "custom_provider.py"
OPS_PATH = BYOK_DIR / "ui" / "operators" / "byok_custom_provider_ops.py"
UPSTREAM_OPS_PATH = BYOK_DIR / "ui" / "operators" / "byok_ops.py"
PROPS_PATH = BYOK_DIR / "ui" / "properties" / "byok_props.py"

ENDPOINT = "http://localhost:11434/v1"


def _load_module(path: Path, name: str):
    if not path.exists():
        pytest.skip("%s not found" % path, allow_module_level=True)
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        pytest.skip("cannot load %s" % path, allow_module_level=True)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


custom_provider = _load_module(CORE_PATH, "mixar_custom_provider_under_test")


def _tree(path: Path) -> ast.Module:
    return ast.parse(path.read_text(encoding="utf-8"), filename=str(path))


def _toplevel_names(tree: ast.Module) -> set:
    names = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    names.add(target.id)
    return names


def _method_names(tree: ast.Module, class_name: str) -> set:
    for node in tree.body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return {
                child.name
                for child in node.body
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef))
            }
    return set()


# ---------------------------------------------------------------------------
# The dropdown entry
# ---------------------------------------------------------------------------

class TestProviderItem:
    def test_item_is_a_blender_enum_triplet(self):
        item = custom_provider.PROVIDER_ITEM
        assert len(item) == 3
        assert all(isinstance(part, str) for part in item)
        assert item[0] == custom_provider.PROVIDER_ID == "custom"
        assert item[1].strip(), "the dropdown needs a visible label"
        assert item[2].strip(), "the dropdown needs a tooltip"

    def test_id_does_not_collide_with_the_other_client_side_options(self):
        # openrouter / codex are upstream's; NONE is its sentinel id.
        assert custom_provider.PROVIDER_ID not in {"openrouter", "codex", "NONE"}

    def test_no_model_is_prefilled(self):
        # A default slug would save a model the endpoint may not serve.
        assert custom_provider.DEFAULT_MODEL == ""


class TestWithCustomItem:
    def test_appends_once_after_the_catalog(self):
        catalog = [("openai", "OpenAI", ""), ("anthropic", "Anthropic", "")]
        merged = custom_provider.with_custom_item(catalog)
        assert [item[0] for item in merged] == ["openai", "anthropic", "custom"]

    def test_is_idempotent(self):
        once = custom_provider.with_custom_item([("openai", "OpenAI", "")])
        twice = custom_provider.with_custom_item(once)
        assert twice == once
        assert [item[0] for item in twice].count("custom") == 1

    def test_offered_when_the_backend_lists_nothing(self):
        # Must be selectable offline, before login, and with an empty catalog.
        assert custom_provider.with_custom_item([]) == [custom_provider.PROVIDER_ITEM]
        assert custom_provider.with_custom_item(None) == [custom_provider.PROVIDER_ITEM]

    def test_keeps_the_loading_sentinel_in_front(self):
        sentinel = ("NONE", "Loading...", "")
        merged = custom_provider.with_custom_item([sentinel])
        assert merged[0] == sentinel
        assert merged[-1][0] == "custom"

    def test_does_not_mutate_the_caller_list(self):
        catalog = [("openai", "OpenAI", "")]
        custom_provider.with_custom_item(catalog)
        assert catalog == [("openai", "OpenAI", "")]

    def test_returns_tuples_blender_can_consume(self):
        merged = custom_provider.with_custom_item([["openai", "OpenAI", ""]])
        assert all(isinstance(item, tuple) for item in merged)


class TestIsCustom:
    def test_matches_only_the_custom_id(self):
        assert custom_provider.is_custom("custom") is True
        for other in ("openrouter", "codex", "openai", "", "NONE", "Custom", None):
            assert custom_provider.is_custom(other) is False


# ---------------------------------------------------------------------------
# Model names
# ---------------------------------------------------------------------------

class TestNormalizeModel:
    def test_trims_padding_from_a_paste(self):
        assert custom_provider.normalize_model("  llama3.1:70b \n") == "llama3.1:70b"

    def test_never_rewrites_the_name(self):
        for name in ("Qwen/Qwen2.5-Coder-32B-Instruct", "gpt-4o-mini", "my.deployment_1"):
            assert custom_provider.normalize_model(name) == name

    def test_empty_inputs_collapse_to_empty(self):
        for empty in ("", "   ", None):
            assert custom_provider.normalize_model(empty) == ""


# ---------------------------------------------------------------------------
# Save rules
# ---------------------------------------------------------------------------

class TestValidate:
    def test_accepts_a_complete_form(self):
        assert custom_provider.validate("llama3.1:70b", "sk-local", ENDPOINT) is None

    def test_missing_endpoint_is_reported_first(self):
        # Without it the key would be sent to the platform default host.
        problem = custom_provider.validate("", "", "")
        assert problem is not None
        assert "endpoint" in problem.lower()

    def test_missing_model_is_rejected(self):
        problem = custom_provider.validate("  ", "sk-local", ENDPOINT)
        assert problem is not None
        assert "model" in problem.lower()

    def test_overlong_model_is_rejected_after_trimming(self):
        too_long = "x" * (custom_provider.MODEL_MAX_LENGTH + 1)
        problem = custom_provider.validate("  " + too_long + "  ", "sk-local", ENDPOINT)
        assert problem is not None
        assert "maximum" in problem.lower()
        assert custom_provider.is_ready(too_long, "sk-local", ENDPOINT) is False

    def test_missing_key_is_rejected(self):
        problem = custom_provider.validate("llama3.1:70b", "   ", ENDPOINT)
        assert problem is not None
        assert "key" in problem.lower()

    def test_messages_tell_the_user_what_to_do(self):
        for args in (("", "", ""), ("", "k", ENDPOINT), ("m", "", ENDPOINT)):
            problem = custom_provider.validate(*args)
            assert problem and problem.endswith(".")
            assert len(problem) > 20


class TestIsReady:
    def test_mirrors_validate(self):
        assert custom_provider.is_ready("llama3.1:70b", "sk-local", ENDPOINT) is True
        assert custom_provider.is_ready("llama3.1:70b", "sk-local", "") is False
        assert custom_provider.is_ready("", "sk-local", ENDPOINT) is False
        assert custom_provider.is_ready("llama3.1:70b", "", ENDPOINT) is False


# ---------------------------------------------------------------------------
# The half that needs Blender: static contract only
# ---------------------------------------------------------------------------

class TestUiModuleContract:
    def test_the_ui_module_parses(self):
        if not OPS_PATH.exists():
            pytest.skip("UI module not present")
        _tree(OPS_PATH)  # raises SyntaxError if the file is broken

    def test_it_exposes_the_auto_discovery_contract(self):
        if not OPS_PATH.exists():
            pytest.skip("UI module not present")
        names = _toplevel_names(_tree(OPS_PATH))
        assert {"classes", "register", "unregister"} <= names

    def test_upstream_dialog_methods_it_patches_still_exist(self):
        if not UPSTREAM_OPS_PATH.exists():
            pytest.skip("byok_ops.py not present")
        methods = _method_names(_tree(UPSTREAM_OPS_PATH), "MIXAR_BYOK_OT_open_dialog")
        # _draw_cloud_fields is where upstream routes any non-openrouter,
        # non-codex provider - our whole form hangs off it.
        assert {"_draw_cloud_fields", "_draw_tall_prop", "invoke"} <= methods

    def test_upstream_save_methods_it_patches_still_exist(self):
        if not UPSTREAM_OPS_PATH.exists():
            pytest.skip("byok_ops.py not present")
        methods = _method_names(_tree(UPSTREAM_OPS_PATH), "MIXAR_BYOK_OT_save")
        assert {"poll", "execute"} <= methods

    def test_upstream_helpers_it_calls_still_exist(self):
        if not UPSTREAM_OPS_PATH.exists():
            pytest.skip("byok_ops.py not present")
        names = _toplevel_names(_tree(UPSTREAM_OPS_PATH))
        assert {"_on_save_done", "_redraw_mixie_chat_areas"} <= names

    def test_props_binds_the_items_function_by_name(self):
        """Why the dropdown patch has to target byok_props too.

        byok_props does `from ...core.model_suggestions import get_provider_items`,
        so patching model_suggestions alone would never reach the dropdown.
        """
        if not PROPS_PATH.exists():
            pytest.skip("byok_props.py not present")
        imported_by_name = {
            alias.name
            for node in ast.walk(_tree(PROPS_PATH))
            if isinstance(node, ast.ImportFrom)
            for alias in node.names
        }
        assert "get_provider_items" in imported_by_name

    def test_it_reuses_the_shared_base_url(self):
        """No second endpoint field, no second store."""
        if not OPS_PATH.exists():
            pytest.skip("UI module not present")
        source = OPS_PATH.read_text(encoding="utf-8")
        assert "base_url_core.get_base_url()" in source
        assert "byok_form_base_url" not in source
