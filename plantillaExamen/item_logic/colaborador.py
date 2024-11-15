from item_logic.crud_inheritance.colaborador_crud import COLABORADORCRUD

crud = COLABORADORCRUD()

async def add(entidad1):
    result = await crud.create_item(entidad1)
    return result

async def get_all(filter):
    if len(filter)==0:
        result = await crud.get_collection()
    else: 
        result = await crud.get_by_filter(filter)
    return result

async def get(email: str):
    result = await crud.get_id(email)
    return result
    
async def delete(email:str):
    result = await crud.delete_id(email)
    return result

async def update(email: str, data: dict):
    result = await crud.update_id(email, data)
    return result

async def get_habilidades(email:str):
    result = await crud.get_habilidades(email)
    return result

async def add_habilidad(email:str, habilidad:str):
    result = await crud.add_habilidad(email,habilidad)
    return result

async def delete_habilidad(email:str, habilidad:str):
    result = await crud.delete_habilidad(email,habilidad)
    return result

async def get_colaboradoresUsuario(email:str):
    result = await crud.get_colaboradoresUsuario(email)
    return result