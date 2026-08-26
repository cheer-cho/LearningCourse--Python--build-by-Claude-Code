# Scenario: a tiny greeting toolkit. Every function below already works —
# your job is ONLY to add type annotations (params + return), not to
# change any logic. Concepts: param/return annotations, `-> None` on a
# procedure, `float`.
# Run: uv run pytest 10-typing -k ex01


def shout(text):
    """Add type hints to this signature (one param, one return type).

    Return `text` uppercased with an exclamation mark appended.

    shout("hello") -> "HELLO!"
    shout("") -> "!"
    """
    return text.upper() + "!"


def repeat(word, times):
    """Add type hints to this signature (two params, one return type).

    Return `word` repeated `times` times, separated by single spaces.

    repeat("go", 3) -> "go go go"
    repeat("hi", 0) -> ""
    """
    return " ".join([word] * times)


def banner(text):
    """Add type hints to this signature — this one returns nothing, so
    say so explicitly with `-> None`.

    Print `text` surrounded by a row of `=` characters.

    banner("Hi") -> prints "=== Hi ==="
    """
    print(f"=== {text} ===")


def ratio(a, b):
    """Add type hints to this signature (both params are numbers, the
    result is always a float).

    Return `a` divided by `b`.

    ratio(9, 2) -> 4.5
    ratio(5, 2) -> 2.5
    """
    return a / b
