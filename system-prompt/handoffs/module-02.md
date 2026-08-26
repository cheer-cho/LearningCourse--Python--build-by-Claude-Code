# Handoff: Module 02 — Values & Variables

Build `02-values-variables/` in the course repo. Read `CONVENTIONS.md`
(same folder) and the master spec first. You own ONLY this folder.

Audience: beginner who has completed module 01 (can run tests, read a
traceback, write a one-line function). Still assume NO knowledge of
conditionals or loops — exercises here must not need them. `if` may not
be used until module 03; simple expressions and conditional expressions
(`x if c else y`) are allowed only in ex05, where the lesson introduces
that one-liner explicitly.

## LESSON.md outline
1. Why this exists: programs are values with names attached; Python's
   core value types and how names bind to them.
2. Diagram: graph of core types (int, float, str, bool, None) grouped
   immutable vs mutable-preview.
3. Numbers: `+ - * / // % **`, `/` always float, `//` floor (mind
   negatives), `round()` banker's rounding gotcha.
4. Strings: quoting, escapes, common methods (upper/lower/strip/split/
   join/replace/startswith), indexing preview, `len()`.
5. f-strings: interpolation, `:.2f`, alignment/padding, `=` debug spec.
6. Names are labels, not boxes — REQUIRED diagram: two names pointing at
   one list object (aliasing) vs rebinding. This is the module's big
   idea.
7. `is` vs `==`, None conventions (`is None`).
8. Type conversions: `int("42")`, `float`, `str`, `ValueError` on bad
   input.
9. Gotchas table: `0.1 + 0.2`, integer division sign, `is` on small ints,
   string immutability.
10. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_numbers.py` — arithmetic drills: `minutes_to_hours_minutes`
  (uses // and %), `apply_discount` (float math, round to 2), `power_area`.
- `ex02_strings.py` — `shout(s)`, `initials("ada lovelace") -> "A.L."`
  (split + upper + join), `clean_username` (strip/lower/replace).
- `ex03_fstrings.py` — `price_tag(name, price) -> "Widget ... $ 3.50"`
  fixed-width alignment; `progress_line(pct)`; `debug_pair(x)` using
  `f"{x=}"`.
- `ex04_bools.py` — comparison chains: `is_teen(age)` via
  `13 <= age <= 19`; `same_object(a, b)` vs `same_value(a, b)` (is vs ==).
- `ex05_none_defaults.py` — `label_or_default(label)` returning
  `"(none)"` when `label is None` (introduce the conditional expression
  `x if cond else y` in the file header — one-liner only).
- `ex06_conversions.py` — `parse_price("$3.50") -> 3.5` (strip + float),
  `age_next_year("41") -> 42`; a test asserts `ValueError` propagates on
  garbage input (`pytest.raises`).
- `ex07_aliasing.py` — prediction drills: functions like
  `shared_append()` that build `a = [1, 2]; b = a; b.append(3)` and must
  return the RESULT the student predicts by completing a return
  statement (stub returns `...`-placeholder list); plus one with
  rebinding `b = b + [3]` showing the difference.
- `ex08_swap_and_augment.py` — tuple-swap `swap(a, b)`, augmented
  assignment drills, precedence puzzle `evaluate()` where the student
  parenthesizes an expression to hit a target value.

## Checkpoint (`checkpoint_02.py`)
Receipt formatter: `format_receipt(store, items)` where items is a list
of `(name, unit_price, qty)` tuples (iteration is NOT needed — cap items
at exactly 3 and unpack: `a, b, c = items`). Produces an aligned
multi-line receipt with subtotal, 7% tax, total — f-string number
formatting throughout. Also `parse_money("$12.30") -> 12.3` reused
inside. Tests check exact output lines.

## SUMMARY.md
Cheat-sheet: operator table, string-method table, f-string format-spec
mini-table, is-vs-== rule, aliasing diagram recap. One mermaid mindmap.
Self-quiz: 8 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
