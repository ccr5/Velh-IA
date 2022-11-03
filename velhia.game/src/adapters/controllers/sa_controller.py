from datetime import datetime
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_use_cases import check_win, check_lose, strategy_plan
from shared.types.game_status import GameStatus
from shared.errors.statistical_algorithm.play_error import PlayError


def play_sa(sa: StatisticalAlgorithmAdapter, moves: GameStatus) -> int:
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
    winner = check_win(sa, moves)
    loser = check_lose(sa, moves)

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
        position = strategy_plan(sa, moves)
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        return position

    else:
        raise PlayError
