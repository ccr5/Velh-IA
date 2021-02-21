from datetime import datetime
from typing import List, Callable, Union, Any, Dict
from entities.agent.agent import Agent
from entities.agent.memory import Memory
from entities.agent.choices import Choices
from usecases.agent.agent_database import DatabaseRepositoryType
from usecases.agent.agent_database import save_agent
from usecases.agent.agent_dto import agent_to_entity, agent_to_adapter
from usecases.agent.agent_adapter_type import AgentAdapter
from shared.types.game_status import GameStatus
from shared.objects import merge_objects, create_object


def create_leader(agent_repository: DatabaseRepositoryType) -> Agent:

    return save_agent(
        agent_repository, create_object(
            [
                ('birth', datetime.now().ctime()),
                ('progenitor', "I'm the first one, bitch ;)"),
                ("becomeLeader", datetime.now().ctime()),
                ("life", 100),
                ("memory", []),
                ("matchsAsLearner", 0),
                ("matchsAsLeader", 0),
                ("victories", 0),
                ("defeats", 0),
                ("draw", 0)
            ], 10
        )
    )


def create_learner(agent_repository: DatabaseRepositoryType, progenitor: str) -> Agent:

    return save_agent(
        agent_repository, create_object(
            [
                ('birth', datetime.now().ctime()),
                ('progenitor', progenitor),
                ("life", 100),
                ("memory", []),
                ("matchsAsLearner", 0),
                ("matchsAsLeader", 0),
                ("victories", 0),
                ("defeats", 0),
                ("draw", 0)
            ], 9
        )
    )


def kill_agent(agent: Union[AgentAdapter, Agent]) -> Union[AgentAdapter, Agent]:
    death_obj: Dict = {'death': datetime.now().ctime()}

    if isinstance(agent, Agent):
        return agent_to_entity(merge_objects(agent, death_obj))
    else:
        return agent_to_adapter(merge_objects(agent, death_obj))


def promote_leader(agent: Union[AgentAdapter, Agent]) -> Union[AgentAdapter, Agent]:
    obj: Dict = {'becomeLeader': datetime.now().ctime()}

    if isinstance(agent, Agent):
        return agent_to_entity(merge_objects(agent, obj))
    else:
        return agent_to_adapter(merge_objects(agent, obj))


def add(agent: Union[AgentAdapter, Agent], field: str, value: Any) -> Union[AgentAdapter, Agent]:
    current_value = agent[field]
    new_value = current_value + value
    obj = {field: new_value}
    return merge_objects(agent, obj)


def looking_for_choices(choices: List[Choices],
                        choices_lenght: int,
                        game_status: GameStatus) -> int:
    """
    Recursive function to looking for choices equals game status
    """

    try:

        if choices_lenght == -1:
            return -1
        else:
            if choices[choices_lenght]['gameStatus'] == game_status:
                return choices[choices_lenght]['action']
            else:
                looking_for_choices(choices, choices_lenght - 1, game_status)

    except:
        raise SystemError


def looking_for_memory(memories: List[Memory],
                       memory_lenght: int,
                       game_status: GameStatus) -> int:
    """
    Recursive function to looking for memories 
    with choices equals game status
    """

    try:

        lenght: int = len(memories[memory_lenght]['choices'])
        position: int = looking_for_choices(
            memories[memory_lenght]['choices'],
            lenght, game_status
        )

        if position == -1 and memory_lenght > 0:
            looking_for_memory(memories, memory_lenght - 1, game_status)
        else:
            return position

    except:
        raise SystemError


def create_new_choice(game_status: GameStatus, start: datetime,
                      time: float, position: int) -> Choices:
    """ Create a choice object """

    try:

        return Choices({'dateRequest': start.ctime(),
                        'gameStatus': game_status,
                        'timeToAct': time,
                        'action': position})

    except:
        raise SystemError


def add_new_choices(choices: List[Choices], choice: Choices) -> List[Choices]:
    """ update a list of choices """

    try:

        return choices + list(choice)

    except:
        raise SystemError
