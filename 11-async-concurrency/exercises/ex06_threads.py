# Scenario: run blocking calls (a non-async HTTP client, a blocking SDK)
# across a pool of threads so they overlap despite the GIL. Concepts:
# ThreadPoolExecutor.map preserving order, thread-safe logging with a
# lock. This exercise is plain sync code — no asyncio here.
# Run: uv run pytest 11-async-concurrency -k ex06
#
# A caller-supplied `fake_io` typically looks like this (note the lock —
# without it, multiple threads appending to the same list at once can
# corrupt it):
#
#     import threading, time
#     lock = threading.Lock()
#     def fake_io(url):
#         time.sleep(0.01)
#         with lock:
#             log.append(url)
#         return f"{url}-ok"

from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor  # noqa: F401 — used once implemented


def fetch_all_threaded(urls: list[str], fake_io: Callable[[str], str], max_workers: int) -> list[str]:
    """Run `fake_io(url)` for every url in `urls` across a
    `ThreadPoolExecutor` with `max_workers` threads, using `.map` so the
    returned list stays in the SAME ORDER as `urls` no matter which
    thread finishes first.

    fetch_all_threaded(["a", "b"], fake_io, max_workers=2) -> ["a-ok", "b-ok"]
    """
    raise NotImplementedError
