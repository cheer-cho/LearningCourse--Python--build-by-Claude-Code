from ex07_files import append_log, count_words, write_lines


def test_write_lines_creates_file_with_each_line(tmp_path):
    path = tmp_path / "notes.txt"
    write_lines(path, ["a", "b", "c"])
    assert path.read_text(encoding="utf-8") == "a\nb\nc\n"


def test_write_lines_overwrites_existing_file(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("old content\n", encoding="utf-8")
    write_lines(path, ["new"])
    assert path.read_text(encoding="utf-8") == "new\n"


def test_write_lines_empty_list_creates_empty_file(tmp_path):
    path = tmp_path / "notes.txt"
    write_lines(path, [])
    assert path.read_text(encoding="utf-8") == ""


def test_count_words_typical_sentence(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("the quick brown fox", encoding="utf-8")
    assert count_words(path) == 4


def test_count_words_ignores_extra_whitespace(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("  one   two\nthree  ", encoding="utf-8")
    assert count_words(path) == 3


def test_count_words_empty_file(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("", encoding="utf-8")
    assert count_words(path) == 0


def test_append_log_creates_file_if_missing(tmp_path):
    path = tmp_path / "log.txt"
    append_log(path, "started")
    assert path.read_text(encoding="utf-8") == "started\n"


def test_append_log_appends_without_overwriting(tmp_path):
    path = tmp_path / "log.txt"
    append_log(path, "started")
    append_log(path, "finished")
    assert path.read_text(encoding="utf-8") == "started\nfinished\n"
