import asyncio

from ex03_tasks import first_done, race


def test_race_returns_both_results_in_call_order():
    log: list[str] = []
    result = asyncio.run(race(log))
    assert result == ("fast", "slow")


def test_race_logs_prove_both_started_before_either_finished():
    log: list[str] = []
    asyncio.run(race(log))
    assert log == ["start:fast", "start:slow", "end:fast", "end:slow"]


def test_first_done_returns_the_fastest_result():
    async def slow() -> str:
        await asyncio.sleep(0.02)
        return "slow"

    async def fast() -> str:
        await asyncio.sleep(0.005)
        return "fast"

    result = asyncio.run(first_done([slow(), fast()]))
    assert result == "fast"


def test_first_done_works_regardless_of_list_order():
    async def slow() -> str:
        await asyncio.sleep(0.02)
        return "slow"

    async def fast() -> str:
        await asyncio.sleep(0.005)
        return "fast"

    result = asyncio.run(first_done([fast(), slow()]))
    assert result == "fast"
