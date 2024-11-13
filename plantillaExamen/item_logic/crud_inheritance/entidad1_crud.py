from bson import ObjectId
from database import MONGOCRUD
import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

MONGO_DETAILS = os.getenv("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Examen 

class ENTIDAD1CRUD(MONGOCRUD):
    def __init__(self):
        super().__init__('Entidad1')