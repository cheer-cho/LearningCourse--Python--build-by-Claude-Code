# Handoff: Module 13 — Testing & Quality

Build `13-testing-quality/` in the course repo. Read `CONVENTIONS.md`
(same folder) and the master spec first. You own ONLY this folder.

Audience: completed modules 01–12 — they've RUN pytest 250+ times;
now they learn to WRITE tests. `hypothesis` is installed in the dev
group; use it (bounded: max_examples ≤ 50, deadline=None, fully
deterministic strategies).

Meta-testing design: exercises stay machine-verifiable by having the
student implement test-support artifacts (factories, fakes, parametrize
case-tables, property predicates) that provided meta-tests consume and
judge. The lesson carries the concepts; the exercises make them
concrete.

## LESSON.md outline
1. Why this exists: untested code is unfinished; tests are how you
   refactor without fear.
2. REQUIRED diagram: pytest's flow — collect → fixtures set up → test
   runs → assert rewrite explains failures → teardown.
3. Anatomy of a good test: arrange/act/assert; one behavior per test;
   naming as documentation.
4. Fixtures: factory functions vs @pytest.fixture, scopes, tmp_path,
   capsys, monkeypatch — table of the built-ins used in this course.
5. Parametrize: tables of cases; ids; covering edges deliberately
   (zero/negative/empty/huge/unicode).
6. Test doubles: fake, stub, mock — table; dependency injection as the
   enabler ("if it's hard to test, the design is telling you
   something").
7. Property-based testing — REQUIRED diagram: example-based (points)
   vs property-based (region) intuition; hypothesis @given, shrinking.
8. TDD — REQUIRED diagram: red → green → refactor loop.
9. Coverage in 4 sentences (`--cov` exists; chasing 100% blindly is a
   smell), ruff as the other quality gate.
10. Gotchas: tests depending on each other, over-mocking, asserting
    implementation not behavior, time/randomness nondeterminism.
11. Try it now → exercises.

## Exercises (exactly 7)
- `ex01_arrange_act_assert.py` — student implements `make_order()` and
  `make_paid_order()` factory helpers (given an Order dataclass) that
  meta-tests use; plus `describe_failure(expected, actual)` producing a
  helpful assertion message.
- `ex02_fixtures.py` — implement `fresh_account()` factory and
  `funded_account(balance)`; and `fake_clock(start)` returning an
  object with `now()` and `advance(secs)` — the workhorse test double;
  meta-tests verify isolation between instances.
- `ex03_parametrize_cases.py` — a given `password_strength(pw)`
  implementation; the student fills `STRENGTH_CASES: list[tuple[str,
  str]]` (password → expected rating) that a provided
  @pytest.mark.parametrize consumes. Meta-test also asserts the case
  table covers required categories (too-short, no-digit, strong,
  unicode, empty) by checking properties of the inputs themselves.
- `ex04_dependency_injection.py` — given `WeatherReport` code
  hard-wired to a nondeterministic/"slow" provider function; student
  refactors to accept an injected provider and implements
  `FakeProvider` (canned responses, records calls); meta-tests use the
  fake to test error and success paths.
- `ex05_monkeypatch_tmppath.py` — implement `read_api_key()` (env var
  with error on absence) and `cache_result(path, key, value)` /
  `cached(path, key)` designed for tmp_path testing; meta-tests use
  monkeypatch.setenv/delenv and tmp_path — the student sees these
  fixtures in action from the consumer side (tests are worth reading —
  say so in the file header).
- `ex06_properties.py` — implement `encode(text)`/`decode(data)` (a
  simple reversible transform, e.g. run-length or caesar) and state
  properties as predicates: `prop_roundtrip(text)`,
  `prop_length_nonneg(text)`; provided hypothesis @given tests feed
  generated strings through the predicates.
- `ex07_tdd_bugfix.py` — TDD from the consumer seat: `slugify(title)`
  ships with 3 real bugs (doesn't lowercase, collapses hyphens wrong,
  keeps unicode punctuation); the provided tests ARE the spec (all
  red); student fixes the implementation until green — no hints in the
  code beyond the tests.

## Checkpoint (`checkpoint_13.py`)
"Cover the legacy function": a given gnarly `shipping_quote(order)`
with many branches, instrumented to record which named branch ran into
a module-level `BRANCHES_HIT` set. Student supplies
`QUOTE_CASES: list[dict]` (order payloads). The meta-test runs every
case through the function, asserts each case's expected value (student
also fills expected totals), and asserts `BRANCHES_HIT` ends up equal
to the full branch-label set — i.e. the student achieved 100% branch
coverage by choosing inputs deliberately. Plus `make_edge_order()`
factory for the nastiest branch.

## SUMMARY.md
Cheat-sheet: fixture built-ins table, parametrize skeleton, fake/stub/
mock table, hypothesis starter, TDD loop, "signs of a bad test" list.
One mermaid mindmap. Self-quiz: 7 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
Keep hypothesis runtime bounded (max_examples ≤ 50, deadline=None).
