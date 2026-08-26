"""This function already WORKS — but it is messy: an unused import, ugly
spacing, a variable that's assigned and never used, and a variable named
`list`, which shadows Python's built-in `list` type.

Clean it up WITHOUT changing what it returns. When you're done, `ruff
check` on this file should report no issues.

Run:  uv run pytest 01-setup-tooling -k ex04
Lint: uv run ruff check 01-setup-tooling/exercises/ex04_ruff_cleanup.py
"""

import os


def total_unique_length(words):
    """Return the summed length of the distinct words in `words`.

    Params:
        words (list[str]): words to measure; duplicates are allowed.

    Returns:
        int: sum of len(word) over the distinct words in `words`
        (a repeated word is only counted once).

    Examples:
        total_unique_length(["a", "bb", "a"]) -> 3
        total_unique_length([]) -> 0
        total_unique_length(["cat", "cat", "cat"]) -> 3
    """
    list = []
    total = 0
    unused = 42
    for word    in words:
        if word not in list:
            list.append( word )
            total = total+len(word)
    return total
