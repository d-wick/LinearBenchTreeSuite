# LinearBenchTreeSuite Architecture

This document describes the architectural structure of LinearBenchTreeSuite,
including public API boundaries, internal layers, and design rationale.

The goal of this architecture is to support:
- clean benchmarking of regression models
- extensibility without API breakage
- reproducible evaluation
- interpretability for tree-based models

---

## Architectural Overview

LinearBenchTreeSuite follows a **layered architecture** with strict separation
between **public APIs** and **internal implementation details**.

At a high level:

```text
User Code / Notebooks
        |
        v
+-------------------------+
|   Public API Domains    |
|-------------------------|
|  data | models | metrics|
+-------------------------+
        |
        v
+-------------------------+
| Internal Implementations|
|-------------------------|
| dataprocessing          |
| decisiontree            |
| randomforest            |
| exrandomtree            |
| experiments             |
+-------------------------+
````

Only the **public API domains** are considered stable.

***

## Public API Domains

The public API is intentionally small and explicit. It consists of three domains:

### 1. `linearbenchtree.data`

**Responsibility**

*   Load raw data
*   Create supervised learning datasets
*   Prepare train/test splits

**Design constraints**

*   No model logic
*   No evaluation logic
*   No experimentation code

**Rationale**
Keeping data concerns isolated allows dataset generation to evolve independently
from modeling and evaluation.

***

### 2. `linearbenchtree.models`

**Responsibility**

*   Train models
*   Generate predictions
*   Provide interpretability helpers

**Exposed concepts**

*   `train_<model>()`
*   `predict_<model>()`
*   `get_feature_importance_<model>()` (when applicable)
*   `benchmark()` for baseline comparison

**Design constraints**

*   No metric formulas
*   No dataset creation
*   No experiment orchestration

**Rationale**
Models should focus on **learning and inference**, not evaluation policy or
experimental workflow.

***

### 3. `linearbenchtree.metrics`

**Responsibility**

*   Define evaluation metrics
*   Ensure consistent scoring across models

**Exposed concepts**

*   `mae_percent(y_true, y_pred)`

**Design constraints**

*   Metrics must be model-agnostic
*   No training logic
*   No workflow orchestration

**Rationale**
Centralizing metrics prevents duplicated formulas, ensures comparability, and
makes evaluation behavior explicit and testable.

***

## Internal Implementation Layers

The following modules are **internal** and not part of the public API.

### `dataprocessing/`

*   Raw data loading helpers
*   Feature engineering
*   Dataset construction internals

### `decisiontree/`

*   Decision tree implementation details
*   Internal evaluators and optimizers

### `randomforest/`

*   Random forest training logic
*   Feature importance extraction
*   Internal optimization routines

### `exrandomtree/`

*   Extra Trees training logic
*   Feature importance extraction
*   Hyperparameter tuning utilities

### `experiments/`

*   Exploratory workflows
*   Model comparisons
*   Notebook-oriented utilities
*   Benchmark orchestration (e.g. train vs test comparisons)

These modules may change freely without API guarantees.

***

## Evaluation Flow

Evaluation is intentionally **compositional**, not implicit.

Typical evaluation flow:

```python
model = train_forest(X_train, y_train)
y_pred = predict_forest(model, X_test)
score = mae_percent(y_test, y_pred)
```

### Key principles

*   Metrics are applied **explicitly**
*   Models do not own evaluation logic
*   Evaluation behavior is transparent and reusable

Model-specific `evaluate_*` helpers may exist internally but are not considered
public API.

***

## Optimization Strategy

Hyperparameter optimization is treated as **experimental infrastructure**.

### Characteristics

*   Encodes research choices
*   May change scoring strategies
*   May evolve parameter ranges

### Architectural decision

*   Optimization utilities remain internal
*   They are excluded from the public API
*   They may live in model modules or `experiments/`

This preserves flexibility while preventing premature API lock-in.

***

## Feature Importance & Interpretability

Feature importance is a **first-class capability** for tree-based models.

### Architectural stance

*   Feature importance helpers are public API
*   Outputs must be labeled and human-readable
*   Raw model internals are not exposed

This supports interpretability without coupling users to specific model classes.

***

## API Stability Guarantees

The following are considered **stable within a major version**:

*   `linearbenchtree.data`
*   `linearbenchtree.models`
*   `linearbenchtree.metrics`
*   Functions explicitly documented in `README.md`

Internal modules carry **no stability guarantees**.

API stability is enforced through:

*   import tests
*   documentation
*   CI validation

***

## Extensibility Summary

When extending LinearBenchTreeSuite:

*   Add new functionality internally first
*   Expose only high-level concepts via public APIs
*   Centralize metrics in `metrics`
*   Keep experimentation and tuning internal
*   Lock new APIs with import tests

For step-by-step extension guidance, see `EXTENDING.md`.

***

## Architectural Philosophy

> **Small APIs, explicit evaluation, internal freedom.**

This philosophy enables rapid iteration without sacrificing reliability or
clarity for users.
