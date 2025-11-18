from fastapi import FastAPI
from routes.bus import router as router_bus
from routes.conductor import router as router_conductor
from routes.ruta import router as router_ruta
from routes.recorrido import router as router_recorrido



app = FastAPI(title="Transportes el Buen Pastor API")

app.include_router(router_bus)
app.include_router(router_conductor)
app.include_router(router_ruta)
app.include_router(router_recorrido)
@app.get("/")
def read_root():
    return {"API de una empresa de Buses"}

