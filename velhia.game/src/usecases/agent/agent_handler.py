from typing import List
from datetime import datetime
from src.entities.multi_agent_system.memory import Memory
from src.entities.multi_agent_system.choices import Choices
from src.shared.types.game_status import GameStatus


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
