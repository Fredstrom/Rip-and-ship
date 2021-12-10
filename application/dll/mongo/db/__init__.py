from pymongo import MongoClient

client = MongoClient('mongodb://root:HelloThere@localhost:27099')
db = client.RipAndShipDB
