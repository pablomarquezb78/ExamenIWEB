from item_logic.crud_inheritance.entidad2_crud import ENTIDAD2CRUD

crud = ENTIDAD2CRUD()

async def add(entidad2):
    result = await crud.create_item(entidad2)
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