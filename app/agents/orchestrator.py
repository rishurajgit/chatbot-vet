from pathlib import Path

from langchain_core.messages import SystemMessage
from app.core.llm import llm

from app.tools.pet_tools import (
    get_all_pets,
    get_pet,
    create_pet,
    update_pet,
    delete_pet,
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