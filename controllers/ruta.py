import json
import logging

from fastapi import HTTPException

from models.ruta import ruta
from Utils.database import execute_query_json



logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_one( id: int ) -> ruta:

    selectscript = """
       SELECT 
       [ID],
       [origen],
       [destino]
       FROM [transporte].[ruta]
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
            raise HTTPException(status_code=404, detail=f"Bus not found")

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Database error: { str(e) }")
    
async def get_all() -> list[ruta]:

    selectscript = """
       SELECT 
       [ID],
       [origen],
       [destino]
        FROM [transporte].[ruta]
    """

    result_dict=[]
    try:
        result = await execute_query_json(selectscript)
        result_dict = json.loads(result)
        return result_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: { str(e) }")