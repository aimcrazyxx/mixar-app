<!--
SPDX-FileCopyrightText: 2026 Mixar fork contributors
SPDX-License-Identifier: GPL-3.0-or-later
-->

# Custom OpenAI-compatible provider

Choose **Custom (OpenAI-compatible)** in the BYOK provider dialog and set:

- **Base URL** — include the API version path when required, for example
  `https://api.example.com/v1`.
- **API key** — sent only as `Authorization: Bearer <key>` and never persisted
  by model discovery.
- **Model** — any model ID may be typed manually.

Use **Load Models from /models** to request `Base URL + /models`. Mixar currently
accepts only the OpenAI list shape:

```json
{"data": [{"id": "model-id"}]}
```

The discovered dropdown is an optional shortcut. Selecting an item copies it
into the free-text Model field, which remains the final override. Results are
kept in memory, tied to the Base URL that produced them, and cleared on logout.
