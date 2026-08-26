import asyncio

from ex02_gather import fetch_all


def test_fetch_all_preserves_input_order_in_results():
    log: list[str] = []
    results = asyncio.run(fetch_all(["a", "b", "c"], log))
    assert results == ["a-data", "b-data", "c-data"]


def test_fetch_all_logs_show_interleaving_not_sequential_order():
    log: list[str] = []
    asyncio.run(fetch_all(["a", "b", "c"], log))
    # all three must have STARTED before any of them finished — that's
    # only possible if they ran concurrently, not one after another.
    last_start_index = max(log.index("start:a"), log.index("start:b"), log.index("start:c"))
    first_end_index = min(log.index("end:a"), log.index("end:b"), log.index("end:c"))
    assert last_start_index < first_end_index


def test_fetch_all_finishes_shorter_delays_first():
    log: list[str] = []
    asyncio.run(fetch_all(["a", "b", "c"], log))
    # "a" got the longest delay (earliest in the list), "c" the shortest
    assert log.index("end:c") < log.index("end:b") < log.index("end:a")


def test_fetch_all_with_two_names():
    log: list[str] = []
    results = asyncio.run(fetch_all(["x", "y"], log))
    assert results == ["x-data", "y-data"]
    assert log.index("end:y") < log.index("end:x")
