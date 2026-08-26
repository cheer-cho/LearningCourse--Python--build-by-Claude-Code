# Scenario: fetch several things concurrently and get results back in
# input order. Concepts: asyncio.gather, event-log assertions instead of
# timing, why gather's result order != completion order.
# Run: uv run pytest 11-async-concurrency -k ex02

import asyncio


async def fake_fetch(name: str, delay: float, log: list[str]) -> str:
    """A fake network call: record "start:<name>", wait `delay` seconds,
    record "end:<name>", then return "<name>-data". Given to you already
    implemented — `fetch_all` below is what you write.

    fake_fetch("a", 0.01, log) -> "a-data"   (and appends to `log` along the way)
    """
    log.append(f"start:{name}")
    await asyncio.sleep(delay)
    log.append(f"end:{name}")
    return f"{name}-data"


async def fetch_all(names: list[str], log: list[str]) -> list[str]:
    """Fetch every name in `names` CONCURRENTLY with `asyncio.gather`,
    using `fake_fetch(name, delay, log)` for each — give earlier names
    in the list a LONGER delay than later ones (e.g. `0.01 * (n - i)`
    seconds for the i-th of n names), so completion order differs from
    input order.

    The returned list must keep the same order as `names` regardless of
    which fake_fetch finishes first — that's what gather guarantees.

    fetch_all(["a", "b"], log) -> ["a-data", "b-data"]
    """
    raise NotImplementedError
