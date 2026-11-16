"""Why closure factories exist: the loop-capture bug, two fixes, and the
trade-off between them. Companion to closure_factory.md.

Run: uv run python playground/05-functions/closure_factory.py
"""

from collections.abc import Callable

LABELS = ["Save", "Cancel", "Delete"]


# --- 1. The bug: every closure shares the SAME loop variables ---------------
def broken(labels: list[str]) -> list[Callable[[], str]]:
    handlers = []
    for i, label in enumerate(labels):

        def handler() -> str:
            return f"{label} clicked (button {i})"  # looked up LATER

        handlers.append(handler)
    return handlers


print("1. broken:")
for h in broken(LABELS):
    print("  ", h())  # all three say "Delete clicked (button 2)"

# Proof they share one variable: the cells are literally the same object.
hs = broken(LABELS)
print("   same cell?", hs[0].__closure__[0] is hs[2].__closure__[0])  # True


# --- 2. Fix A: default-argument trick ---------------------------------------
def with_defaults(labels: list[str]) -> list[Callable[..., str]]:
    handlers = []
    for i, label in enumerate(labels):

        def handler(i: int = i, label: str = label) -> str:  # copied NOW
            return f"{label} clicked (button {i})"

        handlers.append(handler)
    return handlers


print("\n2. default-arg trick:")
for h in with_defaults(LABELS):
    print("  ", h())
print("   leak:", with_defaults(LABELS)[0](99, "Oops"))  # caller can override!


# --- 3. Fix B: a factory gives each handler its own scope --------------------
def create_handler(i: int, label: str) -> Callable[[], str]:
    def handler() -> str:
        return f"{label} clicked (button {i})"

    return handler  # the function itself, not handler()


def with_factory(labels: list[str]) -> list[Callable[[], str]]:
    return [create_handler(i, label) for i, label in enumerate(labels)]


print("\n3. factory:")
for h in with_factory(LABELS):
    print("  ", h())

hs = with_factory(LABELS)
print("   same cell?", hs[0].__closure__[0] is hs[2].__closure__[0])  # False
try:
    hs[0](99, "Oops")  # type: ignore[call-arg]
except TypeError as e:
    print("   override blocked:", e)


# --- 4. The mistake to avoid: a "factory" that returns the RESULT ------------
def not_a_factory(i: int, label: str) -> str:
    return f"{label} clicked (button {i})"  # runs now, returns a str


print("\n4. not a factory:", repr(not_a_factory(0, "Save")), "- a str, not callable")
