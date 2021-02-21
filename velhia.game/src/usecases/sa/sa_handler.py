import random as r
from typing import Union, Any, Tuple, List
from datetime import datetime
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_database import save_sa
from shared.list import merge_list
from shared.objects import create_object, merge_objects
from shared.types.game_status import GameStatus
from shared.errors.statistical_algorithm.strategy_plan_error import StrategyPlanError
from shared.errors.statistical_algorithm.sequence_list_error import SequenceListError
from shared.errors.statistical_algorithm.check_error import CheckError
from shared.errors.statistical_algorithm.count_error import CountError
from shared.errors.statistical_algorithm.create_matrix_error import CreateMatrixError


def create_sa(sa_repository: DatabaseRepositoryType) -> StatisticalAlgorithm:

    return save_sa(sa_repository, create_object(
        [
            ('birth', datetime.now().ctime()),
            ('matchs', 0),
            ('victories', 0),
            ('defeats', 0),
            ('draw', 0)
        ], 5
    ))


def add(sa: Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm], field: str,
        value: Any) -> Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm]:

    current_value = sa[field]
    new_value = current_value + value
    obj = {field: new_value}
    return merge_objects(sa, obj)


def sequence_list(game_status: GameStatus) -> List[Tuple[int, int, int]]:
    """ All sequence to win """

    return [[game_status[0], game_status[1], game_status[2]],
            [game_status[3], game_status[4], game_status[5]],
            [game_status[6], game_status[7], game_status[8]],
            [game_status[0], game_status[3], game_status[6]],
            [game_status[1], game_status[4], game_status[7]],
            [game_status[2], game_status[5], game_status[8]],
            [game_status[0], game_status[4], game_status[8]],
            [game_status[2], game_status[4], game_status[6]]]


def create_matrix(sa: StatisticalAlgorithmAdapter, moves: GameStatus) -> List[GameStatus]:
    """
    all possible game variations
    :param moves: game status
    :return: `list` matrix

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
    >>> matrix
    [
        [0,1,1,1,0,0,1,0,1],
        [0,1,1,1,0,0,0,1,1],
        [0,1,1,1,0,0,1,1,0]
    ]
    """

    matrix = []
    empty_position = len([x for x in moves if x == -1])
    who_begin = sa['enemy'] if len([x for x in moves if x == sa['enemy'][1]]) > len(
        [x for x in moves if x == sa['char'][1]]) else sa['char']
    number_variations = 2 ** empty_position

    while len(matrix) != number_variations:
        new_moves = []

        for x in range(0, len(moves)):

            new_moves.append(r.choice(
                [sa['char'][1], sa['enemy'][1]])) if moves[x] == -1 else new_moves.append(moves[x])

        if new_moves in matrix:
            del new_moves
        else:
            matrix.append(new_moves)
            del new_moves

    return [move for move in matrix if len([x for x in move if x == who_begin[1]]) == 5 and
            len([o for o in move if o != who_begin[1] and o != -1]) == 4]


def count_victories(sa: StatisticalAlgorithmAdapter, matrix: List[GameStatus]) -> int:
    """
    Count how many victories has in a matrix of game variation
    :param matrix: matrix of all possible game variations
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
    >>> victories = sa.count_victories(matrix)
    >>> victories
    100
    """

    result = 0

    for x in matrix:
        checklist = sequence_list(x)

        for y in checklist:

            if y == [sa['char'][1], sa['char'][1], sa['char'][1]]:
                result += 1
            else:
                pass

    return result


def count_defeats(sa: StatisticalAlgorithmAdapter, matrix: List[GameStatus]) -> int:
    """
    Count how many defeats has in a matrix of game variation
    :param matrix: matrix of all possible game variations
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
    >>> defeats = sa.count_defeats(matrix)
    >>> defeats
    3
    """

    result = 0

    for x in matrix:
        checklist = sequence_list(x)

        for y in checklist:

            if y == [sa['enemy'][1], sa['enemy'][1], sa['enemy'][1]]:
                result += 1
            else:
                pass

    return result


def highlights(sa: StatisticalAlgorithmAdapter, moves: GameStatus, position: int) -> Tuple[int, int, int, float]:

    matrix = create_matrix(sa, moves)
    victories = count_victories(sa, matrix)
    defeats = count_defeats(sa, matrix)

    if defeats == 0:
        defeats = 1
    else:
        pass

    ratio = (victories / defeats)

    return (position, victories, defeats, ratio)


def move_options(moves: GameStatus, lenght: int, value: int,
                 move_list: List[Tuple[int, GameStatus]] = []) -> List[Tuple[int, GameStatus]]:

    if len(move_list) < len(moves):
        index: int = lenght - 1
        if moves[index] == -1:
            new_move_list = move_list + [(
                index,
                merge_list(moves, index, value)
            )]
            return move_options(moves, index, value, new_move_list)
        else:
            new_move_list = move_list + [(
                index,
                moves[index]
            )]
            return move_options(moves, index, value, new_move_list)
    else:
        return move_list


def find_best_ratio(options: List[Tuple[int, int, int, float]],
                    lenght: int, ret: Tuple[int, int, int, float] = []) -> Tuple[int, int, int, float]:

    if lenght > 0:
        index: int = lenght - 1

        if len(ret) == 0:
            return find_best_ratio(options, index, options[index])

        elif ret[3] > options[index][3]:
            return find_best_ratio(options, index, ret)

        elif ret[3] == options[index][3]:

            if options[index][1] > ret[3]:
                return find_best_ratio(options, index, options[index])
            else:
                return find_best_ratio(options, index, ret)

        elif ret[3] < options[index][3]:
            return find_best_ratio(options, index, options[index])

        else:
            raise SystemError

    else:
        return ret
