# Scenario: the classic fizzbuzz drill, extended into a full run and a
# multiplication table. Covers: for loops, string accumulators, nested
# loops.
# Run: uv run pytest 03-control-flow -k ex07


def fizzbuzz(n: int) -> str:
    """Classic fizzbuzz rule for a single number.

    n -> result
    3 -> "Fizz"
    5 -> "Buzz"
    15 -> "FizzBuzz"
    7 -> "7"
    """
    raise NotImplementedError


def fizzbuzz_run(limit: int) -> str:
    """Join fizzbuzz(i) for i in 1..limit with ", ", via an accumulator.

    limit -> result
    5 -> "1, 2, Fizz, 4, Buzz"
    """
    raise NotImplementedError


def times_table(n: int) -> str:
    """Build an n-by-n multiplication table as a multi-line string.

    Rows are newline-separated, entries within a row are space-separated,
    both built with nested for loops and string accumulators.

    n -> result
    3 -> "1 2 3\\n2 4 6\\n3 6 9"
    """
    raise NotImplementedError
