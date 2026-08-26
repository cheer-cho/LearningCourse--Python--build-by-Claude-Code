"""Reference solution for ex04_ruff_cleanup. Not imported by tests directly —
scripts/verify_solutions.py overlays this onto the exercise stub.
"""


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
    seen = []
    total = 0
    for word in words:
        if word not in seen:
            seen.append(word)
            total += len(word)
    return total
