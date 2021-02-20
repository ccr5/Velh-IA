from typing import TypedDict, Union
from entities.agent.agent import Agent
from usecases.agent.agent_adapter_type import AgentAdapter
from shared.types.char import Char


class MultiAgentSystemAdapter(TypedDict):

    char: Char
    family_leader: Union[Agent, AgentAdapter]
    family_learner: Union[Agent, AgentAdapter]
    education_leader: Union[Agent, AgentAdapter]
    education_learner: Union[Agent, AgentAdapter]
    religion_leader: Union[Agent, AgentAdapter]
    religion_learner: Union[Agent, AgentAdapter]
