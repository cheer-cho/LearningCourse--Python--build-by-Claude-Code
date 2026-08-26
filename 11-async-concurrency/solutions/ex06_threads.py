from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor


def fetch_all_threaded(urls: list[str], fake_io: Callable[[str], str], max_workers: int) -> list[str]:
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        return list(executor.map(fake_io, urls))
