from shared.objects import create_object
from entities.agent.agent import Agent
from usecases.agent.agent_adapter_type import AgentAdapter


def agent_to_entity(agent_adapter: AgentAdapter) -> Agent:

    items: list = list(agent_adapter.items())
    return Agent(create_object(
        key_list=items,
        lenght=len(items),
        filters=['char', 'createdAt', 'updatedAt', '__v']
    ))


def agent_to_repository(agent: Agent) -> AgentAdapter:

    items: list = list(agent.items())
    return AgentAdapter(create_object(
        key_list=items,
        lenght=len(items),
        obj={'char': ['O', 0]}
    ))
