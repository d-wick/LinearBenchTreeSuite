"""
data_loader_processed.py
------------------------

Utilities for loading processed datasets used by LinearBenchTreeSuite.

This module intentionally resolves data paths relative to the project root,
not the package directory, to keep code and data cleanly separated.
"""

from pathlib import Path
import pandas as pd


def load_raw_csv(filename: str = "new_car_sales_by_make.csv") -> pd.DataFrame:
    """
    Load a processed CSV file from the project-level data directory.

    Parameters
    ----------
    filename : str, default="new_car_sales_by_make.csv"
        Name of the CSV file located under `data/processed/`.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist at the expected location.
    """
    # Resolve project root: src/linearbenchtree/dataprocessing/ -> project root
    project_root = Path(__file__).resolve().parents[3]

    data_path = project_root / "data" / "processed" / filename

    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found: {data_path}")

    return pd.read_csv(data_path)


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