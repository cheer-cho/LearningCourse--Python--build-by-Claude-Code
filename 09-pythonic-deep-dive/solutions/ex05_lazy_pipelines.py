def naturals():
    """Infinite generator of 1, 2, 3, ... Never exhausts on its own —
    only ever consume it through take() or another bounded tool.
    """
    n = 1
    while True:
        yield n
        n += 1


def take(gen, n):
    """Pull the first `n` values out of generator `gen` and return them
    as a list. Consumes exactly `n` values from `gen` — no more.

    take(naturals(), 3) -> [1, 2, 3]
    take(naturals(), 0) -> []
    """
    result = []
    for _ in range(n):
        result.append(next(gen))
    return result


def evens(gen):
    """Yield only the even values produced by `gen`, lazily — pulls one
    value from `gen` at a time, only when asked for the next even one.
    """
    for value in gen:
        if value % 2 == 0:
            yield value


def first_n_even_squares(n):
    """Return the first n even perfect squares, as a list. Built by
    piping naturals() through a squares generator expression, then
    evens(), then take()-ing only n values. Stays lazy the whole way:
    naturals() is infinite and never gets turned into a list.

    first_n_even_squares(3) -> [4, 16, 36]
    first_n_even_squares(0) -> []
    """
    squares = (x * x for x in naturals())
    return take(evens(squares), n)
