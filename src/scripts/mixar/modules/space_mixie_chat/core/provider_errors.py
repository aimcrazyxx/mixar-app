# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later
"""Readable failure text for provider errors shown in the agent steps block.

No bpy imports - pure string work, unit-testable outside Blender.

Why this exists
---------------
When the agent hands a sub-task to a model (generating a 3D asset, modeling an
environment), the request that carries the tool list is assembled and sent by
the Mixar backend, not by this client. If one of those declarations is
malformed the provider rejects the WHOLE request, and the raw rejection lands
in the chat panel as a wall of escaped JSON, repeated once per offending field:

    ClientError: 400 Bad Request. {'message': '{ 'error': { 'code': 400,
    'message': '* GenerateContentRequest.tools[0].function_declarations[24]
    .parameters.properties[location].items: missing field. ...

That is unreadable, and it looks like the user's scene or prompt is at fault.
It is neither: an array parameter was declared without the ``items``
sub-schema that the provider requires.

Scope: make the row say what happened in one line and keep the original text
underneath. This CANNOT fix the declarations - they are not in this
repository. The client only dispatches ``run_tool(scene, name, params)``, and
the only JSON Schema shipped here (scene_graph/core/tools.py::TOOL_SPECS)
declares no array parameters at all. See docs/PROVIDER_ERROR_400_TOOLS.md.
"""
import re

# The cap finish_step_on_bubble already applied to row.detail. Chat step rows
# are unbounded StringProperty fields, so staying inside a bound the UI is
# known to survive is deliberate.
MAX_DETAIL = 500

# How many parameter names to spell out before summarizing the rest.
_MAX_FIELDS_SHOWN = 8

PROVIDER_SCHEMA = "provider_schema"
AUTH = "auth"
QUOTA = "quota"
TIMEOUT = "timeout"
NETWORK = "network"
UNKNOWN = "unknown"

# (kind, needles) checked in order, first match wins - so the specific schema
# signature is recognized before a generic "400 bad request" would be.
_SIGNATURES = (
    (PROVIDER_SCHEMA, (
        "function_declarations", "generatecontentrequest", "missing field",
        "invalid_argument", "invalid json payload",
    )),
    (AUTH, (
        "unauthorized", "permission_denied", "api key", "api_key",
        "invalid authentication", "401", "403",
    )),
    (QUOTA, (
        "resource_exhausted", "insufficient_quota", "rate limit",
        "rate_limit", "quota", "too many requests", "429",
        "not enough credits",
    )),
    (TIMEOUT, ("deadline exceeded", "timed out", "timeout", "504")),
    (NETWORK, (
        "connection refused", "connection reset", "connection aborted",
        "failed to establish", "getaddrinfo", "name or service not known",
        "ssl", "temporarily unavailable", "502", "503",
    )),
)

_HEADLINES = {
    PROVIDER_SCHEMA: (
        "The provider refused the request: the tool list the Mixar backend "
        "sent with it is malformed. No prompt, scene or provider change "
        "avoids it, and a retry fails the same way."
    ),
    AUTH: (
        "The provider refused the credentials. Check the key and the base URL "
        "in AI Provider Settings."
    ),
    QUOTA: (
        "The provider throttled this key or it ran out of quota. Wait, or use "
        "a key that still has quota."
    ),
    TIMEOUT: "The provider did not answer in time. This one is worth retrying.",
    NETWORK: (
        "The provider could not be reached. Check the connection and the base "
        "URL in AI Provider Settings."
    ),
    UNKNOWN: "",
}

_LABELS = {
    PROVIDER_SCHEMA: "Failed - backend tool schema",
    AUTH: "Failed - provider credentials",
    QUOTA: "Failed - provider quota",
    TIMEOUT: "Failed - provider timeout",
    NETWORK: "Failed - provider unreachable",
    UNKNOWN: "Failed",
}

# Only these are transient. INVALID_ARGUMENT is deterministic: the same request
# is rejected every single time, so it must never be retried automatically.
_RETRYABLE = frozenset({TIMEOUT, NETWORK, QUOTA})

_PROPERTY_RE = re.compile(r"properties\[([A-Za-z0-9_]+)\]")
_DECLARATION_RE = re.compile(r"function_declarations\[(\d+)\]")


def _as_text(message) -> str:
    """Never raise on whatever the backend put in the error field."""
    if isinstance(message, str):
        return message
    return "" if message is None else str(message)


def classify(message) -> str:
    """Bucket a raw provider/tool error message into one of the kinds above."""
    lowered = _as_text(message).lower()
    if not lowered.strip():
        return UNKNOWN
    for kind, needles in _SIGNATURES:
        if any(needle in lowered for needle in needles):
            return kind
    return UNKNOWN


def is_retryable(kind) -> bool:
    """True when re-sending the same request could plausibly succeed."""
    return kind in _RETRYABLE


def _unique(values) -> list:
    seen = []
    for value in values:
        if value not in seen:
            seen.append(value)
    return seen


def missing_schema_fields(message) -> list:
    """The parameter names the provider flagged, de-duplicated, in order.

    The provider repeats one line per field, so the raw text names the same
    parameter several times across different declarations.
    """
    return _unique(_PROPERTY_RE.findall(_as_text(message)))


def offending_declarations(message) -> list:
    """The function_declarations indices the provider flagged, in order."""
    return _unique(_DECLARATION_RE.findall(_as_text(message)))


def collapse(message) -> str:
    """Flatten a JSON payload: escaped newlines and runs of blanks become one
    space, so the original still fits on the expanded detail line."""
    text = _as_text(message)
    for escape in ("\\n", "\\r", "\\t"):
        text = text.replace(escape, " ")
    return " ".join(text.split())


def label(kind) -> str:
    """The short row label for a kind."""
    return _LABELS.get(kind, _LABELS[UNKNOWN])


def headline(message, kind=None) -> str:
    """The explanation line, naming the flagged parameters when we know them."""
    kind = kind or classify(message)
    text = _HEADLINES.get(kind, "")
    if kind != PROVIDER_SCHEMA or not text:
        return text
    fields = missing_schema_fields(message)
    if not fields:
        return text
    shown = ", ".join(fields[:_MAX_FIELDS_SHOWN])
    if len(fields) > _MAX_FIELDS_SHOWN:
        shown += " (+%d more)" % (len(fields) - _MAX_FIELDS_SHOWN)
    count = len(fields)
    return "%d array parameter%s %s declared without the required 'items' " \
           "sub-schema: %s. %s" % (
               count, "" if count == 1 else "s",
               "was" if count == 1 else "were", shown, text)


def describe(message, cap: int = MAX_DETAIL):
    """Return ``(row_label, row_detail)`` for a failed step.

    A recognized provider failure becomes one explanatory line followed by the
    flattened original, so nothing is lost. An unrecognized error is passed
    through as-is - a Blender traceback keeps its line breaks and reads exactly
    as it did before this module existed. Both are truncated to ``cap``.
    """
    kind = classify(message)
    explanation = headline(message, kind)
    if explanation:
        original = collapse(message)
        body = explanation
        if original:
            body = "%s\n\nProvider said: %s" % (explanation, original)
    else:
        body = _as_text(message)
    if cap > 0 and len(body) > cap:
        body = body[:cap - 1].rstrip() + "\u2026"
    return label(kind), body
