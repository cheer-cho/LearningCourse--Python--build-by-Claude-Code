# Scenario: a countdown timer, built by hand to see the iteration
# protocol's two halves. Covers __iter__ (iterable) vs __next__
# (iterator) as separate objects, and StopIteration.
# Run: uv run pytest 09-pythonic-deep-dive -k ex03


class Countdown:
    """An ITERABLE that counts down from `start` to 1 (inclusive). Each
    call to `iter(countdown)` (which `for` and `list()` make for you)
    must build a brand-new `_CountdownIter`, so the same Countdown can
    be iterated more than once — proof that the iterable and the
    iterator are separate objects.

    list(Countdown(3)) -> [3, 2, 1]
    c = Countdown(2)
    list(c) -> [2, 1]
    list(c) -> [2, 1]     # restartable: iterating again works
    """

    def __init__(self, start):
        raise NotImplementedError

    def __iter__(self):
        """Return a FRESH _CountdownIter every time — this is what
        makes Countdown restartable."""
        raise NotImplementedError


class _CountdownIter:
    """The iterator half: holds the one piece of mutable state
    (`current`) and knows how to produce the next value or signal
    exhaustion. Private — reach it only via `iter(countdown)`.
    """

    def __init__(self, current):
        raise NotImplementedError

    def __iter__(self):
        """Iterators are their own iterable (`iter(it) is it`)."""
        raise NotImplementedError

    def __next__(self):
        """Return the next value, counting down; raise StopIteration
        once `current` reaches 0."""
        raise NotImplementedError
