"""Map dict key/value pairs to strings. Run: uv run python playground/05-functions/dict_to_strings.py"""

prices = {"apple": 1.5, "banana": 0.25, "cherry": 3}

# JS: Object.entries(prices).map(([k, v]) => `${k}=${v}`)
# Python: .items() gives (key, value) pairs -> unpack them in the comprehension
pairs = [f"{k}={v}" for k, v in prices.items()]
print("list of strings:", pairs)

# Want ONE string? Join them. JS: .join(", ")
print("joined:         ", ", ".join(pairs))

# Skip the intermediate list: pass a generator straight to join()
print("generator:      ", ", ".join(f"{k}={v}" for k, v in prices.items()))

# Format specs work inside f-strings: pad the key, 2 decimals for the value
print("\n".join(f"{k:<8} ${v:.2f}" for k, v in prices.items()))

# Keep it a dict, but turn the values into strings (dict comprehension)
# JS: Object.fromEntries(Object.entries(prices).map(([k, v]) => [k, `$${v}`]))
print("dict -> dict:   ", {k: f"${v:.2f}" for k, v in prices.items()})

# Trap: looping over a dict directly gives KEYS only
print("keys only:      ", [k for k in prices])
