# Scenario: stream values instead of collecting them all upfront.
# Concepts: async generators (`async def` + `yield`), `async for`,
# writing an async version of itertools.islice.
# Run: uv run pytest 11-async-concurrency -k ex05

import asyncio  # noqa: F401 — needed once ticker is implemented
from collections.abc import AsyncIterator


async def ticker(count: int) -> AsyncIterator[int]:
    """An async generator yielding 0, 1, ..., count - 1, awaiting
    `asyncio.sleep(0)` before each yield (a stand-in for "waited for
    the next value to be ready").

    [x async for x in ticker(3)] -> [0, 1, 2]
    """
    raise NotImplementedError
    yield  # pragma: no cover - makes this an async generator for type checkers


async def collect(agen) -> list:
    """Consume the async iterable `agen` fully via `async for`, and
    return everything it yielded as a list, in order.

    collect(ticker(3)) -> [0, 1, 2]
    """
    raise NotImplementedError


async def alimit(agen, n: int) -> list:
    """Async equivalent of `itertools.islice(agen, n)`: pull at most the
    first `n` items from the async iterable `agen` and return them as a
    list. Stop as soon as `n` items are collected — do NOT keep
    consuming `agen` past that point.

    alimit(ticker(10), 3) -> [0, 1, 2]
    alimit(ticker(2), 5) -> [0, 1]   (agen ran out first)
    """
    raise NotImplementedError
