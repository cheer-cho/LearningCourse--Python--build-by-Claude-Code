from pprint import pprint

name = "Ada"
scores = [90, 85, 77]
user = {"name": name, "scores": scores, "tags": {"admin", "beta"}, "meta": {"age": 36, "city": "London"}}

# 1. The f-string "=" trick — prints the expression AND its value
print(f"{name=}")
print(f"{len(scores)=}")
print(f"{sum(scores) / len(scores)=:.1f}")  # combine with a format spec

# 2. !r shows the repr — makes strings, whitespace and None visible
text = "hello "
print(f"{text=}")       # = uses repr by default
print(f"{text!s}|")     # !s: plain str — the trailing space is hard to spot

# 3. pprint for nested data
pprint(user, width=40)
