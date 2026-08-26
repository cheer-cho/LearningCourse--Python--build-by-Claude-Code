class Robot:
    count = 0

    def __init__(self, name):
        self.name = name
        Robot.count += 1

    @classmethod
    def how_many(cls):
        return cls.count


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)
