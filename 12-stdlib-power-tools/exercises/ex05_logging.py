# Scenario: an isolated, testable logger for an app's audit trail —
# writes to an injected stream instead of the real console, and never
# leaks into the root logger. Concepts: getLogger(name), handlers,
# formatters, propagate, logging vs print.
# Run: uv run pytest 12-stdlib-power-tools -k ex05

import logging
from io import StringIO


def make_logger(name: str, level: int, stream: StringIO) -> logging.Logger:
    """Build (or rebuild) a logger named `name` that writes to `stream`
    at `level`, formatted as "LEVEL:name:message". Must be isolated:
    clear any handlers the logger already has (calling this twice with
    the same name must not duplicate output), and set propagate=False
    so nothing reaches the root logger.

    make_logger("app", logging.INFO, StringIO()) -> a Logger instance
    that writes "INFO:app:hello" to the stream when told to log "hello"
    at info level.
    """
    raise NotImplementedError


def audit(logger: logging.Logger, event: str, ok: bool) -> None:
    """Log an audit event on `logger`: info level "OK: {event}" when
    `ok` is True, error level "FAILED: {event}" otherwise.

    audit(logger, "login", True) -> logs "OK: login" at INFO
    audit(logger, "login", False) -> logs "FAILED: login" at ERROR
    """
    raise NotImplementedError
