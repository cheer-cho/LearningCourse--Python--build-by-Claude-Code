# Scenario: flatten nested lists and chain several iterables together.
# Covers `yield from` — delegating a generator's output to another
# iterable instead of re-yielding it in a manual loop.
# Run: uv run pytest 09-pythonic-deep-dive -k ex06


def flatten(nested):
    """Recursively flatten an arbitrarily nested list/tuple structure,
    yielding scalar (non-list/tuple) values in order. Use `yield from`
    to delegate to the recursive call instead of manually re-yielding
    each value in a loop.

    list(flatten([1, [2, 3, [4]], 5])) -> [1, 2, 3, 4, 5]
    list(flatten([])) -> []
    list(flatten([1, (2, 3)])) -> [1, 2, 3]
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters


def concat_all(*iterables):
    """Delegate to each iterable in turn, exhausting one fully before
    moving to the next — one `yield from` per source, chained. Same
    idea as `itertools.chain`, written by hand to drill delegation.

    list(concat_all([1, 2], "ab", (9,))) -> [1, 2, "a", "b", 9]
    list(concat_all()) -> []
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters
