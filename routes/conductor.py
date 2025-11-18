from fastapi import APIRouter, HTTPException, Request, status
from models.conductor import Conductor
from controllers.conductor import (
    create_conductor,
    delete_conductor,
    get_all,
    get_all_recorrido_conductor,
    get_one,
    update_conductor,
    
    get_one_recorrido_conductor
    )

router = APIRouter(prefix="/conductor")

@router.post( "/" , tags=["Conductor"], status_code=status.HTTP_201_CREATED )
async def create_new_conductor(conductor_data: Conductor):
    result = await create_conductor(conductor_data)
    return result

@router.put("/{id}", tags=["Conductor"], status_code=status.HTTP_201_CREATED)
async def update_conductor_information( conductor_data: Conductor , id: int ):
    conductor_data.ID = id
    result = await update_conductor(conductor_data)
    return result


@router.delete("/{id}", tags=["Conductor"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_conductor_data( id: int ):
    status: str =  await delete_conductor(id)
    return status

@router.get("/{id}", tags=["Conductor"], status_code=status.HTTP_200_OK)
async def get_one_conductor( id: int ):
    result: Conductor =  await get_one(id)
    return result

@router.get( "/" , tags=["Conductor"], status_code=status.HTTP_200_OK )
async def get_all_conductor():
    result = await get_all()
    return result

@router.get("/{id}/recorrido", tags=["Conductor"], status_code=status.HTTP_200_OK)
async def get_all_recorrido_of_bus( id: int ):
    result = await get_all_recorrido_conductor(id)
    return result

@router.get("/{id}/recorrido/{recorrido_ID}", tags=["Conductor"], status_code=status.HTTP_200_OK)
async def get_one_recorrido_of_conductor( id: int, recorrido_id: int ):
    result = await get_one_recorrido_conductor(id, recorrido_id)
    return result