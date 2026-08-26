# Scenario: small vectorized numeric utilities — the kind of thing you'd
# reach for numpy instead of a Python loop for. Concepts: dtype-aware
# arrays, vectorized arithmetic, boolean masks, aggregation, broadcasting.
# Run: uv run pytest 14-frameworks-libraries -k ex09

from __future__ import annotations

import numpy as np


def normalize(arr: np.ndarray) -> np.ndarray:
    """Min-max normalize `arr` to the range [0, 1]: `(x - min) / (max - min)`.

    If every value is equal (`max == min`), return an all-zero array of
    the same shape instead of dividing by zero.

    normalize(np.array([0, 5, 10])) -> array([0. , 0.5, 1. ])
    normalize(np.array([7, 7, 7])) -> array([0., 0., 0.])
    """
    raise NotImplementedError


def above_mean(arr: np.ndarray) -> int:
    """Count how many elements of `arr` are strictly greater than
    `arr.mean()`, using a boolean mask (no Python `for` loop).

    above_mean(np.array([1, 2, 3, 4])) -> 2
    """
    raise NotImplementedError


def moving_average(arr: np.ndarray, k: int) -> np.ndarray:
    """Return the moving average of `arr` over window size `k`, as an
    array of length `len(arr) - k + 1`. Assumes `1 <= k <= len(arr)`.

    moving_average(np.array([1, 2, 3, 4, 5]), 2) -> array([1.5, 2.5, 3.5, 4.5])
    moving_average(np.array([1.0, 2.0, 3.0]), 3) -> array([2.0])
    """
    raise NotImplementedError


def grid_distance(points: np.ndarray) -> np.ndarray:
    """Given `points` of shape (n, 2), return the (n, n) matrix of
    pairwise Euclidean distances — `result[i, j]` is the distance from
    `points[i]` to `points[j]`. Fully vectorized: no Python loop over
    pairs (broadcast `points[:, None, :] - points[None, :, :]`).

    grid_distance(np.array([[0, 0], [3, 4]])) -> array([[0., 5.], [5., 0.]])
    """
    raise NotImplementedError
