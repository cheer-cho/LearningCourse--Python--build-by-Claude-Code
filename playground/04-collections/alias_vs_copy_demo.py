# Aliasing vs copying: which object does each name point at?
import copy

# 1. Assignment = a second name for the SAME object
fruits = ["apple", "pear"]
alias = fruits
alias.append("kiwi")
print("1. alias      ->", fruits, "| same object?", alias is fruits)

# 2. Shallow copy = new outer list, items shared
fruits = ["apple", "pear"]
shallow = fruits.copy()
shallow.append("kiwi")
print("2. shallow    ->", fruits, "| same object?", shallow is fruits)

# 3. Shallow copy of NESTED data: inner lists are still shared
grid = [["a"], ["b"]]
shallow_grid = list(grid)
shallow_grid[0].append("!")
print("3. nested shallow ->", grid, "| row shared?", shallow_grid[0] is grid[0])

# 4. Deep copy: everything is new
grid = [["a"], ["b"]]
deep_grid = copy.deepcopy(grid)
deep_grid[0].append("!")
print("4. deep       ->", grid, "| row shared?", deep_grid[0] is grid[0])

# 5. `+` on lists: both sides must be lists
print("5. list + list ->", [1, 2] + [3])
try:
    print([1, 2] + 3)
except TypeError as err:
    print("5. list + int  -> TypeError:", err)
