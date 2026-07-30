from pathlib import Path

from langchain_core.messages import SystemMessage
from app.core.llm import llm
from app.graph.state import ChatState

from app.tools.pet_tools import (
    get_all_pets,
    get_pet,
    create_pet,
    update_pet,
    delete_pet,
    search_pets
)

from app.tools.owner_tools import (
    create_owner,
    get_owner_pets,
)

from app.tools.visit_tools import (
    create_visit,
    get_pet_visits,
    update_visit,
    delete_visit,
)

TOOLS = [
    get_all_pets,
    get_pet,
    create_pet,
    update_pet,
    delete_pet,
    search_pets,
    create_owner,
    get_owner_pets,
    create_visit,
    get_pet_visits,
    update_visit,
    delete_visit,
]
PROMPT_PATH = Path("app/prompts/orchestrator.txt")
SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")


llm_with_tools = llm.bind_tools(TOOLS)


def orchestrator(state: ChatState):
    """
    LangGraph orchestrator node.

    Responsibilities:
    - Load the system prompt.
    - Read the conversation history.
    - Allow the LLM to decide whether to call tools.
    - Return the AIMessage (which may contain tool calls).
    """

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)

    return {
        "messages": [response]
    }