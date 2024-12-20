import pandas as pd

def top_handsets(df, n=10):
    """Identify the top n handsets by customer count"""
    return df.groupby('Handset Name')['Customer Count'].sum().nlargest(n)

def top_manufacturers(df, n=3):
    """Identify the top n handset manufacturers"""
    return df.groupby('Manufacturer')['Customer Count'].sum().nlargest(n)

def top_handsets_per_manufacturer(df, manufacturers, top_n=5):
    """Identify the top n handsets for each manufacturer"""
    top_handsets_by_manufacturer = {}
    for manufacturer in manufacturers:
        manufacturer_data = df[df['Manufacturer'] == manufacturer]
        top_handsets_by_manufacturer[manufacturer] = manufacturer_data.groupby('Handset Name')['Customer Count'].sum().nlargest(top_n)
    return top_handsets_by_manufacturer
