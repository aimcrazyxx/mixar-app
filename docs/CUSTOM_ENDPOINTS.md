<!--
SPDX-FileCopyrightText: 2026 Mixar fork contributors
SPDX-License-Identifier: GPL-3.0-or-later
-->

# Custom endpoints (custom base URL)

Upstream Mixar resolves `backend_url` / `frontend_url` **at build time**: the
values come from `.env`, get written into `config/mixar.json` by
`scripts/generate_config.py`, and the Python addon reads them through
`config.get_server_url()`. Changing the backend therefore meant rebuilding a
Blender fork.

This fork resolves the endpoints **at runtime**, so the same binary can talk to
the hosted backend, your own self-hosted backend, a staging deployment, or
`http://localhost:8000`.

## Precedence

Highest wins:

| # | Layer | Where | Good for |
|---|-------|-------|----------|
| 1 | Environment variables | `MIXAR_BACKEND_URL`, `MIXAR_FRONTEND_URL`, `MIXAR_WS_URL` | one-off launches, CI, scripted tests |
| 2 | User overrides | `endpoints.json` in the Blender user config dir (`.../config/mixar/`) | day-to-day use, set from the UI |
| 3 | Build-time config | `config/mixar.json` (generated from `.env`) | shipped defaults per environment |
| 4 | Built-in defaults | `https://api.mixar.app` / `https://www.mixar.app` | fallback |

The user layer is stored **outside the app bundle**, so it survives updates and
never writes into a code-signed `.app`.

## Using it

### From the UI

`F3` → *Mixar Endpoint Settings*, or **Edit → Mixar Endpoint Settings...**

- **Use custom endpoints** – master switch.
- **Backend base URL** – e.g. `https://api.my-mixar.example` or `http://localhost:8000`.
- **Frontend base URL** – optional; used for the browser SSO pages. Defaults to the backend URL.
- **WebSocket URL** – optional; derived from the backend URL (`https:` → `wss:`) when empty.
- **Allow plain http:// on public hosts** – off by default; `localhost` and LAN/private addresses never need it.
- **Test Connection** – non-blocking probe; any HTTP status below 500 counts as reachable (a `401` still proves something is listening).

After switching backends, sign out and back in: tokens are per-backend.

### From the environment

```bash
MIXAR_BACKEND_URL=http://localhost:8000 \
MIXAR_FRONTEND_URL=http://localhost:3000 \
./mixar
```

### From code

```python
from mixar.config import (
    api_url,
    get_endpoints,
    get_server_url,
    get_ws_url,
    set_custom_endpoints,
)

get_server_url()            # "http://localhost:8000"
api_url("/v1/chat")         # "http://localhost:8000/v1/chat"
get_ws_url()                # "ws://localhost:8000"
get_endpoints().source      # "env" | "user" | "build" | "default"

set_custom_endpoints(backend_url="https://api.my-mixar.example")
```

`mixar.config.http` adds a pooled session with retries and default timeouts:

```python
from mixar.config import http

response = http.get("/v1/models")          # keep-alive, retried, timed out
response = http.post("/v1/chat", json={})  # same session, same pool
```

## Validation rules

- Only `http`/`https` (and `ws`/`wss` for the socket URL) are accepted.
- Bare hosts are upgraded to `https://`.
- Trailing slashes, query strings and fragments are stripped.
- Plain `http://` on a public host is rejected unless explicitly allowed.
- Invalid values are **never persisted**, and a bad value already on disk is
  logged and skipped in favour of the next layer — the app cannot be bricked by
  a typo.

## Diagnostics

```python
from mixar.config import describe_endpoints
describe_endpoints()
# {'backend_url': ..., 'frontend_url': ..., 'ws_url': ...,
#  'resolved_from': 'user', 'allow_insecure': False,
#  'overrides_path': '/.../config/mixar/endpoints.json', 'env_overrides': {}}
```

The resolved endpoints are also logged once at INFO level on first use.

## Known limitation: the native layer

`src/source/creator/` (C++ startup, native auth dialog) reads
`mixar_env_config.h`, which is generated from `.env` at build time. This overlay
covers the Python layer — the AI agent, generation, asset search, WebSocket and
HTTP traffic. If your native login dialog must also point elsewhere, either
export `MIXAR_FRONTEND_URL` before launching or rebuild with `.env` pointing at
your host. Making the C++ side read the same runtime JSON is the natural next
step for this overlay.

## Tests

```bash
python3 -m pytest tests/test_mixar_endpoints.py -q
```
