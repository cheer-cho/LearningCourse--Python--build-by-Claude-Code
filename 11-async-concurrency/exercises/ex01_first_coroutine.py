# Scenario: your first coroutines. Concepts: async def, calling a coroutine
# builds it but doesn't run it, asyncio.run as the sync-to-async entry
# point, and the classic "forgot to await" bug.
# Run: uv run pytest 11-async-concurrency -k ex01


async def fetch_greeting(name: str) -> str:
    """Build and return a greeting for `name`.

    Awaits `asyncio.sleep(0)` first — a stand-in for "some async work
    happened here" that doesn't actually add any real delay.

    fetch_greeting("Ada") -> "Hello, Ada!"
    """
    raise NotImplementedError


def run_fetch(name: str) -> str:
    """Sync wrapper around `fetch_greeting`: start an event loop with
    `asyncio.run`, run `fetch_greeting(name)` to completion, and return
    its result. This is how sync code (a `__main__` block, a script)
    kicks off async work.

    run_fetch("Ada") -> "Hello, Ada!"
    """
    raise NotImplementedError


async def get_greeting_buggy(name: str) -> str:
    """BUG: this is supposed to return the greeting from
    `fetch_greeting`, but it forgot the `await` keyword — so it hands
    back the coroutine OBJECT instead of the string inside it. Fix the
    one missing keyword.

    get_greeting_buggy("Ada") -> "Hello, Ada!"
    """
    return fetch_greeting(name)
