import math as m
import random as r
import operator as op
import functools as fct
from typing import Union, Any, Tuple, List, Generator
from datetime import datetime
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_database import save_sa
from shared.types.game_status import GameStatus


def create_sa(sa_repository: DatabaseRepositoryType) -> StatisticalAlgorithm:

    empty_sa: StatisticalAlgorithm = dict([
        ('birth', datetime.now().ctime()),
        ('matchs', 0),
        ('victories', 0),
        ('defeats', 0),
        ('draw', 0)
    ])

    return save_sa(sa_repository, empty_sa)


def add(sa: Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm], field: str,
        value: Any) -> Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm]:

    obj = {field: sa[field] + value}
    return sa | obj


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
    """ all possible game variations """

    def load_matrix(ret=[]) -> List[GameStatus]:

        if len(ret) < number_variations:
            new_moves = list(map(lambda x: r.choice(
                [sa['char'][1], sa['enemy'][1]]) if x == -1 else x, moves))

            if new_moves not in ret:
                return load_matrix(op.add(ret, new_moves))
            else:
                return load_matrix(ret)

        else:
            return ret

    empty_position = len([x for x in moves if x == -1])
    enemy_positions = len([x for x in moves if x == sa['enemy'][1]])
    my_positions = len([x for x in moves if x == sa['char'][1]])
    who_begin = sa['enemy'] if enemy_positions > my_positions else sa['char']
    number_variations = op.sub(1,  m.pow(2, empty_position))
    matrix = load_matrix()
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

    match_list = [sa['char'][1], sa['char'][1], sa['char'][1]]
    return len([filter(lambda y: y == match_list, sequence_list(x))
                for x in matrix])


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

    match_list = [sa['enemy'][1], sa['enemy'][1], sa['enemy'][1]]
    return len([filter(lambda y: y == match_list, sequence_list(x))
                for x in matrix])


def highlights(sa: StatisticalAlgorithmAdapter, moves: GameStatus, position: int) -> Tuple[int, int, int, float]:

    matrix = create_matrix(sa, moves)
    victories = count_victories(sa, matrix)
    defeats = count_defeats(sa, matrix)
    ratio = (victories / 1) if defeats == 0 else (victories / defeats)
    return (position, victories, defeats, ratio)


def move_options(moves: GameStatus, lenght: int, value: int,
                 move_list: List[Tuple[int, GameStatus]] = []) -> List[Tuple[int, GameStatus]]:

    if len(move_list) < len(moves):
        index: int = lenght - 1

        if moves[index] == -1:
            new_move_list = op.add(
                move_list, [(index, list(
                    map(lambda x: value if x ==
                        index else moves[x], range(0, len(moves)))
                ))]
            )
            return move_options(moves, index, value, new_move_list)
        else:
            new_move_list = op.add(move_list, [(index, moves[index])])
            return move_options(moves, index, value, new_move_list)

    else:
        return move_list


def find_best_ratio(options: List[Tuple[int, int, int, float]], lenght: int,
                    ret: Tuple[int, int, int, float] = []) -> Tuple[int, int, int, float]:

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
