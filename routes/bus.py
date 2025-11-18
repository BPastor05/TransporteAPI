from fastapi import APIRouter, HTTPException, Request, status
from models.bus import Bus
from controllers.bus import (
    create_bus,
    delete_bus,
    get_all,
    get_one,
    get_all_recorrido_bus,
    get_one_recorrido_bus,
    update_bus,
    delete_bus,
    )


router = APIRouter(prefix="/bus")


@router.post( "/" , tags=["Bus"], status_code=status.HTTP_201_CREATED )
async def create_new_bus(bus_data: Bus):
    result = await create_bus(bus_data)
    return result

@router.put("/{ID}", tags=["Bus"], status_code=status.HTTP_201_CREATED)
async def update_bus_information( bus_data: Bus , id: int ):
    bus_data.ID = id
    result = await update_bus(bus_data)
    return result


@router.delete("/{id}", tags=["Bus"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_bus_data( id: int ):
    status: str =  await delete_bus(id)
    return status

@router.get("/{id}", tags=["Bus"], status_code=status.HTTP_200_OK)
async def get_one_bus( id: int ):
    result: Bus =  await get_one(id)
    return result

@router.get( "/" , tags=["Bus"], status_code=status.HTTP_200_OK )
async def get_all_bus():
    result = await get_all()
    return result

@router.get("/{id}/recorrido", tags=["Bus"], status_code=status.HTTP_200_OK)
async def get_all_recorrido_of_bus( id: int ):
    result = await get_all_recorrido_bus(id)
    return result

@router.get("/{id}/recorrido/{recorrido_ID}", tags=["Bus"], status_code=status.HTTP_200_OK)
async def get_one_recorrido_of_bus( id: int, recorrido_id: int ):
    result = await get_one_recorrido_bus(id, recorrido_id)
    return result


