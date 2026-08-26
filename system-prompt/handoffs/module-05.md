# Handoff: Module 05 — Functions

Build `05-functions/` in the course repo. Read `CONVENTIONS.md` (same
folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–04 (values, control flow, collections,
comprehensions). Decorators, generators, closures-as-decorators are
module 09 — do NOT go there. Type hints are module 10 — solutions and
stubs stay unannotated in modules 05–09.

## LESSON.md outline
1. Why this exists: naming a computation so you can reuse and test it;
   functions are values.
2. Anatomy of a call — REQUIRED diagram: flowchart of how arguments map
   to parameters (positional → keyword → defaults → *args → **kwargs).
3. Defaults + the mutable-default trap — REQUIRED diagram: default
   object created ONCE at def-time, shared across calls; the
   `None`-sentinel fix.
4. `*args` / `**kwargs`: collecting and forwarding.
5. Keyword-only (`*,`) and positional-only (`/`) parameters — when APIs
   want them.
6. Scope & LEGB — REQUIRED diagram: Local → Enclosing → Global →
   Builtins lookup; `global` and `nonlocal` in one short paragraph each.
7. Closures: functions that remember; factory pattern.
8. `lambda`: single expressions only, mainly as `key=`; prefer a named
   function when it grows.
9. Recursion: base case + smaller problem; call-stack diagram.
10. Gotchas table: mutable default, closure capturing the loop variable,
    shadowing builtins, returning None implicitly.
11. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_define_return.py` — `rectangle_info(w, h)` returns an
  `(area, perimeter)` tuple; `clamp(value, lo, hi)`; implicit-None
  drill: fix `greet_missing_return`.
- `ex02_defaults_trap.py` — `power(base, exp=2)`; then the trap:
  `add_item(item, items=[])` ships with the REAL bug (shared list) —
  student fixes with the None-sentinel; test calls it twice and asserts
  independence.
- `ex03_star_args.py` — `average(*nums)` (None on empty), `longest(*words)`,
  `html_tag(name, **attrs)` -> `'<a href="x" id="y">'` (sorted attrs),
  `forward_call(func, *args, **kwargs)` pass-through.
- `ex04_keyword_only.py` — `make_user(name, *, admin=False, active=True)`;
  `divide(a, b, /)` positional-only; tests assert `TypeError` when
  called wrongly (`pytest.raises`).
- `ex05_scope.py` — prediction drills on LEGB (return the value a
  snippet produces); `make_id_generator` style counter using `nonlocal`;
  a fix-it where a function wrongly relies on `global`.
- `ex06_closures.py` — `make_multiplier(k)`, `make_accumulator()`,
  and the loop-capture trap: `make_button_handlers` returning a list of
  functions that must each remember THEIR index (fix via default-arg
  binding or a factory).
- `ex07_sorting_keys.py` — `sorted` with `key=lambda`: sort records by
  age, by (last, first); `top_by(items, key_func, n)` taking a function
  as argument.
- `ex08_recursion.py` — `sum_digits(n)`, `flatten(nested)` (arbitrarily
  nested lists), `count_down_up(n)` building a string like
  `"3 2 1 1 2 3"` recursively.

## Checkpoint (`checkpoint_05.py`)
Text-stats toolkit: `word_stats(text, *, min_length=1, stop_words=None)`
(None-sentinel for the mutable default) returning a dict of counts;
`make_formatter(prefix, suffix="")` closure returning a formatting
function; `apply_all(value, *funcs)` threading a value through functions
left-to-right. Tests cover the sentinel behavior, closure independence,
and keyword-only enforcement.

## SUMMARY.md
Cheat-sheet: parameter-kinds table (positional-only / positional-or-kw /
*args / kw-only / **kwargs), LEGB rule, mutable-default recipe, closure
factory pattern. One mermaid mindmap. Self-quiz: 8 questions, answers in
`<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
