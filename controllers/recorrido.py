from datetime import datetime
import json
import logging

from fastapi import HTTPException

from models.recorrido import Recorrido
from Utils.database import execute_query_json



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_one( ID: int ) -> Recorrido:
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
        WHERE r.ID = ?;
    """

    params = [ID]
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
    
async def get_all() -> list[Recorrido]:

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
    """

    result_dict=[]
    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")    
    
async def create_recorrido(recorrido: Recorrido) -> dict:
    
    sql_insert = """  
    INSERT INTO [transporte].[recorrido] (
        ID_Bus,
        ID_Ruta,
        ID_Conductor,
        fecha_inicio
    )
    OUTPUT INSERTED.ID
    VALUES (?, ?, ?, ?);
    """

    recorrido.fecha_inicio = datetime.now()
    params_insert = [
        recorrido.ID_Bus,
        recorrido.ID_Ruta,
        recorrido.ID_Conductor,
        recorrido.fecha_inicio
    ]

    try:
        insert_result = await execute_query_json(sql_insert, params_insert, needs_commit=True)
        inserted = json.loads(insert_result)
        if not inserted or "ID" not in inserted[0]:
            raise HTTPException(status_code=500, detail="Database error: could not retrieve inserted ID")
        new_id = inserted[0]["ID"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    sql_find = """
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
            ON r.ID_Bus = b.ID
        INNER JOIN transporte.Conductor as c
            ON r.ID_Conductor = c.ID
        INNER JOIN transporte.Ruta as ru
            ON r.ID_Ruta = ru.ID
        WHERE r.ID = ?;
    """
    params_find = [new_id]

    try:
        result_find = await execute_query_json(sql_find, params_find)
        result_dict = json.loads(result_find)
        if len(result_dict) > 0:
            return result_dict[0]
        else:
            return {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")   
    
async def update_recorrido( recorrido : Recorrido ) -> Recorrido:

    dict = recorrido.model_dump(exclude_none=True)
    dict["fecha_fin"] = datetime.now()
    keys = [ k for k in  dict.keys() ]
    keys.remove('ID')
    variables = " = ?, ".join(keys)+" = ?"

    updatescript = f"""
        UPDATE [transporte].[recorrido]
        SET {variables}
        WHERE [ID] = ?;
    """

    params = [ dict[v] for v in keys ]
    params.append(recorrido.ID)

    update_result = None
    try:
        update_result = await execute_query_json( updatescript, params, needs_commit=True )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
    sqlfind: str = """
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
        WHERE r.ID = ?; 
    """

    params = [recorrido.ID]

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

async def delete_recorrido(id: int) -> str:

    deletescript = """
        DELETE FROM [transporte].[recorrido]
        WHERE [ID] = ?;
    """

    params = [id];

    try:
        await execute_query_json(deletescript, params=params, needs_commit=True)
        return "DELETED"
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")
