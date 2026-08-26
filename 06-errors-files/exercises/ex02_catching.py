# Scenario: small "don't crash on bad input" helpers. Concepts: catching
# specific exceptions, returning a fallback value, EAFP-style parsing,
# trying several callables until one works.
# Run: uv run pytest 06-errors-files -k ex02


def safe_divide(a, b):
    """Return a / b, or None if `b` is 0 (instead of raising).

    safe_divide(10, 2) -> 5.0
    safe_divide(10, 0) -> None
    """
    raise NotImplementedError


def int_or_default(text, default):
    """Parse `text` as an int; return `default` if it isn't valid.

    Write this EAFP-style: try the conversion, catch the failure —
    don't pre-check with `.isdigit()` or similar.

    int_or_default("42", 0) -> 42
    int_or_default("nope", 0) -> 0
    """
    raise NotImplementedError


def first_working(funcs):
    """Call each zero-argument callable in `funcs` in order; return the
    result of the first one that doesn't raise an exception.

    If every callable raises, let the LAST exception propagate (don't
    catch it) — the caller finds out what actually went wrong.

    first_working([lambda: 1 / 0, lambda: 7]) -> 7
    first_working([lambda: 1 / 0]) -> raises ZeroDivisionError
    """
    raise NotImplementedError
