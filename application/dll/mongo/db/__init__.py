from pymongo import MongoClient
from application.config.mongodb_config import *

client = MongoClient(f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}')
db = client.RipAndShipDB
