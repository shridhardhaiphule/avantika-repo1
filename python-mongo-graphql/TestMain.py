from EnvConstants import EnvConstants

env = EnvConstants.load_env()

print("MONGO_CONNECTION_URL:", env["MONGO_CONNECTION_URL"])
print("MONGO_DB_NAME:", env["MONGO_DB_NAME"])
print("MONGO_COLLECTION_EMPLOYEES:", env["MONGO_COLLECTION_EMPLOYEES"])

from pymongo import MongoClient

client = MongoClient(env["MONGO_CONNECTION_URL"])
db = client[env["MONGO_DB_NAME"]]
collection = db[env["MONGO_COLLECTION_EMPLOYEES"]]

print("✅ Connected to test collection:", collection.name)
