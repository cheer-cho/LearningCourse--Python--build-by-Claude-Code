import functools
import operator


def make_base_parser(base):
    """Return a function that parses a string in the given numeric
    `base` into an int, built with functools.partial around the
    built-in int() (which already accepts a `base` keyword).

    parse_hex = make_base_parser(16)
    parse_hex("ff") -> 255
    parse_binary = make_base_parser(2)
    parse_binary("101") -> 5
    """
    return functools.partial(int, base=base)


def product_of(nums):
    """Multiply every number in `nums` together using functools.reduce
    (an empty product is 1, same as an empty sum is 0).

    product_of([1, 2, 3, 4]) -> 24
    product_of([]) -> 1
    """
    return functools.reduce(operator.mul, nums, 1)


@functools.lru_cache(maxsize=None)  # noqa: UP033 — lru_cache is the exercise's topic
def slow_fib(n):
    """Recursive Fibonacci, memoized with functools.lru_cache so a
    repeated call with the same `n` never recomputes. `slow_fib.calls`
    counts how many times the function BODY actually ran (cache hits
    don't increment it) — proof the cache is working.

    slow_fib.calls = 0
    slow_fib(10) -> 55
    slow_fib.calls -> 11        # n=0..10, each computed once
    slow_fib(10) -> 55          # fully cached
    slow_fib.calls -> 11        # unchanged: no new work
    """
    slow_fib.calls += 1
    if n < 2:
        return n
    return slow_fib(n - 1) + slow_fib(n - 2)


slow_fib.calls = 0


@functools.singledispatch
def describe(value):
    """Describe a value's type and content. Base implementation for any
    type not specifically registered below; int/str/list get their own
    overload via functools.singledispatch (registered by type, not by
    annotation, since this module skips type hints).

    describe(5) -> "int: 5"
    describe("hi") -> "str: 'hi' (2 chars)"
    describe([1, 2]) -> "list: 2 items"
    describe(3.14) -> "value: 3.14"   # fallback: no overload for float
    """
    return f"value: {value!r}"


@describe.register(int)
def _describe_int(value):
    return f"int: {value}"


@describe.register(str)
def _describe_str(value):
    return f"str: {value!r} ({len(value)} chars)"


@describe.register(list)
def _describe_list(value):
    return f"list: {len(value)} items"
