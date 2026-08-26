import functools


def log_calls(log):
    """Decorator FACTORY: returns a decorator that, each time the
    wrapped function is called, appends a "name(args) -> result" string
    to `log` (a list you pass in). Uses functools.wraps so the wrapped
    function keeps its own __name__/__doc__.

    log = []
    @log_calls(log)
    def add(a, b):
        return a + b
    add(2, 3) -> 5
    log -> ["add(2, 3) -> 5"]
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            arg_strs = [repr(a) for a in args]
            arg_strs += [f"{key}={value!r}" for key, value in kwargs.items()]
            log.append(f"{func.__name__}({', '.join(arg_strs)}) -> {result!r}")
            return result

        return wrapper

    return decorator


def count_calls(func):
    """Decorator: wraps `func`, tracking how many times it has been
    called on `wrapper.calls`. functools.wraps keeps __name__/__doc__
    pointing at the original function, not the wrapper.

    @count_calls
    def ping():
        return "pong"
    ping()
    ping()
    ping.calls -> 2
    ping.__name__ -> "ping"
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper
