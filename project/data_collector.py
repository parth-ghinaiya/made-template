import pandas as pd
from kaggle.api.kaggle_api_extended import KaggleApi
from sqlalchemy import create_engine, FLOAT, DATE

# defined const related to dataset
DATASET_DICT = {
    "CRUDE_OIL_DATASET": {
        "dataset_path": "sc231997/crude-oil-price",
        "file_name": "crude-oil-price.csv",
        "database_name": "crude_oil_price",
        "sqlalchemy_datatype": {
            'date': DATE(),
            'price': FLOAT(asdecimal=True),
            'percentChange': FLOAT(asdecimal=True),
            'change': FLOAT(asdecimal=True),
        }
    },
    "GOLD_PRICE_DATASET": {
        "dataset_path": "odins0n/monthly-gold-prices",
        "file_name": "1979-2021.csv",
        "database_name": "gold_prices",
        "sqlalchemy_datatype": {
            'Date': DATE(), 'United States(USD)': FLOAT(asdecimal=True),
            'Europe(EUR)': FLOAT(asdecimal=True), 'Japan(JPY)': FLOAT(asdecimal=True),
            'United Kingdom(GBP)': FLOAT(asdecimal=True), 'Canada(CAD)': FLOAT(asdecimal=True),
            'Switzerland(CHF)': FLOAT(asdecimal=True), 'India(INR)': FLOAT(asdecimal=True),
            'China(CNY)': FLOAT(asdecimal=True), 'Turkey(TRY)': FLOAT(asdecimal=True),
            'Saudi Arabia(SAR)': FLOAT(asdecimal=True), 'Indonesia(IDR)': FLOAT(asdecimal=True),
            'United Arab Emirates(AED)': FLOAT(asdecimal=True), 'Thailand(THB)': FLOAT(asdecimal=True),
            'Vietnam(VND)': FLOAT(asdecimal=True), 'Egypt(EGP)': FLOAT(asdecimal=True),
            'South Korean(KRW)': FLOAT(asdecimal=True), 'Australia(AUD)': FLOAT(asdecimal=True),
            'South Africa(ZAR)': FLOAT(asdecimal=True)
        }
    },
}

# Instantiate the Kaggle API
kaggle_api = KaggleApi()

# Authenticate using the API key
kaggle_api.authenticate()

# Download a datasets in current directory and unzip it
for key, val in DATASET_DICT.items():
    kaggle_api.dataset_download_files(val['dataset_path'], path='./', unzip=True)

# Read the CSV file into a Pandas DataFrame
crude_oil_df = pd.read_csv(DATASET_DICT["CRUDE_OIL_DATASET"]["file_name"])
gold_price_df = pd.read_csv(DATASET_DICT["GOLD_PRICE_DATASET"]["file_name"])

# preprocess the crude-oil dataset
crude_oil_df['date'] = pd.to_datetime(crude_oil_df['date']).dt.date

# insert crude oil data into sqlite database
crud_oil_db_engine = create_engine(f"sqlite:///data/{DATASET_DICT['CRUDE_OIL_DATASET']['database_name']}.sqlite")
crude_oil_df.to_sql(DATASET_DICT['CRUDE_OIL_DATASET']['database_name'], crud_oil_db_engine, index=False,
                    if_exists='replace',
                    dtype=DATASET_DICT['CRUDE_OIL_DATASET']['sqlalchemy_datatype'])

# preprocess the crude-oil dataset
gold_price_df['Date'] = pd.to_datetime(gold_price_df['Date'], format='%d-%m-%Y')

# insert gold price data into sqlite database
gold_price_db_engine = create_engine(f"sqlite:///data/{DATASET_DICT['GOLD_PRICE_DATASET']['database_name']}.sqlite")
gold_price_df.to_sql(DATASET_DICT['GOLD_PRICE_DATASET']['database_name'], gold_price_db_engine, index=False,
                     if_exists='replace',
                     dtype=DATASET_DICT['GOLD_PRICE_DATASET']['sqlalchemy_datatype'])
