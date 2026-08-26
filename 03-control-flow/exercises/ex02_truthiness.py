# Scenario: a form-processing helper needs to pick the first usable
# value and classify how "there" a value is. Covers: truthiness rules,
# `is None` vs `== ""` vs bare truthiness checks.
# Run: uv run pytest 03-control-flow -k ex02


def first_truthy(a, b, c):
    """Return the first truthy of three values, or None if all are falsy.

    Does not use a list — just three plain parameters and an elif chain.

    a, b, c -> result
    0, "", "hi" -> "hi"
    None, 0, False -> None
    "x", "y", "z" -> "x"
    """
    raise NotImplementedError


def describe(value) -> str:
    """Classify a value as "missing", "empty", or "present".

    None is "missing" (never received). "" is "empty" (received, but
    blank). Everything else — including falsy values like 0 or False —
    is "present". This distinguishes falsy-but-real from truly absent.

    value -> result
    None -> "missing"
    "" -> "empty"
    0 -> "present"
    "hi" -> "present"
    """
    raise NotImplementedError
