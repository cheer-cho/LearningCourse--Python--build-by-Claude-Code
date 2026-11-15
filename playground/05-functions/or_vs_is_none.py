# `items or []` vs `if items is None` — they differ for an EMPTY list.


def add_with_or(item, items=None):
    items = items or []  # [] is falsy, so a caller's empty list gets swapped out
    items.append(item)
    return items


def add_with_is_none(item, items=None):
    if items is None:  # only None gets swapped out
        items = []
    items.append(item)
    return items


if __name__ == "__main__":
    mine = []
    add_with_or(1, mine)
    print("or []    ->", mine)  # [] : the caller's list was NOT touched

    mine = []
    add_with_is_none(1, mine)
    print("is None  ->", mine)  # [1] : the caller's list was appended to
