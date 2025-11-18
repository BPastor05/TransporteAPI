import json
import logging

from fastapi import HTTPException

from models.conductor import Conductor
from Utils.database import execute_query_json
from models.recorrido import Recorrido



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def get_one( id: int ) -> Conductor:

    selectscript = """
       SELECT TOP 
        [ID],
        [licencia],
        [nombre]
        FROM [transporte].[Conductor]
        WHERE ID = ?
    """

    params = [id]
    result_dict=[]
    try:
        result = await execute_query_json(selectscript, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            raise HTTPException(status_code=404, detail=f"Conductor not found")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")
    
async def get_all() -> list[Conductor]:

    selectscript = """
       SELECT 
        [ID],
        [licencia],
        [nombre]
        FROM [transporte].[Conductor]
    """
    result_dict=[]
    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

async def delete_conductor( id: int ) -> str:

    deletescript = """
        DELETE FROM [transporte].[conductor]
        WHERE [ID] = ?;
    """

    params = [id];

    try:
        await execute_query_json(deletescript, params=params, needs_commit=True)
        return "DELETED"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

async def update_conductor( conductor :Conductor ) -> Conductor:

    dict = conductor.model_dump(exclude_none=True)

    keys = [ k for k in  dict.keys() ]
    keys.remove('ID')
    variables = " = ?, ".join(keys)+" = ?"

    updatescript = f"""
        UPDATE [transporte].[Conductor]
        SET {variables}
        WHERE [ID] = ?;
    """

    params = [ dict[v] for v in keys ]
    params.append( conductor.ID )

    update_result = None
    try:
        update_result = await execute_query_json( updatescript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    sqlfind: str = """
       SELECT 
        [ID],
        [licencia],
        [nombre]
        FROM [transporte].[Conductor]
        WHERE ID = ?
    """

    params = [conductor.ID]

    result_dict=[]
    try:
        result = await execute_query_json(sqlfind, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")


async def create_conductor(conductor: Conductor) -> Conductor:
    sqlscrip = """  
    INSERT INTO [transporte].[Conductor](
            [ID],
            [licencia],
            [nombre]
    )VALUES(
            ?,
            ?,
            ?
    );
    """
    params = [
        conductor.ID,
        conductor.licencia,
        conductor.nombre
    ]


    try:
        insert_result = await execute_query_json(sqlscrip, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")

    sqlfind: str = """
        SELECT 
        [ID],
        [licencia],
        [nombre]
        FROM [transporte].[Conductor]
        WHERE ID = ?
    """
    params = [conductor.ID]

    result_dict=[]
    try:
        result = await execute_query_json(sqlfind, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    

async def get_one_recorrido_conductor( conductor_ID: int, recorrido_ID: int ) -> Recorrido:
    selectscript = """
      SELECT
            r.ID,
            b.ID as ID_Bus,
            b.placa as placa_bus,
            b.modelo as modelo_bus,
            b.capacidad as capacidad_bus,
            ru.ID as ID_Ruta,
            ru.origen,
            ru.destino,
            c.ID as ID_Conductor,
            c.nombre as nombre_conductor,
            c.licencia as licencia_conductor,
            r.fecha_inicio,
            r.fecha_fin
            FROM transporte.recorrido as r
            INNER JOIN transporte.Bus as b
            on r.ID_Bus = b.ID
            INNER JOIN transporte.Conductor as c
            on r.ID_Conductor = c.ID
            INNER JOIN transporte.Ruta as ru
            on r.ID_Ruta=ru.ID
        WHERE b.ID = ?
        and c.ID =?;
    """

    params = [conductor_ID, recorrido_ID]
    result_dict=[]
    try:
        result = await execute_query_json(selectscript, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict[0]
        else:
            raise HTTPException(status_code=404, detail=f"Recorrido not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")
    
async def get_all_recorrido_conductor(conductor_ID: int) -> Recorrido:
    selectscript = """
      SELECT
            r.ID,
            b.ID as ID_Bus,
            b.placa as placa_bus,
            b.modelo as modelo_bus,
            b.capacidad as capacidad_bus,
            ru.ID as ID_Ruta,
            ru.origen,
            ru.destino,
            c.ID as ID_Conductor,
            c.nombre as nombre_conductor,
            c.licencia as licencia_conductor,
            r.fecha_inicio,
            r.fecha_fin
            FROM transporte.recorrido as r
            INNER JOIN transporte.Bus as b
            on r.ID_Bus = b.ID
            INNER JOIN transporte.Conductor as c
            on r.ID_Conductor = c.ID
            INNER JOIN transporte.Ruta as ru
            on r.ID_Ruta=ru.ID
        WHERE c.ID = ?
    """

    params = [conductor_ID]
    result_dict=[]
    try:
        result = await execute_query_json(selectscript, params=params)
        result_dict = json.loads(result)

        if len(result_dict) > 0:
            return result_dict
        else:
            raise HTTPException(status_code=404, detail=f"Recorrido not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")