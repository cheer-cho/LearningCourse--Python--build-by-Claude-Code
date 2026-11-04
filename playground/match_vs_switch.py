"""match/case is pattern matching, not a switch. Run me and read the output."""

# 1. Literal values: looks exactly like a switch.
def http_status(code: int) -> str:
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500 | 502 | 503:  # "or" pattern; no fall-through needed
            return "Server error"
        case _:  # wildcard = default
            return "Unknown"


# 2. Shapes: a switch can't do this. Destructure and bind in one step.
def describe(point: object) -> str:
    match point:
        case (0, 0):
            return "origin"
        case (x, 0):
            return f"on the x-axis at {x}"
        case (x, y) if x == y:  # guard
            return f"on the diagonal at {x}"
        case {"x": x, "y": y}:  # dict pattern
            return f"dict point ({x}, {y})"
        case _:
            return "something else"


# 3. THE GOTCHA: a bare name is a CAPTURE, not a comparison.
RED = "red"

def bad_color(c: str) -> str:
    match c:
        case RED:  # binds RED = c. Matches EVERYTHING!  # noqa
            return "red?"


def good_color(c: str) -> str:
    match c:
        case "red":  # literal: compares
            return "red"
        case _:
            return "not red"


print(http_status(404), "|", http_status(502), "|", http_status(999))
print(describe((0, 0)), "|", describe((3, 0)), "|", describe((4, 4)))
print(describe({"x": 1, "y": 2}), "|", describe("hi"))
print("bad_color('blue') ->", bad_color("blue"))
print("good_color('blue') ->", good_color("blue"))
