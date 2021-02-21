from datetime import datetime
from typing import Union, Callable, List, Tuple
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_handler import create_sa, add, highlights, move_options, find_best_ratio, sequence_list
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_database import get_sa
from usecases.sa.sa_dto import sa_to_entity
from shared.types.game_status import GameStatus
from shared.errors.statistical_algorithm.play_error import PlayError
from shared.errors.statistical_algorithm.strategy_plan_error import StrategyPlanError


def get_valid_sa(sa_repository: DatabaseRepositoryType) -> StatisticalAlgorithm:

    res: Union[StatisticalAlgorithm, None] = get_sa(sa_repository)

    if res is None:
        return create_sa(sa_repository)
    else:
        return sa_to_entity(res)


def alter_sa(operation: str) -> Callable:

    if operation == 'add':
        return add


def strategy_plan(sa: StatisticalAlgorithmAdapter, moves: GameStatus) -> int:
    """ Find the best position to play using game status """

    results: List[Tuple[int, int, int, GameStatus]] = list(
        map(highlights, move_options(moves, len(moves), sa['char'][-1]))
    )

    best_play: Tuple[int, int, int, GameStatus] = find_best_ratio(
        results, len(results)
    )

    return best_play[0]


def check_win(sa: StatisticalAlgorithmAdapter, moves: GameStatus) -> int:
    """
    Check and return a position to win
    :param moves: game status
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> position = sa.check_win([-1,0,1,0,0,1,0,-1,-1])
    >>> position
    8
    """

    for x in range(0, len(moves)):

        if moves[x] == -1:
            moves[x] = sa['char'][1]
            checklist = sequence_list(moves)

            for y in checklist:

                if y == [sa['char'][1], sa['char'][1], sa['char'][1]]:
                    return x
                else:
                    moves[x] = -1
        else:
            pass


def check_lose(sa: StatisticalAlgorithmAdapter, moves: GameStatus):
    """
    Check and return a position to protect itself
    :param moves: game status
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> position = sa.check_lose([-1,0,1,0,-1,1,0,-1,-1])
    >>> position
    0
    """

    for x in range(0, len(moves)):

        if moves[x] == -1:
            moves[x] = sa['enemy'][1]
            checklist = sequence_list(moves)

            for y in checklist:

                if y == [sa['enemy'][1], sa['enemy'][1], sa['enemy'][1]]:
                    return x
                else:
                    moves[x] = -1
        else:
            pass
