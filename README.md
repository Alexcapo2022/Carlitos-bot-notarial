# Carlitos - Bot Notarial (Backend de IA)

Carlitos es el asistente con Inteligencia Artificial (LLM + RAG) para el sistema Legasys. Permite a los notarios y empleados interactuar con la base de datos a través de lenguaje natural (texto), generar Excel y crear Gráficos en tiempo real.

## Arquitectura

- **Framework**: FastAPI (Python)
- **Agente SQL**: LangChain (`create_sql_agent` con `openai-tools`)
- **Memoria Vectorial (RAG)**: ChromaDB (usado para inyectar el esquema y documentación de la BD)
- **Modelo**: OpenAI (`gpt-4o`)
- **Despliegue**: Docker Compose

## Estructura de Directorios

```
carlitos-botnotarial/
├── app/
│   ├── api/          # Controladores y rutas FastAPI (routes.py)
│   ├── core/         # Configuraciones core (BD, LangChain)
│   ├── models/       # Esquemas Pydantic para Validar Requests/Responses
│   ├── services/     # Lógica de Negocio (agent.py, few_shot.py)
│   ├── static/       # Directorio público donde se guardan Excel y PNG
│   └── tools/        # Herramientas de LangChain (Excel, Gráficos)
├── chromadb/         # Carpeta autogenerada con los Vectores de la BD
├── Dockerfile        # Instrucciones de compilación del microservicio
├── docker-compose.yml# Orquestador del contenedor
├── ingest.py         # Script para leer DATABASE_DOCUMENTATION.md y vectorizarlo
└── main.py           # Punto de entrada de FastAPI
```

---

## Memoria Conversacional (Stateless)

Para mantener a Carlitos ligero, rápido y escalable (sin saturar memoria en Python), **el backend de Python es Stateless (Sin estado)**. 

Esto significa que es responsabilidad del **Frontend (Laravel)** guardar el historial de la conversación en su base de datos y enviarlo en cada petición dentro del arreglo `chat_history`.

### Modelo de Tablas Recomendado para Laravel (MySQL)

Para construir la interfaz en Laravel, deberás crear un par de tablas para guardar los chats. Aquí tienes la sugerencia de migración:

```php
// Tabla principal del Chat (Un hilo de conversación por usuario)
Schema::create('ai_chat_sessions', function (Blueprint $table) {
    $table->id();
    $table->unsignedBigInteger('user_id'); // ID del usuario de P_USUA
    $table->unsignedBigInteger('co_comp'); // Notaría (para no mezclar chats)
    $table->string('title')->nullable();   // Título autogenerado del chat
    $table->timestamps();
});

// Tabla para los Mensajes (El historial que se le envía a Python)
Schema::create('ai_chat_messages', function (Blueprint $table) {
    $table->id();
    $table->foreignId('ai_chat_session_id')->constrained()->onDelete('cascade');
    $table->enum('role', ['user', 'assistant']); // Quién escribió
    $table->text('content'); // El mensaje o respuesta
    $table->timestamps();
});
```

Al hacer la petición POST desde Laravel hacia Python, enviarás el JSON así:

```json
{
    "message": "grafícalo en pastel",
    "co_comp": 97,
    "chat_history": [
        {"role": "user", "content": "¿Cuántos clientes activos tenemos?"},
        {"role": "assistant", "content": "Tienen 125 clientes activos en la notaría."}
    ]
}
```

---

## Few-Shot Learning (Ejemplos de Oro)

Para evitar que Carlitos se equivoque al hacer uniones (`JOIN`) complejas (ejemplo: vincular Kardex con Servicios y Subservicios), se implementó el archivo `app/services/few_shot.py`.

Ahí existe un arreglo con las **Consultas Perfectas**. Cuando Carlitos va a ejecutar SQL, primero lee ese archivo para aprender las reglas de negocio de tu sistema (ej: filtrar por `IN_ESTA = '1'` o `CO_COMP`). 

**Mantenimiento**: Si ves que Carlitos falla respondiendo alguna pregunta recurrente de tus usuarios, solo debes entrar a `few_shot.py` y agregar la pregunta con su respectiva query SQL correcta. Carlitos la aprenderá al instante.

---

## Endpoints Disponibles

### 1. Iniciar Conversación (Onboarding)
- **URL**: `POST http://localhost:8001/onboarding`
- **Uso**: Llama a este endpoint cuando el usuario abra la ventana de chat por primera vez para recibir un saludo cordial.
- **Body**: `{ "message": "", "co_comp": 97 }`

### 2. Hablar con Carlitos
- **URL**: `POST http://localhost:8001/chat`
- **Body**: 
  ```json
  {
      "message": "Exporta a excel los clientes",
      "co_comp": 97,
      "chat_history": []
  }
  ```

### 3. Descarga de Archivos
Todos los archivos (Excel, Imágenes) generados se pueden acceder mediante GET público.
- `GET http://localhost:8001/static/exports/reporte_XYZ.xlsx`
- `GET http://localhost:8001/static/exports/grafico_XYZ.png`
