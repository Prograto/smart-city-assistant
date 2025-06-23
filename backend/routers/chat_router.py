from fastapi import APIRouter
from backend.models.chat_schema import ChatInput
from backend.services.chat_model import generate_chat_response

router = APIRouter()

@router.post("/chat")
def chat_response(data: ChatInput):
    response = generate_chat_response(data.prompt)
    return {"response": response}
