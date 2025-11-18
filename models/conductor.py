from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class Conductor(BaseModel):
    ID: Optional[int] = Field(
        default=None,
        description="ID del Conductor",
    )

    licencia: Optional[int] = Field(
        default=None,
        description="Número de licencia del conductor",
    )

    nombre: Optional[str] = Field(
        default=None,
        description="Nombre del conductor",
        pattern=r"^[A-Za-z\s]+$",
        examples=["Pedro"]
    )

