"""Numbers & conversions cheat sheet. Run: uv run python playground/number_methods.py

Each line prints `expression=result`, thanks to the f-string `=` spec.
"""

print("--- operators ---")
print(f"{7 + 3=}")
print(f"{7 / 2=}")       # true division: always a float
print(f"{10 / 2=}")      # still a float
print(f"{7 // 2=}")      # floor division
print(f"{-7 // 2=}")     # floors toward -infinity, not toward 0
print(f"{7 % 2=}")       # remainder
print(f"{2 ** 10=}")     # power
print(f"{divmod(7, 2)=}")  # (quotient, remainder) in one go

print("\n--- built-in functions ---")
print(f"{abs(-5)=}")
print(f"{round(3.14159, 2)=}")   # returns a number: use it to compute
print(f"{round(3.7)=}")          # no digits: returns an int
print(f"{round(2.5)=}")          # banker's rounding: to the even neighbour
print(f"{round(3.5)=}")
print(f"{min(3, 1, 2)=}")
print(f"{max(3, 1, 2)=}")
print(f"{sum([1, 2, 3])=}")
print(f"{pow(2, 10)=}")

print("\n--- float quirks ---")
print(f"{0.1 + 0.2=}")
print(f"{0.1 + 0.2 == 0.3=}")
print(f"{(3.0).is_integer()=}")
print(f"{(3.5).is_integer()=}")

print("\n--- conversions: str -> number ---")
print(f'{int("42")=}')
print(f'{int(" 42 ")=}')         # surrounding whitespace is OK
print(f'{int("-42")=}')
print(f'{float("3.5")=}')
print(f'{float("1e3")=}')        # scientific notation
print(f'{int("ff", 16)=}')       # parse in another base
print(f'{int("1010", 2)=}')

print("\n--- conversions: number -> number ---")
print(f"{int(3.9)=}")            # truncates toward 0, does NOT round
print(f"{int(-3.9)=}")
print(f"{float(3)=}")

print("\n--- conversions: anything -> str ---")
print(f"{str(42)=}")
print(f"{str(3.5)=}")
print(f"{str(None)=}")

print("\n--- conversions: anything -> bool (truthiness) ---")
print(f"{bool(0)=}")
print(f"{bool(42)=}")
print(f'{bool("")=}')
print(f'{bool("False")=}')       # non-empty string: True!
print(f"{bool(None)=}")

print("\n--- display vs value ---")
price = 3.14159
print(f"{round(price, 2)=}")     # a float you can keep computing with
print(f"{f'{price:.2f}'=}")      # a str: for printing only
print(f"{1234567.891:,.2f}")     # thousands separator
print(f"{42:05d}")               # zero-pad to width 5
print(f"{0.256:.1%}")            # as a percentage
print(f"{255:x} {255:b}")        # hex and binary

print("\n--- readable literals ---")
print(f"{1_000_000=}")           # underscores are ignored, just for humans
print(f"{0xFF=} {0b1010=}")

# --- these raise ValueError: uncomment one at a time to see the error ---
# int("3.5")      # int() won't parse a decimal string; use int(float("3.5"))
# int("abc")
# float("free")
# int("")
