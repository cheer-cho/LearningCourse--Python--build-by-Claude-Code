# How to "find" things in a set.
# Run: uv run python playground/04-collections/set_find.py

langs = {"python", "rust", "go", "typescript"}

# 1. Is it there? -> `in` (fast: O(1) on average)
print("'go' in langs     :", "go" in langs)
print("'java' not in langs:", "java" not in langs)

# 2. No index, no .find(), no .index() -- sets have no positions
try:
    langs[0]  # type: ignore[index]
except TypeError as e:
    print("langs[0] raised   :", e)

# 3. Find the FIRST item matching a condition -> next() + generator
long_name = next((x for x in langs if len(x) > 6), None)
print("first len > 6     :", long_name)
missing = next((x for x in langs if x.startswith("j")), None)
print("starts with 'j'   :", missing)  # default None, no StopIteration

# 4. Find ALL items matching a condition -> set comprehension
short = {x for x in langs if len(x) <= 4}
print("all len <= 4      :", short)

# 5. Any / all matches? -> any() / all()
print("any starts with 'r':", any(x.startswith("r") for x in langs))
print("all lowercase      :", all(x.islower() for x in langs))
