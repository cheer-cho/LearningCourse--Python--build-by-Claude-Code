"""split() only cuts on whitespace, so punctuation stays stuck to the words."""

print("Cat, cat! dog.".split())   # ['Cat,', 'cat!', 'dog.']

# strip() takes an optional argument: a SET of characters to remove from both ends.
print("--==hello==--".strip("-="))   # 'hello'
print("--he-llo--".strip("-"))       # 'he-llo'  <- the middle is left alone

# lower() makes "Cat" and "cat" the same word.
print("HeLLo".lower())               # 'hello'
