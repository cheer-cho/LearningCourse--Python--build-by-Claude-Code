"""What does *funcs actually hold, and how do you pass it on?"""


def show(*items):
    print(f"  got {len(items)} arg(s): {items}")


def add1(x):
    return x + 1


def double(x):
    return x * 2


def square(x):
    return x * x


# 1. Inside the function, *items packs every extra argument into ONE tuple.
print("show(add1, double, square):")
show(add1, double, square)

first, *rest = (add1, double, square)
print(f"\nfirst = {first.__name__}, rest = {[f.__name__ for f in rest]}  (a list)")

# 2. Passing `rest` as-is hands over ONE argument: the whole list.
print("\nshow(rest)   <- no star:")
show(rest)

# 3. A star at the CALL site spreads the list back into separate arguments.
print("\nshow(*rest)  <- with star:")
show(*rest)

# 4. "Threading" = feed each result into the next step.
#    Analogous pattern with plain data (not functions): apply discounts in order.
price = 100.0
for pct in [10, 50]:
    price = price * (1 - pct / 100)  # same variable on both sides: old value in, new value out
    print(f"\nafter {pct}% off -> {price}")
