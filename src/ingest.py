import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """
    Safely loads raw reporting data into a pandas DataFrame.
    Automatically detects if it's a CSV or Excel file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CRITICAL ERROR: Cannot find data file at {filepath}")

    print(f"Loading data from {filepath}...")
    
    # Handle both common data formats
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith(('.xls', '.xlsx')):
        df = pd.read_excel(filepath)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
    
    # Strip whitespace from column names to prevent future headaches
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    return df