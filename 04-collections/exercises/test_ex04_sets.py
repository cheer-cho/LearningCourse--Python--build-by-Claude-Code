from ex04_sets import common_interests, has_duplicates, only_in_first, unique_tags


def test_unique_tags_removes_duplicates():
    assert unique_tags(["python", "web", "python", "cli"]) == {"python", "web", "cli"}


def test_unique_tags_empty_list():
    assert unique_tags([]) == set()


def test_common_interests_typical():
    assert common_interests({"chess", "hiking"}, {"hiking", "reading"}) == {"hiking"}


def test_common_interests_no_overlap():
    assert common_interests({"chess"}, {"reading"}) == set()


def test_only_in_first_typical():
    assert only_in_first({"chess", "hiking"}, {"hiking", "reading"}) == {"chess"}


def test_only_in_first_identical_sets():
    assert only_in_first({"chess"}, {"chess"}) == set()


def test_has_duplicates_false_for_unique_items():
    assert has_duplicates([1, 2, 3]) is False


def test_has_duplicates_true_when_repeated():
    assert has_duplicates([1, 2, 2]) is True


def test_has_duplicates_empty_list():
    assert has_duplicates([]) is False
