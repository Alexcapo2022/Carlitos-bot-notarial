import os
from dotenv import load_dotenv

# Forzar la carga del .env buscando en el directorio padre de 'app'
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from app.api.routes import router as api_router
from app.core.database import engine
from sqlalchemy import text
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Carlitos Bot Notarial API")

# Montar archivos estáticos para descargas (Excel, imágenes)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Registrar las rutas
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Hola, soy Carlitos. API en línea."}

@app.get("/test-db")
def test_db_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            return {"status": "ok", "message": "Conexión exitosa a la base de datos."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error conectando a BD: {str(e)}")
