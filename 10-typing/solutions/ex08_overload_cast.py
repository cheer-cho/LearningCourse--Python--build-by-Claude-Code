# Scenario: a `scale` helper that behaves differently for a single int
# vs a list of ints, plus loading known-shaped JSON. Concepts:
# `@overload` (so callers see the precise return type per input shape),
# and a justified `cast` where a checker can't infer what we already know.
# Run: uv run pytest 10-typing -k ex08

import json
from typing import cast, overload


@overload
def scale(x: int, k: int) -> int: ...
@overload
def scale(x: list[int], k: int) -> list[int]: ...
def scale(x: int | list[int], k: int) -> int | list[int]:
    """Multiply `x` by `k`. If `x` is a list, scale every element.

    scale(3, 2) -> 6
    scale([1, 2, 3], 2) -> [2, 4, 6]
    """
    if isinstance(x, list):
        return [item * k for item in x]
    return x * k


def load_scores(raw: str) -> list[int]:
    """`json.loads` always returns `Any` — mypy can't know its shape. We
    happen to know (from how this function is used) that `raw` always
    decodes to a list of ints, so `cast` tells the checker that, making
    the assumption explicit and reviewable instead of leaking `Any`.

    load_scores("[1, 2, 3]") -> [1, 2, 3]
    """
    data = json.loads(raw)
    return cast(list[int], data)
