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
        self.collection.create_index("email", unique=True)

    async def get_id(self,email: str) -> dict:
        result = await self.collection.find_one({"email": email})
        if result:
            result["_id"] = str(result["_id"])
            return result
        
    async def delete_id(self,email: str):
        deleted = False
        item = await self.collection.find_one({"email": email})
        if item:
            await self.collection.delete_one({"email": email})
            deleted = True
        return deleted


    async def update_id(self,email: str, data: dict):
        if not data:
            return False
        item = await self.collection.find_one({"email": email})
        if item:
            updatedItem = await self.collection.update_one(
                {"email": email}, {"$set": data}
            )
            return bool(updatedItem)