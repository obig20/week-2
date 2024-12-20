import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__),'scriptis'))
from scripts.data_preparation import load_data, select_columns
from scripts.utils import load_data,check_missing_values
from scripts.handle_duplicates import remove_duplicates
from scripts.data_analysis import top_handsets,top_manufacturers,top_handsets_per_manufacturer
from scripts.data_preprocessing import preprocess_data,load_data

# Load data
df = load_data('data/telecom_analysis.csv')

# Select specific columns
selected_columns = select_columns(df, ['Column1', 'Column2'])
print("Selected Columns:\n", selected_columns)
# Remove duplicates
df_unique = remove_duplicates(df)
print("Data without duplicates:\n", df_unique)

