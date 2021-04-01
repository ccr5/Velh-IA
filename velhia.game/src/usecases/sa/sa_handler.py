import math as m
import random as r
import pandas as pd
import operator as op
import functools as fct
import ttg
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

    return sa | {field: sa[field] + value}


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

    def valid_game(game: GameStatus) -> Union[GameStatus, str]:

        values = [moves[x] for x in filled_positions]
        checklist = [int(game[x]) for x in filled_positions]

        if checklist == values:
            return game
        else:
            return 'invalid'

    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    matrix = ttg.Truths(columns).as_pandas().astype(str).values.sum(axis=1)
    filled_positions = [x for x in range(0, len(moves)) if moves[x] != -1]
    filter_matrix = list(x for x in [valid_game(game) for game in matrix]
                         if x != 'invalid')
    final_matrix = list([int(x) for x in game] for game in filter_matrix)
    enemy_positions = len([x for x in moves if x == sa['enemy'][1]])
    my_positions = len([x for x in moves if x == sa['char'][1]])
    who_begin = sa['enemy'] if enemy_positions > my_positions else sa['char']
    return [move for move in final_matrix if len([x for x in move if x == who_begin[1]]) == 5 and
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
    return len(list(filter(lambda y: y == match_list,
                           [sequence for game in matrix
                            for sequence in sequence_list(game)])))


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
    return len(list(filter(lambda y: y == match_list,
                           [sequence for game in matrix
                            for sequence in sequence_list(game)])))


def highlights(sa: StatisticalAlgorithmAdapter, moves: GameStatus, position: int) -> Tuple[int, int, int, float]:

    matrix = create_matrix(sa, moves)
    victories = count_victories(sa, matrix)
    defeats = count_defeats(sa, matrix)
    ratio = victories / 1 if defeats == 0 else victories / defeats
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
            # new_move_list = op.add(move_list, [(index, moves[index])])
            return move_options(moves, index, value, move_list)

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
