# Scenario: a retry policy and a result clamp, both configurable.
# Covers parameterized decorators as three nested layers: factory(args)
# -> decorator(func) -> wrapper(*args, **kwargs).
# Run: uv run pytest 09-pythonic-deep-dive -k ex08

import functools  # noqa: F401 — needed once retry/clamp_result wrap with it


def retry(times):
    """Decorator FACTORY: retries the wrapped function up to `times`
    attempts whenever it raises ValueError, returning the first
    successful result. If every attempt raises, re-raise the last
    ValueError.

    attempts = []
    @retry(3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ValueError("not yet")
        return "ok"
    flaky() -> "ok"       # succeeded on the 3rd attempt
    len(attempts) -> 3
    """
    raise NotImplementedError


def clamp_result(lo, hi):
    """Decorator FACTORY: clamps the wrapped function's numeric return
    value into the closed range [lo, hi].

    @clamp_result(0, 100)
    def score(x):
        return x
    score(150) -> 100
    score(-5) -> 0
    score(50) -> 50
    """
    raise NotImplementedError
