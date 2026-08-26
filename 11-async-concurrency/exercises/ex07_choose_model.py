# Scenario: knowledge check — given a scenario, pick asyncio, threads,
# or processes. Concepts: the I/O-bound vs CPU-bound decision from
# LESSON.md, and the loop.run_in_executor bridge.
# Run: uv run pytest 11-async-concurrency -k ex07

from collections.abc import Callable

SCENARIOS: dict[str, str] = {
    "many_http_calls": "Make 1000 HTTP GET requests to different APIs and collect the responses.",
    "resize_images": "Resize 500 large image files on disk (pure CPU-bound number crunching).",
    "blocking_sdk_calls": "Make 3 calls to a vendor SDK that only ships a blocking (non-async) client.",
    "compress_video": "Compress a folder of video files — CPU-heavy work, no waiting on anything.",
    "poll_many_sockets": "Keep 500 websocket connections open, mostly idle, waiting for messages.",
}


def choose(scenario_key: str) -> str:
    """Given a key into `SCENARIOS`, return which concurrency model
    fits best: `"asyncio"`, `"threads"`, or `"processes"`.

    choose("many_http_calls") -> "asyncio"
    choose("resize_images") -> "processes"
    """
    raise NotImplementedError


async def run_blocking_in_executor(func: Callable[[], object]) -> object:
    """Bridge drill: run the blocking, zero-argument callable `func` off
    the event loop using `loop.run_in_executor(None, func)`, and return
    its result. This is how you call blocking code from inside an
    `async def` without freezing the loop for everyone else.

    run_blocking_in_executor(lambda: 42) -> 42
    """
    raise NotImplementedError
