"""lambda, end to end. Lesson: playground/05-functions/lambda_functions.md

Run: uv run python playground/05-functions/lambda_functions.py
"""


def section(title: str) -> None:
    print(f"\n=== {title} ===")


products = [
    {"name": "mouse", "category": "tech", "price": 25},
    {"name": "apple", "category": "food", "price": 1},
    {"name": "laptop", "category": "tech", "price": 900},
    {"name": "bread", "category": "food", "price": 3},
    {"name": "cable", "category": "tech", "price": 25},
]

# --- 1. A lambda is just a function object --------------------------------
section("1. lambda == def, minus the name")


def double_def(n):
    return n * 2


double_lam = lambda n: n * 2  # only to compare; see section 9

print(double_def(5), double_lam(5))  # 10 10
print(type(double_def) is type(double_lam))  # True: both are `function`
print(double_def.__name__, double_lam.__name__)  # double_def <lambda>

# --- 2. The main job: key= functions -------------------------------------
section("2. key= is called once per item")


def noisy_price(p):
    print(f"  key called on {p['name']!r} -> {p['price']}")
    return p["price"]


cheapest_first = sorted(products, key=noisy_price)
print([p["name"] for p in cheapest_first])

section("2b. same thing with a lambda, plus min / max")
print([p["name"] for p in sorted(products, key=lambda p: p["price"])])
print("cheapest:", min(products, key=lambda p: p["price"])["name"])
print("priciest:", max(products, key=lambda p: p["price"])["name"])
print("longest name:", max(products, key=lambda p: len(p["name"]))["name"])

# --- 3. Tuple keys: sort by several things --------------------------------
section("3. tuple key = 'sort by this, then by that'")
print(sorted([(2, "b"), (1, "z"), (2, "a")]))  # tuples compare item by item
by_cat_then_price = sorted(products, key=lambda p: (p["category"], p["price"]))
print([(p["category"], p["price"], p["name"]) for p in by_cat_then_price])

section("3b. mixed directions: negate the number")
# category A→Z, but price high→low inside each category
mixed = sorted(products, key=lambda p: (p["category"], -p["price"]))
print([(p["category"], p["price"]) for p in mixed])

# --- 4. Don't wrap a function that already exists -------------------------
section("4. pass the function itself")
words = ["kiwi", "Fig", "apple"]
print(sorted(words, key=lambda w: len(w)))  # works, but...
print(sorted(words, key=len))  # ...same thing, no wrapper
print(sorted(words, key=str.lower))  # case-insensitive sort
stock = {"apple": 4, "bread": 9, "kiwi": 2}
print("most stocked:", max(stock, key=stock.get))  # dict method as key

# --- 5. map / filter vs comprehension -------------------------------------
section("5. map/filter + lambda vs comprehension")
prices = [p["price"] for p in products]
print(list(map(lambda x: x * 2, prices)))  # noqa: C417  (ruff prefers the next line)
print([x * 2 for x in prices])  # same result, reads left to right
print(list(filter(lambda x: x > 10, prices)))
print([x for x in prices if x > 10])

# --- 6. What fits in one expression ----------------------------------------
section("6. what a lambda body can hold")
label = lambda n: "even" if n % 2 == 0 else "odd"  # conditional expression: OK
print(label(3), label(4))
# lambda n: return n            -> SyntaxError (return is a statement)
# lambda n: total = n           -> SyntaxError (assignment is a statement)
# lambda n: (print(n); n)       -> SyntaxError (no statement lists)
for bad in ("lambda n: return n", "lambda n: total = n"):
    try:
        compile(bad, "<demo>", "eval")
    except SyntaxError as e:
        print(f"  {bad!r:28} -> SyntaxError: {e.msg}")

# --- 7. Lambdas are closures: the late-binding trap -----------------------
section("7. late binding (same bug as closure_factory.md)")
adders = [lambda x: x + i for i in range(3)]  # noqa: B023  (ruff spots this bug!)
print([f(10) for f in adders])  # [12, 12, 12]: all share the last i
adders_fixed = [lambda x, i=i: x + i for i in range(3)]
print([f(10) for f in adders_fixed])  # [10, 11, 12]

# --- 8. The .get() trap in a key ------------------------------------------
section("8. key returning None blows up the sort")
messy = [{"name": "a", "price": 5}, {"name": "b"}]
try:
    sorted(messy, key=lambda p: p.get("price"))
except TypeError as e:
    print("  .get ->", type(e).__name__, ":", e)
try:
    sorted(messy, key=lambda p: p["price"])
except KeyError as e:
    print("  [ ]  -> KeyError:", e, "(names the missing key: easier to debug)")

# --- 9. Assigning a lambda to a name: tracebacks lose the name ------------
section("9. why PEP 8 says: def, not name = lambda")
try:
    double_lam("x", "y")
except TypeError as e:
    print("  lambda:", e)
try:
    double_def("x", "y")
except TypeError as e:
    print("  def:   ", e)
