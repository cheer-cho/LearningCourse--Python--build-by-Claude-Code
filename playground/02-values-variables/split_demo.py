name = "  ada   lovelace "
print(name.split(" "))   # splits on every single space
print(name.split())      # splits on any whitespace run, ignores the ends

print(".".join(w[0].upper() for w in "grace brewster hopper".split()) + ".")
