"""
test_imports.py
---------------

Import tests for the LinearBenchTreeSuite public API.

These tests verify that high-level API surfaces are importable and callable,
without locking internal implementation details.
"""


def test_package_import():
    """
    Ensure the top-level package is importable.
    """
    import linearbenchtree


def test_data_api_imports():
    """
    Ensure the Data Public API is importable.
    """
    from linearbenchtree.data import (
        load_raw_csv,
        import_data,
        datasets,
    )

    assert callable(load_raw_csv)
    assert callable(import_data)
    assert callable(datasets)


def test_model_api_imports():
    """
    Ensure the Model Public API is importable.
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

    assert callable(benchmark)
    assert callable(train_tree)
    assert callable(predict_tree)
    assert callable(train_forest)
    assert callable(predict_forest)
    assert callable(get_feature_importance_forest)
    assert callable(train_extratrees)
    assert callable(predict_extratrees)
    assert callable(get_feature_importance_extratrees)


def test_metrics_api_import():
    """
    Ensure the Metrics Public API is importable.
    """
    from linearbenchtree.metrics import mae_percent

    assert callable(mae_percent)