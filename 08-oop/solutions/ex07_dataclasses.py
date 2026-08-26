import math
from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    done: bool = False
    tags: list = field(default_factory=list)


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
