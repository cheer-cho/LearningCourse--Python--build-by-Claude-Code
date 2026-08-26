# Reference solution for ex03_while — see exercises/ex03_while.py for
# the scenario.


def countdown(n: int) -> str:
    """Build a launch countdown string with a while loop.

    Counts from n down to 1, then appends "liftoff", all joined with
    hyphens. n < 1 skips straight to "liftoff" (nothing to count down).

    n -> result
    3 -> "3-2-1-liftoff"
    1 -> "1-liftoff"
    0 -> "liftoff"
    """
    if n < 1:
        return "liftoff"
    result = ""
    i = n
    while i >= 1:
        result += f"{i}-"
        i -= 1
    result += "liftoff"
    return result


def collatz_steps(n: int) -> int | None:
    """Count the steps for the Collatz sequence starting at n to reach 1.

    Rule: even n -> n // 2; odd n -> 3 * n + 1. Repeat until n == 1 and
    count how many steps that took. Guards n < 1 by returning None (the
    sequence is only defined for positive integers).

    n -> result
    1 -> 0
    6 -> 8
    0 -> None
    """
    if n < 1:
        return None
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps
