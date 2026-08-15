<!--
SPDX-FileCopyrightText: 2026 Mixar fork contributors
SPDX-License-Identifier: GPL-3.0-or-later
-->

# Custom base URL in AI Provider Settings

Adds a **Custom endpoint → Base URL** field to the existing dialog
(top bar profile menu → *AI Provider Settings*, operator `mixar_byok.open_dialog`).

```
Provider setup
  Provider   [ Codex (ChatGPT sub) v ]
  Model      [ gpt-5.5              ]
  ...
Custom endpoint
  Base URL   [ https://gw.example.com/openai/v1 ] [test] [x]
  Saved
  Point it at any OpenAI-compatible gateway, e.g. http://localhost:11434/v1.
```

## How it behaves

| | |
|---|---|
| Precedence | `MIXAR_BYOK_BASE_URL` env var → saved value → backend default |
| Persistence | `byok.json` in the user config directory: Blender's own config dir, else `%APPDATA%\mixar` / `~/Library/Application Support/mixar` / `~/.config/mixar`. `MIXAR_USER_CONFIG_DIR` overrides it |
| Never touched | `config/mixar.json` inside the install directory — writing there needs admin rights, is wiped by updates and breaks the macOS signature |
| Saved when | immediately on edit (the field is RNA `get`/`set` backed by the store) |
| Reads | cached on (path, mtime, size): the field is read on every redraw, so re-parsing the file several times per frame was worth avoiding. An edit made by hand outside the app is still picked up |
| Writes | atomic (temp file + `os.replace`), so a crash mid-save cannot truncate the settings |
| Sent as | `base_url` in the `PUT /agent/byok` payload, **only when non-empty** |
| Empty value | payload is byte-identical to upstream — nothing regresses |
| Validation | `http`/`https` only, host required, no query/fragment, path preserved, trailing slash dropped |
| Plain `http://` | allowed for localhost/LAN; public hosts need `MIXAR_ALLOW_INSECURE_ENDPOINTS=1` |
| Test button | threaded `GET` of `/models`, `/v1/models`, `/`; anything under HTTP 500 counts as reachable (a `401` proves something is listening). A probe that fails outright still reports back, so the status never sticks on "Testing..." |

## Scope: the provider endpoint only

An earlier revision of this fork also repointed the *Mixar backend* itself, with
its own settings panel and env vars. That override was removed on request: the
hosted backend the build ships with is the default again, and this fork does not
touch it. Only the provider endpoint described here is configurable — which is
also the only one BYOK needs.

## Read this before expecting it to work end to end

BYOK is **server-mediated**: the dialog sends `{provider, model, api_key}` to
the Mixar backend, and the backend calls the provider. The client never talks
to the provider directly. So the field can only take effect where the backend
honours it:

- **Self-hosted / your own backend** — works, as long as it reads `base_url`
  from the BYOK payload. This is the intended target.
- **Hosted `api.mixar.app`** — the field is sent, but a backend that doesn't
  know it will ignore it or answer `422`. If saves start failing after you set
  a URL, clear the field (the `x` button) and the payload returns to upstream
  shape.

## Env-only usage

```bash
MIXAR_BYOK_BASE_URL=http://localhost:4000/v1 ./mixar
```

While that variable is set, the dialog field is read-only and labelled as
locked, so a machine-level setting can't be silently overridden per user.

## Implementation notes

No upstream file was modified. Two additions:

- `src/scripts/mixar/modules/byok/core/base_url.py` — validation, store,
  reachability probe, and the payload patch that adds `base_url` to
  `AgentService.save_credentials_all`
- `src/scripts/mixar/modules/byok/ui/operators/byok_base_url_ops.py` — the
  dialog section, installed by wrapping `MIXAR_BYOK_OT_open_dialog._draw_form`

Both the properties and the payload patch install idempotently from
`register()` and at import time, so the section appears regardless of which
auto-discovery hook the bootstrap applies to that folder. `unregister()`
restores the original method and drops the properties, so *Reload Scripts*
stays clean.

The status line is clipped to a single bounded string before it reaches RNA:
provider and socket errors can be long, multi-line text, and unbounded RNA
strings are a known hazard in this codebase (compare the `GRAPH_*_MAXLEN`
constants in `scene_graph`).

`tests/test_byok_base_url.py` covers the normalizer, the store, precedence and
the env lock without Blender; the packaging workflow byte-compiles both files
on every push, which is the only syntax gate the UI file can have — it imports
`bpy`, so no test on a bare runner can import it.

## See also

- [CUSTOM_PROVIDER.md](CUSTOM_PROVIDER.md) - the provider entry that puts this
  base URL to work: free-text model, your own key, any OpenAI-compatible
  endpoint.
