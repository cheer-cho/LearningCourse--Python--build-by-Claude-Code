s = "   hello world  \n"

print(repr(s.strip()))    # both ends
print(repr(s.lstrip()))   # left only
print(repr(s.rstrip()))   # right only

# Inner spaces are untouched
print(repr("  a   b  ".strip()))

# Strings are immutable: strip returns a NEW string
original = "  hi  "
original.strip()
print(repr(original))     # unchanged!

# Optional argument: a SET of characters to remove (not a substring)
print("xxhixx".strip("x"))
print("--==title==--".strip("-="))
