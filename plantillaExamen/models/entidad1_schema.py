from pydantic import BaseModel, Field, field_validator
from typing import List, Literal
from datetime import datetime

class entidad1Schema(BaseModel):
    email: str = Field(..., description="Dirección de email del usuario")
    nombre: str = Field(..., description="Nombre del usuario")
    contactos: List[str] = Field(default_factory=list, description="Lista de contactos del usuario")

    model_config = {
        "json_schema_extra" : {
            "example" : 
                {
                    "email": "usuario@example.com",
                    "nombre": "Juan Pérez",
                }
        }
    }

    """
    @field_validator('inicio')
    def validate_inicio(cls, value):
        if value.minute%15!=0:
            raise ValueError('El inicio debe estar en intervalos de 15 minutos')
        return value   
    """