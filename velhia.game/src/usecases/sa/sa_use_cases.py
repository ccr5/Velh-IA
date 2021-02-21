from datetime import datetime
from typing import Union, Callable
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_handler import create_sa, add
from usecases.sa.sa_database import get_sa
from usecases.sa.sa_dto import sa_to_entity
from shared.errors.statistical_algorithm.play_error import PlayError


def get_valid_sa(sa_repository: DatabaseRepositoryType) -> StatisticalAlgorithm:

    res: Union[StatisticalAlgorithm, None] = get_sa(sa_repository)

    if res is None:
        return create_sa(sa_repository)
    else:
        return sa_to_entity(res)


def alter_sa(operation: str) -> Callable:

    if operation == 'add':
        return add


def play(self, moves):
    """
    Choose a position to play 
    :param moves: game status
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> position = sa.play([-1,0,1,0,-1,-1,-1,-1,-1])
    >>> position
    4
    """

    start = datetime.now()
    winner = self.check_win(moves)
    loser = self.check_lose(moves)

    if winner is not None and loser is not None:
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        return winner

    elif winner is not None and loser is None:
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        return winner

    elif winner is None and loser is not None:
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        return loser

    elif winner is None and loser is None:
        position = self.strategy_plan(moves)
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        return position

    else:
        raise PlayError
