from fastapi import APIRouter, HTTPException, Request, status
from models.recorrido import Recorrido
from controllers.recorrido import(
update_recorrido,
create_recorrido,
get_all,
get_one,
delete_recorrido
)


router = APIRouter(prefix="/recorrido")


@router.post( "/" , tags=["Recorrido"], status_code=status.HTTP_201_CREATED )
async def create_new_recorrido(recorrido_data: Recorrido):
    result = await create_recorrido(recorrido_data)
    return result

@router.get("/{id}", tags=["Recorrido"], status_code=status.HTTP_200_OK)
async def get_one_recorrido( id: int ):
    result: Recorrido =  await get_one(id)
    return result

@router.get( "/" , tags=["Recorrido"], status_code=status.HTTP_200_OK )
async def get_all_recorrido():
    result = await get_all()
    return result

@router.put("/{ID}", tags=["Recorrido"], status_code=status.HTTP_201_CREATED)
async def update_recorrido_information( recorrido_data: Recorrido , id: int ):
    recorrido_data.ID = id
    result = await update_recorrido(recorrido_data)
    return result

@router.delete("/{id}", tags=["Recorrido"], status_code=status.HTTP_204_NO_CONTENT)
async def delete_recorrido_data( id: int ):
    status: str =  await delete_recorrido(id)
    return status

