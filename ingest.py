import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Cargar variables de entorno
load_dotenv()

def ingest_docs():
    print("Iniciando la ingesta de documentos a ChromaDB...")
    
    all_splits = []

    # Configuración de archivos a ingerir y sus headers de separación
    docs_config = [
        {"path": "docs/ia/DATABASE_DOCUMENTATION.md", "headers": [("## Tabla:", "table_name")]},
        {"path": "docs/ia/BUSINESS_RULES.md", "headers": [("## Regla:", "business_rule")]},
        {"path": "docs/ia/SQL_QUERY_PATTERNS.md", "headers": [("##", "pattern_or_rule")]},
        {"path": "docs/ia/SQL_SOURCE_OF_TRUTH.md", "headers": [("##", "category"), ("###", "subcategory")]},
        {"path": "docs/ia/SQL_TABLE_RULES.md", "headers": [("##", "table_or_topic"), ("###", "detail")]},
        {"path": "docs/ia/SQL_FLAGS_AND_STATUS.md", "headers": [("##", "table_or_flag")]}
    ]

    for doc in docs_config:
        file_path = doc["path"]
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            splitter = MarkdownHeaderTextSplitter(headers_to_split_on=doc["headers"])
            splits = splitter.split_text(content)
            all_splits.extend(splits)
            print(f"Se dividió {file_path} en {len(splits)} fragmentos.")
        else:
            print(f"Advertencia: No se encontró {file_path}. Omitiendo.")

    # 3. Crear el VectorStore local con Chroma
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(
        documents=all_splits,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )
    
    print("¡Ingesta completada! La base de datos vectorial ha sido persistida en ./chroma_db")

if __name__ == "__main__":
    # Validar que la API Key de OpenAI exista
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY no está configurada en el archivo .env")
    else:
        ingest_docs()
