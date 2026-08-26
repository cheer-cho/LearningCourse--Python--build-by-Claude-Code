# Handoff: Module 10 — Type Hints & Static Typing

Build `10-typing/` in the course repo. Read `CONVENTIONS.md` (same
folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–09 AND knows TypeScript well — this is
the module where that pays off. Lean into TS↔Python translation.

## Verification model (this module is special)
Most exercises INVERT the usual shape: working bodies are GIVEN, the
student adds annotations. Wrong or missing types must fail — two layers:
1. **Runtime annotation checks** (fast feedback): tests inspect
   `typing.get_type_hints(func)` / `inspect.signature` and assert the
   expected annotations. Compare via the resolved objects
   (e.g. `hints["items"] == list[int]`), not fragile strings.
2. **mypy strict** (the real check): each test file includes ONE test
   that runs `["uv", "run", "mypy", "--strict", <that exercise file>]`
   via subprocess (check=False) and asserts returncode 0, showing
   stdout in the assert message on failure. The repo root pyproject
   already has `[tool.mypy] strict = true`.
Stub files: bodies present and correct, annotations ABSENT (or
deliberately wrong where the exercise says so) — so the mypy test and
annotation tests are red until solved, while the file still imports
cleanly. Solutions carry full annotations; verify_solutions must go
green INCLUDING the mypy subprocess tests (mypy runs inside the
`.verify` copy — pass the copied file's path, it inherits root config
via cwd; verify this actually works).

## LESSON.md outline
1. Why this exists: Python types are optional, gradual, and checked by
   an external tool — same idea as TS, different engine.
2. REQUIRED table (big, the module's centerpiece): TS ↔ Python
   translations — `string`→`str`, `number`→`int|float`, `T[]`→`list[T]`,
   `Record<K,V>`→`dict[K,V]`, `x?: T`→`T | None`, union types,
   `interface`→`Protocol`/`TypedDict`, `type` alias→`type X = ...`,
   generics `<T>`→`TypeVar`/PEP-695 `def f[T](...)`, `unknown`→`object`,
   `any`→`Any` (and why to avoid), `as`→`cast`.
3. Annotation syntax: params, returns, `-> None`, variables; builtin
   generics (list[int], dict[str, int], tuple fixed vs variadic).
4. `X | None` and narrowing — REQUIRED diagram: flowchart of narrowing
   (is None check / isinstance / early return) mirroring the TS
   narrowing flowchart from the sibling course.
5. Literal, TypedDict (total/NotRequired), NamedTuple vs dataclass.
6. Generics: TypeVar, generic functions and classes; constraints/bound.
   Teach BOTH classic TypeVar syntax and Python 3.12 `def f[T]()` —
   use classic in exercises (mypy-strict-safest), mention new.
7. Protocol = structural typing — "this is TS interfaces"; 
   runtime_checkable.
8. `@overload`; `cast`; when checkers need help.
9. Gradual typing strategy + running mypy; reading its errors.
10. Gotchas: `Any` leaks, mutable default + Optional, str is a
    Sequence[str], forgetting `-> None` on procedures under strict.
11. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_annotate_basics.py` — given bodies: `shout(text)`,
  `repeat(word, times)`, `banner(text)` (returns None → `-> None`),
  `ratio(a, b)` (-> float). Student annotates everything.
- `ex02_collections.py` — annotate: `total(prices: list[float])`,
  `index_by_name(users) -> dict[str, dict[str, object]]`-style,
  `pair() -> tuple[str, int]`, variadic `tuple[int, ...]`.
- `ex03_optional_union.py` — annotate + implement small narrowing
  bodies: `find_user(users, name) -> ... | None`,
  `describe(x: int | str) -> str` via isinstance dispatch; mypy proves
  the narrowing.
- `ex04_typeddict_namedtuple.py` — student DEFINES `Movie` TypedDict
  (title: str, year: int, rating NotRequired) and `Point` NamedTuple,
  then annotates given functions using them.
- `ex05_literal.py` — `sort_direction: Literal["asc", "desc"]` in
  `sort_scores`; `Weekday` Literal alias; exhaustive handling.
- `ex06_generics.py` — annotate with TypeVar: `first(items)`,
  `last_or(items, default)`, and a small generic `Box` class
  (`Generic[T]`): put/get preserve the type; the mypy test includes a
  type-error probe in a comment block explained in the docstring.
- `ex07_protocols.py` — student defines `HasArea(Protocol)` with
  `area() -> float`; annotates `total_area(shapes: Iterable[HasArea])`;
  given Circle/Square classes (no inheritance!) must satisfy it —
  structural typing demonstrated by the mypy test.
- `ex08_overload_cast.py` — `@overload` for
  `scale(x: int, k: int) -> int` / `scale(x: list[int], k: int) ->
  list[int]`; a justified `cast` drill on a json.loads result.

## Checkpoint (`checkpoint_10.py`)
A small untyped "orders" module with given working bodies (~6
functions + a TypedDict-shaped dict + one generic helper + one
Protocol consumer). Student annotates the entire file to mypy-strict
clean; tests = annotation asserts + the mypy subprocess test. This
checkpoint's docstring states the goal plainly: "make mypy --strict
happy without changing behavior".

## SUMMARY.md
Cheat-sheet: the TS↔Python table (condensed), annotation syntax box,
TypedDict/NamedTuple/dataclass chooser table, TypeVar + Protocol
templates, mypy command + common errors decoded. One mermaid mindmap.
Self-quiz: 8 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
Note: `uv run mypy` is already installed; budget for mypy's first-run
cache build. All mypy subprocess tests must pass against solutions via
`uv run python scripts/verify_solutions.py 10`.
