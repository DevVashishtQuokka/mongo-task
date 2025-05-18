from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["news_db"]

tazakhabar_collection = db["tazakhabars"]

