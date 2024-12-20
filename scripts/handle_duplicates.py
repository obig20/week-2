import pandas as pd

def remove_duplicates(df, subset=None):
    df_unique = df.drop_duplicates(subset=subset)
    return df_unique

if __name__ == "__main__":
    df = pd.read_csv('data/your_large_dataset.csv')
    df_unique = remove_duplicates(df)
    print(df_unique)
