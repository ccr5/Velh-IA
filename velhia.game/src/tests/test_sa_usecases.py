from adapters.controllers.sa_controller import play_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_use_cases import check_win, check_lose
from usecases.sa.sa_handler import create_matrix, count_defeats, count_victories, sequence_list


sa: StatisticalAlgorithmAdapter = dict([
    ('birth', '2021-02-21 14:32:09.000Z'),
    ('matchs', 0),
    ('victories', 0),
    ('defeats', 0),
    ('draw', 0),
    ('char', ['X', 1]),
    ('enemy', ['O', 0]),
    ('empty', ['O', 0])
])


class TestSA:

    def test_play(self) -> None:
        position = play_sa(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4

    def test_strategy_plan(self) -> None:
        position = play_sa(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4

    def test_create_matrix(self) -> None:
        matrix = create_matrix(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert len(matrix) == 126

    def test_count_victories(self) -> None:
        matrix = create_matrix(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        nVictories = count_victories(sa, matrix)
        assert nVictories == 120

    def test_count_defeats(self) -> None:
        matrix = create_matrix(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        nDefeats = count_defeats(sa, matrix)
        assert nDefeats == 48

    def test_check_win(self) -> None:
        position = check_win(sa, [-1, 0, 1, 0, 0, 1, 0, -1, -1])
        assert position == 8

    def test_check_lose(self) -> None:
        position = check_lose(sa, [-1, 0, 1, 0, -1, 1, 0, -1, -1])
        assert position == 0

    def test_sequence_list(self) -> None:
        ret = sequence_list([-1, 0, 1, 0, -1, 1, 0, -1, -1])
        res = [[-1, 0, 1], [0, -1, 1], [0, -1, -1],
               [-1, 0, 0], [0, -1, -1], [1, 1, -1],
               [-1, -1, -1],   [1, -1, 0]]
        assert ret == res
