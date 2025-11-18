from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re

class Bus(BaseModel):
   ID: Optional[int]= Field(
      default=None,
      description="ID autoincrementable para el bus"
   )

   placa: Optional[str] = Field(
      default=None,
      description="Placa del bus",
      examples=["ABC123", "56ABD00"]
   )

   modelo: Optional[str] = Field(
      default=None,
      description="Modelo del bus",
      pattern=r"^[A-Za-z0-9\s\-]+$",
      examples=["Nissan Urban", "Discovery"]
   )

   capacidad: Optional[int] = Field(
      default=None,
      description="Capacidad del bus"
   )