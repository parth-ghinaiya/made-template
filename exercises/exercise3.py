import pandas as pd

# Defining the dataset URL and selected columns
DATASET_URL = 'https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv'
required_cols = [0, 1, 2, 12, 22, 32, 42, 52, 62, 72]

# Column names for the dataset
col_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

# Reading CSV data into a DataFrame with customized parameters
df = pd.read_csv(
    DATASET_URL,
    sep=';',
    encoding="iso-8859-1",
    header=None,
    usecols=required_cols,
    names=col_names,
    skiprows=6,
    skipfooter=4,
    engine='python',
    na_values='.',
    thousands=',',
    dtype={'CIN': str, 'date': str}
)

# Filtering rows where 'petrol' column does not contain '-'
df = df[~df['petrol'].astype(str).str.contains('-')]

# Filtering rows where 'CIN' column has exactly five characters
df = df[df['CIN'].str.len() == 5]

# Converting selected columns to integer data type
int_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
for col in int_columns:
    df[col] = df[col].astype('int64')

# Writing the processed data to an SQLite database named 'cars'
df.to_sql('cars', 'sqlite:///cars.sqlite', if_exists='replace', index=False)
