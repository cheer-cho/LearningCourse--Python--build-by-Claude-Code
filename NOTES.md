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
**Status:** improving: removed all of them right after the review (2026-11-04); ex02 written with no parentheses unprompted (2026-11-04)
