# 📘 LinearBenchTreeSuite — Car Sales Forecasting  
### Benchmarking Four Machine Learning Models for Monthly New‑Car Sales Prediction

This project provides a modular machine learning framework for forecasting monthly new‑car sales by manufacturer. It compares four regression models — Linear Regression, Decision Tree, Random Forest, and Extra Trees — using a consistent rolling‑window dataset and a unified evaluation workflow.

The goal is to understand which model performs best, how tuning affects accuracy, and which historical months contribute most to predictive performance.

---

## 📂 Project Structure

```
project/
│
├── data/
│   ├── external/
│   ├── interim/
│   ├── processed/
│   │   └── new_car_sales_by_make.csv
│   └── raw/
│
├── notebooks/
│   ├── guides/
│   └── analysis/
│
├── src/
│   ├── dataprocessing/
│   │   ├── __init__.py
│   │   ├── benchmark_linear_regr.py
│   │   ├── data_loader_processed.py
│   │   └── dataset_creation.py
│   │
│   ├── decisiontree/
│   │   ├── __init__.py
│   │   ├── parameter_opt.py
│   │   └── regression_tree.py
│   │
│   ├── randomforest/
│   │   ├── __init__.py
│   │   └── random_forest.py
│   │
│   ├── exrandomtree/
│   │   ├── __init__.py
│   │   └── ex_random_tree.py
│   │
│   └── experiments/
│       ├── __init__.py
│       └── features_opt_exploration.py
│
└── README.md
```

---

## 📊 Dataset Overview

The dataset contains monthly new‑car sales by manufacturer.  
It is pivoted so that:

- **Rows** = car manufacturers  
- **Columns** = months (`YYYY-MM`)  
- **Values** = units sold  

This structure enables creation of rolling windows for supervised learning.  
For example, a 12‑month window predicts the next month’s sales.

---

## 🔧 How the Pipeline Works

### **1. Data Loading**
`dataprocessing.data_loader_processed` loads the processed CSV from `data/processed/`.

### **2. Rolling Window Creation**
`dataprocessing.dataset_creation.datasets()` converts the pivoted table into:

- `X_train` — rolling windows of past 12 months  
- `Y_train` — next‑month sales  
- `X_test`, `Y_test` — held‑out evaluation set  

Example shapes from the notebook:

- `X_train`: `(6305, 12)`  
- `Y_train`: `(6305,)`  
- `X_test`: `(780, 12)`  
- `Y_test`: `(780,)`

### **3. Model Training, Tuning, and Evaluation**
Each model family has its own module under `src/`, following a consistent pattern:

#### **Linear Regression (Benchmark)**
- No tuning  
- Provides a baseline MAE% for comparison  
- Implemented in `benchmark_linear_regr.py`

#### **Decision Tree**
- Hyperparameter tuning via `parameter_opt.py`  
- Training, prediction, and evaluation via `regression_tree.py`  
- Captures non‑linear patterns

#### **Random Forest**
- Tuning via `optimize_forest()`  
- Training and prediction via `train_forest()` and `predict_forest()`  
- Feature importance extraction included

#### **Extra Trees**
- Similar to Random Forest but with more randomness  
- Often yields the best accuracy  
- Feature importance extraction included

### **4. Evaluation Metrics**
All models use **Mean Absolute Error (MAE%)** on both training and test sets.

---

## 🧪 Model Comparison (MAE%)

| Model              | Train MAE% | Test MAE% |
|-------------------|------------|-----------|
| Linear Regression | 17.85      | 17.82     |
| Decision Tree     | 16.80      | 18.13     |
| Random Forest     | 12.05      | 17.68     |
| Extra Trees       | 11.54      | 17.31     |

**Key Insight:**  
Tree‑based models outperform Linear Regression, with **Extra Trees** and **Random Forest** achieving the strongest results.

---

## 📈 Visuals Included in the Analysis Notebook

### **1. Feature Importance**
Random Forest and Extra Trees modules include built‑in feature importance extraction.  
Plots show which historical months contribute most to predictions.

### **2. Actual vs Predicted Sales**
The notebook visualizes all models on the same chart, making it easy to compare performance across the test set.

---

## 🚀 Usage

### **Running the Analysis**
The simplest way to explore the project is through the Jupyter notebook in:

```
notebooks/analysis/
```

It demonstrates:

- Importing modules directly from `src/`
- Creating datasets
- Running each model
- Visualizing results

### **Using the Modular Code**
Each model family exposes:

- A tuning function  
- A training function  
- A prediction function  
- An evaluation function  

This makes it easy to:

- Swap models  
- Add new model families  
- Run experiments  
- Extend the pipeline

---

## 🧱 Adding a New Model (High‑Level Guide)

To add a new model:

1. Create a new subpackage under `src/` (e.g., `xgboost/`)  
2. Add:
   - `parameter_opt.py` (optional)
   - `train_model.py`
   - `predict_model.py`
   - `evaluate_model.py`
3. Follow the same function signatures as existing models  
4. Import and run it in the notebook or a script

This keeps the project consistent and extensible.

---

## 🏁 Key Takeaways

- Tree‑based models outperform Linear Regression for this dataset  
- Extra Trees provides the best overall accuracy  
- Feature importance reveals which months matter most  
- The modular design makes the project easy to extend and reuse  
- The notebook provides a clear, reproducible workflow for analysis 