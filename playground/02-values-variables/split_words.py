"""str.split() — with no argument vs. with an argument."""

messy = "  hello   world\tfrom\nPython  "

# No argument: split on ANY run of whitespace, and drop empty pieces.
print(messy.split())        # ['hello', 'world', 'from', 'Python']

# With " ": split on EVERY single space, so you get empty strings.
print(messy.split(" "))     # ['', '', 'hello', '', '', 'world\tfrom\nPython', '', '']

# Explicit separator: the usual way to parse CSV-ish data.
print("a,b,c".split(","))   # ['a', 'b', 'c']

# maxsplit: stop after N cuts.
print("key=value=more".split("=", 1))  # ['key', 'value=more']

# The reverse: join a list back into a string.
print(" ".join(messy.split()))  # 'hello world from Python'  <- whitespace cleaned up
