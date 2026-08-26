def sort_by_age(records):
    return sorted(records, key=lambda r: r["age"])


def sort_by_last_first(records):
    return sorted(records, key=lambda r: (r["last"], r["first"]))


def top_by(items, key_func, n):
    return sorted(items, key=key_func, reverse=True)[:n]
