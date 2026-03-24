"""
dataset_creation.py
-------------------

This module handles data import, cleaning, pivoting, and rolling‑window dataset
generation for the LinearBenchTreeSuite forecasting pipeline.

It provides:
- `import_data()`: Loads and pivots the processed car sales dataset.
- `datasets()`: Creates supervised learning windows for model training/testing.
- `main()`: Convenience function to generate df, X_train, Y_train, X_test, Y_test.

The output of this module forms the foundation for all downstream ML models.
"""

from __future__ import annotations

import pandas as pd
import numpy as np
from typing import Tuple

from dataprocessing.data_loader_processed import load_raw_csv


def import_data() -> pd.DataFrame:
    """
    Load, clean, and pivot the processed car sales dataset.

    This function:
    - Loads the raw CSV using `load_raw_csv()`
    - Combines Year and Month into a single "Period" column
    - Formats the period as YYYY-MM
    - Pivots the dataset so:
        * Rows   = car manufacturers (Make)
        * Columns = monthly periods
        * Values  = units sold (Quantity)
    - Exports the pivoted dataset to an Excel file for reference

    Returns
    -------
    pd.DataFrame
        Pivoted dataset with manufacturers as rows and monthly periods as columns.
    """
    data: pd.DataFrame = load_raw_csv()

    # Create a standardized YYYY-MM period column
    data["Period"] = (
        data["Year"].astype(str) + "-" + data["Month"].astype(str)
    )
    data["Period"] = pd.to_datetime(data["Period"]).dt.strftime("%Y-%m")

    # Pivot the dataset
    df: pd.DataFrame = pd.pivot_table(
        data=data,
        values="Quantity",
        index="Make",
        columns="Period",
        aggfunc="sum",
        fill_value=0,
    )

    # Export for validation/debugging
    df.to_excel("LBTS_Clean_Demand.xlsx")

    return df


def datasets(
    df: pd.DataFrame,
    x_len: int = 12,
    y_len: int = 1,
    y_test_len: int = 12
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Create rolling-window training and test datasets for supervised learning.

    Parameters
    ----------
    df : pd.DataFrame
        Pivoted dataset where rows are manufacturers and columns are monthly periods.
    x_len : int, default=12
        Number of past months used as input features.
    y_len : int, default=1
        Number of future months to predict.
    y_test_len : int, default=12
        Number of months reserved for the final test set.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]
        X_train, Y_train, X_test, Y_test arrays.

    Notes
    -----
    - Uses a sliding window across all available months.
    - Ensures no data leakage by reserving the final `y_test_len` months for testing.
    - If predicting a single month (`y_len == 1`), the target arrays are flattened.
    """
    D: np.ndarray = df.values
    periods: int = D.shape[1]

    # Training windows
    loops: int = periods + 1 - x_len - y_len - y_test_len
    train: list[np.ndarray] = [
        D[:, col : col + x_len + y_len] for col in range(loops)
    ]
    train_arr: np.ndarray = np.vstack(train)
    X_train, Y_train = np.split(train_arr, [x_len], axis=1)

    # Test windows
    max_col_test: int = periods + 1 - x_len - y_len
    test: list[np.ndarray] = [
        D[:, col : col + x_len + y_len] for col in range(loops, max_col_test)
    ]
    test_arr: np.ndarray = np.vstack(test)
    X_test, Y_test = np.split(test_arr, [x_len], axis=1)

    # Flatten if predicting a single period
    if y_len == 1:
        Y_train = Y_train.ravel()
        Y_test = Y_test.ravel()

    return X_train, Y_train, X_test, Y_test


def main() -> Tuple[pd.DataFrame, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Convenience function to load data and generate training/testing datasets.

    Returns
    -------
    Tuple containing:
        df       : pd.DataFrame
        X_train  : np.ndarray
        Y_train  : np.ndarray
        X_test   : np.ndarray
        Y_test   : np.ndarray
    """
    df = import_data()
    X_train, Y_train, X_test, Y_test = datasets(df)
    return df, X_train, Y_train, X_test, Y_test


# ---------------------------------------------------------------------------
# The block below ensures that `main()` only runs when this file is executed
# directly (e.g., `python dataset_creation.py`) and NOT when the module is
# imported elsewhere in the project.
#
# This prevents unintended side effects — such as automatically loading data
# or generating datasets — when other modules import functions from here.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()