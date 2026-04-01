"""
test_model_api.py
-----------------

Import tests for the model public API.

These tests verify that high-level model training, prediction, and
interpretability functions are available via the public API layer.
"""

from linearbenchtree.models import (
    benchmark,
    train_tree,
    predict_tree,
    train_forest,
    predict_forest,
    get_feature_importance_forest,
    train_extratrees,
    predict_extratrees,
    get_feature_importance_extratrees,
)


def test_model_api_imports() -> None:
    """
    Ensure all public model API functions are importable and callable.
    """
    assert callable(benchmark)
    assert callable(train_tree)
    assert callable(predict_tree)
    assert callable(train_forest)
    assert callable(predict_forest)
    assert callable(get_feature_importance_forest)
    assert callable(train_extratrees)
    assert callable(predict_extratrees)
    assert callable(get_feature_importance_extratrees)