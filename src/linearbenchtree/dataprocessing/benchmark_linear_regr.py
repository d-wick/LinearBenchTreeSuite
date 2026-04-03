"""
benchmark_linear_regr.py
------------------------

This module provides a simple linear regression benchmark model for the
LinearBenchTreeSuite forecasting pipeline.

It includes:
- `benchmark()`: Fits a Linear Regression model and returns predictions.
- `bench_test()`: Computes MAE% for training and test predictions.
- `main()`: Convenience function for running the benchmark end-to-end.

This model serves as the baseline against which all tree-based models are compared.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Tuple

from sklearn.linear_model import LinearRegression

from linearbenchtree.metrics import mae_percent


def benchmark(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    X_test: np.ndarray
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Fit a Linear Regression model and generate predictions.

    Parameters
    ----------
    X_train : np.ndarray
        Training feature matrix.
    Y_train : np.ndarray
        Training target vector.
    X_test : np.ndarray
        Test feature matrix.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray]
        Y_train_pred : np.ndarray
            Predictions for the training set.
        Y_test_pred : np.ndarray
            Predictions for the test set.
    """
    reg = LinearRegression()
    reg = reg.fit(X_train, Y_train)

    Y_train_pred = reg.predict(X_train)
    Y_test_pred = reg.predict(X_test)

    return Y_train_pred, Y_test_pred


def bench_test(
    Y_train: np.ndarray,
    Y_train_pred: np.ndarray,
    Y_test: np.ndarray,
    Y_test_pred: np.ndarray
) -> Tuple[float, float]:
    """
    Compute Mean Absolute Error percentage (MAE%) for training and test sets.

    MAE% is defined as:
        mean(|actual - predicted|) / mean(actual)

    This function is intentionally kept in the benchmark module because it
    compares train vs test performance for a baseline workflow. The underlying
    MAE% computation is delegated to the shared metrics API.

    Parameters
    ----------
    Y_train : np.ndarray
        Actual training targets.
    Y_train_pred : np.ndarray
        Predicted training targets.
    Y_test : np.ndarray
        Actual test targets.
    Y_test_pred : np.ndarray
        Predicted test targets.

    Returns
    -------
    Tuple[float, float]
        MAE_train : float
            Training MAE% as a decimal.
        MAE_test : float
            Test MAE% as a decimal.
    """
    MAE_train = mae_percent(Y_train, Y_train_pred)
    MAE_test = mae_percent(Y_test, Y_test_pred)
    return MAE_train, MAE_test


def main() -> None:
    """
    Example execution of the benchmark model.

    This function is primarily for debugging or demonstration purposes.
    It assumes that dataset creation has already been performed elsewhere.
    """
    from dataprocessing.dataset_creation import main as data_main

    df, X_train, Y_train, X_test, Y_test = data_main()

    Y_train_pred, Y_test_pred = benchmark(X_train, Y_train, X_test)
    MAE_train, MAE_test = bench_test(Y_train, Y_train_pred, Y_test, Y_test_pred)

    print("Linear Regression Benchmark Results:")
    print(f"Train MAE%: {MAE_train * 100:.2f}")
    print(f"Test MAE%:  {MAE_test * 100:.2f}")


# ---------------------------------------------------------------------------
# The block below ensures that `main()` only runs when this file is executed
# directly (e.g., `python benchmark_linear_regr.py`) and NOT when imported.
#
# This prevents unintended model training or evaluation when other modules
# import the benchmark functions.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()