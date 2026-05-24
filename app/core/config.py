import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_HOST: str = "127.0.0.1"
    DB_PORT: str = "3306"
    DB_USER: str = "carlitos_readonly"
    DB_PASS: str = ""
    DB_NAME: str = "legasys-tambini"
    OPENAI_API_KEY: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()

from urllib.parse import quote_plus

# Construir URL de base de datos de forma segura
encoded_pass = quote_plus(settings.DB_PASS) if settings.DB_PASS else ""
DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{encoded_pass}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
