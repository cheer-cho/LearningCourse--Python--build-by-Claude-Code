from ex05_scope import (
    LEVEL,
    make_id_generator,
    read_global_total,
    register_click,
    shadowed_local,
)


def test_shadowed_local_returns_local_value():
    assert shadowed_local() == "local"


def test_shadowed_local_does_not_change_the_global():
    shadowed_local()
    assert LEVEL == "global"


def test_read_global_total_reads_without_reassigning():
    assert read_global_total() == 1
    assert read_global_total() == 1  # calling again gives the same answer


def test_make_id_generator_increments_from_default_start():
    next_id = make_id_generator()
    assert next_id() == 1
    assert next_id() == 2
    assert next_id() == 3


def test_make_id_generator_respects_custom_start():
    next_id = make_id_generator(100)
    assert next_id() == 100


def test_make_id_generator_instances_are_independent():
    a = make_id_generator()
    b = make_id_generator()
    a()
    a()
    assert b() == 1


def test_register_click_increments_and_persists_across_calls():
    first = register_click()
    second = register_click()
    assert second == first + 1
