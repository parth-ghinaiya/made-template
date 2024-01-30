import zipfile
from urllib.request import urlretrieve
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

# defined constants for the zip file, the extracted file and the columns we want to use
ZIP_FILE_URL = "https://gtfs.rhoenenergie-bus.de/GTFS.zip"
ZIP_FILE_PATH = "GTFS.zip"
EXTRACTED_FILE_NAME = "stops.txt"
REQUIRED_COLUMNS = ["stop_id", "stop_name", "stop_lat", "stop_lon", "zone_id"]

# retrieve zip file
urlretrieve(ZIP_FILE_URL, ZIP_FILE_PATH)
with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
    zip_ref.extract(EXTRACTED_FILE_NAME)

# reshape data
df = pd.read_csv(EXTRACTED_FILE_NAME, usecols=REQUIRED_COLUMNS)

# filter data for zone_id 2001
df = df[df["zone_id"] == 2001]

# Text validation for stop_name
df["stop_name"] = df["stop_name"].astype(str)

# Geographic coordinates validation for stop_lat and stop_lon
valid_lat_range = (df["stop_lat"] >= -90) & (df["stop_lat"] <= 90)
valid_lon_range = (df["stop_lon"] >= -90) & (df["stop_lon"] <= 90)
df = df[valid_lat_range & valid_lon_range]

# create sqlite database and table
engine = create_engine('sqlite:///gtfs.sqlite')
metadata = MetaData()
stops_table = Table('stops', metadata,
                    Column('stop_id', Integer, primary_key=True),
                    Column('stop_name', String),
                    Column('stop_lat', Float),
                    Column('stop_lon', Float),
                    Column('zone_id', Integer))

metadata.create_all(engine)

df.to_sql('stops', con=engine, if_exists='replace', index=False,
          dtype={
                    'stop_id': Integer,
                    'stop_name': String,
                    'stop_lat': Float,
                    'stop_lon': Float,
                    'zone_id': Integer
                }
          )
