"""Closures under the hood: cells, independent state, and late binding.

Run: uv run python playground/05-functions/closure_cells.py
"""

from collections.abc import Callable


# ── 1. A closure keeps the outer variable alive after the outer returns ──
def make_greeter(greeting: str) -> Callable[[str], str]:
    def greet(name: str) -> str:
        return f"{greeting}, {name}!"

    return greet  # make_greeter's frame is gone, but `greeting` survives


hi = make_greeter("Hi")
yo = make_greeter("Yo")
print("1. Captured values")
print("  ", hi("Ada"), "|", yo("Ada"))

# Peek inside: captured names live in "cells" attached to the function.
print("   free vars:  ", hi.__code__.co_freevars)  # ('greeting',)
assert hi.__closure__ is not None and yo.__closure__ is not None
print("   hi's cell:  ", hi.__closure__[0].cell_contents)  # Hi
print("   yo's cell:  ", yo.__closure__[0].cell_contents)  # Yo


# ── 2. Each factory call = a fresh cell = independent state ──────────────
def make_step_counter(step: int) -> Callable[[], int]:
    value = 0

    def advance() -> int:
        nonlocal value
        value += step
        return value

    return advance


by_one = make_step_counter(1)
by_ten = make_step_counter(10)
print("\n2. Independent state")
print("   by_one:", by_one(), by_one(), by_one())  # 1 2 3
print("   by_ten:", by_ten(), by_ten())  # 10 20  (unaffected by by_one)


# ── 3. Closures capture the VARIABLE, not its value at that moment ───────
def make_reader() -> tuple[Callable[[], str], Callable[[str], None]]:
    mood = "calm"

    def read() -> str:
        return mood  # looked up when read() RUNS, not when it was defined

    def set_mood(new: str) -> None:
        nonlocal mood
        mood = new

    return read, set_mood


read, set_mood = make_reader()
print("\n3. Late binding (shared cell)")
print("   before:", read())  # calm
set_mood("excited")
print("   after: ", read())  # excited: read() sees the new value


# ── 4. Closure vs class: same idea, two spellings ────────────────────────
class StepCounter:
    def __init__(self, step: int) -> None:
        self.step = step
        self.value = 0

    def advance(self) -> int:
        self.value += self.step
        return self.value


obj = StepCounter(5)
fn = make_step_counter(5)
print("\n4. Closure vs class")
print("   class:  ", obj.advance(), obj.advance())  # 5 10
print("   closure:", fn(), fn())  # 5 10
