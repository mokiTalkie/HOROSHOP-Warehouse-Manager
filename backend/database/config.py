import os
from motor.motor_asyncio import AsyncIOMotorClient

from dotenv import load_dotenv

load_dotenv()

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_CONNECTION_STRING = os.getenv("DB_CONNECTION_STRING").replace(
    "<db_password>", DB_PASSWORD
)

DB_CLIENT = AsyncIOMotorClient(DB_CONNECTION_STRING)[f"{os.getenv("DB_NAME")}"]
