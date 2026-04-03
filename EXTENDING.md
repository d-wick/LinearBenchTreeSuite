# EXTENDING LinearBenchTreeSuite

This document describes how to extend LinearBenchTreeSuite with new models,
metrics, or data workflows while preserving API stability and architectural
consistency.

If you are adding functionality, **read this document before writing code**.

---

## Guiding Principles

LinearBenchTreeSuite follows a few core design principles:

1. **Small, stable public APIs**
2. **Clear separation of concerns**
3. **Internal implementation freedom**
4. **Explicit evaluation logic**

Extensions should reinforce these principles rather than weaken them.

---

## Public API Domains

Only the following package domains are considered **public and stable**:

- `linearbenchtree.data`
- `linearbenchtree.models`
- `linearbenchtree.metrics`

Anything outside these namespaces is **internal** and may change without notice.

If you are unsure where new code belongs, it is probably internal.

---

## Adding a New Model

### 1. Create an internal implementation module

Add your model implementation under an appropriate internal directory, for example:

```text
linearbenchtree/
├── mynewmodel/
│   ├── __init__.py
│   └── my_model.py
````

This module may include:

*   training logic
*   prediction helpers
*   optimization utilities
*   debugging `main()` functions

These files are **not public API**.

***

### 2. Define the public model interface

Expose only high‑level functions via the **Model Public API**:

*   `train_<model>()`
*   `predict_<model>()`
*   `get_feature_importance_<model>()` (if applicable)

Do **not** expose:

*   optimization routines
*   parameter search helpers
*   experiment orchestration logic

Add the public exports to:

```python
linearbenchtree/models/__init__.py
```

Example:

```python
from ..mynewmodel.my_model import (
    train_my_model,
    predict_my_model,
)

__all__ = [
    "train_my_model",
    "predict_my_model",
]
```

***

### 3. Evaluation logic

Model implementations **must not define new metric formulas**.

All evaluation metrics belong in the `metrics` domain.

Correct usage:

```python
from linearbenchtree.metrics import mae_percent

score = mae_percent(y_true, y_pred)
```

Model‑specific `evaluate_*` helpers may exist internally but are not part of the
public API.

***

### 4. Feature importance

If your model supports interpretability:

✅ Expose a public `get_feature_importance_<model>()` function  
✅ Return labeled, user‑readable outputs (e.g., DataFrames)  
❌ Do not expose raw model internals

Feature importance functions are considered **public API**.

***

## Adding a New Metric

Metrics are **first‑class API concepts**.

### 1. Add a metric implementation

Create a new file under:

```text
linearbenchtree/metrics/
```

Example:

```text
metrics/
├── mae.py
├── rmse.py
```

Each metric must:

*   be model‑agnostic
*   accept `(y_true, y_pred)`
*   return a numeric scalar

***

### 2. Expose the metric

Add the metric to:

```python
linearbenchtree/metrics/__init__.py
```

Example:

```python
from .rmse import rmse

__all__ = ["rmse"]
```

***

### 3. Lock the metric API

Add a minimal import test:

```python
def test_rmse_import():
    from linearbenchtree.metrics import rmse
    assert callable(rmse)
```

This ensures API stability without over‑specifying behavior.

***

## Optimization & Hyperparameter Tuning

Hyperparameter optimization utilities are considered **internal**.

They may:

*   use `GridSearchCV`, `RandomizedSearchCV`, or custom strategies
*   change parameter ranges
*   evolve over time

For this reason:

❌ Do NOT expose `optimize_*()` functions as public API  
✅ Keep them inside model modules or under `experiments/`  
✅ Document them as experimental if used in notebooks

Optimization behavior is **not version‑stable**.

***

## Experiments & Benchmarks

Functions that:

*   compare multiple models
*   evaluate train vs test performance
*   orchestrate workflows (e.g. `bench_test()`)

belong to:

*   internal modules
*   notebooks
*   `experiments/`

They are intentionally excluded from the public API.

***

## Testing Expectations

Every public API addition must include:

✅ An import test  
✅ Clear documentation  
✅ Consistent naming

Public API tests should:

*   verify importability
*   avoid running models
*   avoid loading data

***

## Documentation Expectations

When extending the project:

*   Update `README.md` for user‑facing changes
*   Update `ARCHITECTURE.md` for structural changes
*   Keep `EXTENDING.md` aligned with new conventions

Documentation is part of the API contract.

***

## Summary

When extending LinearBenchTreeSuite:

✅ Add models internally, expose them deliberately  
✅ Centralize evaluation in `metrics`  
✅ Expose feature importance where appropriate  
✅ Keep optimization internal  
✅ Lock APIs with import tests

When in doubt, **favor simplicity and stability**.

These rules exist to ensure external users can rely on the library
while internal implementations evolve freely.