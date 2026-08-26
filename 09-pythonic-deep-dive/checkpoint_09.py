# Checkpoint 09 — Text-pipeline toolkit
#
# Combines everything this module taught: lazy generators (tokens,
# unique), a hand-written decorator (memoized), and the iteration +
# container protocols (Corpus). Build a small toolkit for tokenizing
# and inspecting a body of text, entirely lazily.
# Run: uv run pytest 09-pythonic-deep-dive -k checkpoint

import functools  # noqa: F401 — needed once memoized() is implemented
import re

_WORD_RE = re.compile(r"[a-zA-Z0-9']+")


def tokens(lines):
    """Lazily yield lowercase word tokens from an iterable of lines.
    Split on runs of non-alphanumeric characters. Pull one line at a
    time from `lines` — never build an intermediate list of lines or
    words, so this works over an infinite `lines` iterable too.

    list(tokens(["Hello, world!", "Bye world"]))
    -> ["hello", "world", "bye", "world"]
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters


def unique(iterable):
    """Lazily yield each distinct item from `iterable` the first time
    it's seen, preserving first-seen order. Pull one item at a time —
    never materialize `iterable` into a list.

    list(unique([1, 2, 1, 3, 2])) -> [1, 2, 3]
    list(unique([])) -> []
    """
    raise NotImplementedError
    yield  # pragma: no cover - marks this def as a generator for linters


def memoized(func):
    """Decorator: caches `func`'s results keyed by its call arguments.
    Write your own cache (a dict), don't reach for functools.lru_cache
    — the point is to prove you understand what it does under the
    hood. Expose `wrapper.cache_clear()` to empty the cache.

    calls = []
    @memoized
    def add(a, b):
        calls.append((a, b))
        return a + b
    add(1, 2); add(1, 2)
    len(calls) -> 1              # second call was a cache hit
    add.cache_clear()
    add(1, 2)
    len(calls) -> 2              # cache was emptied, so it ran again
    """
    raise NotImplementedError


class Corpus:
    """Wraps a list of text lines with lazy, protocol-driven word
    access — the checkpoint's capstone, combining dunders, generators,
    and the pipeline above.

    __len__       -> number of lines.
    __iter__      -> yields each distinct token lazily, first-seen
                     order, via the tokens()/unique() pipeline.
    __contains__  -> True if `word` (case-insensitive) appears anywhere.
    vocabulary    -> property: sorted list of every distinct token.

    c = Corpus(["Hello world", "hello there"])
    len(c) -> 2
    list(c) -> ["hello", "world", "there"]
    "world" in c -> True
    "bye" in c -> False
    c.vocabulary -> ["hello", "there", "world"]
    """

    def __init__(self, lines):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        """Return an iterator over unique tokens — delegate to
        unique(tokens(self.lines))."""
        raise NotImplementedError

    def __contains__(self, word):
        raise NotImplementedError

    @property
    def vocabulary(self):
        raise NotImplementedError
