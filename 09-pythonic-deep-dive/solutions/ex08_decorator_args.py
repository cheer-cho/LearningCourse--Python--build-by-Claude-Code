import functools


def retry(times):
    """Decorator FACTORY: retries the wrapped function up to `times`
    attempts whenever it raises ValueError, returning the first
    successful result. If every attempt raises, re-raises the last
    ValueError.

    attempts = []
    @retry(3)
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise ValueError("not yet")
        return "ok"
    flaky() -> "ok"       # succeeded on the 3rd attempt
    len(attempts) -> 3
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except ValueError as exc:
                    last_error = exc
            raise last_error

        return wrapper

    return decorator


def clamp_result(lo, hi):
    """Decorator FACTORY: clamps the wrapped function's numeric return
    value into the closed range [lo, hi].

    @clamp_result(0, 100)
    def score(x):
        return x
    score(150) -> 100
    score(-5) -> 0
    score(50) -> 50
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return max(lo, min(hi, result))

        return wrapper

    return decorator
