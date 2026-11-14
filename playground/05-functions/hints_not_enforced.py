def clamp(value, lo, hi) -> int:
    if value < lo:
        return "lo"  # wrong type, on purpose
    return value


print(clamp(-3, 0, 10))  # Python runs it happily
