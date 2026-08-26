def format_money(cents):
    dollars, remainder = divmod(cents, 100)
    return f"${dollars}.{remainder:02d}"


def pick_fix(options):
    for key, description in options.items():
        if "new module" in description or "third module" in description:
            return key
    raise ValueError("no standard-fix description found in options")
