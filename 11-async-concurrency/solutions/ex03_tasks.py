import asyncio


async def _worker(name: str, delay: float, log: list[str]) -> str:
    log.append(f"start:{name}")
    await asyncio.sleep(delay)
    log.append(f"end:{name}")
    return name


async def race(log: list[str]) -> tuple[str, str]:
    fast_task = asyncio.create_task(_worker("fast", 0.01, log))
    slow_task = asyncio.create_task(_worker("slow", 0.03, log))
    fast_result = await fast_task
    slow_result = await slow_task
    return fast_result, slow_result


async def first_done(coros: list) -> object:
    tasks = [asyncio.ensure_future(coro) for coro in coros]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    for task in pending:
        task.cancel()
    if pending:
        await asyncio.gather(*pending, return_exceptions=True)
    return done.pop().result()
