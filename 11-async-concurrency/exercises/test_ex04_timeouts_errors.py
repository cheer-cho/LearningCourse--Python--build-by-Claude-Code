import asyncio

from ex04_timeouts_errors import fetch_with_timeout, gather_safe


def test_fetch_with_timeout_returns_result_when_fast_enough():
    async def quick() -> str:
        await asyncio.sleep(0)
        return "data"

    result = asyncio.run(fetch_with_timeout(quick, 1.0, "fallback"))
    assert result == "data"


def test_fetch_with_timeout_returns_fallback_when_too_slow():
    async def slow() -> str:
        await asyncio.sleep(0.05)
        return "data"

    result = asyncio.run(fetch_with_timeout(slow, 0.01, "fallback"))
    assert result == "fallback"


def test_fetch_with_timeout_builds_a_fresh_coroutine_each_call():
    calls = []

    async def quick() -> str:
        calls.append(1)
        return "data"

    asyncio.run(fetch_with_timeout(quick, 1.0, "fallback"))
    asyncio.run(fetch_with_timeout(quick, 1.0, "fallback"))
    assert len(calls) == 2


def test_gather_safe_splits_results_and_errors():
    async def ok() -> int:
        return 1

    async def bad() -> int:
        raise ValueError("boom")

    async def ok2() -> int:
        return 2

    results, errors = asyncio.run(gather_safe([ok(), bad(), ok2()]))
    assert results == [1, 2]
    assert len(errors) == 1
    assert isinstance(errors[0], ValueError)


def test_gather_safe_all_success_has_no_errors():
    async def ok() -> int:
        return 42

    results, errors = asyncio.run(gather_safe([ok(), ok()]))
    assert results == [42, 42]
    assert errors == []
