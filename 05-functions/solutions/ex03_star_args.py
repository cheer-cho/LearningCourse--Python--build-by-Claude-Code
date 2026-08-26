def average(*nums):
    if not nums:
        return None
    return sum(nums) / len(nums)


def longest(*words):
    if not words:
        return None
    return max(words, key=len)


def html_tag(tag_name, **attrs):
    parts = [f'{key}="{value}"' for key, value in sorted(attrs.items())]
    if not parts:
        return f"<{tag_name}>"
    return f"<{tag_name} {' '.join(parts)}>"


def forward_call(func, *args, **kwargs):
    return func(*args, **kwargs)
