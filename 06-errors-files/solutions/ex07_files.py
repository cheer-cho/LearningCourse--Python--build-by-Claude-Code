def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(line + "\n" for line in lines)


def count_words(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    return len(text.split())


def append_log(path, message):
    with open(path, "a", encoding="utf-8") as f:
        f.write(message + "\n")
