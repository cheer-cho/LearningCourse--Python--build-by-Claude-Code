import asyncio


async def fake_fetch(name: str, delay: float, log: list[str]) -> str:
    log.append(f"start:{name}")
    await asyncio.sleep(delay)
    log.append(f"end:{name}")
    return f"{name}-data"


async def fetch_all(names: list[str], log: list[str]) -> list[str]:
    n = len(names)
    calls = (fake_fetch(name, 0.01 * (n - i), log) for i, name in enumerate(names))
    results = await asyncio.gather(*calls)
    return list(results)
