# Checkpoint 11 — Async download manager
#
# A worker pool of `worker_count` coroutines pulls jobs off an
# asyncio.Queue and "downloads" them, but a semaphore caps how many
# downloads run at once (2), no matter how many workers there are. One
# job can fail without stopping the rest. This combines gather/tasks,
# a semaphore, and gather_safe-style error collection from this module.
# Run: uv run pytest 11-async-concurrency -k checkpoint

import asyncio

MAX_CONCURRENT_DOWNLOADS = 2


async def _download(
    job_id: str,
    should_fail: bool,
    semaphore: asyncio.Semaphore,
    active: list[int],
    limit_log: list[int],
) -> str:
    """Simulate downloading one job, gated by `semaphore` so at most
    `MAX_CONCURRENT_DOWNLOADS` run at once. Records the current number
    of active downloads into `limit_log` every time one starts, so
    tests can assert the cap was respected (and actually reached).

    Raises `ValueError` if `should_fail` is True, after "starting" the
    download — a realistic download-that-fails, not a call that never
    even tried.
    """
    async with semaphore:
        active[0] += 1
        limit_log.append(active[0])
        await asyncio.sleep(0)
        active[0] -= 1
        if should_fail:
            raise ValueError(f"download failed: {job_id}")
        return f"{job_id}-content"


async def download_all(
    jobs: list[tuple[str, bool]], worker_count: int, limit_log: list[int]
) -> tuple[dict[str, str], list[str]]:
    """Download every job in `jobs` using a pool of `worker_count`
    workers pulling from a shared `asyncio.Queue`, with a semaphore
    capping concurrent downloads at `MAX_CONCURRENT_DOWNLOADS` (use
    `_download`, passing it `limit_log`).

    Each job is a `(job_id, should_fail)` pair. A job that fails is
    recorded as a message in the returned `errors` list — it must NOT
    stop the other workers from processing the rest of the queue.

    Returns `(results, errors)`:
    - `results`: dict mapping each successful `job_id` to its content.
    - `errors`: list of error messages (strings) for jobs that failed.

    download_all([("a", False), ("bad", True)], 2, []) ->
        ({"a": "a-content"}, ["download failed: bad"])
    """
    raise NotImplementedError
