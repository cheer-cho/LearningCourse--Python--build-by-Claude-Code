from ex10_functools import describe, make_base_parser, product_of, slow_fib


def test_make_base_parser_hex():
    parse_hex = make_base_parser(16)
    assert parse_hex("ff") == 255


def test_make_base_parser_binary():
    parse_binary = make_base_parser(2)
    assert parse_binary("101") == 5


def test_make_base_parser_returns_independent_functions():
    parse_hex = make_base_parser(16)
    parse_octal = make_base_parser(8)
    assert parse_hex("10") == 16
    assert parse_octal("10") == 8


def test_product_of_multiplies_everything():
    assert product_of([1, 2, 3, 4]) == 24


def test_product_of_empty_is_one():
    assert product_of([]) == 1


def test_slow_fib_computes_correctly():
    assert slow_fib(10) == 55


def test_slow_fib_caches_repeat_calls():
    slow_fib.cache_clear()
    slow_fib.calls = 0
    assert slow_fib(10) == 55
    calls_after_first = slow_fib.calls
    assert slow_fib(10) == 55
    assert slow_fib.calls == calls_after_first


def test_slow_fib_body_runs_once_per_distinct_n():
    slow_fib.cache_clear()
    slow_fib.calls = 0
    slow_fib(10)
    assert slow_fib.calls == 11  # n = 0..10, each computed exactly once


def test_describe_int():
    assert describe(5) == "int: 5"


def test_describe_str():
    assert describe("hi") == "str: 'hi' (2 chars)"


def test_describe_list():
    assert describe([1, 2]) == "list: 2 items"


def test_describe_fallback_for_unregistered_type():
    assert describe(3.14) == "value: 3.14"
