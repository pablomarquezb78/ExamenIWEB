from item_logic.crud_inheritance.tareas_crud import TAREASCRUD

crud = TAREASCRUD()

async def add(tareas):
    result = await crud.create_item(tareas)
    return result

async def get_all(filter):
    if len(filter)==0:
        result = await crud.get_collection()
    else: 
        result = await crud.get_by_filter(filter)
    return result

async def get(id: str):
    result = await crud.get_id(id)
    return result
    
async def delete(id:str):
    result = await crud.delete_id(id)
    return result

async def update(id: str, data: dict):
    result = await crud.update_id(id, data)
    return result

async def add_colaborador(id: str, colaborador: str):
    result = await crud.add_colaborador(id,colaborador)
    return result

async def get_candidatos(id:str):
    result = await crud.get_candidatos(id)
    return result