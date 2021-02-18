from src.shared.objects import create_object
from src.entities.agent.agent import Agent
from src.usecases.agent.agent_adapter_type import AgentAdapter


def to_entity(agent_adapter: AgentAdapter) -> Agent:

    items: list = list(agent_adapter.items())
    return create_object(
        key_list=items,
        lenght=len(items),
        filters=['char']
    )


def to_repository(agent: Agent) -> AgentAdapter:

    items: list = list(agent.items())
    return create_object(
        key_list=items,
        lenght=len(items),
        obj={'char': ['O', 0]}
    )
