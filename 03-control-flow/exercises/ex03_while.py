# Scenario: a rocket launch script needs a countdown string, and mission
# control wants to know how many Collatz steps a number takes. Covers:
# while loops, loop guards, the infinite-loop mistake.
# Run: uv run pytest 03-control-flow -k ex03


def countdown(n: int) -> str:
    """Build a launch countdown string with a while loop.

    Counts from n down to 1, then appends "liftoff", all joined with
    hyphens. n < 1 skips straight to "liftoff" (nothing to count down).

    n -> result
    3 -> "3-2-1-liftoff"
    1 -> "1-liftoff"
    0 -> "liftoff"
    """
    raise NotImplementedError


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
    raise NotImplementedError
