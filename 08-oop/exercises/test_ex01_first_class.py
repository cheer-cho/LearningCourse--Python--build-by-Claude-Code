from ex01_first_class import Dog, oldest_dog, rename_dog


def test_init_stores_name_and_age():
    rex = Dog("Rex", 2)
    assert rex.name == "Rex"
    assert rex.age == 2


def test_bark_uses_the_dogs_name():
    assert Dog("Rex", 2).bark() == "Rex says Woof!"
    assert Dog("Fido", 5).bark() == "Fido says Woof!"


def test_birthday_increments_age_in_place():
    rex = Dog("Rex", 2)
    rex.birthday()
    assert rex.age == 3


def test_birthday_returns_nothing():
    rex = Dog("Rex", 2)
    assert rex.birthday() is None


def test_two_dogs_have_independent_state():
    rex = Dog("Rex", 2)
    fido = Dog("Fido", 5)
    rex.birthday()
    assert rex.age == 3
    assert fido.age == 5


def test_oldest_dog_picks_the_highest_age():
    rex, fido = Dog("Rex", 2), Dog("Fido", 5)
    assert oldest_dog([rex, fido]) is fido


def test_oldest_dog_single_item():
    rex = Dog("Rex", 2)
    assert oldest_dog([rex]) is rex


def test_rename_dog_mutates_in_place():
    rex = Dog("Rex", 2)
    rename_dog(rex, "Max")
    assert rex.name == "Max"


def test_rename_dog_returns_nothing():
    rex = Dog("Rex", 2)
    assert rename_dog(rex, "Max") is None
