# Scenario: a tiny kennel app tracks dogs by name and age. Concepts:
# class definition, __init__, self, instance methods, mutating state.
# Run: uv run pytest 08-oop -k ex01


class Dog:
    """A pet dog with a name and an age in years."""

    def __init__(self, name, age):
        """Store name and age on the new instance.

        Dog("Rex", 2).name -> "Rex"
        Dog("Rex", 2).age -> 2
        """
        raise NotImplementedError

    def bark(self):
        """Return this dog's bark line: "<name> says Woof!"

        Dog("Rex", 2).bark() -> "Rex says Woof!"
        """
        raise NotImplementedError

    def birthday(self):
        """Add 1 to this dog's age, mutating it in place. Returns nothing.

        rex = Dog("Rex", 2)
        rex.birthday()
        rex.age -> 3
        """
        raise NotImplementedError


def oldest_dog(dogs):
    """Return the Dog with the highest age from a non-empty list.

    If there's a tie, return the first one that reaches that age.

    oldest_dog([Dog("Rex", 2), Dog("Fido", 5)]) -> the Fido instance
    """
    raise NotImplementedError


def rename_dog(dog, new_name):
    """Rename `dog` in place: set its .name to `new_name`. Returns nothing.

    rex = Dog("Rex", 2)
    rename_dog(rex, "Max")
    rex.name -> "Max"
    """
    raise NotImplementedError
