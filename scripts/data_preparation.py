import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def select_columns(df, columns):
    selected_columns = df[columns]
    return selected_columns

if __name__ == "__main__":
    df = load_data('data/telecom_analysis.csv')
    selected_columns = select_columns(df, ['Column1', 'Column2'])
    print(selected_columns)
