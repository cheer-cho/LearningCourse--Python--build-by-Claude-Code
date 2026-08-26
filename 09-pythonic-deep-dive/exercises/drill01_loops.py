# Idiom drill: index-juggling loops -> enumerate/zip. Every function
# below already has a working "clunky" version — see the block comment
# right here, NOT inside any function (the tests inspect each function's
# own source, so keep your rewrite free of the anti-pattern):
#
#     def _pair_up_clunky(names, scores):
#         result = []
#         for i in range(len(names)):
#             result.append((names[i], scores[i]))
#         return result
#
#     def _numbered_lines_clunky(lines):
#         result = []
#         for i in range(len(lines)):
#             result.append(f"{i + 1}: {lines[i]}")
#         return result
#
# Your job: replace each `raise NotImplementedError` with an idiomatic
# one-liner using enumerate() and/or zip() — no `range(len(...))`
# indexing anywhere in your rewrite.
# Run: uv run pytest 09-pythonic-deep-dive -k drill01


def pair_up(names, scores):
    """Pair each name with its score at the same position.

    pair_up(["Ada", "Bo"], [90, 70]) -> [("Ada", 90), ("Bo", 70)]
    pair_up([], []) -> []
    """
    raise NotImplementedError


def numbered_lines(lines):
    """Number each line starting at 1, as "N: text" strings.

    numbered_lines(["a", "b"]) -> ["1: a", "2: b"]
    numbered_lines([]) -> []
    """
    raise NotImplementedError


def elementwise_diff(a, b):
    """Return the absolute difference between `a` and `b` at each
    shared position (extra items in the longer list are ignored).

    elementwise_diff([10, 20, 30], [1, 25, 30]) -> [9, 5, 0]
    elementwise_diff([], []) -> []
    """
    raise NotImplementedError


def first_index_of(items, target):
    """Return the position of the first `target` in `items`, or -1 if
    it isn't there.

    first_index_of(["a", "b", "c"], "c") -> 2
    first_index_of(["a", "b"], "z") -> -1
    """
    raise NotImplementedError
