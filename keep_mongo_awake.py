# keep_mongo_awake.py
from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI")

def ping_mongo():
    try:
        client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        print("✅ MongoDB Atlas pinged successfully.")
    except Exception as e:
        print("❌ Ping failed:", e)

if __name__ == "__main__":
    ping_mongo()
