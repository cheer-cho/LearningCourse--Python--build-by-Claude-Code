"""How tuples compare, and why that makes them great sort keys.

Run: uv run python playground/05-functions/tuple_sort_keys.py
"""

# 1. Tuples compare left to right. The first difference decides.
print(("Adler", "Bo") < ("Lovelace", "Ada"))   # True  -> "A" < "L", done
print(("Smith", "Ann") < ("Smith", "Zed"))     # True  -> tie on "Smith", so "Ann" < "Zed"

# 2. sorted() on bare tuples uses that same rule.
dates = [(2024, 3), (2023, 11), (2024, 1)]
print(sorted(dates))  # [(2023, 11), (2024, 1), (2024, 3)]  year first, then month

# 3. Analogy: events as dicts. Sort by year, ties broken by month.
events = [
    {"name": "launch", "year": 2024, "month": 3},
    {"name": "beta", "year": 2023, "month": 11},
    {"name": "alpha", "year": 2024, "month": 1},
]
by_date = sorted(events, key=lambda e: (e["year"], e["month"]))
for e in by_date:
    print(e["name"], (e["year"], e["month"]))
