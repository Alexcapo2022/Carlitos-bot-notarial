from sqlalchemy import create_engine, inspect
from langchain_community.utilities import SQLDatabase
from app.core.config import DATABASE_URL
import os
import re

# Crear el motor de SQLAlchemy
engine = create_engine(DATABASE_URL, pool_recycle=3600)

# Leer las tablas documentadas para incluirlas explícitamente y ahorrar cientos de miles de tokens
documented_tables = []
docs_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "DATABASE_DOCUMENTATION.md")
if os.path.exists(docs_path):
    with open(docs_path, 'r', encoding='utf-8') as f:
        content = f.read()
        # Buscar: ## Tabla: `NOMBRE_TABLA`
        documented_tables = re.findall(r'## Tabla:\s*`(\w+)`', content)

# Validar que las tablas existan realmente en la BD
if documented_tables:
    inspector = inspect(engine)
    existing_tables = inspector.get_table_names()
    valid_tables = [t for t in documented_tables if t in existing_tables]
    db = SQLDatabase(engine, include_tables=valid_tables)
else:
    db = SQLDatabase(engine)
