from bson import ObjectId
from database import MONGOCRUD
import motor.motor_asyncio
import os
from dotenv import load_dotenv
import item_logic.colaborador as colaborador_logic

load_dotenv(dotenv_path='.env')

MONGO_DETAILS = os.getenv("MONGO_URI")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.Examen 

class TAREASCRUD(MONGOCRUD):
    def __init__(self):
        super().__init__('Tareas')

    async def add_colaborador(self,id: str, colaborador: str):
        tarea = await self.get_id(id)
        colaboradorEntity = await colaborador_logic.get(colaborador)

        habilidadesColaborador = colaboradorEntity['habilidades']
        habilidadesTarea = tarea['habilidades']

        comparten_habilidad = any(habilidad in habilidadesColaborador for habilidad in habilidadesTarea)
        puede_agregar_colaborador = len(tarea['colaboradores']) < tarea['segmentos']

        if not (colaborador and tarea and comparten_habilidad and puede_agregar_colaborador):
            return False
        else:
            updatedItem = await self.collection.update_one(
                {"_id": ObjectId(id)},
                {"$addToSet": {"colaboradores": colaborador}}
            )
            return bool(updatedItem)
        
    async def get_candidatos(self, id: str):
        tarea = await self.get_id(id)
        colaboradores = await colaborador_logic.get_all(filter={})

        if not tarea:
            raise ValueError("Tarea not found")

        habilidadesTarea = set(tarea['habilidades'])
        candidatos = []

        for colaborador in colaboradores:
            habilidadesColaborador = set(colaborador['habilidades'])
            if habilidadesTarea & habilidadesColaborador:
                candidatos.append(colaborador['email'])

        return candidatos