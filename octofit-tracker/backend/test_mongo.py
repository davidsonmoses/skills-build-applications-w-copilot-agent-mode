from pymongo import MongoClient

try:
    client = MongoClient("mongodb://0.0.0.0:27017/")
    print("MongoDB connection successful!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("Error connecting to MongoDB:", e)