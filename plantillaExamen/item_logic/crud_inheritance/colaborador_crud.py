from bson import ObjectId
from database import MONGOCRUD
import motor.motor_asyncio
import os
from dotenv import load_dotenv

import item_logic.tarea as tarea_logic

load_dotenv(dotenv_path='.env')

MONGO_DETAILS = os.getenv("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Examen 

class COLABORADORCRUD(MONGOCRUD):
    def __init__(self):
        super().__init__('Colaboradores')
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
        
    async def get_habilidades(self,email: str):
        result = await self.collection.find_one({"email": email})
        if result:
            return result['habilidades']

    async def add_habilidad(self,email: str, habilidad: str):
        colaborador = await self.collection.find_one({"email": email})
        if not colaborador:
            return False
        else:
            updatedItem = await self.collection.update_one(
                {"email": email},
                {
                "$push": {"habilidades": habilidad}
                }
            )
            return bool(updatedItem)
        
    async def delete_habilidad(self,email: str, habilidad: str):
        colaborador = await self.collection.find_one({"email": email})
        if not colaborador:
            return False
        else:
            updatedItem = await self.collection.update_one(
                {"email": email},
                {
                "$pull": {"habilidades": habilidad}
                }
            )
            return bool(updatedItem)
        
    async def get_colaboradoresUsuario(self, email: str):
        result = await self.collection.find_one({"email": email})
        tareas = await tarea_logic.get_all(filter={"responsable": email})

        if result and tareas:
            emailColaboradores = set() 

            for tarea in tareas:
                for colaborador in tarea['colaboradores']:
                    emailColaboradores.add(colaborador)

            return list(emailColaboradores)  

        return [] 