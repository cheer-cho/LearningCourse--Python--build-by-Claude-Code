"""Counts how many times the loop+recursion hybrid of apply_all calls itself."""

calls = 0


def hybrid(value, *funcs):
    global calls
    calls += 1
    if not funcs:
        return value
    for fn in funcs:
        if callable(fn):
            func, *rest = funcs  # always the FIRST function, whatever fn is
            result = func(value)
            hybrid(result, *rest)  # result thrown away
    return hybrid(result, *rest)


def add1(x: int) -> int:
    return x + 1


for n in range(1, 9):
    calls = 0
    answer = hybrid(0, *[add1] * n)
    print(f"{n} functions -> answer {answer}, {calls:>6} calls to hybrid")
