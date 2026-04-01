"""
random_forest.py
----------------

This module provides a complete Random Forest Regressor workflow for the
LinearBenchTreeSuite forecasting pipeline.

It includes:
- `train_forest()`: Train a Random Forest model.
- `predict_forest()`: Generate predictions.
- `evaluate_forest()`: Compute MAE%.
- `get_feature_importance()`: Extract labeled feature importances.
- `optimize_forest()`: Hyperparameter tuning via RandomizedSearchCV.
- `main()`: Optional debugging entry point.

The goal is to keep the model logic modular, reusable, and consistent with
other model families in the project.
"""

from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Dict, Any, Optional

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV

from linearbenchtree.metrics import mae_percent


# ------------------------------------------------------------
# Train model
# ------------------------------------------------------------
def train_forest(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    n_estimators: int = 200,
    max_depth: Optional[int] = 9,
    min_samples_split: int = 10,
    min_samples_leaf: int = 7,
    max_features: int = 6,
    bootstrap: bool = True,
    n_jobs: int = -1,
    random_state: int = 42
) -> RandomForestRegressor:
    """
    Train a Random Forest Regressor with specified hyperparameters.

    Parameters
    ----------
    X_train : np.ndarray
        Training feature matrix.
    Y_train : np.ndarray
        Training target vector.
    n_estimators : int, default=200
        Number of trees in the forest.
    max_depth : int or None, default=9
        Maximum depth of each tree.
    min_samples_split : int, default=10
        Minimum samples required to split an internal node.
    min_samples_leaf : int, default=7
        Minimum samples required in a leaf node.
    max_features : int, default=6
        Number of features considered when looking for the best split.
    bootstrap : bool, default=True
        Whether bootstrap samples are used.
    n_jobs : int, default=-1
        Number of parallel jobs.
    random_state : int, default=42
        Random seed for reproducibility.

    Returns
    -------
    RandomForestRegressor
        The trained Random Forest model.
    """
    model = RandomForestRegressor(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_features=max_features,
        bootstrap=bootstrap,
        n_jobs=n_jobs,
        random_state=random_state
    )
    model.fit(X_train, Y_train)
    return model


# ------------------------------------------------------------
# Predict
# ------------------------------------------------------------
def predict_forest(model: RandomForestRegressor, X: np.ndarray) -> np.ndarray:
    """
    Generate predictions using a trained Random Forest model.

    Parameters
    ----------
    model : RandomForestRegressor
        A fitted Random Forest model.
    X : np.ndarray
        Feature matrix for prediction.

    Returns
    -------
    np.ndarray
        Predicted values.
    """
    return model.predict(X)


# ------------------------------------------------------------
# Evaluate
# ------------------------------------------------------------
def evaluate_forest(Y_true: np.ndarray, Y_pred: np.ndarray) -> float:
    """
    Compute MAE% relative to the mean of the true values.

    MAE% is defined as:
        mean(|actual - predicted|) / mean(actual)

    This function delegates to the shared metrics API to ensure consistent
    evaluation across all model families.

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
    return mae_percent(Y_true, Y_pred)


# ------------------------------------------------------------
# Feature Importance
# ------------------------------------------------------------
def get_feature_importance_forest(model: RandomForestRegressor, X_train: np.ndarray) -> pd.DataFrame:
    """
    Return a DataFrame of feature importances labeled as:
    Month (t-12), ..., Month (t-1)

    Parameters
    ----------
    model : RandomForestRegressor
        A trained Random Forest model.
    X_train : np.ndarray
        Training feature matrix used to determine number of features.

    Returns
    -------
    pd.DataFrame
        Feature importances with labeled rows.
    """
    n_features = X_train.shape[1]
    labels = [f"Month (t-{n_features - i})" for i in range(n_features)]
    importances = model.feature_importances_.reshape(-1, 1)
    return pd.DataFrame(importances, index=labels, columns=["Importance"])


# ------------------------------------------------------------
# Hyperparameter Optimization
# ------------------------------------------------------------
def optimize_forest(
    X_train: np.ndarray,
    Y_train: np.ndarray,
    param_dist: Optional[Dict[str, Any]] = None,
    cv: int = 6,
    n_iter: int = 200,
    scoring: str = "neg_mean_absolute_error",
    n_jobs: int = -1,
    verbose: int = 2,
    random_state: int = 42
) -> Dict[str, Any]:
    """
    Run RandomizedSearchCV to optimize Random Forest hyperparameters.

    Parameters
    ----------
    X_train : np.ndarray
        Training feature matrix.
    Y_train : np.ndarray
        Training target vector.
    param_dist : dict or None, default=None
        Hyperparameter search space.
    cv : int, default=6
        Number of cross-validation folds.
    n_iter : int, default=200
        Number of parameter settings sampled.
    scoring : str, default="neg_mean_absolute_error"
        Scoring metric for optimization.
    n_jobs : int, default=-1
        Number of parallel jobs.
    verbose : int, default=2
        Verbosity level.
    random_state : int, default=42
        Random seed.

    Returns
    -------
    dict
        Contains:
        - "model": best estimator
        - "params": best hyperparameters
        - "cv_results": full CV results
        - "search": RandomizedSearchCV object
    """
    if param_dist is None:
        param_dist = {
            "max_features": list(range(3, 8)),
            "max_depth": list(range(6, 11)),
            "min_samples_split": list(range(5, 15)),
            "min_samples_leaf": list(range(5, 15)),
            "bootstrap": [True, False]
        }

    base_model = RandomForestRegressor(
        n_estimators=50,
        n_jobs=n_jobs,
        random_state=random_state
    )

    search = RandomizedSearchCV(
        estimator=base_model,
        param_distributions=param_dist,
        n_iter=n_iter,
        cv=cv,
        scoring=scoring,
        n_jobs=n_jobs,
        verbose=verbose,
        random_state=random_state
    )

    search.fit(X_train, Y_train)

    return {
        "model": search.best_estimator_,
        "params": search.best_params_,
        "cv_results": search.cv_results_,
        "search": search
    }


# ------------------------------------------------------------
# Main (debugging)
# ------------------------------------------------------------
def main() -> None:
    """
    Example execution for debugging.

    Loads a dataset, trains a Random Forest model, evaluates it,
    and prints MAE%. This function is not used in production but
    is helpful for quick validation.
    """
    from dataprocessing.dataset_creation import main as data_main

    df, X_train, Y_train, X_test, Y_test = data_main()

    model = train_forest(X_train, Y_train)
    Y_train_pred = predict_forest(model, X_train)
    Y_test_pred = predict_forest(model, X_test)

    mae_train = evaluate_forest(Y_train, Y_train_pred)
    mae_test = evaluate_forest(Y_test, Y_test_pred)

    print("Random Forest Results:")
    print(f"Train MAE%: {mae_train * 100:.2f}")
    print(f"Test MAE%:  {mae_test * 100:.2f}")


# ---------------------------------------------------------------------------
# Ensures `main()` only runs when this file is executed directly.
# Prevents unintended training or tuning when imported elsewhere.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()