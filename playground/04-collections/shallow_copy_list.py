"""list(a) makes a NEW list box, but the items inside are SHARED."""

a = [1, "hi", [10, 20]]
c = list(a)  # shallow copy (same as a.copy() or a[:])

# 1. The outer lists are different objects
print("a is c        ->", a is c)  # False: new list object
print("a == c        ->", a == c)  # True: same contents

# 2. But each slot points to the SAME item object
for i, (x, y) in enumerate(zip(a, c)):
    print(f"a[{i}] is c[{i}]  ->", x is y)  # True for every slot

# 3. Changing the OUTER list of c does not touch a
c.append("new")
c[0] = 99
print("\nafter c.append / c[0] = 99")
print("a =", a)
print("c =", c)

# 4. Mutating a SHARED inner item shows up in both
c[2].append(30)
print("\nafter c[2].append(30)")
print("a =", a)
print("c =", c)
