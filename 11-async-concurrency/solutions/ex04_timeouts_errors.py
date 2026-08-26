import asyncio
from collections.abc import Callable, Coroutine


async def fetch_with_timeout(coro_factory: Callable[[], Coroutine], timeout: float, fallback: object) -> object:
    try:
        return await asyncio.wait_for(coro_factory(), timeout)
    except TimeoutError:
        return fallback


async def gather_safe(coros: list) -> tuple[list, list[BaseException]]:
    outcomes = await asyncio.gather(*coros, return_exceptions=True)
    results = []
    errors: list[BaseException] = []
    for outcome in outcomes:
        if isinstance(outcome, BaseException):
            errors.append(outcome)
        else:
            results.append(outcome)
    return results, errors
