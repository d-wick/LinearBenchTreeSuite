<p align="center">
  <img src="assets/LinearBenchTreeSuite_BannerS.png" alt="LinearBenchTreeSuite Banner" width="100%">
</p>

# 📘 LinearBenchTreeSuite  
### A Modular, Installable Benchmarking Framework for Rolling‑Window Time‑Series Forecasting

**Case Study: Monthly New‑Car Sales by Manufacturer**

LinearBenchTreeSuite is a modular, extensible machine‑learning framework designed to benchmark multiple regression models on structured time‑series forecasting tasks. Using publicly available monthly new‑car sales data as a case study, the project evaluates four model families:

- **Linear Regression** (baseline)
- **Decision Tree**
- **Random Forest**
- **Extra Trees**

The framework emphasizes **clarity**, **reproducibility**, and **extensibility**, and is now structured as a **proper Python package** that supports both normal and editable installs.

---

## 🌟 Key Features

- **Package‑first architecture** — all reusable code lives under `src/linearbenchtree/`
- **Modular model families** — consistent train / predict / evaluate / tune interfaces
- **Rolling‑window dataset creation** — fair, supervised comparisons
- **Unified evaluation metric (MAE%)**
- **Feature importance extraction** for tree‑based models
- **Hyperparameter optimization** via `RandomizedSearchCV`
- **Notebook‑driven analysis**, backed by importable package code

---

## 📦 Installation

### Option 1: Normal install (recommended for users)

Use this when you want to **use** the package without modifying it:

```bash
pip install .
````

Or directly from GitHub:

```bash
pip install git+https://github.com/<your-username>/LinearBenchTreeSuite.git
```

This mirrors how end users and CI systems install the package.

***

### Option 2: Editable install (recommended for development)

Use this when you are **actively developing** the package or running notebooks:

```bash
pip install -e ".[dev]"
```

Editable installs link Python directly to the source code, so changes to `.py` files are picked up immediately.

***

## 📓 Notebook Workflow (Development)

When working in Jupyter notebooks during development:

1.  Install the package in editable mode
2.  Enable IPython autoreload at the top of the notebook:

```python
%load_ext autoreload
%autoreload 2
```

This allows you to edit package code under `src/linearbenchtree/` and see changes without restarting the kernel.

***

## 📂 Project Structure

```text
project/
│
├── data/
│   └── processed/
│       └── new_car_sales_by_make.csv
│
├── notebooks/
│   └── analysis/
│       └── LinearBenchTreeSuite_Example.ipynb
│
├── src/
│   └── linearbenchtree/
│       ├── dataprocessing/
│       ├── decisiontree/
│       ├── randomforest/
│       ├── exrandomtree/
│       └── __init__.py
│
├── pyproject.toml
├── ARCHITECTURE.md
├── EXTENDING.md
└── README.md
```

Only code under `src/linearbenchtree/` is installed and importable.

***

## 🚀 Usage

### Running the analysis notebook

The primary demonstration notebook lives in:

    notebooks/analysis/LinearBenchTreeSuite_Example.ipynb

It demonstrates:

*   dataset creation
*   model training
*   tuning
*   evaluation
*   visualization

***

### Using the package in scripts

All model families expose consistent functions:

```python
from linearbenchtree.dataprocessing.data_loader_processed import load_data
from linearbenchtree.randomforest.random_forest import train_forest
```

This makes the framework reusable outside notebooks.

***

## 📐 Architecture & Extension

*   For a system‑level view of how data, models, and notebooks interact, see  
    ➡️ **ARCHITECTURE.md**

*   For guidance on adding new models, features, or metrics, see  
    ➡️ **EXTENDING.md**

***

## 🏁 Key Takeaways

*   Tree‑based models outperform Linear Regression for this task
*   Extra Trees delivers the strongest overall accuracy
*   Feature importance reveals which historical months matter most
*   The framework is now:
    *   installable
    *   testable
    *   extensible
    *   reusable across projects
