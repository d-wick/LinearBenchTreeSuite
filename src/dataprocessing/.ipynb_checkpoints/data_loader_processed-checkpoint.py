"""
data_loader_processed.py
------------------------

This module provides utilities for loading processed datasets used in the
LinearBenchTreeSuite forecasting pipeline.

It dynamically resolves the project root directory, locates the processed data
folder, and exposes a single function:

- `load_raw_csv()`: Loads a processed CSV file from the project's data directory.

A `main()` function is included for quick debugging or validation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional
import pandas as pd

# Dynamically determine project root (assumes this file is in src/dataprocessing/)
ROOT_DIR: Path = Path(__file__).resolve().parents[2]
DATA_DIR: Path = ROOT_DIR / "data" / "processed"


def load_raw_csv(filename: str = "new_car_sales_by_make.csv") -> pd.DataFrame:
    """
    Load a processed CSV file from the project's data/processed directory.

    Parameters
    ----------
    filename : str, default="new_car_sales_by_make.csv"
        Name of the CSV file to load.

    Returns
    -------
    pd.DataFrame
        The loaded dataset as a pandas DataFrame.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist in the processed data directory.
    """
    file_path: Path = DATA_DIR / filename

    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    return pd.read_csv(file_path)


def main() -> pd.DataFrame:
    """
    Convenience function to load and return the default processed dataset.

    Returns
    -------
    pd.DataFrame
        The loaded processed dataset.
    """
    df = load_raw_csv()
    return df


# ---------------------------------------------------------------------------
# The block below ensures that `main()` only runs when this file is executed
# directly (e.g., `python data_loader_processed.py`) and NOT when the module
# is imported elsewhere in the project.
#
# This prevents unintended side effects — such as automatically loading data —
# when other modules import functions from here.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    main()