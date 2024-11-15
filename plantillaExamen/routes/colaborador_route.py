from fastapi import APIRouter, HTTPException, Body, Query
from models.colaborador_schema import colaboradorSchema
import item_logic.colaborador as colaborador_logic
from typing import Optional
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.post("/")
async def add_colaborador(entidad1: colaboradorSchema = Body(...)):
    try:
        result = await colaborador_logic.add(entidad1.model_dump())
        return result
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed") 
    
@router.get("/")
async def getAll_colaborador():
    try:
        filter = {}
        result = await colaborador_logic.get_all(filter)
        return result
    except Exception  as e:
        print(f"Failed to retrieve colaboradors: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve colaboradors") 
    
@router.get("/{email}")    
async def get_colaborador(email: str):
    try:
        result = await colaborador_logic.get(email)
        return result
    except Exception as e:
        print(f"Failed to retrieve colaborador: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve colaborador") 
    
@router.delete("/{email}")
async def delete_colaborador(email:str):
    try:
        result = await colaborador_logic.delete(email)
        return result
    except Exception as e:
        print(f"Failed to delete colaborador: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete colaborador") 
    
@router.get("/{email}/habilidades")    
async def get_habilidades_colaborador(email: str):
    try:
        result = await colaborador_logic.get_habilidades(email)
        return result
    except Exception as e:
        print(f"Failed to retrieve habilidades: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve habilidades") 
    
@router.post("/{email}/habilidades")    
async def add_habilidad_colaborador(email: str, habilidad: str):
    try:
        result = await colaborador_logic.add_habilidad(email,habilidad)
        return result
    except Exception as e:
        print(f"Failed to add habilidad: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to add habilidad")

@router.delete("/{email}/habilidades")    
async def delete_habilidad_colaborador(email: str, habilidad: str):
    try:
        result = await colaborador_logic.delete_habilidad(email,habilidad)
        return result
    except Exception as e:
        print(f"Failed to delete habilidad: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete habilidad")  
    
@router.get("/{id}/get_colaboradoresUsuario")
async def get_colaboradoresUsuario(email:str):
    try:
        result = await colaborador_logic.get_colaboradoresUsuario(email)
        return result
    except Exception  as e:
        print(f"Failed to retrieve colaboradores of Usuario: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve colaboradores of Usuario")  
