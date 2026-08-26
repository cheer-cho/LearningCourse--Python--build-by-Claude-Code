# Handoff: Module 07 — Modules & Organization

Build `07-modules-organization/` in the course repo. Read
`CONVENTIONS.md` (same folder) and the master spec first. You own ONLY
this folder.

Audience: completed modules 01–06. No classes (module 08), no type
hints (module 10).

## Two special rules for this module
This module creates PACKAGES inside `exercises/`, which needs care:

1. **Naming**: the unique-filename rule applies to packages too —
   prefix every package and module with `mod07_` (e.g. `mod07_shop/`).
   The root conftest puts `exercises/` and the module root on sys.path,
   so `import mod07_shop` works from tests.
2. **The `_impl` pattern (required)**: `scripts/verify_solutions.py`
   overlays only FLAT `solutions/*.py` files onto `exercises/*.py` and
   the root `checkpoint_NN.py` — it cannot reach files nested inside
   package folders. Therefore: package files are GIVEN and thin — each
   imports its logic from a flat companion stub, e.g.
   `mod07_shop/pricing.py` contains only
   `from mod07_shop_pricing_impl import discounted` while
   `mod07_shop_pricing_impl.py` sits flat in `exercises/` and is the
   file the student edits (and the solution overlays). Say this in each
   affected file header ("edit the _impl file, not the package file").
   You MUST prove the pattern works by running
   `uv run python scripts/verify_solutions.py 07` → exit 0.

## LESSON.md outline
1. Why this exists: real programs span files; imports are how Python
   finds and wires them.
2. Import forms — table: `import x`, `from x import y`,
   `import x as z`, `from x import *` (and why to avoid the last).
3. REQUIRED diagram: flowchart of import resolution — sys.modules
   cache → sys.path search → module executes ONCE → cached.
4. Packages: folders with `__init__.py`; what `__init__` is for
   (public API, re-exports, `__all__`).
5. `if __name__ == "__main__"` recap for packages/scripts.
6. Circular imports — REQUIRED diagram: A imports B imports A → the
   standard fix (extract shared code into a third module).
7. "Batteries included": a table of go-to stdlib modules (math,
   statistics, string, random, datetime, json, re, pathlib,
   collections, itertools) — one line each; deep dive is module 12.
8. Project hygiene: pyproject.toml, `uv add`, virtualenvs —
   conceptual, 3 short paragraphs (repo is already set up; the student
   must NOT modify it).
9. Gotchas: shadowing a stdlib module with your filename,
   `from x import *` pollution, import-time side effects.
10. Try it now → exercises.

## Exercises (exactly 6)
- `ex01_import_forms.py` — functions that must use specific stdlib
  imports (named in docstrings): `circle_area` (math.pi),
  `middle_value` (statistics.median), `alphabet_position`
  (string.ascii_lowercase).
- `ex02_stdlib_pick.py` — "pick the right tool": `gcd_of` (math.gcd),
  `most_common_word` (collections.Counter — preview),
  `shuffle_deterministic(items, seed)` (a `random.Random(seed)`
  instance, never the global random — deterministic tests).
- `ex03` — package `mod07_shop/` (`__init__.py` given with re-exports;
  `pricing.py` and `cart.py` given as thin `_impl` importers). Student
  implements flat stubs `mod07_shop_pricing_impl.py` (`discounted`)
  and `mod07_shop_cart_impl.py` (`cart_total`, which imports
  `discounted` from the pricing impl). Test file
  `test_ex03_shop_package.py` uses only `from mod07_shop import ...`.
- `ex04_init_api.py` — package `mod07_geo/` where the LEARNING TARGET
  is the `__init__`: `mod07_geo/__init__.py` is given as
  `from ex04_init_api import *`-free thin importer of
  `ex04_init_api.py`, the flat stub where the student defines
  `distance`, `midpoint`, a private `_helper`, and `__all__`; the
  given `__init__` re-exports via the student's `__all__`. Test
  asserts `from mod07_geo import distance, midpoint` works and the
  helper is not in the package's public API.
- `ex05_script_main.py` — a runnable script: `run(argv)` returns an
  exit code and prints a report; `main()` guard calls
  `sys.exit(run(sys.argv[1:]))`. Tests call `run([...])` directly
  (capsys) AND once via subprocess
  (`["uv", "run", "python", <path>, "arg"]`, check=False) asserting
  stdout and exit code.
- `ex06_circular_fix.py` — the story (file header): `mod07_orders.py`
  and `mod07_customers.py` (both given, tiny) used to import each
  other for `format_money` and crashed with ImportError. The fix is
  half-done: both now import from flat stub `ex06_circular_fix.py`,
  where the student implements `format_money(cents)` and
  `pick_fix(options)` — a mini-quiz function returning which of three
  described strategies is the standard circular-import fix. Tests
  import orders + customers together (proving no cycle) and check both
  functions.

## Checkpoint
`checkpoint_07.py` (module root, flat as usual) — the student builds
the guts of a `checkpoint_07_pkg/` inventory package (given thin:
`__init__.py`, `inventory.py`, `reports.py` all importing from
`checkpoint_07.py`): implement `add_item`, `remove_item`,
`stock_count`, and `low_stock_report` (report imports nothing extra —
plain functions over a dict). `test_checkpoint_07.py` exercises the
package surface only (`from checkpoint_07_pkg import ...`), proving
the wiring. Solution: flat `solutions/checkpoint_07.py`.

## SUMMARY.md
Cheat-sheet: import-forms table, package-anatomy snippet, circular-fix
recipe, stdlib go-to table. One mermaid mindmap. Self-quiz: 6
questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md —
especially item 3 (verify_solutions) given the package caveat above.
