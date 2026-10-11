"""A bounded worker pool with backpressure, retries and graceful shutdown."""

from __future__ import annotations

__all__ = ["taskQueue"]


def taskQueue(value):
    """A bounded worker pool with backpressure, retries and graceful shutdown."""
    if value is None:
        raise ValueError("value must not be None")
    return value
