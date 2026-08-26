# Scenario: prediction + fix drills about copying vs aliasing. Concepts:
# assignment binds a name (doesn't copy), shallow copy (list(x), x[:],
# x.copy()) vs copy.deepcopy for nested data.
# Run: uv run pytest 04-collections -k ex08

import copy  # noqa: F401 — needed once safe_flat_copy/independent_deep_copy are implemented


def broken_reset(scores: list[int]) -> list[int]:
    """Return a fresh list that starts out equal to `scores`. Appending
    to the RETURNED list must NOT change `scores`.

    This function is broken: it returns `scores` itself, an alias, not a
    copy. Fix the body (don't change the signature or docstring).

    broken_reset([1, 2, 3]) -> a new list [1, 2, 3]; appending 4 to it
    must leave the original [1, 2, 3] untouched.
    """
    return scores  # BUG: this is an alias, not a copy — fix it


def deep_trap(board: list[list[int]]) -> list[list[int]]:
    """Return a fully independent copy of `board`, a list of lists.
    Mutating a ROW of the returned board must NOT change `board`.

    This function is broken: `list(board)` only copies the outer list —
    the inner rows are still shared with `board`. Fix the body using
    `copy.deepcopy` (don't change the signature or docstring).

    deep_trap([[1, 2], [3, 4]]) -> a new board where appending to
    result[0] leaves board[0] as [1, 2].
    """
    return list(board)  # BUG: shallow copy — inner rows are still shared


def safe_flat_copy(base: list[int], extra: int) -> list[int]:
    """Return a new list containing every item of `base` plus `extra`
    appended at the end. `base` itself must be unchanged afterwards.

    safe_flat_copy([1, 2, 3], 4) -> [1, 2, 3, 4]
    (and the original [1, 2, 3] passed in is still [1, 2, 3])
    """
    raise NotImplementedError


def independent_deep_copy(board: list[list[int]], row: int, value: int) -> list[list[int]]:
    """Return a deep copy of `board` with `value` appended to row number
    `row` — in the COPY only. `board` itself must be completely
    unchanged afterwards, including its inner rows.

    independent_deep_copy([[1, 2], [3, 4]], 0, 99) -> [[1, 2, 99], [3, 4]]
    (and the original board's row 0 is still [1, 2])
    """
    raise NotImplementedError
