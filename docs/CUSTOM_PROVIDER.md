<!--
SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited

SPDX-License-Identifier: GPL-3.0-or-later
-->

# Custom provider (OpenAI-compatible)

Mixar's BYOK dialog only ever offered providers the backend catalog enables,
plus two client-side entries (OpenRouter and Codex). All of them pin the
endpoint server-side. This fork already let you override the base URL
(see [CUSTOM_BASE_URL.md](CUSTOM_BASE_URL.md)) - but there was no provider to
attach that URL to, so an Ollama / vLLM / LM Studio / LiteLLM box, or a gateway
the backend has never heard of, still could not be selected.

**Custom (OpenAI-compatible)** is that missing entry. It is always in the
Provider dropdown - offline, before login, and when the backend enables nothing
at all.

## Using it

1. Open the BYOK dialog (key icon in the Mixie Chat topbar).
2. Scroll to **Custom endpoint** and set your base URL, e.g.
   `http://localhost:11434/v1`. Hit **Test** to check it answers.
3. Set **Provider** to *Custom (OpenAI-compatible)*.
4. **Model**: free text, exactly as your endpoint serves it -
   `llama3.1:70b`, `Qwen/Qwen2.5-Coder-32B-Instruct`, an Azure deployment name.
   There is no dropdown, because a custom endpoint has no catalog to read.
5. **API Key**: required. Endpoints that ignore auth still accept any
   placeholder, and the field keeps the saved row honest.
6. **Save**.

The Save button stays greyed out until all three exist. The dialog says which
one is missing.

## What is sent

```
PUT /agent/byok
{ "provider": "custom", "model": "<your model>",
  "api_key": "<your key>", "base_url": "<resolved base URL>" }
```

`base_url` is added by the payload patch in `core/base_url.py`, so the endpoint
is stored in exactly one place. Resolution order is unchanged:

| Priority | Source                                   |
|----------|------------------------------------------|
| 1        | `MIXAR_BYOK_BASE_URL` environment variable |
| 2        | The value stored from the dialog          |
| 3        | Platform default (not used by this provider) |

When the env var is set it wins and the field is locked - the custom provider
follows the same rule, and its form shows the endpoint read-only so there is
never a second URL field competing with the one above it.

## Requirements for the endpoint

* OpenAI-compatible `/chat/completions`.
* **Tool / function calling.** The agent drives Blender through tools; a model
  without them will chat and do nothing. This is the most common cause of
  "it answers but never touches my scene".
* Reachable from the machine running Mixar. `localhost` is fine.

## Troubleshooting

| Symptom | Cause |
|---|---|
| Save is greyed out | No endpoint, no model, or no key - the dialog names the missing one. |
| "No endpoint yet" in red | The Custom endpoint field is empty; set it first. |
| Endpoint field is locked | `MIXAR_BYOK_BASE_URL` is set in the environment. |
| 404 on save | Base URL is missing its version path - most servers want `/v1`. |
| Provider error 400 about tools | The model has no tool calling; see [PROVIDER_ERROR_400_TOOLS.md](PROVIDER_ERROR_400_TOOLS.md). |
| Model rejected by the server | The name is not what the endpoint serves - it is passed through verbatim. |

## How it is built

No upstream file is edited; both modules are new and the feature installs
itself with runtime patches, the same approach as the base URL work. That is
what keeps upstream merges clean.

| File | Role |
|---|---|
| `src/scripts/mixar/modules/byok/core/custom_provider.py` | Rules: the dropdown item, the id check, the list merge, the save validation. No `bpy`, so it is unit-tested. |
| `src/scripts/mixar/modules/byok/ui/operators/byok_custom_provider_ops.py` | Blender side: the `byok_form_custom_model` property and the patches. |

Patched at runtime, all restored on unregister:

* `get_provider_items` in **both** `byok_props` and `model_suggestions`.
  `byok_props` imports the function by name, so patching only
  `model_suggestions` would never reach the dropdown; patching
  `model_suggestions` as well is what makes "Current configuration" print the
  friendly label instead of the raw id.
* `MIXAR_BYOK_OT_open_dialog._draw_cloud_fields` - upstream's `_draw_form`
  routes every non-OpenRouter, non-Codex provider there, so wrapping that one
  method (rather than `_draw_form`) composes with the base URL section instead
  of fighting it.
* `MIXAR_BYOK_OT_save.poll` / `.execute` - custom validation and
  `provider='custom'` on save.
* `MIXAR_BYOK_OT_open_dialog.invoke` - prefills the active custom model when
  the dialog reopens.

## Tests

`tests/test_byok_custom_provider.py` covers the rules directly and, because the
UI half cannot be imported without Blender, statically asserts that every
upstream symbol it patches still exists. An upstream rename fails the suite
instead of silently disabling the feature. CI additionally byte-compiles both
new files, and both are in the installer overlay marker lists.

## Known gap

Logging out clears the BYOK form fields from a hardcoded list in
`space_mixie_chat/ui/operators/auth_ops.py`, which does not include
`byok_form_custom_model`. The leftover value is a model name, not credential
material - keys and the Codex bundle are still wiped. Fixing it means editing
an upstream file, so it is left alone deliberately.
