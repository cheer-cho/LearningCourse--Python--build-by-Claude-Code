"""How to type-hint a function that returns a function."""

from collections.abc import Callable


# Callable[[arg types], return type]
#   Callable[[str], str]  ->  takes one str, returns a str
#   Callable[[], bool]    ->  takes nothing, returns a bool
def make_greeter(greeting: str) -> Callable[[str], str]:
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet  # no () -> we return the function itself


def make_toggle() -> Callable[[], bool]:
    state = False

    def toggle() -> bool:
        nonlocal state
        state = not state
        return state

    return toggle


hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada!

flip = make_toggle()
print(flip(), flip(), flip())  # True False True
