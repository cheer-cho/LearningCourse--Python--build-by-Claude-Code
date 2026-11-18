"""append vs extend vs +.  Run: uv run python playground/05-functions/append_vs_extend.py"""

a = [1, 2]
a.append([3, 4])  # adds ONE item: the list itself
print("append:", a)  # [1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])  # adds EACH item from the iterable
print("extend:", b)  # [1, 2, 3, 4]

c = [1, 2]
c.extend("hi")  # any iterable works: a string gives its characters
print("extend str:", c)  # [1, 2, 'h', 'i']

d = [1, 2]
same = d
d.extend([3])  # mutates in place, returns None
print("extend mutates:", same, "| returns:", [].extend([1]))

e = [1, 2]
f = e + [3]  # builds a NEW list; e is untouched
print("plus:", e, f)
