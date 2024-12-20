import pandas as pd

def load_data(file_path):
    """Load dataset from CSV"""
    return pd.read_csv(file_path)

def check_missing_values(df):
    """Check for missing values in the dataframe"""
    return df.isnull().sum()
