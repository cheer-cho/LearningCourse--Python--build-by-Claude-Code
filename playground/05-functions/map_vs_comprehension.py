"""JS `arr.map(fn)` -> Python. Run: uv run python playground/05-functions/map_vs_comprehension.py"""

nums = [1, 2, 3, 4]

# JS: nums.map(n => n * 2)

# 1) The Pythonic way: a list comprehension
doubled = [n * 2 for n in nums]
print("comprehension:", doubled)

# 2) The built-in map() -- note it returns a lazy iterator, not a list
lazy = map(lambda n: n * 2, nums)
print("raw map():   ", lazy)          # <map object ...>  -- not a list!
print("list(map()): ", list(lazy))    # wrap in list() to materialise it
print("map again:   ", list(lazy))    # [] -- iterator is used up after one pass

# 3) map() shines when you already have a named function (no lambda needed)
words = ["  hi ", " there  "]
print("map(str.strip):", list(map(str.strip, words)))
print("comprehension: ", [w.strip() for w in words])

# 4) JS gives you (value, index) in map; Python uses enumerate()
# JS: arr.map((x, i) => `${i}:${x}`)
print("with index:", [f"{i}:{x}" for i, x in enumerate(["a", "b", "c"])])

# 5) map + filter in one go -- JS: nums.filter(n => n % 2).map(n => n ** 2)
print("filter+map:", [n**2 for n in nums if n % 2])

# 6) map() over two lists in parallel (JS has no direct equivalent)
print("zip-style map:", list(map(lambda a, b: a + b, [1, 2], [10, 20])))
