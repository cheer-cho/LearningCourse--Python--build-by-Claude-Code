words = ["ada", "lovelace"]

# Normal for loop
firsts = []
for w in words:
    firsts.append(w[0])
print(firsts)

# List comprehension: same thing, one expression
print([w[0] for w in words])

# Optional filter at the end
print([w[0] for w in ["ada", "", "lovelace"] if w])

# A lambda is something else: a tiny unnamed function
first_letter = lambda w: w[0]
print(first_letter("grace"))
