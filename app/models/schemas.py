from pydantic import BaseModel
from typing import List, Dict, Optional

class ChatRequest(BaseModel):
    message: str
    co_comp: int
    chat_history: Optional[List[Dict[str, str]]] = []

class ChatResponse(BaseModel):
    reply: str
