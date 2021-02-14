import random as r
from typing import List
from .agent_types import RememberType
from usecases.agent.agent_handler import looking_for_memory, create_new_choice, add_new_choices
from src.entities.multi_agent_system.agent import Agent
from src.entities.multi_agent_system.choices import Choices
from src.entities.multi_agent_system.memory import Memory
from src.entities.match.match import Match
from src.shared.types.game_status import GameStatus
from src.shared.errors.agent.remember_error import RememberError
from src.shared.errors.agent.memorize_error import MemorizeError
from src.shared.errors.agent.learn_error import LearnError


def memorize(memory: Memory, choice: Choices) -> Memory:
    """ Add a new choice in the memory """

    try:
        pass
    except:
        raise MemorizeError


def learn(choice: List[Choices], match: Match,
          game_status: GameStatus,
          start: datetime, end: datetime,
          position: int) -> List[Choices]:
    """
    Add a new choice in the memory
    """

    try:

        time: timedelta = end - start
        int_time: float = time.microseconds / 1000000
        new_choice: Choices = create_new_choice(match, game_status,
                                                int_time, position)

        new_list_choice: List[Choices] = list([choice, new_choice])
        return new_list_choice

    except:
        raise LearnError


def remember(agent: Agent, game_status: GameStatus) -> RememberType:
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
                return RememberType({
                    "position": r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8]),
                    "memorize": memorize
                })

            else:
                # return r.choice([position, r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])])
                return RememberType({
                    "position": position,
                    "memorize": memorize
                })

    else:
        raise RememberError


def memorize(memory: Memory, match: Match,
             game_status: GameStatus,
             time: float, position: int) -> Agent:
    """ Add a new choice in the memory """

    try:

        choice: Choices = create_new_choice(match, game_status,
                                            int_time, position)

        new_list_choice: List[Choices] = add_new_choices(
            memory['choices'], choice
        )

        new_memory: Memory = add_new_choices_in_memory(memory, new_list_choice)
        return new_memory

    except:
        raise MemorizeError


def check_life(agent: Agent) -> bool:
    """ Return true if an agent is alive """

    if agent['life'] > 0:
        return True
    else:
        return False


def update_agent(agent: Agent, field: str) -> Agent:
    """ update an agent """

    if field == 'death':
        return {**agent, **{'death': field}}
