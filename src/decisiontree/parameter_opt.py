"""
parameter_opt.py
----------------

This module provides hyperparameter optimization utilities for the
Decision Tree Regressor used in the LinearBenchTreeSuite pipeline.

It includes:
- `optimize_tree()`: Run RandomizedSearchCV to tune Decision Tree hyperparameters.
- `evaluate_tree()`: Compute MAE% for evaluating predictions.
- `main()`: Optional debugging entry point.

The goal is to keep tuning logic modular, reusable, and consistent with
other model families in the project.
"""

from __future__ import annotations

import numpy as np
from typing import Dict, Any, Optional

from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import RandomizedSearchCV


def optimize_tree(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    param_dist: Optional[Dict[str, Any]] = None,
    cv: int = 10,
    n_iter: int = 100,
    scoring: str = "neg_mean_absolute_error",
    n_jobs: int = -1,
    verbose: int = 1
) -> Dict[str, Any]:
    """
    Run RandomizedSearchCV to optimize Decision Tree hyperparameters.

    Parameters
    ----------
    X_train : np.ndarray
        Training feature matrix.
    Y_train : np.ndarray
        Training target vector.
    param_dist : dict or None, default=None
        Dictionary of hyperparameter distributions to sample from.
        If None, a default search space is used.
    cv : int, default=10
        Number of cross-validation folds.
    n_iter : int, default=100
        Number of parameter settings sampled.
    scoring : str, default="neg_mean_absolute_error"
        Scoring metric for optimization.
    n_jobs : int, default=-1
        Number of parallel jobs.
    verbose : int, default=1
        Verbosity level for RandomizedSearchCV.

    Returns
    -------
    dict
        A dictionary containing:
        - "model": best estimator
        - "params": best hyperparameters
        - "cv_results": full CV results
        - "search": the RandomizedSearchCV object
    """
    # Default parameter grid if none provided
    if param_dist is None:
        max_depth = list(range(5, 11)) + [None]
        min_samples_leaf = list(range(5, 20))
        param_dist = {
            "max_depth": max_depth,
            "min_samples_leaf": min_samples_leaf
        }

    base_model = DecisionTreeRegressor()

    search = RandomizedSearchCV(
        estimator=base_model,
        param_distributions=param_dist,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        n_jobs=n_jobs,
        verbose=verbose,
        random_state=42
    )

    search.fit(X_train, Y_train)

    return {
        "model": search.best_estimator_,
        "params": search.best_params_,
        "cv_results": search.cv_results_,
        "search": search
    }


def evaluate_tree(Y_true: np.ndarray, Y_pred: np.ndarray) -> float:
    """
    Compute MAE% relative to the mean of the true values.

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

    Loads a dataset, runs hyperparameter optimization, and prints the
    best parameters and resulting MAE%. This function is not used in
    production but is helpful for quick validation.
    """
    from dataprocessing.dataset_creation import main as data_main
    from decisiontree.regression_tree import predict_tree

    df, X_train, Y_train, X_test, Y_test = data_main()

    results = optimize_tree(X_train, Y_train)
    model = results["model"]

    Y_train_pred = predict_tree(model, X_train)
    Y_test_pred = predict_tree(model, X_test)

    mae_train = evaluate_tree(Y_train, Y_train_pred)
    mae_test = evaluate_tree(Y_test, Y_test_pred)

    print("Optimized Decision Tree Results:")
    print("Best Parameters:", results["params"])
    print(f"Train MAE%: {mae_train * 100:.2f}")
    print(f"Test MAE%:  {mae_test * 100:.2f}")


# ---------------------------------------------------------------------------
# The block below ensures that `main()` only runs when this file is executed
# directly (e.g., `python parameter_opt.py`) and NOT when imported.
#
# This prevents unintended hyperparameter searches from running when other
# modules import the optimization utilities.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()