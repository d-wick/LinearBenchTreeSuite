# 🏗️ LinearBenchTreeSuite — Architecture Overview

LinearBenchTreeSuite is structured as a **proper Python package** with a clear separation between:

- reusable library code
- notebooks and experimentation
- data storage
- tests and packaging infrastructure

This document explains how those layers fit together and how code flows through the system.

---

## 🎯 Architectural Goals

The architecture is designed to be:

- **Modular** — each model family is isolated and interchangeable
- **Package‑first** — all reusable logic is importable as a library
- **Notebook‑friendly** — supports interactive ML workflows
- **Extensible** — easy to add new models, features, and metrics
- **Installable** — works with both editable and normal installs

---

## 🧱 High‑Level Layered View

```

┌────────────────────────────────────────────┐
│           User / Developer Layer           │
│--------------------------------------------│
│ • Jupyter notebooks                        │
│ • Python scripts                           │
│ • CLI / future automation                  │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│        LinearBenchTreeSuite Package        │
│--------------------------------------------│
│ src/linearbenchtree/                       │
│ • dataprocessing                           │
│ • decisiontree                             │
│ • randomforest                             │
│ • exrandomtree                             │
└────────────────────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────┐
│              Data Layer                    │
│--------------------------------------------│
│ • data/processed/ CSVs                     │
│ • external data sources                    │
└────────────────────────────────────────────┘

```

Only the **package layer** (`src/linearbenchtree/`) is installed and importable.

---

## 📦 Package Boundary (Critical Concept)

```

src/
└── linearbenchtree/
├── dataprocessing/
├── decisiontree/
├── randomforest/
├── exrandomtree/
└── **init**.py

```

### Key rules

- ✅ Everything under `src/linearbenchtree/` is **library code**
- ✅ Everything outside is **not importable** after installation
- ❌ Notebooks must never rely on repo‑relative imports
- ❌ No logic should live directly in notebooks

This ensures that:

- `pip install .` behaves like a real user install
- editable installs behave identically to normal installs (except for reload behavior)
- packaging tests are meaningful

---

## 🔧 Core Package Modules

### `dataprocessing/` — Data Preparation & Baselines

Responsibilities:
- load processed datasets
- construct rolling‑window supervised datasets
- provide baseline models and evaluation helpers

Key modules:
- `data_loader_processed.py`
- `dataset_creation.py`
- `benchmark_linear_regr.py`

This layer is **model‑agnostic** and feeds all downstream models.

---

### `decisiontree/` — Decision Tree Models

Responsibilities:
- train, predict, and evaluate decision trees
- hyperparameter optimization via `RandomizedSearchCV`

Key modules:
- `regression_tree.py`
- `parameter_opt.py`

---

### `randomforest/` — Random Forest Models

Responsibilities:
- ensemble training and prediction
- feature importance extraction
- hyperparameter tuning

Key module:
- `random_forest.py`

---

### `exrandomtree/` — Extra Trees Models

Responsibilities:
- high‑variance ensemble modeling
- evaluation and feature importance
- hyperparameter tuning

Key module:
- `ex_random_tree.py`

---

## 📓 Notebook Layer (Analysis & Exploration)

```

notebooks/
└── analysis/
└── LinearBenchTreeSuite\_Example.ipynb

````

Notebooks are **clients of the package**, not part of it.

They should:
- import from `linearbenchtree.*`
- orchestrate experiments
- visualize results
- never contain reusable logic

During development, notebooks typically use:
```python
%load_ext autoreload
%autoreload 2
````

This supports rapid iteration with editable installs.

***

## 📂 Data Layer

    data/
    ├── raw/
    ├── interim/
    ├── processed/
    │   └── new_car_sales_by_make.csv
    └── external/

Design principles:

*   data is **never packaged**
*   paths are passed explicitly
*   package code does not assume a working directory

This keeps the library reusable across projects.

***

## 🧪 Tests & Packaging Infrastructure

    tests/
    └── test_imports.py

Purpose:

*   lock in packaging correctness
*   ensure all public import paths remain valid
*   prevent regressions during refactors

These tests validate **structure**, not model behavior.

***

## 🔁 Editable vs Normal Install (Architectural Impact)

### Editable install

```bash
pip install -e .
```

*   links Python directly to `src/linearbenchtree/`
*   used for development and notebooks
*   code changes picked up immediately (with autoreload)

### Normal install

```bash
pip install .
```

*   installs a built snapshot into `site-packages`
*   mirrors user and CI behavior
*   used to validate correctness

The architecture supports **both** without modification.

***

## 🔌 Extension Points

The architecture is intentionally open at these points:

*   add new model families as new subpackages
*   add metrics in a shared evaluation module
*   add visualization utilities
*   add orchestration layers (CLI, pipeline, config)

See **EXTENDING.md** for concrete extension instructions.

***

## 🏁 Summary

LinearBenchTreeSuite is architected as a **real Python package**, not just a notebook project:

*   reusable code lives in `src/linearbenchtree`
*   notebooks consume the package
*   data lives outside the package
*   tests protect the structure
*   editable installs support development
*   normal installs support users

This foundation allows the project to scale from:

> *exploratory analysis* → *reusable framework* → *production‑ready tool*