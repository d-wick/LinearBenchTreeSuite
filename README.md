# 📘 LinearBenchTreeSuite  
### A Modular Benchmarking Framework for Rolling‑Window Time‑Series Forecasting  
**Case Study: Monthly New‑Car Sales by Manufacturer**

LinearBenchTreeSuite is a modular, extensible machine‑learning framework designed to benchmark multiple regression models on structured time‑series forecasting tasks.  
Using publicly available monthly new‑car sales data as a case study, the project evaluates four model families:

- **Linear Regression** (baseline)  
- **Decision Tree**  
- **Random Forest**  
- **Extra Trees**

The framework emphasizes clarity, reproducibility, and extensibility — making it suitable both as a portfolio project and as a foundation for real‑world forecasting pipelines.

---

## 🌟 Key Features

- **Modular architecture** — each model family lives in its own subpackage with training, prediction, evaluation, and tuning utilities.  
- **Rolling‑window dataset creation** — consistent supervised‑learning windows for fair model comparison.  
- **Unified evaluation metric (MAE%)** — easy cross‑model comparison.  
- **Feature importance extraction** — interpretability for tree‑based models.  
- **Hyperparameter optimization** — RandomizedSearchCV for Decision Tree, Random Forest, and Extra Trees.  
- **Notebook‑driven analysis** — clean, reproducible workflow for exploration and visualization.

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
│   ├── analysis/
│   │   └── LinearBenchTreeSuite_Example.ipynb
│   └── guides/
│
├── src/
│   ├── dataprocessing/
│   │   ├── benchmark_linear_regr.py
│   │   ├── data_loader_processed.py
│   │   └── dataset_creation.py
│   │
│   ├── decisiontree/
│   │   ├── parameter_opt.py
│   │   └── regression_tree.py
│   │
│   ├── exrandomtree/
│   │   └── ex_random_tree.py
│   │
│   ├── randomforest/
│   │   └── random_forest.py
│   │
│   └── __init__.py
│
├── ARCHITECTURE.md
├── EXTENDING.md
└── README.md
```

---

## 📊 Dataset Overview

The case‑study dataset contains **monthly new‑car sales by manufacturer**, pivoted into a modeling‑friendly structure:

- **Rows** → manufacturers  
- **Columns** → months (`YYYY‑MM`)  
- **Values** → units sold  

This format enables rolling‑window supervised learning.  
For example, a 12‑month window predicts the next month’s sales.

---

## 🔧 Pipeline Overview

### **1. Data Loading**  
`data_loader_processed.py` loads the processed CSV from `data/processed/`.

### **2. Rolling‑Window Dataset Creation**  
`dataset_creation.datasets()` produces:

- `X_train` — past 12 months  
- `Y_train` — next‑month target  
- `X_test`, `Y_test` — held‑out evaluation set  

### **3. Model Training & Tuning**  
Each model family follows the same structure:

#### **Linear Regression (Baseline)**  
- No tuning  
- Establishes a performance floor  
- Implemented in `benchmark_linear_regr.py`

#### **Decision Tree**  
- Tuning via `parameter_opt.py`  
- Training & evaluation via `regression_tree.py`

#### **Random Forest**  
- Tuning via `optimize_forest()`  
- Feature importance extraction included

#### **Extra Trees**  
- More randomness → often best performance  
- Feature importance extraction included

### **4. Evaluation Metric**  
All models use **Mean Absolute Error Percentage (MAE%)**:

\[
\text{MAE\%} = \frac{\text{mean}(|y - \hat{y}|)}{\text{mean}(y)}
\]

---

## 🧪 Model Comparison (MAE%)

| Model              | Train MAE% | Test MAE% |
|-------------------|------------|-----------|
| Linear Regression | 17.85      | 17.82     |
| Decision Tree     | 16.80      | 18.13     |
| Random Forest     | 12.05      | 17.68     |
| Extra Trees       | 11.54      | 17.31     |

**Insight:**  
Tree‑based models outperform Linear Regression, with **Extra Trees** and **Random Forest** delivering the strongest results.

---

## 📈 Visuals in the Notebook

### **Feature Importance**  
Random Forest and Extra Trees modules include built‑in feature importance extraction.

### **Actual vs Predicted**  
The notebook overlays predictions from all models to compare performance visually.

---

## 🚀 Usage

### **Run the Analysis Notebook**  
Located in:

```
notebooks/analysis/
```

It demonstrates:

- dataset creation  
- model training  
- tuning  
- evaluation  
- visualization  

### **Using the Modular Code in Scripts**  
Each model family exposes:

- `train_*`  
- `predict_*`  
- `evaluate_*`  
- `optimize_*` (where applicable)  

This makes experimentation and extension straightforward.

---

## 🧱 Adding a New Model (High‑Level Guide)

To add a new model family:

1. Create a new subpackage under `src/` (e.g., `xgboost/`)  
2. Add:  
   - `parameter_opt.py` (optional)  
   - `train_model.py`  
   - `predict_model.py`  
   - `evaluate_model.py`  
3. Follow the same function signatures as existing models  
4. Import and run in the notebook or scripts  

This keeps the architecture consistent and scalable.

---

## 🙏 Acknowledgment 

Some modeling concepts — particularly around rolling‑window forecasting and tree‑based model evaluation — were inspired by  
**_Data Science for Supply Chain Forecasting_ by Nicolas Vandeput**.  
The implementation, modular structure, and extensions in this repository are my own.

---

## 🏁 Key Takeaways

- Tree‑based models outperform Linear Regression for this forecasting task  
- Extra Trees provides the best overall accuracy  
- Feature importance reveals which historical months matter most  
- The modular design makes the framework easy to extend and reuse  
- The notebook provides a clear, reproducible workflow for analysis

---

## 📐 Project Architecture

For a high‑level overview of how the data, models, and modules interact, see:

➡️ **[ARCHITECTURE.md](ARCHITECTURE.md)**

