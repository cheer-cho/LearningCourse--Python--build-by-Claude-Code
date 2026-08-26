# Scenario: an infinite number stream, filtered and capped through a
# pipeline of generators. Covers laziness — each stage does work only
# when the next one asks for it — by composing small generators.
# Run: uv run pytest 09-pythonic-deep-dive -k ex05


def naturals():
    """Infinite generator of 1, 2, 3, ... Never exhausts on its own —
    only ever consume it through take() or another bounded tool.
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters


def take(gen, n):
    """Pull the first `n` values out of generator `gen` and return them
    as a list. Consumes exactly `n` values from `gen` — no more.

    take(naturals(), 3) -> [1, 2, 3]
    take(naturals(), 0) -> []
    """
    raise NotImplementedError


def evens(gen):
    """Yield only the even values produced by `gen`, lazily — pulls one
    value from `gen` at a time, only when asked for the next even one.
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters


def first_n_even_squares(n):
    """Return the first n even perfect squares, as a list. Build it by
    piping naturals() through a squares generator expression, then
    evens(), then take()-ing only n values. Stay lazy the whole way:
    naturals() must never get turned into a list.

    first_n_even_squares(3) -> [4, 16, 36]
    first_n_even_squares(0) -> []
    """
    raise NotImplementedError
