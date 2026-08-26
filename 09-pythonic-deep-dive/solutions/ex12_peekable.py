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
        self._iterator = iter(iterable)
        self._cache = self._SENTINEL

    def peek(self, default=None):
        """Return the next value without consuming it. If the
        underlying iterator is exhausted, return `default` instead of
        raising."""
        if self._cache is self._SENTINEL:
            try:
                self._cache = next(self._iterator)
            except StopIteration:
                return default
        return self._cache

    def __next__(self):
        if self._cache is not self._SENTINEL:
            value = self._cache
            self._cache = self._SENTINEL
            return value
        return next(self._iterator)

    def __iter__(self):
        return self
