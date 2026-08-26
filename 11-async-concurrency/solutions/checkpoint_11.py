import asyncio

MAX_CONCURRENT_DOWNLOADS = 2


async def _download(
    job_id: str,
    should_fail: bool,
    semaphore: asyncio.Semaphore,
    active: list[int],
    limit_log: list[int],
) -> str:
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
    queue: asyncio.Queue[tuple[str, bool]] = asyncio.Queue()
    for job in jobs:
        queue.put_nowait(job)

    semaphore = asyncio.Semaphore(MAX_CONCURRENT_DOWNLOADS)
    active = [0]
    results: dict[str, str] = {}
    errors: list[str] = []

    async def worker() -> None:
        while True:
            try:
                job_id, should_fail = queue.get_nowait()
            except asyncio.QueueEmpty:
                return
            try:
                content = await _download(job_id, should_fail, semaphore, active, limit_log)
                results[job_id] = content
            except ValueError as exc:
                errors.append(str(exc))

    workers = [asyncio.create_task(worker()) for _ in range(worker_count)]
    await asyncio.gather(*workers)
    return results, errors
