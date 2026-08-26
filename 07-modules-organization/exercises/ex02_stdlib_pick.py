# Scenario: everyday utility functions where picking the right stdlib
# tool beats writing it by hand. Concepts: deciding WHICH module to
# import for a job (no imports are given below — add your own).
# Run: uv run pytest 07-modules-organization -k ex02


def gcd_of(a, b):
    """Return the greatest common divisor of `a` and `b`.

    Use `math.gcd` — don't hand-write Euclid's algorithm.

    gcd_of(12, 18) -> 6
    gcd_of(7, 13) -> 1
    """
    raise NotImplementedError


def most_common_word(text):
    """Return the most frequent word in `text` (split on whitespace).

    Use `collections.Counter` — a dict subclass built for counting (a
    preview; the full deep-dive is module 12). Its `.most_common(n)`
    method returns a list of `(item, count)` pairs, highest count
    first.

    most_common_word("a b a c a b") -> "a"
    """
    raise NotImplementedError


def shuffle_deterministic(items, seed):
    """Return a NEW list containing `items` shuffled, deterministically,
    based on `seed`. Does not modify `items`.

    Create your own `random.Random(seed)` instance and call `.shuffle()`
    on a copy — never call the global `random` module's functions
    directly, or the result won't be reproducible the way the tests
    expect.

    shuffle_deterministic([1, 2, 3], seed=1) -> the same order every
    time it's called with seed=1, and some permutation of [1, 2, 3]
    """
    raise NotImplementedError
