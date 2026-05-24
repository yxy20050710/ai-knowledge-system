from fastapi import FastAPI
from pydantic import BaseModel
from app.services.llm_service import chat_with_ai
from app.api.upload import router as upload_router #
from app.services.rag_service import rag_chat

app = FastAPI()
app.include_router(upload_router)

class ChatRequest(BaseModel):
    message: str

class RagRequest(BaseModel):
    session_id: str
    collection_name: str
    message: str

@app.get("/")
def root():
    return {
        "message": "AI Agent System Running"
    }

@app.post("/chat")
def chat(request:ChatRequest):
    result = chat_with_ai(request.message)
    return {
        "message": result
    }

@app.post("/rag-chat")
def rag_api(request:RagRequest):
    result = rag_chat(
        request.session_id,
        request.collection_name,
        request.message
        )
    return result