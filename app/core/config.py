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

# Construir URL de base de datos
DATABASE_URL = f"mysql+pymysql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
