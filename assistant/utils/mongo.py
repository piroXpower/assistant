from pymongo import MongoClient
from assistant.conf import MOMGO_DB_URI

# DB
client = MongoClient(MONGO_DB_URI)
db = client["blaze"]

x_users = db.x_users

# Add chat to DB
print("LOADED DATABASE SUCCESSFULLY ") 
