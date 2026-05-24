from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.agent import ask_carlitos

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """
    Endpoint principal para conversar con Carlitos
    """
    agent_response = ask_carlitos(request.message, request.co_comp, request.chat_history)
    
    return ChatResponse(
        reply=agent_response["reply"]
    )

@router.post("/onboarding")
def onboarding_endpoint(request: ChatRequest):
    """
    Endpoint que Laravel llama al abrir el chat por primera vez.
    No ejecuta queries, solo saluda.
    """
    mensaje = "¡Hola! Soy Carlitos, tu asistente notarial con Inteligencia Artificial. ¿En qué te puedo ayudar hoy? (Ej. 'Cuántos trámites hay', 'Exporta los usuarios a Excel', 'Grafica los kardex')"
    return ChatResponse(reply=mensaje)
