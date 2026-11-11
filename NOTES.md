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
**Status:** improving: rewrote `go` and `repeat` with guard cases after the review (2026-11-05). Quiz 2026-11-06: needed the question reworded plus an analogous example, then wrote `case ("repeat", n) if n > 0:` correctly; re-quiz once more cold

## 2026-11-05 — 03 / checkpoint_03
**Mistake:** Used `is` to compare values (`guess is secret`, `result is "correct!"`). Tests passed only by accident: CPython caches small ints and interns some string literals, so identity happened to match. Python even emits `SyntaxWarning: "is" with 'str' literal`.
**Correction:** `==` compares values; `is` compares object identity. Use `is` only for singletons: `None`, `True`/`False`, sentinels. Demo: `playground/03-control-flow/is_vs_equals.py`.
**Status:** improving — fixed both after one hint (missed the int one at first)

## 2026-11-05 — 03 / checkpoint_03
**Mistake:** Wrote `play_round` without the `for/else` its docstring asked for, so an empty guess list returned `""`. Also used `enumerate(...)` plus `index + 1` instead of `enumerate(..., start=1)`.
**Correction:** Read the docstring as a spec: when it names a construct and an edge case, there should be a branch for that case. `enumerate(xs, start=1)` gives 1-based counters directly.
Follow-up: the fix used `if not len(results):` — Pythonic is `if not results:` (empty list is already falsy; see ex02_truthiness).
**Status:** improving — all three applied on review (for/else, `not results`, enumerate start). Confirm they stick in module 04 before marking overcome

## 2026-11-06 — 04 / dict `.get()` counting pattern
**Mistake:** Twice treated the default as the value that gets *stored*, skipping the `+ 1` on a key's first occurrence. (1) In TS: `counts[word] == undefined ? 0 : counts[word] + 1`, so new words were stored as 0. (2) Predicted `counts.get(word, 10) + 1` stores 10 on first sight, when it stores 11.
**Correction:** `.get(key, default)` only answers "the current value, or the default if the key is missing." The `+ 1` then applies to whatever comes back, in both cases. Read it as two steps: look up, then update. In TS that's `(counts[word] ?? 0) + 1`, with the `+ 1` outside the fallback.
**Status:** improving: wrote `words.get(word, 0) + 1` correctly in ex03_dicts (2026-11-06). Check again when Counter/defaultdict come up in module 04

## 2026-11-06 — 04 / comprehensions
**Mistake:** Predicted that `{name: len(name) for name in names}` and `{name[0] for name in names}` both return lists. Read every comprehension as a list, whatever brackets it uses.
**Correction:** The brackets decide the result type: `[...]` gives a list, `{k: v ...}` (with a colon) gives a dict, `{x ...}` (no colon) gives a set, which removes duplicates and has no order. Demo: `playground/04-collections/comprehension_shapes.py`.
**Status:** improving: got dict vs set right on the second try (2026-11-06); ex06_comprehensions (2026-11-06): wrote list, dict, and set comprehensions with the right brackets unprompted. Quiz 2026-11-09: answered `type({})` is `dict` and the empty set is `set()`, both correct. One more cold check later, then mark overcome

## 2026-11-06 — 04 / ex01_lists
**Mistake:** Tests passed, but the code skipped what the docstring asked for. Same root as ex05 and ex06 in module 03. (1) `insert_sorted` used `append` + `sort()`, ignoring "already sorted" and the `insert` concept. (2) `without_negatives` used a comprehension when the docstring said "plain `for` loop". (3) `top_three` used `sorted(...)[::-1]` instead of `sorted(..., reverse=True)`.
**Correction:** The docstring is part of the spec. When it names a construct or a precondition (e.g. "already sorted"), the solution should use it. Tests can check *what* comes back, not *how*. For a list that is already sorted, find the index and `insert` (in real code, `bisect.insort`). To sort descending, use `reverse=True`, not a reversed copy.
**Status:** improving: all three rewritten to spec after a nudge plus a flowchart for the index scan (2026-11-06). Minor follow-ups: a redundant `elif item >= x` (the opposite of the `if`, so use `else` or break first), and the name `positive_nums` for a filter that keeps 0.

## 2026-11-06 — 04 / ex02_tuples_unpacking
**Mistake:** Tests passed, but again the docstring's named construct went unused: `distance` indexed `p[0]`, `q[1]` when the docstring said "unpacking each tuple into its x, y parts". Also `min_max` sorted the whole list (O(n log n)) to read two ends, `return (head, rest)` kept the habit of parenthesizing tuples, and debug `print(...)` calls were left at module level, so they run on every import (including pytest's).
**Correction:** Same root as ex01: the docstring is spec. Unpack into names (`x1, y1 = p`) so the math reads like the formula. `min()` and `max()` are each one O(n) pass. The comma makes the tuple, so `return head, rest`. Scratch prints go under `if __name__ == "__main__":` or in `playground/`.
**Status:** improving: everything fixed, including the leftover parentheses (2026-11-06). Watch for unparenthesized tuples sticking in ex03+. ex03_dicts (2026-11-06): debug `print(...)` calls left at module level again (removed on review, plus renamed `words` → `counts`); the docstring spec was followed fully (`.get` with a default, `.split()`, counting idiom). ex04_sets (2026-11-06): clean — no stray prints, every function a one-liner; used `.intersection()`/`.difference()` methods where the operators `&`/`-` fit. ex06_comprehensions (2026-11-06): module-level `print(...)` calls again (3rd time in module 04), so this is now a habit to break. Default to `playground/` for scratch runs. Fixed on review (2026-11-07) by moving them under `if __name__ == "__main__":` at file level, with correct PEP 8 spacing

