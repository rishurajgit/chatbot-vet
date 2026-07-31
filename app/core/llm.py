from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI 
from app.core.config import settings


llm = ChatGoogleGenerativeAI(
    # model=settings.GROQ_MODEL,
    # api_key=settings.GROQ_API_KEY,
    
    model=settings.GEMINI_MODEL,
    api_key=settings.GEMINI_API_KEY,
    temperature=0,
)