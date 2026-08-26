def unique_tags(tags: list[str]) -> set[str]:
    return set(tags)


def common_interests(a: set[str], b: set[str]) -> set[str]:
    return a & b


def only_in_first(a: set[str], b: set[str]) -> set[str]:
    return a - b


def has_duplicates(items: list[int]) -> bool:
    return len(set(items)) != len(items)
