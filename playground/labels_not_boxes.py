"""Variables are labels pointing at values, not boxes holding them."""

# 1. Two labels, one value
a = [1, 2, 3]
b = a  # no copy! b is a second label on the SAME list
b.append(4)
print("a:", a)  # a sees the change too
print("same object?", a is b, "| id(a) == id(b):", id(a) == id(b))

# 2. Re-assigning moves the label; it doesn't touch the value
x = 10
y = x
x = x + 1  # builds a NEW int 11, moves the x label onto it
print("x:", x, "y:", y)  # y still points at 10

# 3. Want a real second list? Ask for a copy
c = a.copy()
c.append(99)
print("a:", a, "c:", c, "| same object?", a is c)
