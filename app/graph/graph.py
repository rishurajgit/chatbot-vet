# from langgraph.graph import StateGraph
# from langgraph.prebuilt import ToolNode, tools_condition

# from app.graph.state import ChatState
# from app.agents.orchestrator import orchestrator, TOOLS

# workflow = StateGraph(ChatState)

# tool_node = ToolNode(TOOLS)

# workflow.add_node("orchestrator", orchestrator)
# workflow.add_node("tools", tool_node)

# workflow.set_entry_point("orchestrator")

# workflow.add_conditional_edges(
#     "orchestrator",
#     tools_condition,
# )

# workflow.add_edge("tools", "orchestrator")

# graph = workflow.compile()

from langgraph.graph import START, END, StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from app.graph.state import ChatState
from app.agents.orchestrator import orchestrator

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
from app.core.llm import llm

llm_with_tools = llm.bind_tools(tools)
tool_node = ToolNode(tools)

builder = StateGraph(ChatState)

builder.add_node("orchestrator", orchestrator)
builder.add_node("tools", tool_node)

builder.add_edge(START, "orchestrator")

builder.add_conditional_edges(
    "orchestrator",
    tools_condition,
)

builder.add_edge("tools", "orchestrator")

graph = builder.compile()