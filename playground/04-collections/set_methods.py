# A tour of set methods: adding, removing, comparing, and combining.
# Run: uv run python playground/04-collections/set_methods.py

# --- 1. Adding -------------------------------------------------------------
tags = {"python"}
tags.add("rust")  # one item
tags.update(["go", "zig"], "ab")  # many items, from ANY iterables
print("after add/update:", sorted(tags))  # "ab" adds "a" and "b"!

# --- 2. Removing -----------------------------------------------------------
tags.remove("a")  # KeyError if missing
tags.discard("not-there")  # silent if missing (no error)
popped = tags.pop()  # removes and returns an arbitrary item
print("popped:", popped)
try:
    tags.remove("not-there")
except KeyError as e:
    print("remove() raised KeyError:", e)
tags.clear()
print("after clear:", tags)  # set(), not {}

# --- 3. Comparing (return bool) --------------------------------------------
small = {1, 2}
big = {1, 2, 3}
print("small.issubset(big)   :", small.issubset(big))  # same as small <= big
print("big.issuperset(small) :", big.issuperset(small))  # same as big >= small
print("small.isdisjoint({9}) :", small.isdisjoint({9}))  # no items in common

# --- 4. Combining: method vs operator --------------------------------------
a = {1, 2, 3}
print("a.union([3, 4])     :", a.union([3, 4]))  # methods take any iterable
try:
    a | [3, 4]  # type: ignore[operator]
except TypeError as e:
    print("a | [3, 4] raised   :", e)  # operators need both sides to be sets

# --- 5. Combining in place (the *_update family) ----------------------------
a = {1, 2, 3}
a.intersection_update({2, 3, 4})  # same as a &= {2, 3, 4}
print("after intersection_update:", a)
a.difference_update({3})  # same as a -= {3}
print("after difference_update  :", a)

# --- 6. Copy ---------------------------------------------------------------
original = {1, 2}
clone = original.copy()  # same as set(original)
clone.add(99)
print("original:", original, " clone:", clone)
