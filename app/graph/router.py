from app.graph.state import ChatState


def route_after_slot_filling(state: ChatState) -> str:
    """
    Decide whether to ask the user for more information
    or execute the requested action.
    """

    if state.get("missing_fields"):
        return "ask_user"

    return "execute"