from langgraph.graph import StateGraph
from langgraph.prebuilt import ToolNode, tools_condition

from app.graph.state import ChatState
from app.agents.orchestrator import orchestrator, TOOLS

workflow = StateGraph(ChatState)

tool_node = ToolNode(TOOLS)

workflow.add_node("orchestrator", orchestrator)
workflow.add_node("tools", tool_node)

workflow.set_entry_point("orchestrator")

workflow.add_conditional_edges(
    "orchestrator",
    tools_condition,
)

workflow.add_edge("tools", "orchestrator")

graph = workflow.compile()