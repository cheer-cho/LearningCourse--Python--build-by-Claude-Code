import random
import statistics


def sample_scores(rng: random.Random, n: int) -> list[int]:
    return [rng.randint(0, 100) for _ in range(n)]


def summarize(nums: list[float]) -> dict[str, float | None]:
    stdev = statistics.stdev(nums) if len(nums) >= 2 else None
    return {
        "mean": statistics.mean(nums),
        "median": statistics.median(nums),
        "stdev": stdev,
    }


def weighted_pick(rng: random.Random, options: dict[str, float]) -> str:
    keys = list(options.keys())
    weights = list(options.values())
    return rng.choices(keys, weights=weights, k=1)[0]
