# Scenario: sorting a list of records with a custom key, and a
# reusable "top N by some measure" helper. Concepts: `sorted(key=...)`
# with `lambda`, passing a function as an ordinary argument.
# Run: uv run pytest 05-functions -k ex07


def sort_by_age(records):
    """Return a NEW list of records (dicts with a "age" key) sorted by
    age, ascending. Use `sorted(..., key=lambda r: ...)`. Must not
    mutate `records`.

    sort_by_age([{"first": "Bo", "age": 29}, {"first": "Ada", "age": 36}])
    -> [{"first": "Bo", "age": 29}, {"first": "Ada", "age": 36}]
    """
    raise NotImplementedError


def sort_by_last_first(records):
    """Return a NEW list of records (dicts with "first" and "last" keys)
    sorted by the (last, first) name pair. Use a `lambda` returning a
    tuple as the key.

    sort_by_last_first([
        {"first": "Ada", "last": "Lovelace"},
        {"first": "Bo", "last": "Adler"},
    ]) -> [
        {"first": "Bo", "last": "Adler"},
        {"first": "Ada", "last": "Lovelace"},
    ]
    """
    raise NotImplementedError


def top_by(items, key_func, n):
    """Return the top `n` items from `items`, ranked highest-first by
    `key_func(item)`. `key_func` is an ordinary function argument — call
    it, don't assume what it computes. If `n` is bigger than
    `len(items)`, return all of `items`, fully sorted.

    top_by([3, 1, 4, 1, 5], key_func=lambda x: x, n=2) -> [5, 4]
    """
    raise NotImplementedError
