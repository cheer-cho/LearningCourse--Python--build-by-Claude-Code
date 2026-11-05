# Shadowing a built-in: naming a variable `sum` hides Python's sum().
# Run: uv run python playground/03-control-flow/shadow_builtin_sum.py

print(sum([1, 2, 3]))  # 6 — the built-in works

sum = 0  # now `sum` points at an int, not the function
for i in range(3, 10, 3):
    sum += i
print(sum)  # 18

try:
    print(sum([1, 2, 3]))
except TypeError as err:
    print("TypeError:", err)  # 'int' object is not callable

del sum  # remove our name; the built-in shows through again
print(sum(range(3, 10, 3)))  # 18 — the one-liner version of the loop
