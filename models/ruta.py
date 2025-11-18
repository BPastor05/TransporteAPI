from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class ruta(BaseModel):
    ID: Optional[int] = Field(
        default=None,
        description="ID autoincrementable de la Ruta"
    )

    origen: Optional[str] = Field(
        pattern=r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' -]+$",
        default=None,
        description="Origen de la Ruta"
    )

    destino: Optional[str] = Field(
        pattern=r"^[A-Za-zÁÉÍÓÚÜÑáéíóúüñ' -]+$",
        default=None,
        description="Destino de la ruta"
    )