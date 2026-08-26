# Scenario: a tiny number-theory toolkit needs a smallest-divisor finder,
# a primality check, and a character search. Covers: break, for/else.
# Run: uv run pytest 03-control-flow -k ex05


def first_divisor(n: int) -> int | None:
    """Find the smallest divisor of n that is 2 or greater.

    Loops upward from 2 and breaks the moment a divisor is found. A
    prime n divides itself, so the loop always finds something once
    n >= 2. Guards n < 2 by returning None.

    n -> result
    12 -> 2
    9 -> 3
    7 -> 7   (7 is prime — its smallest divisor > 1 is itself)
    1 -> None
    """
    raise NotImplementedError


def is_prime(n: int) -> bool:
    """Check primality with a for/else loop.

    Tries every candidate divisor from 2 up to (but not including) n.
    If any divides n evenly, break out — n is not prime. If the loop
    finishes without breaking, the else runs and reports n is prime.

    n -> result
    7 -> True
    8 -> False
    1 -> False
    """
    raise NotImplementedError


def find_char(s: str, c: str) -> int:
    """Find the index of the first occurrence of c in s.

    Walks s with enumerate to get index + character together, and
    breaks as soon as it matches. Returns -1 if c never appears.

    s, c -> result
    "hello", "l" -> 2
    "hello", "z" -> -1
    """
    raise NotImplementedError
