# 🧱 How to Extend This Framework  
### Adding New Models, Features, or Workflows

LinearBenchTreeSuite was intentionally designed to be **modular**, **predictable**, and **easy to extend**. Whether you want to add a new model family, incorporate additional features, or build new evaluation workflows, the architecture supports clean, low‑friction expansion.

This guide outlines the recommended patterns for extending the framework.

---

## 🔧 1. Adding a New Model Family

Every model family in the project follows the same structure:

```
src/
  newmodel/
    __init__.py
    train_newmodel.py
    predict_newmodel.py
    evaluate_newmodel.py
    parameter_opt.py   (optional)
```

### **Step‑by‑Step**

#### **1. Create a new subpackage**
Example:

```
src/xgboost/
```

#### **2. Add the core modules**
At minimum, include:

- `train_xgboost.py`  
- `predict_xgboost.py`  
- `evaluate_xgboost.py`  

Each should follow the same function signatures as existing models:

```python
def train_xgboost(X_train, Y_train, ...):
    ...

def predict_xgboost(model, X):
    ...

def evaluate_xgboost(Y_true, Y_pred):
    ...
```

This ensures compatibility with the notebook and any future automation.

#### **3. (Optional) Add hyperparameter tuning**
If the model supports tuning, add:

```
parameter_opt.py
```

Use the same return structure as other tuning modules:

```python
{
    "model": best_estimator,
    "params": best_params,
    "cv_results": search.cv_results_,
    "search": search
}
```

#### **4. Import and use in the notebook**
Add a new section in the analysis notebook:

- Train  
- Predict  
- Evaluate  
- Compare MAE%  
- Visualize feature importance (if applicable)

---

## 🧩 2. Adding New Features to the Dataset

If you want to expand beyond the 12‑month rolling window:

### **Modify `dataset_creation.py`**

You can:

- change the window size  
- add lagged features  
- add moving averages  
- add seasonal indicators  
- incorporate external regressors  

Example:

```python
df["MA_3"] = df["sales"].rolling(3).mean()
```

Just ensure the new features are included in the final `X_train` and `X_test` matrices.

---

## 📊 3. Adding New Evaluation Metrics

All models currently use **MAE%**, but you can easily add:

- RMSE  
- MAPE  
- SMAPE  
- R²  
- Weighted metrics  

Add new functions to:

```
src/dataprocessing/benchmark_linear_regr.py
```

or create a dedicated module:

```
src/evaluation/metrics.py
```

Then update the notebook to compute and compare them.

---

## 🧠 4. Adding New Visualizations

Common additions include:

- Residual plots  
- Error distributions  
- Feature importance heatmaps  
- Prediction intervals  
- Model‑vs‑model scatter plots  

Add these to:

```
notebooks/analysis/
```

or create a reusable plotting module:

```
src/visualization/plots.py
```

---

## 🏗️ 5. Integrating External Models or Libraries

The framework is compatible with:

- XGBoost  
- LightGBM  
- CatBoost  
- Prophet  
- ARIMA/SARIMA  
- Neural networks (PyTorch, TensorFlow, Keras)

Just follow the same modular pattern:

- `train_*`  
- `predict_*`  
- `evaluate_*`  
- `optimize_*` (optional)

This keeps the architecture clean and predictable.

---

## 🚀 6. Automating the Entire Pipeline

If you want to turn this into a production‑style pipeline, you can add:

- a `main.py` orchestrator  
- a configuration system (`config.yaml`)  
- logging  
- experiment tracking (MLflow, Weights & Biases)  
- CLI commands  

The current structure already supports this with minimal refactoring.

---

## 🧩 7. Converting the Framework Into a Python Package

If you want to pip‑install your own framework:

1. Add a `pyproject.toml`  
2. Add a `setup.cfg` or `setup.py`  
3. Rename `src/` to a package name (e.g., `linearbenchtreesuite/`)  
4. Publish to PyPI or install locally with `pip install -e .`

This is a natural next step if you want to use the framework across multiple projects.

---

## 🏁 Summary

Extending LinearBenchTreeSuite is straightforward because the architecture is:

- **modular**  
- **consistent**  
- **predictable**  
- **well‑documented**  

Whether you’re adding new models, new features, new metrics, or new workflows, the framework is designed to grow with you.