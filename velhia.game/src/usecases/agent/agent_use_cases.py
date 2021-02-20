import random as r
from typing import List, Union, Any, Callable
from datetime import datetime, timedelta
from usecases.agent.agent_handler import looking_for_memory, create_new_choice, add_new_choices, kill_agent, add, promote_leader
from entities.agent.agent import Agent
from entities.agent.choices import Choices
from entities.agent.memory import Memory
from entities.match.match import Match
from usecases.agent.agent_adapter_type import AgentAdapter
from shared.types.game_status import GameStatus
from shared.objects import merge_objects
from shared.errors.agent.remember_error import RememberError
from shared.errors.agent.memorize_error import MemorizeError
from shared.errors.agent.learn_error import LearnError
from shared.errors.handler.agent.check_life_error import CheckLifeError


def alter(operation: str) -> Callable:

    if operation == 'add':
        return add
    elif operation == 'kill':
        return kill_agent
    elif operation == 'promote':
        return promote_leader


def check_agent(agent: Union[AgentAdapter, Agent], validation: str):

    if validation == 'life':
        return agent['life'] > 0


def learn(choice_list: List[Choices], new_choice: Choices) -> List[Choices]:
    """ Add a new choice in the memory """

    try:
        return list([choice_list, new_choice])

    except:
        raise LearnError


def remember(agent: Agent, game_status: GameStatus):
    """ Remember a game when was received a game status like now """

    if len(agent['memory']) > 0:

        if len(agent['memory'][0]['choices']) == 0:
            return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        else:
            position: int = looking_for_memory(
                agent['memory'],
                len(agent['memory']),
                game_status
            )

            if position == -1:
                return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

            else:
                # return r.choice([position, r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])])
                return position

    else:
        raise RememberError


def memorize(memory: Memory, match: Match,
             game_status: GameStatus,
             time: float, position: int) -> Agent:
    """ Add a new choice in the memory """

    try:

        choice: Choices = create_new_choice(match, game_status,
                                            time, position)

        new_list_choice: List[Choices] = add_new_choices(
            memory['choices'], choice
        )

        return 1

    except:
        raise MemorizeError
