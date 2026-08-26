# Reference solution for ex07_fizzbuzz_plus — see
# exercises/ex07_fizzbuzz_plus.py for the scenario.


def fizzbuzz(n: int) -> str:
    """Classic fizzbuzz rule for a single number.

    n -> result
    3 -> "Fizz"
    5 -> "Buzz"
    15 -> "FizzBuzz"
    7 -> "7"
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def fizzbuzz_run(limit: int) -> str:
    """Join fizzbuzz(i) for i in 1..limit with ", ", via an accumulator.

    limit -> result
    5 -> "1, 2, Fizz, 4, Buzz"
    """
    result = ""
    for i in range(1, limit + 1):
        if result:
            result += ", "
        result += fizzbuzz(i)
    return result


def times_table(n: int) -> str:
    """Build an n-by-n multiplication table as a multi-line string.

    Rows are newline-separated, entries within a row are space-separated,
    both built with nested for loops and string accumulators.

    n -> result
    3 -> "1 2 3\\n2 4 6\\n3 6 9"
    """
    result = ""
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            if row:
                row += " "
            row += str(i * j)
        if result:
            result += "\n"
        result += row
    return result
