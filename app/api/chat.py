# from fastapi import APIRouter
# from langchain_core.messages import HumanMessage

# from app.graph.graph import graph
# from app.schemas.chat import ChatRequest, ChatResponse

# router = APIRouter(
#     prefix="/chat",
#     tags=["Chat"],
# )

# @router.post("/", response_model=ChatResponse)
# async def chat(request: ChatRequest):
#     result = await graph.ainvoke(
#     {
#         "messages": [
#             HumanMessage(content=request.message)
#         ]
#     }
# )
    
#     response = result["messages"][-1].content
    
#     return ChatResponse(
#         response=response
#     )

from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage

from app.graph.graph import graph
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = await graph.ainvoke(
            {
                "messages": [
                    HumanMessage(content=request.message)
                ]
            }
        )

        response = result["messages"][-1].content

        return ChatResponse(
            response=response
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )