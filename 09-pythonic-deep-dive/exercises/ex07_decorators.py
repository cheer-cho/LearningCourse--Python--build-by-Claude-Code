# Scenario: two function decorators for observability — a call logger
# and a call counter. Covers plain decorators, decorator FACTORIES
# (a decorator that takes arguments), and functools.wraps.
# Run: uv run pytest 09-pythonic-deep-dive -k ex07

import functools  # noqa: F401 — needed once log_calls/count_calls wrap with it


def log_calls(log):
    """Decorator FACTORY: returns a decorator that, each time the
    wrapped function is called, appends a "name(args) -> result" string
    to `log` (a list you pass in). Use functools.wraps so the wrapped
    function keeps its own __name__/__doc__.

    log = []
    @log_calls(log)
    def add(a, b):
        return a + b
    add(2, 3) -> 5
    log -> ["add(2, 3) -> 5"]
    """
    raise NotImplementedError


def count_calls(func):
    """Decorator: wraps `func`, tracking how many times it has been
    called on `wrapper.calls`. functools.wraps keeps __name__/__doc__
    pointing at the original function, not the wrapper.

    @count_calls
    def ping():
        return "pong"
    ping()
    ping()
    ping.calls -> 2
    ping.__name__ -> "ping"
    """
    raise NotImplementedError
