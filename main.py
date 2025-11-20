from fastapi import FastAPI
from routes.bus import router as router_bus
from routes.conductor import router as router_conductor
from routes.ruta import router as router_ruta
from routes.recorrido import router as router_recorrido
import uvicorn



app = FastAPI(title="Transportes el Buen Pastor API version 0.1.0")

app.include_router(router_bus)
app.include_router(router_conductor)
app.include_router(router_ruta)
app.include_router(router_recorrido)
@app.get("/")
def read_root():
    return {"API de una empresa de Buses"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

