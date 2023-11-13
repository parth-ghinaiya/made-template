import pandas as pd
from sqlalchemy import create_engine, INTEGER, FLOAT, BIGINT, NVARCHAR

# created a SQLAlchemy engine to connect a db
engine = create_engine('sqlite:///airports.sqlite')

# read csv fro given url
df = pd.read_csv(
    'https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv',
    sep=';')


# defined column types based on sqlalchemy
types = {
    'column_1': BIGINT(),
    'column_2': NVARCHAR(length=512),
    'column_3': NVARCHAR(length=256),
    'column_4': NVARCHAR(length=128),
    'column_5': NVARCHAR(length=16),
    'column_6': NVARCHAR(length=16),
    'column_7': FLOAT(asdecimal=True),
    'column_8': FLOAT(asdecimal=True),
    'column_9': INTEGER(),
    'column_10': FLOAT(asdecimal=True),
    'column_11': NVARCHAR(length=16),
    'column_12': NVARCHAR(length=256),
    'geo_punkt': NVARCHAR(length=512),
}

# Write the dataframe to the SQLite database
df.to_sql("airports", engine, index=False, dtype=types)
