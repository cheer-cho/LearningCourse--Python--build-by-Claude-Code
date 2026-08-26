class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says Woof!"

    def birthday(self):
        self.age += 1


def oldest_dog(dogs):
    oldest = dogs[0]
    for dog in dogs[1:]:
        if dog.age > oldest.age:
            oldest = dog
    return oldest


def rename_dog(dog, new_name):
    dog.name = new_name
