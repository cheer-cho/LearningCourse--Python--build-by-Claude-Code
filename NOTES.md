# Instructor Notes — Recurring Mistakes

The instructor logs recurring mistakes here and revisits them during
quizzes and reviews. Format:

```
## YYYY-MM-DD — module/exercise
**Mistake:** what happened (the misconception, not just the code)
**Correction:** the right mental model
**Status:** open | improving | overcome
```

---

## 2026-10-30 — 01 / ex03_main_guard
**Mistake:** Put `if __name__ == "__main__": return` *inside* `main()`, thinking the guard belongs to the function.
**Correction:** The guard belongs to the *file*. It wraps the top-level `main()` call so the file only does work when run directly. Functions stay plain and always work when called.
**Status:** improving — checkpoint_01 (2026-10-30) put the guard at file level correctly

## 2026-10-30 — 02 / names & references (intro)
**Mistake:** Thought `b = a` makes `b` permanently follow `a`, so after `a = a + [3]` "b still = a".
**Correction:** `b = a` binds `b` to the *object* `a` points at right now, not to the name `a`. Assignment only moves the label on its left; rebinding `a` never moves `b`. Only mutation (`a += [3]`, `.append`) is visible through both names.
**Status:** improving: predicted ex07 `rebind_vs_alias` correctly (2026-11-01); next check: `b += [3]` mutates lists

## 2026-10-31 — 02 / ex01_numbers
**Mistake:** Used `f"{x:.2f}"` to "round" a number to return, then wrapped it in `int()`. That gives a `str` (or a `ValueError` from `int("40.00")`), not a float.
**Correction:** `round(x, 2)` returns a number, so use it to compute or return a value. `f"{x:.2f}"` returns a string, so use it only for display. Watch that the return type matches the annotation.
**Status:** improving: fixed with `round()` after a hint

## 2026-10-31 — 02 / ex02_strings
**Mistake:** Unpacked with list brackets, `[first, last] = s.split(" ")`, the way TS writes `const [a, b] = ...`. Also used `split(" ")` out of habit.
**Correction:** In Python, write tuple unpacking without brackets: `first, last = s.split()`. With no argument, `split()` splits on any run of whitespace and drops empty pieces from the ends, so it's the safer default. Use `split(" ")` only when you really mean "split on every single space".
**Status:** improving: fixed both in the same session after review

## 2026-11-01 — 02 / ex04_bools
**Mistake:** Wrapped boolean expressions in `if cond: return True / return False` (all three functions). Also wrote `age >= 13 and age <= 19` instead of a chained comparison.
**Correction:** Comparisons (`==`, `is`, `<=`) already evaluate to a `bool`, so `return cond` directly. Python allows chained comparisons: `13 <= age <= 19`.
**Status:** improving: wrote all three one-liners (incl. the chained comparison) after hints

## 2026-11-02 — 02 / checkpoint_02
**Mistake:** Left a trailing comma after each `line1 = f"..."` assignment, which silently made `line1` a 1-tuple, so `"\n".join(...)` raised `TypeError: expected str instance, tuple found`.
**Correction:** In Python the *comma* makes a tuple, not the parentheses: `x = 5,` is `(5,)`. TS has no equivalent, so a stray comma (e.g. copied from a list literal) is easy to miss. If a `print` shows `('...',)`, look for a trailing comma.
**Status:** improving: found and fixed it after a hint. Also still wrapping unpacking targets in parentheses (`(a, b, c) = items[0]`) and unpacking per index instead of `(a1, b1, c1), (...), (...) = items`.

## 2026-11-04 — 03 / ex01_branches
**Mistake:** Wrapped every `if`/`elif` condition in parentheses, `if (score >= 90):`, the way TS/JS requires `if (...)`. Same root habit as the parenthesized unpacking targets in checkpoint_02.
**Correction:** In Python the colon ends the condition, so no parentheses are needed: `if score >= 90:`. PEP 8 style leaves them out. Use parentheses only to group a sub-expression or to break a long condition across lines.
**Status:** improving: removed all of them right after the review (2026-11-04); ex02 written with no parentheses unprompted (2026-11-04); slipped back once in ex03 (`while (n != 1):`) and removed it after the review

## 2026-11-04 — 03 / ex03_while
**Mistake:** Two infinite loops. (1) `countdown` never changed `n` inside `while n > 0:`, so the condition stayed true forever. (2) `collatz_steps` guarded only `n == 0` when the spec said `n < 1`, so `-3` cycled between -1 and -2 forever.
**Correction:** Every `while` loop needs a start value, a condition, and a step that moves toward ending it. Check that the body changes what the condition tests. A guard should reject the whole range of invalid input (`n < 1`), not one example of it (`n == 0`). Write the guard in the same words as the spec.
**Status:** improving: fixed both after concept- and nudge-level hints (2026-11-04)

## 2026-11-04 — 03 / ex04_for_range
**Mistake:** (1) Named an accumulator `sum`, shadowing the built-in `sum()` for the rest of the function. (2) Added `if n < 0: return None` to `stripes`, a guard the spec never asked for, and it breaks the `-> str` return type (mypy flags it). `range(-3)` is already empty, so the loop returns `""` anyway.
**Correction:** Don't reuse built-in names (`sum`, `list`, `str`, `max`, `id`, `input`) for variables; pick `total`, `items`, etc. Guards follow the spec: add one only when the docstring says so, and make the returned value match the annotation. Opposite side of the ex03 lesson: write the guard the spec asks for — no narrower, no extra.
**Status:** improving: renamed to `total` and removed the extra guard after the review (2026-11-05); mypy clean

## 2026-11-05 — 03 / ex05_break_else
**Mistake:** (1) `is_prime` guarded only `n == 1`, so `is_prime(0)` and `is_prime(-7)` returned `True` (empty `range` → `else` runs). Same root as ex03's `n == 0` guard. (2) Used `return` inside every `for` loop and still added an `else:`, which then never matters, so the `break`/`else` pattern the exercise teaches went unused.
**Correction:** A guard covers the whole invalid range (`n < 2`), not one example of it. `return` exits the function, so an `else` after the loop is redundant: either drop the `else` and put the fallback after the loop, or use `break` + `else` when the loop sets a variable that later code uses.
**Status:** improving: guard fixed to `n <= 1` after a nudge (2026-11-05); removed the redundant `else` from `is_prime` once shown return-vs-break side by side (playground `return_vs_break_else.py`)

## 2026-11-05 — 03 / ex06_match
**Mistake:** Matched loose patterns (`("go", direction)`, `("repeat", times)`) and then decided the outcome with a ternary inside the case body. Tests pass, but the guard clause the exercise teaches went unused. Same root as ex05: the result is right, but the construct the exercise teaches isn't used.
**Correction:** In `match`, the pattern (plus an optional `if` guard) is where the decision lives. Write one `case` per outcome, e.g. `case ("repeat", n) if n > 0:` then `case ("repeat", _):`. Each case reads as one rule, and the body just returns. Use a tuple or set for fixed membership checks, not a list.
**Status:** improving: rewrote `go` and `repeat` with guard cases after the review (2026-11-05)
