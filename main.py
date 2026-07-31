from fastapi import FastAPI

from app.api.chat import router as chat_router

app = FastAPI(
    title="Veterinary AI Chatbot",
)

app.include_router(chat_router)
# app.include_router(auth_router)