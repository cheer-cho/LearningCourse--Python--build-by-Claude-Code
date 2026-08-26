import asyncio

from ex01_first_coroutine import fetch_greeting, get_greeting_buggy, run_fetch


def test_fetch_greeting_returns_hello_name():
    assert asyncio.run(fetch_greeting("Ada")) == "Hello, Ada!"


def test_fetch_greeting_handles_a_different_name():
    assert asyncio.run(fetch_greeting("Grace")) == "Hello, Grace!"


def test_run_fetch_returns_the_greeting():
    assert run_fetch("Grace") == "Hello, Grace!"


def test_run_fetch_works_for_another_name():
    assert run_fetch("Ada") == "Hello, Ada!"


def test_get_greeting_buggy_returns_a_string_not_a_coroutine():
    result = asyncio.run(get_greeting_buggy("Ada"))
    assert result == "Hello, Ada!"


def test_get_greeting_buggy_with_another_name():
    assert asyncio.run(get_greeting_buggy("Grace")) == "Hello, Grace!"
