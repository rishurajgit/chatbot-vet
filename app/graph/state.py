from typing import Annotated, Any

from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]
        
    # intent: str | None
        
    # collected_data: dict[str, Any]
        
    # missing_fields: list[str]
    
    # waiting_for_input: bool