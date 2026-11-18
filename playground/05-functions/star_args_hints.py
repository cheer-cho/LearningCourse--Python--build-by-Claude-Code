"""The hint on *args describes ONE item. Python builds the tuple type for you.

Run:  uv run mypy playground/05-functions/star_args_hints.py
"""

from collections.abc import Callable
from typing import reveal_type


def total(*nums: int) -> int:  # each argument is an int
    reveal_type(nums)  # mypy: tuple[int, ...]
    return sum(nums)


def wrong(*nums: list[int]) -> None:  # each argument is a LIST of ints
    reveal_type(nums)  # mypy: tuple[list[int], ...]


# Callable has two slots: Callable[[arg types], return type]
#   Callable[[str], int]   takes one str, returns an int
#   Callable[..., int]     takes anything, returns an int  (... = "any arguments")
def call_each(*handlers: Callable[[str], None]) -> None:
    reveal_type(handlers)  # mypy: tuple[def (str), ...]
    for handler in handlers:
        handler("hi")


total(1, 2, 3)
wrong([1, 2], [3])
call_each(print)
