import random as r
from datetime import datetime
from typing import Union, Callable, List, Tuple
from itertools import repeat
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_handler import create_sa, add, highlights, move_options, find_best_ratio, sequence_list
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_database import get_sa
from usecases.sa.sa_mapper import sa_to_entity
from shared.types.game_status import GameStatus


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

    options = move_options(moves, len(moves), sa['char'][-1])
    positions_options = list(map(lambda x: x[0], options))
    moves_options = list(map(lambda x: x[1], options))

    results: List[Tuple[int, int, int, GameStatus]] = list(
        map(highlights, repeat(sa), moves_options, positions_options)
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

    match_list = [sa['char'][1], sa['char'][1], sa['char'][1]]
    sequence_matrix = list(sequence_list(
        list(map(lambda z: sa['char'][1] if z == x and moves[z] == -1 else moves[z],
                 range(0, len(moves)))))
        for x in range(0, len(moves))
    )
    positions = list(filter(lambda x: x is not False,
                            [isequence if x == match_list else False
                             for isequence in range(0, len(sequence_matrix))
                             for x in sequence_matrix[isequence]]))

    if len(positions) > 0:
        return r.choice(positions)
    else:
        return None


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

    match_list = [sa['enemy'][1], sa['enemy'][1], sa['enemy'][1]]
    sequence_matrix = list(sequence_list(
        list(map(lambda z: sa['enemy'][1] if z == x and moves[z] == -1 else moves[z],
                 range(0, len(moves)))))
        for x in range(0, len(moves))
    )
    positions = list(filter(lambda x: x is not False,
                            [isequence if x == match_list else False
                             for isequence in range(0, len(sequence_matrix))
                             for x in sequence_matrix[isequence]]))

    if len(positions) > 0:
        return r.choice(positions)
    else:
        return None
