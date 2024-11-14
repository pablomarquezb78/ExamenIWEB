from fastapi import APIRouter, HTTPException, Body, Query
from models.entidad1_schema import entidad1Schema
import item_logic.entidad1 as entidad1_logic
from typing import Optional
from pymongo.errors import DuplicateKeyError

router = APIRouter()

@router.post("/")
async def add_user(entidad1: entidad1Schema = Body(...)):
    try:
        result = await entidad1_logic.add(entidad1.model_dump())
        return result
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed") 
    
@router.get("/")
async def get_users():
    try:
        result = await entidad1_logic.get_all()
        return result
    except Exception  as e:
        print(f"Failed to retrieve users: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve users") 
    
@router.get("/{email}")    
async def get_user(email: str):
    try:
        result = await entidad1_logic.get(email)
        return result
    except Exception as e:
        print(f"Failed to retrieve user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve user") 
    
@router.delete("/{email}")
async def delete_user(email:str):
    try:
        result = await entidad1_logic.delete(email)
        return result
    except Exception as e:
        print(f"Failed to delete user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete user") 
    
@router.put("/{email}")
async def update_user(email: str, entidad1: entidad1Schema = Body(...)):
    try:
        result = await entidad1_logic.update(email,entidad1.model_dump())
        return result
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already exists")
    except Exception as e:
        print(f"Failed to update user: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update user") 