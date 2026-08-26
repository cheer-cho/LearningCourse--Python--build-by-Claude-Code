from ex07_sorting_keys import sort_by_age, sort_by_last_first, top_by

RECORDS = [
    {"first": "Ada", "last": "Lovelace", "age": 36},
    {"first": "Bo", "last": "Adler", "age": 29},
    {"first": "Cy", "last": "Adler", "age": 45},
]


def test_sort_by_age_ascending():
    result = sort_by_age(RECORDS)
    assert [r["age"] for r in result] == [29, 36, 45]


def test_sort_by_age_does_not_mutate_input():
    original = list(RECORDS)
    sort_by_age(RECORDS)
    assert RECORDS == original


def test_sort_by_last_first_orders_by_last_then_first():
    result = sort_by_last_first(RECORDS)
    assert [(r["last"], r["first"]) for r in result] == [
        ("Adler", "Bo"),
        ("Adler", "Cy"),
        ("Lovelace", "Ada"),
    ]


def test_top_by_highest_age():
    result = top_by(RECORDS, lambda r: r["age"], 2)
    assert [r["first"] for r in result] == ["Cy", "Ada"]


def test_top_by_n_larger_than_items_returns_all_sorted():
    result = top_by(RECORDS, lambda r: r["age"], 10)
    assert len(result) == 3
    assert [r["first"] for r in result] == ["Cy", "Ada", "Bo"]


def test_top_by_with_plain_numbers():
    assert top_by([3, 1, 4, 1, 5], lambda x: x, 2) == [5, 4]
