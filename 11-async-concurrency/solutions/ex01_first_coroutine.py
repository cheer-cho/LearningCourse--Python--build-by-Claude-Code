import asyncio


async def fetch_greeting(name: str) -> str:
    await asyncio.sleep(0)
    return f"Hello, {name}!"


def run_fetch(name: str) -> str:
    return asyncio.run(fetch_greeting(name))


async def get_greeting_buggy(name: str) -> str:
    return await fetch_greeting(name)
