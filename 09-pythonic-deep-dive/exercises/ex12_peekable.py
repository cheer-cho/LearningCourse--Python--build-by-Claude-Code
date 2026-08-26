# Scenario: a capstone-ish iterator wrapper that can look ahead one
# value. Covers composing the iteration protocol you built by hand in
# ex03 into a general-purpose tool over ANY iterable.
# Run: uv run pytest 09-pythonic-deep-dive -k ex12


class Peekable:
    """Wraps any iterable, adding peek() — a look at the next value
    without consuming it. Works over any iterable by converting it to
    a real iterator internally with iter(); proves the iterator
    protocol is enough to build new tools on top of.

    p = Peekable([1, 2, 3])
    p.peek() -> 1
    next(p) -> 1
    p.peek() -> 2
    list(p) -> [2, 3]
    Peekable([]).peek() -> None          # default when exhausted
    Peekable([]).peek("done") -> "done"  # caller-supplied default
    """

    _SENTINEL = object()

    def __init__(self, iterable):
        raise NotImplementedError

    def peek(self, default=None):
        """Return the next value without consuming it. If the
        underlying iterator is exhausted, return `default` instead of
        raising."""
        raise NotImplementedError

    def __next__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
