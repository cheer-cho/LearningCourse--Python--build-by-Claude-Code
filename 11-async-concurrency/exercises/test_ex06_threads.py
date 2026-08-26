import threading
import time

from ex06_threads import fetch_all_threaded


def test_fetch_all_threaded_preserves_input_order():
    log: list[str] = []
    lock = threading.Lock()

    def fake_io(url: str) -> str:
        time.sleep(0.01)
        with lock:
            log.append(url)
        return f"{url}-ok"

    results = fetch_all_threaded(["a", "b", "c"], fake_io, max_workers=3)
    assert results == ["a-ok", "b-ok", "c-ok"]


def test_fetch_all_threaded_calls_fake_io_for_every_url():
    log: list[str] = []
    lock = threading.Lock()

    def fake_io(url: str) -> str:
        time.sleep(0.01)
        with lock:
            log.append(url)
        return f"{url}-ok"

    fetch_all_threaded(["a", "b", "c"], fake_io, max_workers=3)
    assert sorted(log) == ["a", "b", "c"]


def test_fetch_all_threaded_works_with_a_single_worker():
    def fake_io(url: str) -> str:
        return f"{url}-ok"

    results = fetch_all_threaded(["x", "y", "z"], fake_io, max_workers=1)
    assert results == ["x-ok", "y-ok", "z-ok"]


def test_fetch_all_threaded_empty_urls_returns_empty_list():
    def fake_io(url: str) -> str:
        return f"{url}-ok"

    assert fetch_all_threaded([], fake_io, max_workers=2) == []
