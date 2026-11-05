"""`is` asks "same object?"; `==` asks "same value?"."""

a = 42
b = int("42")
print(f"{a} == {b}: {a == b}   {a} is {b}: {a is b}")  # True, True (small-int cache)

a = 10**20
b = int("1" + "0" * 20)
print(f"big == big: {a == b}  big is big: {a is b}")  # True, False!

word = "correct!"
built = "".join(["correct", "!"])
print(f"== : {word == built}   is : {word is built}")  # True, False!
