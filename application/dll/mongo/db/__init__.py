from pymongo import MongoClient

client = MongoClient('mongodb://root:HelloThere@localhost:27077')
db = client.RipAndShipDB
