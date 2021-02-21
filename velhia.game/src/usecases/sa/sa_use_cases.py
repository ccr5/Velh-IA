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


def strategy_plan(moves):
    """
    Find the best position to play using game status
    :param moves: game status
    :return: `int` int

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> position = sa.strategy_plan([-1,1,1,0,0,0,-1,-1,-1])
    >>> position
    0
    """

    try:
        best_position = [-1, -10]
        victory = 0
        defeats = 0

        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = char[1]
                matrix = create_matrix(moves)
                number_victories = count_victories(matrix)
                number_defeats = count_defeats(matrix)

                if number_defeats == 0:
                    number_defeats = 1
                else:
                    pass

                ratio = (number_victories / number_defeats)

                if best_position[1] > ratio:
                    pass

                elif best_position[1] == ratio:

                    if number_victories > victory:
                        best_position[0] = x
                        best_position[1] = ratio
                        victory = number_victories
                        defeats = number_defeats
                    else:
                        pass

                elif best_position[1] < ratio:
                    best_position[0] = x
                    best_position[1] = ratio
                    victory = number_victories
                    defeats = number_defeats

                else:
                    pass

                moves[x] = -1

            else:
                pass

        return best_position[0]

    except:
        raise StrategyPlanError


def create_matrix(moves):
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

    try:

        matrix = []
        empty_position = len([x for x in moves if x == -1])
        who_begin = enemy if len([x for x in moves if x == enemy[1]]) > len(
            [x for x in moves if x == char[1]]) else char
        number_variations = 2 ** empty_position

        while len(matrix) != number_variations:
            new_moves = []

            for x in range(0, len(moves)):

                new_moves.append(r.choice(
                    [char[1], enemy[1]])) if moves[x] == -1 else new_moves.append(moves[x])

            if new_moves in matrix:
                del new_moves
            else:
                matrix.append(new_moves)
                del new_moves

        return [move for move in matrix if len([x for x in move if x == who_begin[1]]) == 5 and
                len([o for o in move if o != who_begin[1] and o != -1]) == 4]

    except:
        raise CreateMatrixError


def count_victories(matrix):
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

    try:

        result = 0

        for x in matrix:
            checklist = sequence_list(x)

            for y in checklist:

                if y == [char[1], char[1], char[1]]:
                    result += 1
                else:
                    pass

        return result

    except:
        raise CountError


def count_defeats(matrix):
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

    try:

        result = 0

        for x in matrix:
            checklist = sequence_list(x)

            for y in checklist:

                if y == [enemy[1], enemy[1], enemy[1]]:
                    result += 1
                else:
                    pass

        return result

    except:
        raise CountError


def check_win(moves):
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

    try:

        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = char[1]
                checklist = sequence_list(moves)

                for y in checklist:

                    if y == [char[1], char[1], char[1]]:
                        return x
                    else:
                        moves[x] = -1
            else:
                pass

    except:
        raise CheckError


def check_lose(moves):
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

    try:

        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = enemy[1]
                checklist = sequence_list(moves)

                for y in checklist:

                    if y == [enemy[1], enemy[1], enemy[1]]:
                        return x
                    else:
                        moves[x] = -1
            else:
                pass

    except:
        raise CheckError
