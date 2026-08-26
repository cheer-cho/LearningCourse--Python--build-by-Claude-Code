def flatten(nested):
    """Recursively flatten an arbitrarily nested list/tuple structure,
    yielding scalar (non-list/tuple) values in order. `yield from`
    delegates to the recursive call instead of manually re-yielding
    each value in a loop.

    list(flatten([1, [2, 3, [4]], 5])) -> [1, 2, 3, 4, 5]
    list(flatten([])) -> []
    list(flatten([1, (2, 3)])) -> [1, 2, 3]
    """
    for item in nested:
        if isinstance(item, (list, tuple)):
            yield from flatten(item)
        else:
            yield item


def concat_all(*iterables):
    """Delegate to each iterable in turn, exhausting one fully before
    moving to the next — one `yield from` per source, chained. Same
    idea as `itertools.chain`, written by hand to drill delegation.

    list(concat_all([1, 2], "ab", (9,))) -> [1, 2, "a", "b", 9]
    list(concat_all()) -> []
    """
    for iterable in iterables:
        yield from iterable
