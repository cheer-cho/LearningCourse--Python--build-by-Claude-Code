# Handoff: Module 09 — Pythonic Deep-Dive (THE HEART OF THE COURSE)

Build `09-pythonic-deep-dive/` in the course repo. Read
`CONVENTIONS.md` (same folder) and the master spec first. You own ONLY
this folder.

This is the course's flagship module — give it the most care, the most
exercises (12 + 4 idiom drills), and the richest checkpoint. Its theme:
Python's power comes from PROTOCOLS (dunders) and LAZINESS (iterators/
generators), composed by functions that take/return functions
(decorators). A student finishing this module writes Python that reads
like Python.

Audience: completed modules 01–08. No type hints (module 10).

## LESSON.md outline (may run a bit longer than other modules — but
   still tight prose; let the diagrams carry it)
1. Why this exists: `len(x)`, `for x in y`, `with`, `+` — every one is
   a protocol YOUR objects can join.
2. The data model — REQUIRED diagram: builtin/syntax on the left
   (len, for, in, +, ==, f-string, with, ()) mapped to the dunder each
   dispatches to.
3. Iteration protocol — REQUIRED diagram: iterable —__iter__→ iterator
   —__next__→ values → StopIteration; for-loops are sugar over it.
4. Generators — REQUIRED sequence diagram: caller and generator
   exchanging next()/yield, suspended state in between; generators ARE
   iterators; genexps; laziness = work only when asked; `yield from`.
5. Decorators — REQUIRED diagram: `@deco` rewiring name → wrapper
   around original; parameterized decorators as 3 layers;
   `functools.wraps`.
6. Context managers: the `__enter__`/`__exit__` flow;
   `@contextlib.contextmanager` = generator + one yield.
7. functools (partial, lru_cache, reduce, singledispatch) and
   itertools (chain, islice, groupby-needs-sorted, product, pairwise)
   — micro-example each.
8. What "Pythonic" means — comparison table: clunky vs idiomatic
   (range(len()) vs enumerate/zip; accumulator loop vs comprehension/
   sum/any; getter-setter vs property; key-in-check vs .get/setdefault;
   index juggling vs unpacking).
9. Gotchas: generators exhaust once; groupby without sort; decorators
   losing metadata without wraps; mutable state captured in closures.
10. Try it now → exercises (mention the drills explicitly).

## Exercises (exactly 12, `ex01`–`ex12`)
- `ex01_operator_dunders.py` — `Money`: `__add__`, `__mul__` (by int),
  `__lt__`/`__le__` (enable sorted), `__hash__` consistent with
  `__eq__`; return NotImplemented for foreign types.
- `ex02_container_protocol.py` — `Deck`: build once from ranks×suits;
  `__len__`, `__getitem__` (index AND slice → free `for`/`in`/
  `random.choice` compatibility), `__contains__`.
- `ex03_manual_iterator.py` — `Countdown`: separate iterable/iterator
  discipline (`__iter__` returns fresh iterator object `_CountdownIter`
  with `__next__` + StopIteration); test iterates it twice to prove
  restartability.
- `ex04_generators.py` — `countdown_gen(n)` (same behavior, 4 lines);
  `chunks(items, size)`; `running_total(nums)`.
- `ex05_lazy_pipelines.py` — `naturals()` infinite generator;
  `take(gen, n)`; `evens(gen)`; composed pipeline
  `first_n_even_squares(n)`; tests prove laziness by piping `naturals()`
  through and only taking 5.
- `ex06_yield_from.py` — `flatten(nested)` with `yield from` recursion;
  `interleave_files(*iterables)`-style delegation drill.
- `ex07_decorators.py` — `@log_calls(log)` appending "name(args) ->
  result"; `@count_calls` exposing `.calls`; both with
  `functools.wraps`; test asserts `__name__` survives.
- `ex08_decorator_args.py` — `@retry(times)` retrying on ValueError
  (test uses a flaky closure succeeding on 3rd try); `@clamp_result(lo,
  hi)`.
- `ex09_context_managers.py` — class-based `Stopwatch(clock)` (clock
  injected as a callable for determinism) usable as `with Stopwatch(c)
  as s:` then `s.elapsed`; generator-based `@contextmanager
  ledger_transaction(ledger)` (commit list on success, roll back on
  exception — test both paths).
- `ex10_functools.py` — `partial` drills (make `to_hex` etc. from
  `int`); `@lru_cache` on `slow_fib` with a call-counter proving cache
  hits; `singledispatch` `describe()` for int/str/list.
- `ex11_itertools.py` — `top_pairs` (product), `window(seq)` (pairwise),
  `group_by_grade(students)` (sorted + groupby),
  `first_matching(iterable, pred)` (islice/filter — no list()).
- `ex12_peekable.py` — capstone-ish: `Peekable` iterator wrapper class:
  `peek()` (default arg for exhausted), `__next__`, `__iter__`; works
  over any iterable, proves protocol mastery.

## Idiom drills (exactly 4 files: `drill01`–`drill04`)
Each file presents working-but-clunky code as a commented reference
implementation, and the student re-implements idiomatically. Tests
check behavior AND enforce the idiom via source inspection
(`inspect.getsource(func)`) asserting the anti-pattern's absence:
- `drill01_loops.py` — `range(len(...))` indexing → enumerate/zip
  (source must not contain `range(len`).
- `drill02_accumulators.py` — manual accumulator/flag loops → sum with
  genexp, any, all, max(key=) (source must not contain `.append`).
- `drill03_lookups.py` — "if key in d:" ladders → `.get`,
  `.setdefault`, `try/except KeyError` (source must not contain
  `in d:`-style membership-check — pick a robust marker, e.g. assert
  `"if " not in source` for the specific functions where a single
  expression suffices).
- `drill04_java_class.py` — getter/setter class → property or
  dataclass (source of the rewrite must not contain `get_` / `set_`).
Choose source-markers carefully so the reference solutions pass their
own drills (verify!).

## Checkpoint (`checkpoint_09.py`)
Text-pipeline toolkit combining all three pillars:
- `tokens(lines)` generator: lazily yield lowercase words from an
  iterable of lines (regex or split — stay lazy).
- `unique(iterable)` generator preserving first-seen order, lazy.
- `@memoized` decorator (own implementation, not lru_cache) with
  `.cache_clear()`.
- `Corpus` class wrapping a list of lines: `__len__`, `__iter__`
  (yields tokens lazily via the pipeline), `__contains__` (word
  lookup), and a `vocabulary` property (sorted unique tokens).
Tests must prove laziness (feed an infinite generator into
`tokens`/`unique` + islice), memoization (call counting), and every
protocol.

## SUMMARY.md
Cheat-sheet: dunder→syntax table, generator patterns, decorator
templates (plain + parameterized), contextmanager template, clunky→
Pythonic table (the module's soul — make this one great), functools/
itertools quick reference. One mermaid mindmap. Self-quiz: 10
questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
Expect this module to have the largest test count in the course.
