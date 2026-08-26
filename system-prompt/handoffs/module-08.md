# Handoff: Module 08 — Object-Oriented Python

Build `08-oop/` in the course repo. Read `CONVENTIONS.md` (same folder)
and the master spec first. You own ONLY this folder.

Audience: completed modules 01–07. No type hints (module 10) — even
though dataclasses normally use annotations, module-08 dataclass
exercises may use bare annotations like `name: str` since dataclasses
require them; keep annotations minimal there and say in the lesson
"annotations get their full module (10)". Dunder protocols beyond the
basics (`__repr__`, `__eq__`, `__len__`, `__contains__`) are module 09.

## LESSON.md outline
1. Why this exists: bundling state + behavior; when a class earns its
   place vs a dict/function (be opinionated — Pythonic, not Java).
2. Class anatomy — REQUIRED diagram: class → instances; `__init__`;
   `self` is just the instance.
3. Instance vs class attributes — REQUIRED diagram: lookup goes
   instance → class; the shared-mutable-class-attribute trap.
4. Properties: computed attributes, validation on set; "don't write
   getters/setters".
5. `@classmethod` (alternative constructors) vs `@staticmethod` vs
   instance method — comparison table.
6. Inheritance & MRO — REQUIRED diagram: small hierarchy + how lookup
   walks it; `super()`.
7. Dunder basics: `__repr__` (always write one), `__eq__`, `__len__`,
   `__contains__`.
8. Dataclasses: what they generate; `field(default_factory=...)`;
   `frozen=True`.
9. ABCs vs duck typing — short table; `abc.ABC` + `@abstractmethod`.
10. Gotchas: mutable class attribute, forgetting `self`, comparing
    without `__eq__`, overriding without calling `super().__init__`.
11. Try it now → exercises.

## Exercises (exactly 8)
- `ex01_first_class.py` — `Dog`: `__init__(name, age)`, `bark()`,
  `birthday()` mutating age.
- `ex02_class_attrs.py` — `Robot` with a class-level counter of
  instances (fixed via classmethod or class attr discipline) AND the
  trap: `Team` shipping with `members = []` at class level (real bug —
  two teams share members); student moves it into `__init__`.
- `ex03_properties.py` — `Temperature`: stores celsius, `fahrenheit`
  property (get + set converts), `celsius` setter validating >=
  -273.15 raising ValueError.
- `ex04_classmethods.py` — `Pizza`: `margherita()` / `hawaiian()`
  factory classmethods; `from_string("pepperoni,olives")`; staticmethod
  `valid_topping(name)`.
- `ex05_dunders.py` — `Money(amount_cents, currency)`: `__repr__`,
  `__eq__` (same currency+amount; NotImplemented for other types),
  `__add__` (same currency only, else raise ValueError). Plus
  `Playlist`: `__len__`, `__contains__`.
- `ex06_inheritance.py` — `Shape` base (`area` raises
  NotImplementedError, `describe()` uses area); `Circle`, `Rectangle`
  override with `super().__init__(name)`; `total_area(shapes)`
  polymorphic.
- `ex07_dataclasses.py` — convert a dict-shaped record into
  `@dataclass Task` (title, done=False, tags via default_factory);
  `@dataclass(frozen=True) Point` with a `distance_to` method; test
  asserts frozen raises on assignment and generated `__eq__` works.
- `ex08_abc_ducks.py` — `Storage(ABC)` with abstract `save(key, value)`
  / `load(key)`; concrete `MemoryStorage` (dict-backed) and
  `PrefixedStorage` wrapping another storage (composition); duck-typing
  drill `describe_quacker(obj)` using hasattr — no isinstance.

## Checkpoint (`checkpoint_08.py`)
Mini library system: `LibraryItem` base (title, year, `__repr__`,
`loan_period` = 21); `Book(LibraryItem)` (author, loan_period 28) and
`Dvd(LibraryItem)` (loan_period 7) via super(); `@dataclass Member`
(name, card_id, borrowed via default_factory); `Library` with
`add(item)`, `__len__`, `__contains__` (by title), `checkout(member,
title)` raising a custom `CheckoutError` when absent, and a
`catalog` property returning sorted titles. Tests cover polymorphic
loan periods, dunder behavior, and the error path.

## SUMMARY.md
Cheat-sheet: class skeleton, property recipe, method-kinds table,
dataclass options table, ABC-vs-duck table. One mermaid mindmap.
Self-quiz: 8 questions, answers in `<details>`.

Finish with every "Definition of done" check from CONVENTIONS.md.
