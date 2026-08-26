import asyncio
from collections.abc import AsyncIterator


async def ticker(count: int) -> AsyncIterator[int]:
    for i in range(count):
        await asyncio.sleep(0)
        yield i


async def collect(agen) -> list:
    result = []
    async for item in agen:
        result.append(item)
    return result


async def alimit(agen, n: int) -> list:
    result = []
    if n <= 0:
        return result
    async for item in agen:
        result.append(item)
        if len(result) >= n:
            break
    return result
