# from pathlib import Path

# from langchain_core.messages import SystemMessage
# from app.core.llm import llm
# from app.graph.state import ChatState

# from app.utils.required_fields import REQUIRED_FIELDS

# from app.tools.pet_tools import (
#     get_all_pets,
#     get_pet,
#     create_pet,
#     update_pet,
#     delete_pet,
#     search_pets,
# )

# from app.tools.owner_tools import (
#     create_owner,
#     get_owner_pets,
# )

# from app.tools.visit_tools import (
#     create_visit,
#     get_pet_visits,
#     update_visit,
#     delete_visit,
# )

# TOOLS = [
#     get_all_pets,
#     get_pet,
#     create_pet,
#     update_pet,
#     delete_pet,
#     search_pets,
#     create_owner,
#     get_owner_pets,
#     create_visit,
#     get_pet_visits,
#     update_visit,
#     delete_visit,
# ]
# PROMPT_PATH = Path("app/prompts/orchestrator.txt")
# SYSTEM_PROMPT = PROMPT_PATH.read_text(encoding="utf-8")


# llm_with_tools = llm.bind_tools(TOOLS)


# def orchestrator(state: ChatState):
#     """
#     LangGraph orchestrator node.

#     Responsibilities:
#     - Load the system prompt.
#     - Read the conversation history.
#     - Allow the LLM to decide whether to call tools.
#     - Return the AIMessage (which may contain tool calls).
#     """

#     messages = [
#         SystemMessage(content=SYSTEM_PROMPT),
#         *state["messages"],
#     ]

#     response = llm_with_tools.invoke(messages)

#     return {
#         "messages": [response]
#     }

from langchain_core.messages import SystemMessage

from app.prompts.loader import load_prompt
from app.core.llm import llm

from app.tools.pet_tools import (
    get_all_pets,
    get_pet,
    create_pet,
    update_pet,
    delete_pet,
)

from app.tools.owner_tools import (
    get_all_owners,
    get_owner,
    create_owner,
    update_owner,
    delete_owner,
    get_owner_pets,
)

from app.tools.visit_tools import (
    get_pet_visits,
    create_visit,
    update_visit,
    delete_visit,
)

tools = [
    get_all_pets,
    get_pet,
    create_pet,
    update_pet,
    delete_pet,

    get_all_owners,
    get_owner,
    create_owner,
    update_owner,
    delete_owner,
    get_owner_pets,

    get_pet_visits,
    create_visit,
    update_visit,
    delete_visit,
]

llm_with_tools = llm.bind_tools(tools)

system_prompt = load_prompt("orchestrator.txt")


async def orchestrator(state):
    messages = [
        SystemMessage(content=system_prompt),
        *state["messages"],
    ]

    response = await llm_with_tools.ainvoke(messages)

    return {
        "messages": [response]
    }