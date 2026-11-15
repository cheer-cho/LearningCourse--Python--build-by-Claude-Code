# The three zones of a signature: positional-only | either | keyword-only
def f(a, /, b, *, c):
    return a, b, c


calls = [
    "f(1, 2, c=3)",
    "f(1, b=2, c=3)",
    "f(a=1, b=2, c=3)",
    "f(1, 2, 3)",
]

for src in calls:
    try:
        print(f"{src:20} -> {eval(src)}")
    except TypeError as e:
        print(f"{src:20} -> TypeError: {e}")
