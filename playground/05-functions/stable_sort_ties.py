# How sorted(..., key=..., reverse=True) handles ties.
# Run: uv run python playground/05-functions/stable_sort_ties.py

words = ["bb", "a", "cc"]

# Step 1: what the key function sees
print([(w, len(w)) for w in words])  # [('bb', 2), ('a', 1), ('cc', 2)]

# Step 2: ascending vs descending
print(sorted(words, key=len))                # ['a', 'bb', 'cc']
print(sorted(words, key=len, reverse=True))  # ['bb', 'cc', 'a']

# Step 3: top 2 = first two of the descending list
print(sorted(words, key=len, reverse=True)[:2])  # ['bb', 'cc']

# Ties keep their ORIGINAL order, even with reverse=True.
# Swap the input order and the tie flips with it:
print(sorted(["cc", "a", "bb"], key=len, reverse=True))  # ['cc', 'bb', 'a']

# Compare: sorting then reversing is NOT the same thing.
print(sorted(words, key=len)[::-1])  # ['cc', 'bb', 'a']  <- tie order flipped
