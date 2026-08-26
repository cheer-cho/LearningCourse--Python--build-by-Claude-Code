# Scenario: don't let one slow or broken call take down the whole batch.
# Concepts: asyncio.wait_for + TimeoutError, gather(..., return_exceptions=True).
# Run: uv run pytest 11-async-concurrency -k ex04

import asyncio  # noqa: F401 — needed once fetch_with_timeout/gather_safe are implemented
from collections.abc import Callable, Coroutine


async def fetch_with_timeout(coro_factory: Callable[[], Coroutine], timeout: float, fallback: object) -> object:
    """Call `coro_factory()` to build a fresh coroutine, then await it
    with a `timeout`-second limit via `asyncio.wait_for`. Return its
    result if it finishes in time; return `fallback` instead if it
    raises `TimeoutError`.

    A factory (not a coroutine object) is passed in because a coroutine
    can only be awaited once — the factory lets the caller (and the
    tests) build a new one each time this is called.

    fetch_with_timeout(quick_coro_factory, 1.0, "default") -> (the real result)
    fetch_with_timeout(slow_coro_factory, 0.01, "default") -> "default"
    """
    raise NotImplementedError


async def gather_safe(coros: list) -> tuple[list, list[BaseException]]:
    """Run every coroutine in `coros` concurrently with
    `asyncio.gather(..., return_exceptions=True)`, then split the
    outcomes into two lists — `(results, errors)` — in the same
    relative order they appeared, so one broken coroutine doesn't stop
    the others from reporting their results.

    gather_safe([ok_coro, failing_coro]) -> ([<ok result>], [<the exception>])
    """
    raise NotImplementedError
