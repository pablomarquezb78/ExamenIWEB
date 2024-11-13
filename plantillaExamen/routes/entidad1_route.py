from fastapi import APIRouter, HTTPException, Body, Query
from models.entidad1_schema import entidad1Schema
import item_logic.entidad1 as entidad1_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_entidad1(entidad1: entidad1Schema = Body(...)):
    try:
        result = await entidad1_logic.add(entidad1.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed") 
    
@router.get("/")
async def get_entidad1s():
    try:
        filter = {}
        result = await entidad1_logic.get_all(filter)
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve events") 
    
@router.get("/{id}")    
async def get_entidad1(id: str):
    try:
        result = await entidad1_logic.get(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve event") 
    
@router.delete("/{id}")
async def delete_entidad1(id:str):
    try:
        result = await entidad1_logic.delete(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete event") 
    
@router.put("/{id}")
async def update_entidad1(id: str, entidad1: entidad1Schema = Body(...)):
    try:
        result = await entidad1_logic.update(id,entidad1.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update event") 