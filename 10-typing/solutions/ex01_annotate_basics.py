# Scenario: a tiny greeting toolkit. Every function below already works —
# your job is ONLY to add type annotations (params + return), not to
# change any logic. Concepts: param/return annotations, `-> None` on a
# procedure, `float`.
# Run: uv run pytest 10-typing -k ex01


def shout(text: str) -> str:
    """Return `text` uppercased with an exclamation mark appended.

    shout("hello") -> "HELLO!"
    shout("") -> "!"
    """
    return text.upper() + "!"


def repeat(word: str, times: int) -> str:
    """Return `word` repeated `times` times, separated by single spaces.

    repeat("go", 3) -> "go go go"
    repeat("hi", 0) -> ""
    """
    return " ".join([word] * times)


def banner(text: str) -> None:
    """Print `text` surrounded by a row of `=` characters.

    banner("Hi") -> prints "=== Hi ==="
    """
    print(f"=== {text} ===")


def ratio(a: float, b: float) -> float:
    """Return `a` divided by `b`.

    ratio(9, 2) -> 4.5
    ratio(5, 2) -> 2.5
    """
    return a / b
