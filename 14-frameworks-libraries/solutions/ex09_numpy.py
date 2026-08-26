import numpy as np


def normalize(arr: np.ndarray) -> np.ndarray:
    low, high = arr.min(), arr.max()
    if high == low:
        return np.zeros_like(arr, dtype=float)
    return (arr - low) / (high - low)


def above_mean(arr: np.ndarray) -> int:
    return int(np.sum(arr > arr.mean()))


def moving_average(arr: np.ndarray, k: int) -> np.ndarray:
    cumsum = np.cumsum(np.insert(arr.astype(float), 0, 0.0))
    return (cumsum[k:] - cumsum[:-k]) / k


def grid_distance(points: np.ndarray) -> np.ndarray:
    diff = points[:, None, :] - points[None, :, :]
    return np.sqrt((diff.astype(float) ** 2).sum(axis=-1))
