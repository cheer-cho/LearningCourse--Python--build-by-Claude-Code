# Scenario: a robot factory needs a running count of every robot ever
# built, and a sports league needs teams with independent rosters.
# Concepts: class attributes vs instance attributes, the shared-mutable-
# class-attribute trap.
# Run: uv run pytest 08-oop -k ex02


class Robot:
    """Every robot built increments a count shared by the whole class.

    `Robot.count` (a CLASS attribute, given below) must reflect the
    total number of Robot instances ever created — not just the ones
    still alive, all of them, ever. Increment it through the class
    itself (`Robot.count += 1`), not `self.count += 1` — the latter
    would create a brand-new INSTANCE attribute on `self` and leave the
    shared class attribute untouched.
    """

    count = 0  # given: one counter, shared by the whole class

    def __init__(self, name):
        """Store `name` on the instance and bump Robot.count by 1.

        Robot("R1"); Robot("R2")
        Robot.count -> 2
        """
        raise NotImplementedError

    @classmethod
    def how_many(cls):
        """Return the total number of robots built so far.

        Robot.how_many() -> Robot.count
        """
        raise NotImplementedError


class Team:
    """BUG: `members` is defined at class level below, so every Team
    ends up sharing the exact same list — adding a player to one team
    quietly adds them to every other team too.

    Fix it: move `members` into `__init__` so each Team instance gets
    its OWN list.
    """

    members = []  # noqa: RUF012 -- BUG (intentional): shared across every Team instance — move this!

    def __init__(self, name):
        self.name = name

    def add_member(self, person):
        """Add `person` to this team's roster.

        team = Team("Reds")
        team.add_member("Ada")
        team.members -> ["Ada"]
        """
        self.members.append(person)
