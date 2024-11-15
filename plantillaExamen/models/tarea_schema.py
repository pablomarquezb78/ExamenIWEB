from pydantic import BaseModel, Field, field_validator
from typing import List, Literal
from datetime import datetime

class tareaSchema(BaseModel):
    responsable: str = Field(..., description="Dirección de email del usuario responsable de la tarea")
    descripcion: str = Field(..., max_length=50, description="Descripción breve de la tarea")
    habilidades: List[str] = Field(default_factory=list, description="Habilidades adecuadas para participar en la tarea")
    segmentos: int = Field(..., description="Duración estimada de la tarea")
    colaboradores: List[str] = Field(default_factory=list, description="Direccion de email de los colaboradores")

    model_config = {
        "json_schema_extra" : {
            "example" : 
                {
                    "responsable": "usuario@example.com",
                    "descripcion": "Tarea de ejemplo",
                    "habilidades": ["Python", "Django"],
                    "segmentos": 1,
                    "colaboradores": ["usuario1@example.com"]
                }
        }
    }

    @field_validator('colaboradores')
    def validate_colaboradores(cls, value, values):
        segmentos = values.data.get('segmentos')
        if segmentos is not None and len(value) > segmentos:
            raise ValueError('El número de colaboradores debe ser igual al número de segmentos')
        return value