def password_strength(pw: str) -> str:
    if not pw:
        return "empty"
    if len(pw) < 8:
        return "too-short"
    if not any(char.isdigit() for char in pw):
        return "weak"
    return "strong"


STRENGTH_CASES: list[tuple[str, str]] = [
    ("", "empty"),
    ("abc", "too-short"),
    ("longpassword", "weak"),
    ("longpassword1", "strong"),
    ("pásswörd1", "strong"),
]
