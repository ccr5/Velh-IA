from typing import List
from entities.agent.agent import Agent
from usecases.agent.agent_adapter_type import AgentAdapter
from shared.objects import create_object


def agent_to_entity(agent_adapter: AgentAdapter) -> Agent:

    items: List = list(agent_adapter.items())
    return Agent(create_object(
        key_list=items,
        lenght=len(items),
        filters=['char', 'createdAt', 'updatedAt', '__v']
    ))


def agent_to_adapter(agent: Agent) -> AgentAdapter:

    items: List = list(agent.items())
    return AgentAdapter(create_object(
        key_list=items,
        lenght=len(items),
        filters=['createdAt', 'updatedAt', '__v'],
        obj={'char': ('O', 0)}
    ))
