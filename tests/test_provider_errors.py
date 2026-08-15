# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Tests for the readable provider-error text in the agent steps block.

Hermetic on purpose: both modules under test are loaded straight from disk into
a synthetic package, so this file needs no bpy, no mixar package import and
none of the app's third-party dependencies. That is what lets the packaging
workflow gate on it with nothing but pytest installed.
"""
import importlib.util
import sys
import types
from pathlib import Path

CORE_DIR = (
    Path(__file__).resolve().parents[1]
    / "src" / "scripts" / "mixar" / "modules" / "space_mixie_chat" / "core"
)
PACKAGE = "mixar_fork_chat_core"

# The 400 this fork actually hit, trimmed to three of the repeated lines. Quote
# characters are simplified - the classifier only looks at the wording.
SCHEMA_ERROR = (
    "ClientError: 400 Bad Request. {'message': '{\\n  'error': {\\n    "
    "'code': 400,\\n    'message': '* GenerateContentRequest.tools[0]"
    ".function_declarations[24].parameters.properties[location].items: "
    "missing field.\\n* GenerateContentRequest.tools[0]"
    ".function_declarations[24].parameters.properties[look_at].items: "
    "missing field.\\n* GenerateContentRequest.tools[0]"
    ".function_declarations[11].parameters.properties[placements].items: "
    "missing field.\\n',\\n    'status': 'INVALID_ARGUMENT'\\n  }\\n}'}"
)


def _load_modules():
    package = sys.modules.get(PACKAGE)
    if package is None:
        package = types.ModuleType(PACKAGE)
        package.__path__ = [str(CORE_DIR)]
        sys.modules[PACKAGE] = package
    loaded = []
    # provider_errors first: steps_format imports it relatively.
    for name in ("provider_errors", "steps_format"):
        full = "%s.%s" % (PACKAGE, name)
        module = sys.modules.get(full)
        if module is None:
            spec = importlib.util.spec_from_file_location(
                full, CORE_DIR / ("%s.py" % name)
            )
            module = importlib.util.module_from_spec(spec)
            sys.modules[full] = module
            spec.loader.exec_module(module)
        loaded.append(module)
    return loaded


provider_errors, steps_format = _load_modules()


class _Row:
    """Stand-in for one MixieChatStepItem."""

    def __init__(self):
        self.item_id = ""
        self.kind = "TOOL"
        self.label = ""
        self.target = ""
        self.detail = ""
        self.status = "PENDING"


class _Rows(list):
    def add(self):
        row = _Row()
        self.append(row)
        return row


class _Bubble:
    def __init__(self):
        self.step_items = _Rows()
        self.steps_summary = ""


def _bubble_with_running_step(request_id="req-1", label="Generating"):
    bubble = _Bubble()
    row = bubble.step_items.add()
    row.item_id = request_id
    row.label = label
    row.status = "RUNNING"
    return bubble


# --- classification ---------------------------------------------------------


def test_the_schema_400_is_recognized():
    assert provider_errors.classify(SCHEMA_ERROR) == provider_errors.PROVIDER_SCHEMA


def test_every_flagged_parameter_is_listed_once_in_order():
    assert provider_errors.missing_schema_fields(SCHEMA_ERROR) == [
        "location",
        "look_at",
        "placements",
    ]


def test_the_repeated_declaration_indices_collapse():
    assert provider_errors.offending_declarations(SCHEMA_ERROR) == ["24", "11"]


def test_the_headline_names_the_missing_sub_schema():
    headline = provider_errors.headline(SCHEMA_ERROR)
    assert "items" in headline
    assert "location" in headline
    assert "backend" in headline.lower()


def test_credentials_quota_timeout_and_network_are_told_apart():
    cases = (
        ("AuthenticationError: 401 Incorrect API key provided",
         provider_errors.AUTH),
        ("429 RESOURCE_EXHAUSTED: quota exceeded for this project",
         provider_errors.QUOTA),
        ("ReadTimeout: the request timed out after 600s",
         provider_errors.TIMEOUT),
        ("ConnectionError: [Errno 111] Connection refused",
         provider_errors.NETWORK),
        ("", provider_errors.UNKNOWN),
    )
    for message, expected in cases:
        assert provider_errors.classify(message) == expected, message


def test_a_schema_400_is_never_retryable():
    assert not provider_errors.is_retryable(provider_errors.PROVIDER_SCHEMA)
    assert provider_errors.is_retryable(provider_errors.TIMEOUT)
    assert provider_errors.is_retryable(provider_errors.NETWORK)


def test_a_non_string_error_does_not_explode():
    label, detail = provider_errors.describe({"code": 400})
    assert label == "Failed"
    assert "400" in detail


# --- detail text ------------------------------------------------------------


def test_the_detail_explains_and_stays_within_the_cap():
    label, detail = provider_errors.describe(SCHEMA_ERROR)
    assert label == "Failed - backend tool schema"
    assert len(detail) <= provider_errors.MAX_DETAIL
    assert "3 array parameters" in detail
    assert "Provider said:" in detail
    # The escaped-newline wall is flattened into one readable line.
    assert "\\n" not in detail


def test_an_unrecognized_error_is_passed_through_verbatim():
    raw = "Traceback (most recent call last):\n  File \"x.py\"\nValueError: no"
    label, detail = provider_errors.describe(raw)
    assert label == "Failed"
    assert detail == raw


def test_the_cap_is_honoured_for_long_unknown_errors():
    label, detail = provider_errors.describe("x" * 900)
    assert label == "Failed"
    assert len(detail) == provider_errors.MAX_DETAIL
    assert detail.endswith("\u2026")


# --- wiring into the steps block --------------------------------------------


def test_a_failed_row_gets_the_readable_message():
    bubble = _bubble_with_running_step()
    updated = steps_format.finish_step_on_bubble(
        bubble, "req-1", {"success": False, "error": SCHEMA_ERROR}
    )
    row = bubble.step_items[0]
    assert updated is True
    assert row.status == "FAILED"
    assert row.label == "Failed - backend tool schema"
    assert "items" in row.detail
    assert len(row.detail) <= provider_errors.MAX_DETAIL


def test_a_failure_with_no_message_keeps_the_upstream_label():
    bubble = _bubble_with_running_step()
    steps_format.finish_step_on_bubble(bubble, "req-1", {"success": False})
    row = bubble.step_items[0]
    assert row.status == "FAILED"
    assert row.label == "Failed"
    assert row.detail == ""


def test_a_successful_row_is_untouched_by_the_wrapper():
    bubble = _bubble_with_running_step(label="Create cube")
    steps_format.finish_step_on_bubble(
        bubble, "req-1", {"success": True, "created_objects": ["Cube"]}
    )
    row = bubble.step_items[0]
    assert row.status == "DONE"
    assert row.label == "Create cube"
    assert row.target == "1 created"
    assert row.detail == "Created: Cube"


def test_an_unknown_request_id_updates_nothing():
    bubble = _bubble_with_running_step()
    updated = steps_format.finish_step_on_bubble(
        bubble, "other", {"success": False, "error": SCHEMA_ERROR}
    )
    assert updated is False
    assert bubble.step_items[0].status == "RUNNING"
    assert bubble.step_items[0].label == "Generating"


def test_the_newest_matching_row_wins():
    bubble = _bubble_with_running_step()
    second = bubble.step_items.add()
    second.item_id = "req-1"
    second.label = "Modeling environment"
    second.status = "RUNNING"
    steps_format.finish_step_on_bubble(
        bubble, "req-1", {"success": False, "error": SCHEMA_ERROR}
    )
    assert bubble.step_items[0].status == "RUNNING"
    assert bubble.step_items[1].label == "Failed - backend tool schema"


def test_the_upstream_helpers_still_work():
    assert steps_format.format_steps_summary(["READ", "READ"]) == "Read 2 files"
    assert steps_format.infer_step_kind("get_object_list") == "READ"
    assert steps_format.humanize_tool_name("create_cube") == "Create cube"
