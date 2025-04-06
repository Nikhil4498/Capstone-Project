import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Use environment variable for MongoDB URI
MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["cost_dashboard"]
cost_collection = db["cloud_costs"]
