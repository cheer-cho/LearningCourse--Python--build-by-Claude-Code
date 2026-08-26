import asyncio

from ex05_async_iterators import alimit, collect, ticker


def test_ticker_yields_the_expected_range():
    async def run() -> list[int]:
        return [x async for x in ticker(3)]

    assert asyncio.run(run()) == [0, 1, 2]


def test_ticker_with_zero_count_yields_nothing():
    async def run() -> list[int]:
        return [x async for x in ticker(0)]

    assert asyncio.run(run()) == []


def test_collect_gathers_everything_in_order():
    assert asyncio.run(collect(ticker(4))) == [0, 1, 2, 3]


def test_collect_on_empty_generator_returns_empty_list():
    assert asyncio.run(collect(ticker(0))) == []


def test_alimit_stops_at_n():
    assert asyncio.run(alimit(ticker(10), 3)) == [0, 1, 2]


def test_alimit_stops_early_without_exhausting_the_source():
    log: list[int] = []

    async def source():
        for i in range(5):
            log.append(i)
            yield i

    result = asyncio.run(alimit(source(), 2))
    assert result == [0, 1]
    assert log == [0, 1]  # item 2 was never pulled from the source


def test_alimit_returns_fewer_items_if_source_runs_out_first():
    assert asyncio.run(alimit(ticker(2), 5)) == [0, 1]
