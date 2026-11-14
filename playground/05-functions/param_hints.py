# 1. Basic: name: type
def area(width: float, height: float) -> float:
    return width * height


# 2. With a default: name: type = default  (spaces around = here!)
def greet(name: str, punctuation: str = "!") -> str:
    return f"Hello, {name}{punctuation}"


# 3. Collections as parameters
def total(prices: list[float]) -> float:
    return sum(prices)


# 4. Returns nothing -> None
def log(message: str) -> None:
    print(f"[log] {message}")


# 5. *args / **kwargs: hint the type of EACH item
def add_all(*nums: int) -> int:  # nums is tuple[int, ...]
    return sum(nums)


def show(**options: str) -> None:  # options is dict[str, str]
    print(options)


print(area(3, 4))
print(greet("Ada"), greet("Ada", "?"))
print(total([1.5, 2.5]))
log("saved")
print(add_all(1, 2, 3))
show(color="red", size="L")

# area("3", 4)  # uncomment: Python returns "3333" (str * int repeats!); mypy flags it
