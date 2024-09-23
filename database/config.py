import os
from pymongo.mongo_client import MongoClient

from dotenv import load_dotenv

load_dotenv()


DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING").replace(
    "<db_password>", DB_PASSWORD
)

DB_CLIENT = MongoClient(DB_CONNECTION_STRING)[f"{os.getenv("DB_NAME")}"]

def initialize_database() -> None:
    required_collections = ["Shelves", "Racks", "Reserved", "Service", "Delivered"]
    existing_collections = DB_CLIENT.list_collections()

    for collection in required_collections:
        if collection not in existing_collections:
            DB_CLIENT.create_collection(name=collection)
            
            print("Collection created")

initialize_database()