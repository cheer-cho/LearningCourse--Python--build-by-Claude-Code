from ex03_star_args import average, forward_call, html_tag, longest


def test_average_multiple_numbers():
    assert average(1, 2, 3) == 2.0


def test_average_single_number():
    assert average(5) == 5.0


def test_average_no_arguments_is_none():
    assert average() is None


def test_longest_typical():
    assert longest("cat", "elephant", "dog") == "elephant"


def test_longest_tie_returns_first():
    assert longest("aa", "bb") == "aa"


def test_longest_no_arguments_is_none():
    assert longest() is None


def test_html_tag_sorts_attrs_alphabetically():
    assert html_tag("a", href="x", id="y") == '<a href="x" id="y">'


def test_html_tag_reorders_out_of_order_attrs():
    assert html_tag("input", type="text", name="q") == '<input name="q" type="text">'


def test_html_tag_no_attrs():
    assert html_tag("br") == "<br>"


def test_forward_call_positional_args():
    assert forward_call(max, 1, 5, 3) == 5


def test_forward_call_keyword_args():
    assert forward_call(sorted, [3, 1, 2], reverse=True) == [3, 2, 1]
