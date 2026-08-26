import pytest

pytest.importorskip("numpy")

import numpy as np
from ex09_numpy import above_mean, grid_distance, moving_average, normalize
from numpy.testing import assert_allclose


def test_normalize_typical_range():
    result = normalize(np.array([0, 5, 10]))
    assert_allclose(result, [0.0, 0.5, 1.0])


def test_normalize_constant_array_returns_zeros():
    result = normalize(np.array([7, 7, 7]))
    assert_allclose(result, [0.0, 0.0, 0.0])


def test_above_mean_counts_strictly_greater():
    assert above_mean(np.array([1, 2, 3, 4])) == 2


def test_above_mean_all_equal_counts_zero():
    assert above_mean(np.array([5, 5, 5])) == 0


def test_moving_average_window_two():
    result = moving_average(np.array([1, 2, 3, 4, 5]), 2)
    assert_allclose(result, [1.5, 2.5, 3.5, 4.5])


def test_moving_average_window_equals_length():
    result = moving_average(np.array([1.0, 2.0, 3.0]), 3)
    assert_allclose(result, [2.0])


def test_grid_distance_two_points():
    result = grid_distance(np.array([[0, 0], [3, 4]]))
    assert_allclose(result, [[0.0, 5.0], [5.0, 0.0]])


def test_grid_distance_is_symmetric_with_zero_diagonal():
    points = np.array([[0, 0], [1, 1], [2, 5]])
    result = grid_distance(points)
    assert_allclose(np.diag(result), [0.0, 0.0, 0.0])
    assert_allclose(result, result.T)
