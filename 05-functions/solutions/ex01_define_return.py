def rectangle_info(width, height):
    return width * height, 2 * (width + height)


def clamp(value, lo, hi):
    if value < lo:
        return lo
    if value > hi:
        return hi
    return value


def greet_missing_return(name):
    message = f"Hello, {name}!"
    return message
