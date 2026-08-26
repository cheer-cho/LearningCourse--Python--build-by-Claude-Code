import functools
import re

_WORD_RE = re.compile(r"[a-zA-Z0-9']+")


def tokens(lines):
    """Lazily yield lowercase word tokens from an iterable of lines.
    Splits on runs of non-alphanumeric characters. Pulls one line at a
    time from `lines` — never builds an intermediate list of lines or
    words, so it works over an infinite `lines` iterable too.

    list(tokens(["Hello, world!", "Bye world"]))
    -> ["hello", "world", "bye", "world"]
    """
    for line in lines:
        for match in _WORD_RE.finditer(line.lower()):
            yield match.group()


def unique(iterable):
    """Lazily yield each distinct item from `iterable` the first time
    it's seen, preserving first-seen order. Pulls one item at a time —
    never materializes `iterable` into a list.

    list(unique([1, 2, 1, 3, 2])) -> [1, 2, 3]
    list(unique([])) -> []
    """
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


def memoized(func):
    """Decorator: caches `func`'s results keyed by its call arguments.
    A from-scratch cache (not functools.lru_cache), so the module
    proves it understands what lru_cache does under the hood. Exposes
    `wrapper.cache_clear()` to empty the cache.

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
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]

    def cache_clear():
        cache.clear()

    wrapper.cache_clear = cache_clear
    return wrapper


class Corpus:
    """Wraps a list of text lines with lazy, protocol-driven word
    access — the checkpoint's capstone, combining dunders, generators,
    and a decorator-friendly helper.

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
        self.lines = lines

    def __len__(self):
        return len(self.lines)

    def __iter__(self):
        return unique(tokens(self.lines))

    def __contains__(self, word):
        return word.lower() in tokens(self.lines)

    @property
    def vocabulary(self):
        return sorted(set(tokens(self.lines)))
