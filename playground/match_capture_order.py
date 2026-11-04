"""A capture pattern BEFORE other cases: Python refuses to compile this file."""

RED = "red"

def color(c: str) -> str:
    match c:
        case RED:          # captures anything -> the cases below can never run
            return "red"
        case "blue":
            return "blue"
        case _:
            return "other"

print("this line never prints")
print(color("blue"))
