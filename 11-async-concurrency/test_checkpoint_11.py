import asyncio

from checkpoint_11 import download_all


def test_download_all_returns_content_for_every_job():
    jobs = [("a", False), ("b", False), ("c", False)]
    limit_log: list[int] = []
    results, errors = asyncio.run(download_all(jobs, worker_count=2, limit_log=limit_log))
    assert results == {"a": "a-content", "b": "b-content", "c": "c-content"}
    assert errors == []


def test_download_all_collects_one_failure_without_stopping_others():
    jobs = [("a", False), ("bad", True), ("c", False)]
    limit_log: list[int] = []
    results, errors = asyncio.run(download_all(jobs, worker_count=3, limit_log=limit_log))
    assert results == {"a": "a-content", "c": "c-content"}
    assert len(errors) == 1
    assert "bad" in errors[0]


def test_download_all_never_exceeds_the_concurrency_cap():
    jobs = [(f"job{i}", False) for i in range(6)]
    limit_log: list[int] = []
    asyncio.run(download_all(jobs, worker_count=6, limit_log=limit_log))
    assert limit_log
    assert max(limit_log) <= 2


def test_download_all_actually_reaches_the_concurrency_cap():
    jobs = [(f"job{i}", False) for i in range(6)]
    limit_log: list[int] = []
    asyncio.run(download_all(jobs, worker_count=6, limit_log=limit_log))
    assert max(limit_log) == 2


def test_download_all_empty_jobs_returns_empty_results():
    limit_log: list[int] = []
    results, errors = asyncio.run(download_all([], worker_count=2, limit_log=limit_log))
    assert results == {}
    assert errors == []


def test_download_all_multiple_failures_all_collected():
    jobs = [("a", True), ("b", True), ("c", False)]
    limit_log: list[int] = []
    results, errors = asyncio.run(download_all(jobs, worker_count=2, limit_log=limit_log))
    assert results == {"c": "c-content"}
    assert len(errors) == 2
