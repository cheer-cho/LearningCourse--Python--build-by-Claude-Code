"""Unpacking works on ANY iterable, not just tuples."""

a, b = (1, 2)                 # tuple
print("tuple: ", a, b)

a, b = [3, 4]                 # list
print("list:  ", a, b)

x, y, z = "abc"               # str -> characters
print("str:   ", x, y, z)

a, b = {10, 20}               # set -> works, but ORDER is not guaranteed!
print("set:   ", a, b)

k1, k2 = {"name": "Ada", "age": 36}   # dict -> unpacks the KEYS
print("dict:  ", k1, k2)

(k, v), *rest = {"name": "Ada", "age": 36}.items()  # items() -> (key, value) pairs
print("items: ", k, v, rest)

a, b, c = range(3)            # range
print("range: ", a, b, c)

first, *middle, last = "python"   # star works on any iterable; middle is ALWAYS a list
print("star:  ", first, middle, last)

# Count must match (unless you use *)
try:
    a, b = [1, 2, 3]
except ValueError as e:
    print("error: ", e)
