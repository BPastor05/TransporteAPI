from fastapi import APIRouter, HTTPException, Request, status
from models.ruta import ruta
from controllers.ruta import (
    get_all,
    get_one
    )

router = APIRouter(prefix="/ruta")

@router.get("/{id}", tags=["Ruta"], status_code=status.HTTP_200_OK)
async def get_one_ruta( id: int ):
    result: ruta =  await get_one(id)
    return result

@router.get( "/" , tags=["Ruta"], status_code=status.HTTP_200_OK )
async def get_all_ruta():
    result = await get_all()
    return result