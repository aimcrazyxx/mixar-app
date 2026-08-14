# SPDX-FileCopyrightText: 2024 Mixar Authors
# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Mixar Config
"""

from .config import (
    add_config,
    get_config,
    get_environment,
    get_frontend_url,
    get_server_url,
    load_mixar_config,
)
from .logging_config import get_logger

__all__ = [
    "get_logger",
    "get_config",
    "get_environment",
    "get_server_url",
    "get_frontend_url",
    "load_mixar_config",
    "add_config",
]

# --- BEGIN mixar-custom-endpoints overlay ---
from .endpoints import (  # noqa: E402,F811
    EndpointError,
    api_url,
    clear_custom_endpoints,
    get_endpoints,
    get_frontend_url,
    get_server_url,
    get_ws_url,
    set_custom_endpoints,
)
from .endpoints import describe as describe_endpoints  # noqa: E402
from .endpoints import invalidate as invalidate_endpoints  # noqa: E402
from .store import (  # noqa: E402,F811
    add_config,
    get_config,
    get_user_config_path,
    load_mixar_config,
    reload_config,
)

__all__ = list(__all__) + [
    "EndpointError",
    "api_url",
    "clear_custom_endpoints",
    "describe_endpoints",
    "get_endpoints",
    "get_user_config_path",
    "get_ws_url",
    "invalidate_endpoints",
    "reload_config",
    "set_custom_endpoints",
]
# --- END mixar-custom-endpoints overlay ---
