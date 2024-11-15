from fastapi import APIRouter, HTTPException, Body, Query
from models.tarea_schema import tareaSchema
import item_logic.tarea as tarea_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_tarea(tarea: tareaSchema = Body(...)):
    try:
        result = await tarea_logic.add(tarea.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed") 
    
@router.get("/")
async def getAll_tarea(
    habilidad: Optional[str] = Query(None),
    colaborador: Optional[str] = Query(None),
    completamenteAsignada: Optional[bool] = Query(None),
):
    try:
        filter = {}

        if habilidad:
            filter["habilidades"] = {"$in": [habilidad]}

        if colaborador:
            filter["colaboradores"] = {"$in": [colaborador]}

        if completamenteAsignada is not None:
            if completamenteAsignada:
                filter["$expr"] = {"$eq": [{"$size": "$colaboradores"}, "$segmentos"]}

        result = await tarea_logic.get_all(filter)
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve tarea") 
    
@router.get("/{id}")    
async def get_tarea(id: str):
    try:
        result = await tarea_logic.get(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve tarea") 
    
@router.delete("/{id}")
async def delete_tarea(id:str):
    try:
        result = await tarea_logic.delete(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete tarea") 
    
@router.put("/{id}")
async def update_tarea(id: str, tarea: tareaSchema = Body(...)):
    try:
        result = await tarea_logic.update(id,tarea.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update tarea") 
    
@router.post("/{id}/colaboradores")    
async def add_colaborador_tarea(id: str, colaborador: str):
    try:
        result = await tarea_logic.add_colaborador(id,colaborador)
        return result
    except Exception as e:
        print(f"Failed to add colaborador: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to add colaborador")
    
@router.get("/{id}/candidatos")
async def get_candidatos(id:str):
    try:
        result = await tarea_logic.get_candidatos(id)
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve candidatos")