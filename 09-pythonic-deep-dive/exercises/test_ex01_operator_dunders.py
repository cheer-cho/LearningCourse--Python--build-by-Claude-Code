from ex01_operator_dunders import Money


def test_add_combines_cents():
    assert Money(500) + Money(150) == Money(650)


def test_add_foreign_type_raises_type_error():
    import pytest

    with pytest.raises(TypeError):
        Money(500) + 150


def test_mul_scales_by_int():
    assert Money(500) * 3 == Money(1500)


def test_rmul_scales_by_int_from_the_left():
    assert 3 * Money(500) == Money(1500)


def test_mul_foreign_type_raises_type_error():
    import pytest

    with pytest.raises(TypeError):
        Money(500) * Money(2)


def test_eq_compares_by_cents():
    assert Money(500) == Money(500)
    assert Money(500) != Money(499)


def test_eq_against_foreign_type_is_false_not_error():
    assert (Money(500) == "500") is False


def test_hash_consistent_with_eq():
    assert hash(Money(500)) == hash(Money(500))


def test_hash_allows_use_in_a_set():
    assert {Money(500), Money(500), Money(100)} == {Money(500), Money(100)}


def test_lt_and_le_enable_sorting():
    assert Money(100) < Money(500)
    assert Money(100) <= Money(100)
    assert sorted([Money(500), Money(100), Money(300)]) == [
        Money(100),
        Money(300),
        Money(500),
    ]


def test_repr_is_unambiguous():
    assert repr(Money(500)) == "Money(500)"
