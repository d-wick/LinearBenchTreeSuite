"""
Model Public API
----------------

This module defines the public, stable API for model training, prediction,
and interpretation within LinearBenchTreeSuite.

Only high-level, user-facing functions are exposed here. Internal helpers,
experiments, and optimization routines are intentionally excluded.
"""

from ..dataprocessing.benchmark_linear_regr import benchmark

from ..decisiontree.regression_tree import (
    train_tree,
    predict_tree,
)

from ..randomforest.random_forest import (
    train_forest,
    predict_forest,
    get_feature_importance_forest
)

from ..exrandomtree.ex_random_tree import (
    train_extratrees,
    predict_extratrees,
    get_feature_importance_extratrees
)

__all__ = [
    "benchmark",
    "train_tree",
    "predict_tree",
    "train_forest",
    "predict_forest",
    "get_feature_importance_forest",
    "train_extratrees",
    "predict_extratrees",
    "get_feature_importance_extratrees",
]