import asyncio

from ex07_choose_model import choose, run_blocking_in_executor


def test_choose_many_http_calls_is_asyncio():
    assert choose("many_http_calls") == "asyncio"


def test_choose_resize_images_is_processes():
    assert choose("resize_images") == "processes"


def test_choose_blocking_sdk_calls_is_threads():
    assert choose("blocking_sdk_calls") == "threads"


def test_choose_compress_video_is_processes():
    assert choose("compress_video") == "processes"


def test_choose_poll_many_sockets_is_asyncio():
    assert choose("poll_many_sockets") == "asyncio"


def test_run_blocking_in_executor_returns_the_result():
    def blocking() -> int:
        return 42

    assert asyncio.run(run_blocking_in_executor(blocking)) == 42


def test_run_blocking_in_executor_does_not_block_other_coroutines():
    log: list[str] = []

    def blocking() -> str:
        log.append("blocking-done")
        return "blocking-result"

    async def other() -> None:
        log.append("other-ran")

    async def main() -> str:
        result, _ = await asyncio.gather(run_blocking_in_executor(blocking), other())
        return result

    result = asyncio.run(main())
    assert result == "blocking-result"
    assert "other-ran" in log
    assert "blocking-done" in log
