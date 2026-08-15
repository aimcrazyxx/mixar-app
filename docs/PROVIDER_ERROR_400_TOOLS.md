<!-- SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited -->
<!-- SPDX-License-Identifier: GPL-3.0-or-later -->

# The 400 INVALID_ARGUMENT on delegated tool calls

## Symptom

A prompt runs, the agent thinks for a while, and then one or more steps fail
with a wall of escaped JSON:

```
generation (failed): ClientError: 400 Bad Request. {'message': '{
  "error": {
    "code": 400,
    "message": "* GenerateContentRequest.tools[0].function_declarations[24]
                 .parameters.properties[location].items: missing field.
               * ... .function_declarations[11].properties[placements].items: missing field.
               ...",
    "status": "INVALID_ARGUMENT"
```

Observed on the `generation` and `modeling.environment` steps - the ones where
the agent delegates a sub-task to a model (generate a 3D asset, model an
environment). Declarations flagged so far: 11, 12, 15, 16, 17, 19, 24.
Parameters flagged: `placements`, `object_names`, `chain_ids`, `assignments`,
`mesh_names`, `location`, `look_at`, `rotation`.

## What the provider is actually complaining about

In the provider's schema dialect an array must declare the type of its
elements. This is rejected:

```json
{ "name": "location", "type": "array" }
```

and this is accepted:

```json
{ "name": "location", "type": "array", "items": { "type": "number" } }
```

The accepted subset is `type, format, description, nullable, enum, items,
properties, required, minItems, maxItems, propertyOrdering`. One malformed
entry invalidates the whole request, which is why the step fails before any
Blender work happens - and why the count of failures matches the count of
malformed fields, not anything about the scene.

## Why it happens with every provider

Because the failing request is not the one your selected provider serves. The
tool list is assembled by the Mixar backend and sent to the model it uses for
that sub-task, so the provider picked in *AI Provider Settings* (and its custom
base URL) does not change the malformed payload. Same 400, every provider.

## Why this repository cannot fix it

The declarations are not here. Verified against `Mixar-AI/mixar-app` at
`faff745`:

| Searched for | Hits |
| --- | --- |
| `function_declarations` | 0 |
| `modeling.environment` | 0 |
| `genai` | 0 |
| `look_at` | 0 |
| `tool_name` | 19, all client-side dispatch |

The client is a thin executor: it receives a tool name plus params and runs
`run_tool(scene, "<tool_name>", {<params>})`. The only JSON Schema shipped in
the repository is `scene_graph/core/tools.py::TOOL_SPECS`, and it declares no
array parameters at all - every one of its seven tools takes either nothing or
a single `object_name` string. `AGENT_TOOLS.md` confirms the direction of
travel: *"Hand this to an implementer to wire these into the agent/backend tool
registry"*. The registry lives on the server; the names in the error message
(`placements`, `chain_ids`, `mesh_names`, ...) match ordinary Python keyword
arguments in `moodboard`, `hunyuan`, `paint/core/agent_tools/` and `director`,
so the server's declarations were written to mirror those signatures, and the
list parameters were converted to `"type": "array"` without `items`.

## The upstream fix

In the backend tool registry, give every array parameter an `items` sub-schema.
For the eight flagged parameters that means:

| Parameter | `items` |
| --- | --- |
| `object_names`, `mesh_names`, `chain_ids` | `{"type": "string"}` |
| `location`, `look_at`, `rotation` | `{"type": "number"}` (plus `minItems: 3`, `maxItems: 3`) |
| `placements` | `{"type": "object", "properties": {"object_name": {"type": "string"}, "image_x": {"type": "number"}, "image_y": {"type": "number"}}}` |
| `assignments` | `{"type": "object"}` with the material-assignment fields |

A generic guard is worth adding too: walk every declaration before sending it
and attach a permissive `items` to any `array` that lacks one. That turns this
class of bug into a degraded schema instead of a hard 400.

## What this fork does about it

It cannot fix the schema, so it fixes the message.
`space_mixie_chat/core/provider_errors.py` classifies the raw text and
`steps_format.py` wraps `finish_step_on_bubble`, so a failed row reads:

> **Failed - backend tool schema**
> 8 array parameters were declared without the required 'items' sub-schema:
> placements, object_names, chain_ids, assignments, mesh_names, location,
> look_at, rotation. The provider refused the request: the tool list the Mixar
> backend sent with it is malformed. No prompt, scene or provider change avoids
> it, and a retry fails the same way.
> Provider said: ClientError: 400 Bad Request. ...

The original text is kept underneath, credential / quota / timeout / network
failures get their own one-line explanation, and an error the classifier does
not recognize is passed through untouched. There is no automatic retry:
`INVALID_ARGUMENT` is deterministic, so retrying only burns time.

Covered by `tests/test_provider_errors.py`, which the packaging workflow gates
on.
