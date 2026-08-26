def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None


def int_or_default(text, default):
    try:
        return int(text)
    except ValueError:
        return default


def first_working(funcs):
    last_error = None
    for func in funcs:
        try:
            return func()
        except Exception as e:  # noqa: BLE001 — deliberately broad: "try callables until one works"
            last_error = e
    raise last_error
