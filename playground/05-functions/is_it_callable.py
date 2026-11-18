"""How to check whether something is a function (or can be called like one)."""

import inspect


def greet(name: str) -> str:
    return f"hi {name}"


class Doubler:
    def __call__(self, x: int) -> int:  # instances of this class can be called
        return x * 2


candidates = {
    "def function": greet,
    "lambda": lambda x: x + 1,
    "built-in (len)": len,
    "class (int)": int,
    "object with __call__": Doubler(),
    "number": 42,
    "string": "greet",
    "list of functions": [greet],
}

print(f"{'thing':<22} {'callable()':<12} {'inspect.isfunction()'}")
for label, thing in candidates.items():
    print(f"{label:<22} {callable(thing)!s:<12} {inspect.isfunction(thing)}")

# EAFP: often you don't check first, you just call it and handle failure.
try:
    candidates["number"](5)
except TypeError as err:
    print(f"\nEAFP caught: {err}")
