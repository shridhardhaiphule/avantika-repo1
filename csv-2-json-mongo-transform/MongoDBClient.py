from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, db_name="stock_db"):
        self.client = MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]

    def insert_many(self, collection_name, data):
        collection = self.db[collection_name]
        collection.insert_many(data)
        print(f"✅ Inserted {len(data)} records into MongoDB collection '{collection_name}'")

    def close(self):
        self.client.close()