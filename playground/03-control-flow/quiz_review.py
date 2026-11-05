"""Quiz answers, demonstrated."""

# Q1: truthiness looks at the container, not at what's inside it
print(bool([0]), bool([]), bool([None]), bool([[]]))  # True False True True


# Q3: `==` can be overridden; `is` can't
class Weird:
    def __eq__(self, other: object) -> bool:
        return True  # claims to equal everything


w = Weird()
print(w == None, w is None)  # True False  <- `==` lied, `is` didn't
