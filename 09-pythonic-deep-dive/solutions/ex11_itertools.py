import itertools


def top_pairs(items_a, items_b, n):
    """Return the first `n` pairs (a, b) from the Cartesian product of
    `items_a` and `items_b`, using itertools.product to build the pairs
    and itertools.islice to cap the count — never materializes the
    whole product first.

    top_pairs([1, 2], ["x", "y"], 3) -> [(1, "x"), (1, "y"), (2, "x")]
    top_pairs([1], ["x"], 5) -> [(1, "x")]
    """
    return list(itertools.islice(itertools.product(items_a, items_b), n))


def window(seq):
    """Yield consecutive overlapping pairs from `seq`, via
    itertools.pairwise.

    list(window([1, 2, 3, 4])) -> [(1, 2), (2, 3), (3, 4)]
    list(window([1])) -> []
    list(window([])) -> []
    """
    return itertools.pairwise(seq)


def group_by_grade(students):
    """Group `students` (dicts with "name" and "grade") by grade
    letter, returning {grade: [names]}. itertools.groupby only groups
    CONSECUTIVE equal keys, so the input must be sorted by grade first.

    group_by_grade([
        {"name": "Ada", "grade": "A"},
        {"name": "Bo", "grade": "B"},
        {"name": "Cy", "grade": "A"},
    ]) -> {"A": ["Ada", "Cy"], "B": ["Bo"]}
    """
    ordered = sorted(students, key=lambda student: student["grade"])
    return {
        grade: [student["name"] for student in group]
        for grade, group in itertools.groupby(ordered, key=lambda student: student["grade"])
    }


def first_matching(iterable, pred):
    """Return the first item in `iterable` for which `pred(item)` is
    true, or None if nothing matches. Stays lazy: built from filter()
    and next(), so it stops pulling from `iterable` at the first hit
    instead of scanning it into a list.

    first_matching([1, 3, 4, 7], lambda x: x % 2 == 0) -> 4
    first_matching([1, 3, 5], lambda x: x % 2 == 0) -> None
    """
    return next(filter(pred, iterable), None)
