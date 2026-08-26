import math
import random
from collections import Counter


def gcd_of(a, b):
    return math.gcd(a, b)


def most_common_word(text):
    counts = Counter(text.split())
    return counts.most_common(1)[0][0]


def shuffle_deterministic(items, seed):
    result = list(items)
    random.Random(seed).shuffle(result)
    return result
