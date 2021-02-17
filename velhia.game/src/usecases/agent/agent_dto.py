from src.shared.objects import create_object
from src.shared.lists import concat_list
from src.entities.agent.agent import Agent
from src.usecases.agent.agent_adapter_type import AgentAdapter


def to_entity(agent_adapter: AgentAdapter) -> Agent:

    items: list = list(agent_adapter.items())
    return Agent(
        create_object(
            items, len(items), ['char']
        )
    )


def to_repository(agent: Agent) -> AgentAdapter:

    items: list = concat_list(
        agent.items(), [('char', ['O', 0])]
    )

    return AgentAdapter(
        create_object(
            items, len(items)
        )
    )
