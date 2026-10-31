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
**Status:** open

## 2026-10-31 — 02 / ex01_numbers
**Mistake:** Used `f"{x:.2f}"` to "round" a number to return, then wrapped it in `int()`. That gives a `str` (or a `ValueError` from `int("40.00")`), not a float.
**Correction:** `round(x, 2)` returns a number, so use it to compute or return a value. `f"{x:.2f}"` returns a string, so use it only for display. Watch that the return type matches the annotation.
**Status:** improving: fixed with `round()` after a hint
