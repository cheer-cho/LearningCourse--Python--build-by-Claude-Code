"""Scope drills: read vs assign, `global`, `nonlocal`, and UnboundLocalError.

Run: uv run python playground/05-functions/legb_global_nonlocal.py
"""

from collections.abc import Callable

# ── 1. LEGB lookup: the first ring that has the name wins ─────────────────
color = "global red"


def outer() -> str:
    color = "enclosing green"

    def inner() -> str:
        # no `color` here (Local) → found in outer (Enclosing)
        return color

    return inner()


def no_enclosing() -> str:
    # no Local, no Enclosing → Global
    return color


def uses_builtin() -> int:
    # `len` isn't Local, Enclosing, or Global → Builtins
    return len("abc")


print("1. LEGB")
print("   inner():       ", outer())  # enclosing green
print("   no_enclosing():", no_enclosing())  # global red
print("   uses_builtin():", uses_builtin())  # 3


# ── 2. Read vs assign: an assignment ANYWHERE makes the name local ────────
score = 10


def read_only() -> int:
    return score + 1  # read → finds the global. No keyword needed.


def assign_new_local() -> int:
    score = 99  # assignment → brand-new LOCAL `score`; global untouched
    return score


def read_then_assign() -> int:
    # Python saw `score = ...` below at compile time, so `score` is local
    # for the WHOLE body, including this first line → nothing bound yet.
    score = score + 1  # noqa: F823 (deliberate bug)
    return score


print("\n2. Read vs assign")
print("   read_only():       ", read_only())  # 11
print("   assign_new_local():", assign_new_local())  # 99
print("   global score after:", score)  # still 10
try:
    read_then_assign()
except UnboundLocalError as err:
    print("   read_then_assign(): UnboundLocalError ->", err)


# ── 3. `global`: rebind the module-level name ─────────────────────────────
debug = False


def enable_debug() -> None:
    global debug  # "when I assign `debug`, I mean the module's `debug`"
    debug = True


print("\n3. global")
print("   debug before:", debug)  # False
enable_debug()
print("   debug after: ", debug)  # True


# ── 4. `nonlocal`: rebind the enclosing function's name ───────────────────
def make_limiter(max_calls: int) -> Callable[[], bool]:
    """Return a function that says True for the first `max_calls` calls."""
    remaining = max_calls

    def allow() -> bool:
        nonlocal remaining  # without this: UnboundLocalError, like section 2
        if remaining == 0:
            return False
        remaining -= 1
        return True

    return allow


print("\n4. nonlocal")
allow = make_limiter(2)
print("   ", [allow() for _ in range(4)])  # [True, True, False, False]


# ── 5. Mutating is NOT assigning → no keyword needed ──────────────────────
def make_logger() -> tuple[Callable[[str], None], Callable[[], list[str]]]:
    history: list[str] = []

    def log(msg: str) -> None:
        history.append(msg)  # mutates the SAME list; `history` isn't rebound

    def get() -> list[str]:
        return history

    return log, get


print("\n5. Mutation vs rebinding")
log, get = make_logger()
log("start")
log("stop")
print("   history:", get())  # ['start', 'stop']
