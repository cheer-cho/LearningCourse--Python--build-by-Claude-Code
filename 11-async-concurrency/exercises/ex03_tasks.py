# Scenario: start work in the background with create_task, and race
# several coroutines against each other. Concepts: create_task starts
# running immediately (unlike a plain coroutine), keeping task
# references, asyncio.wait with FIRST_COMPLETED.
# Run: uv run pytest 11-async-concurrency -k ex03

import asyncio


async def _worker(name: str, delay: float, log: list[str]) -> str:
    """A fake unit of work: record "start:<name>", wait `delay`
    seconds, record "end:<name>", return `name`. Given to you already
    implemented, for `race` to build tasks from.
    """
    log.append(f"start:{name}")
    await asyncio.sleep(delay)
    log.append(f"end:{name}")
    return name


async def race(log: list[str]) -> tuple[str, str]:
    """Use `asyncio.create_task` to start two `_worker` calls —
    `_worker("fast", 0.01, log)` and `_worker("slow", 0.03, log)` — so
    both are running in the background at once, THEN await both (fast
    first, then slow) and return their results as `(fast_result,
    slow_result)`.

    Creating both tasks before awaiting either is the point: `log` ends
    up showing both "start:" entries before either "end:" entry, proving
    they overlapped instead of running one after the other.

    race(log) -> ("fast", "slow")
    """
    raise NotImplementedError


async def first_done(coros: list) -> object:
    """Run every coroutine in `coros` concurrently and return the
    result of whichever one finishes FIRST, using `asyncio.wait(...,
    return_when=asyncio.FIRST_COMPLETED)`. The other coroutines are
    cancelled — their results are discarded.

    first_done([slow_coro, fast_coro]) -> whatever fast_coro returned
    """
    raise NotImplementedError
