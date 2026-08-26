class Countdown:
    """An ITERABLE that counts down from `start` to 1 (inclusive). Each
    call to `iter(countdown)` (which `for` and `list()` make for you)
    builds a brand-new `_CountdownIter`, so the same Countdown can be
    iterated more than once — proof that the iterable and the iterator
    are separate objects.

    list(Countdown(3)) -> [3, 2, 1]
    c = Countdown(2)
    list(c) -> [2, 1]
    list(c) -> [2, 1]     # restartable: iterating again works
    """

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        """Returns a FRESH iterator every time — this is what makes
        Countdown restartable."""
        return _CountdownIter(self.start)


class _CountdownIter:
    """The iterator half: holds the one piece of mutable state
    (`current`) and knows how to produce the next value or signal
    exhaustion. Private — reach it only via `iter(countdown)`.
    """

    def __init__(self, current):
        self.current = current

    def __iter__(self):
        """Iterators are their own iterable (`iter(it) is it`)."""
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
