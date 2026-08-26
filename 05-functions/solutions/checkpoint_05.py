def word_stats(text, *, min_length=1, stop_words=None):
    if stop_words is None:
        stop_words = set()
    counts = {}
    for raw_word in text.lower().split():
        word = raw_word.strip(".,!?;:\"'")
        if len(word) < min_length or word in stop_words:
            continue
        counts[word] = counts.get(word, 0) + 1
    return counts


def make_formatter(prefix, suffix=""):
    def format_value(value):
        return f"{prefix}{value}{suffix}"

    return format_value


def apply_all(value, *funcs):
    result = value
    for func in funcs:
        result = func(result)
    return result
