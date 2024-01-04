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


def authenticate_kaggle():
    """
    authenticate kaggle
    api credentials are stored in os env
    :return:
    """
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()

    return kaggle_api


def download_dataset(kaggle_api):
    """
    Download a datasets in current directory and unzip it
    :param kaggle_api:
    :return:
    """
    for key, val in DATASET_DICT.items():
        kaggle_api.dataset_download_files(val['dataset_path'], path='./', unzip=True)

    return


def get_and_preprocess_crude_oil_dataframe():
    """
    create crude oil dataframe and preprocess it from csv
    :param:
    :return:
    """
    # create crude oil dataframe from csv
    crude_oil_df = pd.read_csv(DATASET_DICT["CRUDE_OIL_DATASET"]["file_name"])

    # preprocess the crude-oil dataset
    crude_oil_df['date'] = pd.to_datetime(crude_oil_df['date']).dt.date

    return crude_oil_df


def get_and_preprocess_gold_price_dataframe():
    """
    create gold price dataframe and preprocess it from csv
    :param:
    :return:
    """
    # create crude oil dataframe from csv
    gold_price_df = pd.read_csv(DATASET_DICT["GOLD_PRICE_DATASET"]["file_name"])

    # preprocess the crude-oil dataset
    gold_price_df['Date'] = pd.to_datetime(gold_price_df['Date'], format='%d-%m-%Y')

    return gold_price_df


def dump_dataset_to_db(dataframe, db_name, datatype):
    """
    insert data into sqlite database
    :param dataframe:
    :param db_name:
    :param datatype:
    :return:
    """

    db_engine = create_engine(f"sqlite:///../data/{db_name}.sqlite")
    dataframe.to_sql(db_name, db_engine, index=False, if_exists='replace', dtype=datatype)
    return


def data_collector():
    """
    collect data from kaggle and store it into local sqlite database with appropriate datatype
    :return:
    """
    kaggle_api = authenticate_kaggle()

    # download dataset in local storage
    download_dataset(kaggle_api)

    # create crude oil dataframe from csv
    crude_oil_df = get_and_preprocess_crude_oil_dataframe()

    # create crude oil dataframe from csv
    gold_price_df = get_and_preprocess_gold_price_dataframe()

    # insert crude oil data into sqlite database
    dump_dataset_to_db(dataframe=crude_oil_df, db_name=DATASET_DICT['CRUDE_OIL_DATASET']['database_name'],
                       datatype=DATASET_DICT['CRUDE_OIL_DATASET']['sqlalchemy_datatype'])

    # insert gold price data into sqlite database
    dump_dataset_to_db(dataframe=gold_price_df, db_name=DATASET_DICT['GOLD_PRICE_DATASET']['database_name'],
                       datatype=DATASET_DICT['GOLD_PRICE_DATASET']['sqlalchemy_datatype'])

    return


if __name__ == "__main__":
    data_collector()
