"""The brackets decide what a comprehension builds."""

names = ["Ada", "Alan", "Grace", "Guido"]

squares = [n * n for n in range(5)]
evens = [n for n in range(10) if n % 2 == 0]
lengths = {name: len(name) for name in names}
initials = {name[0] for name in names}

for label, value in [
    ("squares", squares),
    ("evens", evens),
    ("lengths", lengths),
    ("initials", initials),
]:
    print(f"{label:9} {type(value).__name__:5} {value}")
