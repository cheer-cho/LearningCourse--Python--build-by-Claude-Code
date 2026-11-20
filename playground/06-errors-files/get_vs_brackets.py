# .get() vs [] on a missing dict key.
# Run: uv run python playground/06-errors-files/get_vs_brackets.py

data = {"name": "Ada"}

# 1. .get() never raises. A missing key gives None (or your default).
print(data.get("divisor"))       # None
print(data.get("divisor", 1))    # 1

# 2. [] raises KeyError right where the key is missing.
try:
    data["divisor"]
except KeyError as err:
    print(f"KeyError: {err}")    # KeyError: 'divisor'

# 3. Why it matters: with .get() the failure shows up later, as a different error.
try:
    100 / data.get("divisor")
except TypeError as err:
    print(f"TypeError: {err}")   # unsupported operand type(s) for /: 'int' and 'NoneType'
