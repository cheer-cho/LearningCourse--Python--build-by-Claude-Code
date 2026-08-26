def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


def flatten(nested):
    if not nested:
        return []
    first, *rest = nested
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    return [first] + flatten(rest)


def count_down_up(n):
    if n == 1:
        return "1 1"
    return f"{n} {count_down_up(n - 1)} {n}"
