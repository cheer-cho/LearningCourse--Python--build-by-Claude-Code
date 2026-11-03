letters = ["X", "Y", "Z"]

print("-".join(letters))          # separator goes BETWEEN items
print("-".join(letters) + "-")    # want it at the end too? add it yourself
print("".join(letters))           # empty separator: just glue them

# join needs strings in the list
words = ["red", "green", "blue"]
firsts = [w[0] for w in words]    # build a list of first letters
print(firsts)
print(", ".join(firsts))
