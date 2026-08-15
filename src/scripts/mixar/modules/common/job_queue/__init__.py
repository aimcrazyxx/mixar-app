# SPDX-FileCopyrightText: 2026 Adeveda Enterprises Private Limited
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""Reusable feature-agnostic generation job queue.

Public surface:
    from mixar.modules.common.job_queue import (
        Job, JobState, get_queue, TERMINAL_STATES, RUNNING_STATES,
        # Helpers for concrete queue implementations
        get_queue_with_listener,
        create_scene_flag_listener,
        show_batch_summary_popup,
        download_images_to_moodboard,
        extract_image_urls,
    )

The names above are resolved lazily (PEP 562). Importing them eagerly here
created a cycle: this module pulled in ``core.queue_manager``, which reaches
``core.model_io`` -> ``core.downloader`` -> ``..constants``, and that last hop
re-entered this package while it was still half-executed, so ``get_queue`` did
not exist yet. It surfaced as::

    ImportError: cannot import name 'get_queue' from partially initialized
    module mixar.modules.common.job_queue.core.queue_manager

which took eight test modules down with it. Deferring the lookup to first use
breaks the cycle without changing what callers can import.
"""

from importlib import import_module

# name -> module that defines it, relative to this package.
_LAZY_EXPORTS = {
    "Job": ".core.job",
    "JobState": ".core.job",
    "TERMINAL_STATES": ".core.job",
    "RUNNING_STATES": ".core.job",
    "get_queue": ".core.queue_manager",
    "FeatureQueue": ".core.queue_manager",
    "AsyncGLBJob": ".core.generic_jobs",
    "StreamingVideoJob": ".core.generic_jobs",
    "SyncImageJob": ".core.generic_jobs",
    "enqueue_generation": ".core.enqueue",
    "create_scene_flag_listener": ".core.helpers",
    "download_images_to_moodboard": ".core.helpers",
    "extract_image_urls": ".core.helpers",
    "get_queue_with_listener": ".core.helpers",
    "show_batch_summary_popup": ".core.helpers",
}


def __getattr__(name):
    """Import the defining submodule on first access, then cache the value."""
    module_name = _LAZY_EXPORTS.get(name)
    if module_name is None:
        raise AttributeError(
            "module {0!r} has no attribute {1!r}".format(__name__, name)
        )
    value = getattr(import_module(module_name, __name__), name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(set(globals()) | set(_LAZY_EXPORTS))


__all__ = (
    "Job",
    "JobState",
    "TERMINAL_STATES",
    "RUNNING_STATES",
    "get_queue",
    "FeatureQueue",
    # Generic jobs
    "AsyncGLBJob",
    "SyncImageJob",
    "StreamingVideoJob",
    "enqueue_generation",
    # Helpers
    "create_scene_flag_listener",
    "download_images_to_moodboard",
    "extract_image_urls",
    "get_queue_with_listener",
    "show_batch_summary_popup",
)
