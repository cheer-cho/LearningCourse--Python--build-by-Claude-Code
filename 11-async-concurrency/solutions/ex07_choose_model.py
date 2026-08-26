import asyncio
from collections.abc import Callable

SCENARIOS: dict[str, str] = {
    "many_http_calls": "Make 1000 HTTP GET requests to different APIs and collect the responses.",
    "resize_images": "Resize 500 large image files on disk (pure CPU-bound number crunching).",
    "blocking_sdk_calls": "Make 3 calls to a vendor SDK that only ships a blocking (non-async) client.",
    "compress_video": "Compress a folder of video files — CPU-heavy work, no waiting on anything.",
    "poll_many_sockets": "Keep 500 websocket connections open, mostly idle, waiting for messages.",
}

_ANSWERS: dict[str, str] = {
    "many_http_calls": "asyncio",
    "resize_images": "processes",
    "blocking_sdk_calls": "threads",
    "compress_video": "processes",
    "poll_many_sockets": "asyncio",
}


def choose(scenario_key: str) -> str:
    return _ANSWERS[scenario_key]


async def run_blocking_in_executor(func: Callable[[], object]) -> object:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(None, func)
