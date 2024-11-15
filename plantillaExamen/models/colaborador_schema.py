from pydantic import BaseModel, Field, field_validator
from typing import List, Literal
from datetime import datetime

class colaboradorSchema(BaseModel):
    email: str = Field(..., description="Dirección de email del colaborador")
    nombre: str = Field(..., description="Nombre del usuario")
    habilidades: List[str] = Field(default_factory=list, description="Habilidades adecuadas para participar en la tarea")
    tareas: List[str] = Field(default_factory=list, description="Tareas en las que ha participado el usuario")

    model_config = {
        "json_schema_extra" : {
            "example" : 
                {
                    "email": "usuario@example.com",
                    "nombre": "Juan Pérez",
                    "habilidades": ["Python", "Django"]
                }
        }
    }