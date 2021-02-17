from typing import TypedDict
from src.entities.agent.agent import Agent
from src.shared.types.char import Char


class MultiAgentSystemAdapter(TypedDict):

    char: Char
    family_leader: Agent
    family_learner: Agent
    education_leader: Agent
    education_learner: Agent
    religion_leader: Agent
    religion_learner: Agent
