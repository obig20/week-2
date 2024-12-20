import pandas as pd
from scripts.utils import load_data, check_missing_values

def preprocess_data(file_path):
    """Load and preprocess the data"""
    df = load_data(file_path)
    
    missing_values = check_missing_values(df)
    print(f"Missing Values:\n{missing_values}")
    df.dropna(subset=['Handset Name'], inplace=True)
    
    return df


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns

if __name__ == "__main__":
    df = load_data('data/your_large_dataset.csv')
    selected_columns = select_columns(df, ['Column1', 'Column2'])
    print(selected_columns)
