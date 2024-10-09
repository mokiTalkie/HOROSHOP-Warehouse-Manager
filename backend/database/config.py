import os
from pymongo import MongoClient

from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING").replace(
    "<db_password>", DB_PASSWORD
)

DB_CLIENT = MongoClient(DB_CONNECTION_STRING)[DB_NAME]
