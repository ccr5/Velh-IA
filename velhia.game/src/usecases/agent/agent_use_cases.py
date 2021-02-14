from typing import List
from datetime import timedelta
from .agent_handler import looking_for_memory, create_new_choice
from src.entities.multi_agent_system.agent import Agent
from src.entities.multi_agent_system.choices import Choices
from src.entities.match.match import Match
from src.shared.types.game_status import GameStatus
from src.shared.errors.agent.remember_error import RememberError
from src.shared.errors.agent.memorize_error import MemorizeError
from src.shared.errors.agent.learn_error import LearnError


def remember(agent: Agent, game_status: GameStatus) -> int:
    """
    Remember a game when was received a game status like now
    """

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


def memorize(choice: List[Choices], match: Match, 
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
                                                start, end, position)

        new_list_choice: List[Choices] = list([choice, new_choice])
        return new_list_choice

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
                                                start, end, position)

        new_list_choice: List[Choices] = list([choice, new_choice])
        return new_list_choice

    else:
        raise LearnError
