def require_positive(n):
    if n <= 0:
        raise ValueError(f"expected a positive number, got {n}")
    return n


def parse_age(text):
    try:
        age = int(text)
    except ValueError:
        raise ValueError(f"invalid age: {text!r}") from None
    if age < 0:
        raise ValueError(f"age cannot be negative: {age}")
    return age
