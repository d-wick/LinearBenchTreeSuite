"""
regression_tree.py
------------------

This module provides clean, reusable utilities for training, predicting, and
evaluating a Decision Tree Regressor within the LinearBenchTreeSuite pipeline.

It includes:
- `train_tree()`: Train a regression tree with configurable hyperparameters.
- `predict_tree()`: Generate predictions from a trained model.
- `evaluate_tree()`: Compute MAE% for model evaluation.
- `main()`: Optional debugging entry point.

The goal is to keep the model logic simple, modular, and easy to extend.
"""

from __future__ import annotations

import numpy as np
from typing import Optional
from sklearn.tree import DecisionTreeRegressor


def train_tree(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    max_depth: Optional[int] = 5,
    min_samples_leaf: int = 5,
    criterion: str = "mse"
) -> DecisionTreeRegressor:
    """
    Train a Decision Tree Regressor with specified hyperparameters.

    Parameters
    ----------
    X_train : np.ndarray
        Training feature matrix.
    Y_train : np.ndarray
        Training target vector.
    max_depth : int or None, default=5
        Maximum depth of the tree. None allows unlimited depth.
    min_samples_leaf : int, default=5
        Minimum number of samples required in a leaf node.
    criterion : str, default="mse"
        Function to measure the quality of a split.
        (Note: 'mse' was replaced by 'squared_error' in newer sklearn versions.)

    Returns
    -------
    DecisionTreeRegressor
        The trained regression tree model.
    """
    model = DecisionTreeRegressor(
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        criterion=criterion
    )
    model.fit(X_train, Y_train)
    return model


def predict_tree(model: DecisionTreeRegressor, X: np.ndarray) -> np.ndarray:
    """
    Generate predictions using a trained regression tree model.

    Parameters
    ----------
    model : DecisionTreeRegressor
        A fitted regression tree model.
    X : np.ndarray
        Feature matrix for prediction.

    Returns
    -------
    np.ndarray
        Predicted values.
    """
    return model.predict(X)


def evaluate_tree(Y_true: np.ndarray, Y_pred: np.ndarray) -> float:
    """
    Compute MAE% relative to the mean of the true values.

    MAE% is defined as:
        mean(|actual - predicted|) / mean(actual)

    Parameters
    ----------
    Y_true : np.ndarray
        Actual target values.
    Y_pred : np.ndarray
        Predicted target values.

    Returns
    -------
    float
        MAE as a decimal (e.g., 0.12 = 12%).
    """
    return np.mean(abs(Y_true - Y_pred)) / np.mean(Y_true)


def main() -> None:
    """
    Example execution for debugging.

    Loads a dataset, trains a regression tree, generates predictions,
    and prints MAE%. This function is not used in production but is
    helpful for quick validation.
    """
    from dataprocessing.dataset_creation import main as data_main

    df, X_train, Y_train, X_test, Y_test = data_main()

    model = train_tree(X_train, Y_train)
    Y_train_pred = predict_tree(model, X_train)
    Y_test_pred = predict_tree(model, X_test)

    mae_train = evaluate_tree(Y_train, Y_train_pred)
    mae_test = evaluate_tree(Y_test, Y_test_pred)

    print("Decision Tree Results:")
    print(f"Train MAE%: {mae_train * 100:.2f}")
    print(f"Test MAE%:  {mae_test * 100:.2f}")


# ---------------------------------------------------------------------------
# The block below ensures that `main()` only runs when this file is executed
# directly (e.g., `python regression_tree.py`) and NOT when imported.
#
# This prevents unintended model training or evaluation when other modules
# import the functions from this file.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()