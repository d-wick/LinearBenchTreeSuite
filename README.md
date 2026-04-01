<p align="center">
  <img src="assets/LinearBenchTreeSuite_BannerS.png" alt="LinearBenchTreeSuite Banner" width="100%">
</p>


# LinearBenchTreeSuite

LinearBenchTreeSuite is a lightweight, modular Python package for benchmarking
linear and tree‑based regression models on time‑series and tabular datasets.

The project emphasizes:
- clean separation between **data**, **models**, and **metrics**
- a small, stable **public API**
- reproducible benchmarking workflows
- interpretability via feature importance for tree models

---

## Installation

### From source (recommended for development)

From the project root:

```bash
pip install .
````

For editable (development) installs:

```bash
pip install -e .
```

### Package name vs import name

The package is distributed under the name:

```bash
pip install linearbenchtree-suite
```

and imported in Python as:

```python
import linearbenchtree
```


***

## Package Structure

```text
linearbenchtree/
├── data/        # Public data-loading and dataset creation API
├── models/      # Public model training, prediction, and interpretation API
├── metrics/     # Public evaluation metrics API
│
├── dataprocessing/   # Internal implementation details
├── decisiontree/
├── randomforest/
├── exrandomtree/
└── experiments/      # Experimental and exploratory workflows
```

Only `data`, `models`, and `metrics` are considered **public API domains**.
All other modules are internal and may change without notice.

***

## Data API

The Data API provides utilities for loading raw data and constructing
supervised learning datasets.

```python
from linearbenchtree.data import (
    load_raw_csv,
    import_data,
    datasets,
)
```

### Key functions

*   `load_raw_csv()`  
    Load a CSV file from the project’s data directory.

*   `import_data()`  
    Convenience wrapper around raw data loading.

*   `datasets()`  
    Create rolling‑window training and test datasets suitable for
    time‑series regression.

***

## Model API

The Model API exposes **high‑level, user‑facing model operations**:
training, prediction, and interpretability.

```python
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
```

### Baseline

*   `benchmark()`  
    Train a linear regression baseline and generate predictions.
    This serves as a reference point for all tree‑based models.

***

### Decision Tree

*   `train_tree()`
*   `predict_tree()`

***

### Random Forest

*   `train_forest()`
*   `predict_forest()`
*   `get_feature_importance_forest()`

Returns labeled feature importance values for interpretability.

***

### Extra Trees

*   `train_extratrees()`
*   `predict_extratrees()`
*   `get_feature_importance_extratrees()`

Returns labeled feature importance values for interpretability.

***

## Metrics API

The Metrics API provides **model‑agnostic evaluation functions**.
Metric logic is centralized here to ensure consistency across models.

```python
from linearbenchtree.metrics import mae_percent
```

### Available metrics

*   `mae_percent(y_true, y_pred)`

Mean Absolute Error expressed as a percentage of the mean true value:

    mean(|actual − predicted|) / mean(actual)

This is the **canonical evaluation metric** used throughout the project.

***

## Evaluation Philosophy

*   Metrics (e.g. `mae_percent`) are **public and model‑agnostic**
*   Model‑specific `evaluate_*` helpers exist internally for convenience
*   Users are encouraged to compose evaluation explicitly:

```python
y_pred = predict_forest(model, X_test)
score = mae_percent(y_test, y_pred)
```

This keeps evaluation flexible and extensible as new metrics are added.

***

## Optimization & Tuning (Internal)

Hyperparameter optimization utilities (e.g. `optimize_*`) are intentionally
**not part of the public API**.

These functions:

*   encode experimental choices
*   may change as research evolves
*   are safe to use internally and in notebooks

They are not guaranteed to be stable across releases.

***

## Public API Guarantees

The following are guaranteed to remain stable within a major version:

*   `linearbenchtree.data`
*   `linearbenchtree.models`
*   `linearbenchtree.metrics`
*   all functions explicitly documented in this README

Internal modules are free to change.

***

## Development & Extension

For details on extending the project with new models or metrics, see:

*   `EXTENDING.md`
*   `ARCHITECTURE.md`

***

## License

MIT License

***

See `VERSIONING.md` for API stability and compatibility guarantees.




