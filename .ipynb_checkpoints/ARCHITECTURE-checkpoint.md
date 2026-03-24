# 🏗️ LinearBenchTreeSuite — Architecture Diagram

                 ┌────────────────────────────────────────┐
                 │              Data Layer                │
                 └────────────────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────────────────┐
        │                        dataprocessing/                       │
        │--------------------------------------------------------------│
        │ • data_loader_processed.py  → Loads processed CSV            │
        │ • dataset_creation.py       → Builds rolling-window datasets │
        │ • benchmark_linear_regr.py  → Baseline linear regression     │
        └──────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────────────────┐
        │                     Modeling Layer (src/)                    │
        └──────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
     ┌────────────────────────────────────────────────────────────────────────┐
     │                         Model Family Modules                           │
     │------------------------------------------------------------------------│
     │  decisiontree/                                                         │
     │     • regression_tree.py      → Train / predict / evaluate             │
     │     • parameter_opt.py        → Hyperparameter tuning                  │
     │                                                                        │
     │  randomforest/                                                         │
     │     • random_forest.py        → Train / predict / evaluate / tune      │
     │                                                                        │
     │  exrandomtree/                                                         │
     │     • ex_random_tree.py       → Train / predict / evaluate / tune      │
     └────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────────────────┐
        │                    Evaluation & Comparison                   │
        │--------------------------------------------------------------│
        │ • Unified MAE% metric across all models                      │
        │ • Feature importance (RF / ExtraTrees)                       │
        │ • Train/test performance comparison                          │
        └──────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────────────────┐
        │                     Notebook Layer (analysis/)               │
        │--------------------------------------------------------------│
        │ • End-to-end workflow demonstration                          │
        │ • Visualizations (feature importance, predictions)           │
        │ • Model comparison tables                                    │
        └──────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
        ┌──────────────────────────────────────────────────────────────┐
        │                     User / Developer Layer                   │
        │--------------------------------------------------------------│
        │ • Run notebooks                                              │
        │ • Import modules for experiments                             │
        │ • Extend framework with new models                           │
        └──────────────────────────────────────────────────────────────┘