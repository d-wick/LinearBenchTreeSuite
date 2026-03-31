# 🧱 Extending LinearBenchTreeSuite
### Adding Models, Features, Metrics, and Workflows

LinearBenchTreeSuite is designed to be **modular**, **package‑first**, and **easy to extend**.  
This guide explains how to extend the framework correctly now that it is a **proper Python package**.

> **Important:**  
> All reusable code lives under `src/linearbenchtree/`.  
> Notebooks and scripts *consume* the package — they do not define it.

---

## 🔧 Development Setup (Required)

If you are extending the framework, you should be working in **editable mode**.

```bash
pip install -e ".[dev]"
````

This ensures:

*   changes to `.py` files are picked up immediately
*   imports behave the same as a real install
*   notebooks and tests reflect package behavior

During notebook development, enable autoreload:

```python
%load_ext autoreload
%autoreload 2
```

***

## 📦 Package Boundary (Non‑Negotiable Rule)

    src/
    └── linearbenchtree/

### ✅ Allowed

*   add new subpackages under `linearbenchtree/`
*   import using `linearbenchtree.<module>`

### ❌ Not allowed

*   importing from repo‑relative paths
*   adding logic directly to notebooks
*   assuming the working directory

This ensures `pip install .` works for all users.

***

## 🔧 1. Adding a New Model Family

Each model family is a **subpackage** under `linearbenchtree/`.

### Example structure

    src/linearbenchtree/
    └── xgboost/
        ├── __init__.py
        ├── train_xgboost.py
        ├── predict_xgboost.py
        ├── evaluate_xgboost.py
        └── parameter_opt.py   # optional

### Step‑by‑step

#### 1️⃣ Create the subpackage

```bash
mkdir src/linearbenchtree/xgboost
touch src/linearbenchtree/xgboost/__init__.py
```

#### 2️⃣ Implement core functions

Each model should expose predictable functions:

```python
def train_xgboost(X_train, y_train, **kwargs):
    ...

def predict_xgboost(model, X):
    ...

def evaluate_xgboost(y_true, y_pred):
    ...
```

This consistency allows:

*   notebook reuse
*   future automation
*   fair model comparison

#### 3️⃣ (Optional) Add hyperparameter tuning

If applicable, include `parameter_opt.py` that returns:

```python
{
    "model": best_estimator,
    "params": best_params,
    "cv_results": search.cv_results_,
    "search": search,
}
```

***

## 🧩 2. Adding New Dataset Features

All feature engineering lives in:

    linearbenchtree/dataprocessing/dataset_creation.py

You may:

*   change window sizes
*   add lagged features
*   add rolling statistics
*   add external regressors

Example:

```python
df["MA_3"] = df["sales"].rolling(3).mean()
```

Ensure all new features are included in:

*   `X_train`
*   `X_test`

***

## 📊 3. Adding New Evaluation Metrics

Current default metric is **MAE%**, but others can be added.

### Option A — Extend existing baseline module

    linearbenchtree/dataprocessing/benchmark_linear_regr.py

### Option B — Create a dedicated metrics module

    linearbenchtree/evaluation/metrics.py

Recommended metrics:

*   RMSE
*   MAPE / SMAPE
*   R²
*   weighted metrics

***

## 🎨 4. Adding Visualizations

Visualizations are **not part of the core package** unless they are reusable.

### ✅ Notebook‑only visuals

    notebooks/analysis/

### ✅ Reusable plots

    linearbenchtree/visualization/plots.py

Examples:

*   residual plots
*   feature importance charts
*   prediction vs actual overlays

***

## ➕ 5. Adding New Dependencies (Important)

### Rule

> If a module is imported anywhere under `src/linearbenchtree/`,
> it **must** be declared in `pyproject.toml`.

### Example

If you add:

```python
import xgboost
```

Update `pyproject.toml`:

```toml
[project]
dependencies = [
  "xgboost>=2.0",
]
```

### ✅ Use version *lower bounds*

*   Do **not** pin exact versions
*   Exact versions belong in `environment.yml`

After adding a dependency:

```bash
pip uninstall linearbenchtree-suite
pip install .
```

***

## 🧪 6. Protecting Extensions with Tests

Every new **public module or subpackage** should be import‑tested.

Add to:

    tests/test_imports.py

Example:

```python
def test_xgboost_import():
    import linearbenchtree.xgboost
```

This prevents future refactors from breaking packaging.

***

## 🔁 7. Editable vs Normal Install (Extension Context)

| Task                   | Install Mode |
| ---------------------- | ------------ |
| Developing / extending | Editable     |
| Running notebooks      | Editable     |
| Testing packaging      | Normal       |
| CI / users             | Normal       |

Always validate extensions with:

```bash
pip install .
```

Editable installs can hide mistakes — normal installs expose them.

***

## 🚀 8. Future Extension Paths

The current architecture supports:

*   CLI entry points
*   configuration files (`yaml`)
*   experiment tracking (MLflow, W\&B)
*   orchestration pipelines
*   productionization

These can be added without restructuring the package.

***

## 🏁 Summary

Extending LinearBenchTreeSuite correctly means:

*   ✅ add code under `src/linearbenchtree/`
*   ✅ use absolute package imports
*   ✅ install in editable mode during development
*   ✅ declare dependencies explicitly
*   ✅ lock changes with import tests

Following these rules keeps the framework:

*   predictable
*   installable
*   reusable
*   contributor‑friendly