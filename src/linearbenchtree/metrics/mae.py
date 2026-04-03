"""
mae.py
------

This module contains core metric functions used throughout LinearBenchTreeSuite.

The primary goal is to centralize evaluation logic so that:
- model modules do not duplicate metric formulas
- results are consistent across model families
- future metrics (RMSE, MAPE, SMAPE, etc.) can be added in one place

It includes:
- `mae_percent()`: Mean Absolute Error as a percentage of the mean true value.
"""

from __future__ import annotations

import numpy as np


def mae_percent(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """
    Compute Mean Absolute Error as a percentage of the mean of the true values.

    MAE% is defined as:
        mean(|actual - predicted|) / mean(actual)

    Parameters
    ----------
    y_true : np.ndarray
        Actual target values.
    y_pred : np.ndarray
        Predicted target values.

    Returns
    -------
    float
        MAE as a decimal (e.g., 0.12 = 12%).
    """
    return float(np.mean(np.abs(y_true - y_pred)) / np.mean(y_true))