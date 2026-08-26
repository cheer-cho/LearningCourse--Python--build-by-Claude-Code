# Reference solution for ex02_truthiness — see exercises/ex02_truthiness.py
# for the scenario.


def first_truthy(a, b, c):
    """Return the first truthy of three values, or None if all are falsy.

    Does not use a list — just three plain parameters and an elif chain.

    a, b, c -> result
    0, "", "hi" -> "hi"
    None, 0, False -> None
    "x", "y", "z" -> "x"
    """
    if a:
        return a
    elif b:
        return b
    elif c:
        return c
    else:
        return None


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
    if value is None:
        return "missing"
    elif value == "":
        return "empty"
    else:
        return "present"