## 2026-11-08 — 04 / ex07_records
**Mistake:** (1) `emails_of` added `if user["email"]`, a filter the spec never asked for (a TS `.filter(u => u.email)` reflex). It silently drops `""` emails and still raises `KeyError` on a missing key. (2) `find_user` returned `{ "name", name }`, a **set** (comma, no colon), not the matching record, and returned `"Nobody"` (copied from the docstring example's *input*) instead of `None`. (3) `== True` in a filter. (4) Briefly swapped early return for a sentinel + `break`.
**Correction:** Do exactly what the spec says and let bad data fail loudly, with no defensive filters unless the spec asks for one. A colon makes a dict and a comma-only `{}` makes a set (same root as the comprehension-brackets entry). When you find the item, return the object you already hold (`return user`). Read docstring examples as `call -> result`. Use truthiness, not `== True`. In a search function, return inside the loop and `return None` after it.
**Status:** improving: all fixed after concept/nudge hints (2026-11-09); no stray prints this time. Minor leftover: `.get("name")` where `["name"]` fits. ex05_slicing (2026-11-09): clean, no stray prints, no extra guards, and the one guard it has (`if not items` before `% len(items)`) is needed

## 2026-11-09 — 04 / ex05_slicing
**Mistake:** Wrote `items[1:len(items) - 1]` instead of using a negative index. Not a bug, just the long way round.
**Correction:** Negative indices count from the end: `-1` is the last item. So "drop first and last" is `items[1:-1]`, and "last three" is `s[-3:]`. Slices never raise `IndexError`, so `[1][1:-1]` and `[][1:-1]` both give `[]`. (JS `arr.slice(1, -1)` works the same way.)
**Status:** improving: switched to `items[1:-1]` after the review (2026-11-09); it was typed `[1:- 1]` at first (a space after a unary minus). Check for `len(x) - k` inside brackets in later exercises

## 2026-11-09 — 04 / ex08_copy_alias
**Mistake:** (1) `safe_flat_copy` returned `base + extra`, a list plus an int, which raises `TypeError`. `+` on lists only joins two lists. (2) `independent_deep_copy` made the deep copy and then appended to `board` (the original), not to `copied`, so it mutated the input and returned a copy without the new value. (3) `broken_reset` used `copy.deepcopy` on a flat `list[int]`; it works, but a shallow copy is enough there.
**Correction:** After copying, keep track of which name points at which object. The copy is the one you change and return. Use a shallow copy (`list(x)`, `x.copy()`, `x[:]`) when the items are immutable (ints, strs), and save `deepcopy` for nested mutable data. Demo: `playground/04-collections/alias_vs_copy_demo.py`.
**Status:** improving: both bugs fixed after one hint each (2026-11-09): `base + [extra]` and `copied[row].append(value)`. Then switched `broken_reset` to `list(scores)` and predicted the `board[:]` + `other[0].append(99)` puzzle correctly (shared rows, unshared outer list). Check once more in a later quiz, then mark overcome

## 2026-11-10 — 04 / checkpoint_04
**Mistake:** Tests passed, but two spec bugs got through. (1) `honor_roll` never called `sorted`, even though the docstring says "sorted alphabetically". It worked only because the test data was already in alphabetical order (`{"Zed": [95], "Ada": [92]}` → `['Zed', 'Ada']`). (2) `class_stats` started with `highest_score = 0` and `best_student = None`, so if every average is 0 it returns `None` as the best student. A made-up starting value is a guess about the data. (3) Module-level `book = {}` / `print(book)` was left in again (4th time in module 04). (4) TS-style hand-written loops where a comprehension or a built-in fits: `averages` built its dict with a loop, and `class_stats` counted by hand when `len(book)` and `max(..., key=...)` already do the job.
**Correction:** Check every phrase of the docstring against the code: "sorted" means a `sorted(...)` call. Don't invent a starting value for a max. Use `max(iterable, key=...)`, or start from the first real item. Use built-ins (`len`, `sum`, `max`) and comprehensions before writing manual counters.
Follow-up (2026-11-10): fixed `averages` (dict comprehension) and removed the stray print. But the `honor_roll` fix used `[...].sort()`, which returns `None`. That's the TS habit of chaining `arr.sort()`. In Python, methods that change an object in place return `None`, so use `sorted(...)` when you want a value back. A half-typed line in `class_stats` was also left in, a SyntaxError that broke collection of the whole file.
**Status:** improving: all fixed (2026-11-10). `class_stats` was rewritten with `len`, `averages()` plus `max(..., key=...)`, a flattening comprehension, and `sum/len`. Along the way it briefly divided a list by an int and divided by the student count instead of the score count, both fixed after a nudge. Leftovers: the helper is annotated `dict[str, float]` instead of `tuple[str, float]`, it still has `return (a, b, c)` parentheses, and `max(d, key=d.get)` hasn't been learned yet. Quiz later on `sorted` vs `.sort()` and on overall avg vs avg of avgs
