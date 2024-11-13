from fastapi import APIRouter, HTTPException, Body, Query
from models.entidad2_schema import entidad2Schema
import item_logic.entidad2 as entidad2_logic
from typing import Optional

router = APIRouter()

@router.post("/")
async def add_entidad1(entidad2: entidad2Schema = Body(...)):
    try:
        result = await entidad2_logic.add(entidad2.model_dump())
        return result
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed") 
    
@router.get("/")
async def get_entidad1s():
    try:
        filter = {}
        result = await entidad2_logic.get_all(filter)
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve events") 
    
@router.get("/{id}")    
async def get_entidad1(id: str):
    try:
        result = await entidad2_logic.get(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve event") 
    
@router.delete("/{id}")
async def delete_entidad1(id:str):
    try:
        result = await entidad2_logic.delete(id)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete event") 
    
@router.put("/{id}")
async def update_entidad2(id: str, entidad2: entidad2Schema = Body(...)):
    try:
        result = await entidad2_logic.update(id,entidad2.model_dump())
        return result
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update event") 