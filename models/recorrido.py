from dataclasses import field
from email.policy import default
from token import OP
from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re
from datetime import datetime

class Recorrido(BaseModel):
    ID: Optional[int] = Field(
        default=None,
        description="Id autoinvrementable de la ruta"
    )

    ID_Bus: Optional[int] = Field(
        default=None,
        description="ID del Bus"
    )

    placa_bus: Optional[str] = Field(
        default=None,
        description="Placa del Bus"
    )

    modelo_bus: Optional[str]= Field(
        default=None,
        description="Modelo de Bus"
    )

    capacidad_bus: Optional[int]= Field(
        default=None,
        description="Capacidad del Bus"
    )

    ID_Ruta: Optional[int]= Field(
        default=None,
        description="ID de la ruta"
    )

    origen: Optional[str]= Field(
        default=None,
        description="Origen de la Ruta"
    )

    destino: Optional[str]= Field(
        default=None,
        description="destino de la ruta"
    )

    ID_Conductor: Optional[int]=Field(
        default=None,
        description="ID del conductor"
    )

    nombre_conductor: Optional[str]= Field(
        default=None,
        description="Nombre del Conductor"
    )

    licencia_conductor: Optional[int]=Field(
        default=None,
        description="Numero de Licencia del conductor"
    )

    fecha_inicio: Optional[datetime]=Field(
        default=None,
        description="fecha en la que se inicio el recorrido"
    )

    fecha_fin: Optional[datetime]=Field(
        default=None,
        description="fecha final del recorrido"
    )





