from typing import List
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

    lenght: int = len(memories[memory_lenght]['choices'])
    position: int = looking_for_choices(
        memories[memory_lenght]['choices'], 
        lenght, game_status
    )

    try:

        if position = -1 and memory_lenght > 0:
            looking_for_memory(memories, memory_lenght - 1, game_status)
        else:
            return position

    except:
        raise SystemError


def create_new_choice(match: Match, game_status: GameStatus, 
                      start: datetime, end: datetime, 
                      position: int) -> Choices:
    """
    Create a choice object
    """
    
    try:

        return Choices({'dateRequest': start.ctime(),
                        'gameStatus': game_status,
                        'timeToAct': time,
                        'action': position})
    
    except:
        raise SystemError
