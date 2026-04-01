"""
test_metrics_api.py
-------------------

Import tests for the metrics public API.

These tests ensure that core evaluation metrics exposed by the
LinearBenchTreeSuite metrics domain are importable and callable.

The goal is to lock the public metrics API and prevent accidental
renames or removals during refactoring.
"""

from linearbenchtree.metrics import mae_percent


def test_mae_percent_importable() -> None:
    """
    Verify that `mae_percent` is importable from the metrics API.

    This test does not validate numerical correctness, only that the
    public API surface exists and remains stable.
    """
    assert callable(mae_percent)