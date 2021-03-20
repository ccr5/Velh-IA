from itertools import repeat
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_handler import create_matrix, add, sequence_list, count_defeats, count_victories
from usecases.sa.sa_handler import highlights, move_options, find_best_ratio


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


class TestSAHandler:

    def test_create_sa(self) -> None:
        pass

    def test_add(self) -> None:

        field = 'matchs'
        value = 1
        new_sa = add(sa, field, value)
        check_sa = sa
        check_sa['matchs'] = 1
        assert check_sa == new_sa

    def test_sequence_list(self) -> None:
        ret = sequence_list([-1, 0, 1, 0, -1, 1, 0, -1, -1])
        res = [[-1, 0, 1], [0, -1, 1], [0, -1, -1],
               [-1, 0, 0], [0, -1, -1], [1, 1, -1],
               [-1, -1, -1],   [1, -1, 0]]
        assert ret == res

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

    def test_highlights(self) -> None:

        results = highlights(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1], 4)
        assert results == (4, 120, 48, 2.5)

    def test_move_options(self) -> None:

        move_list = move_options([-1, -1, -1, -1, -1, -1, -1, -1, -1], 9, 1)
        result = [(8, [-1, -1, -1, -1, -1, -1, -1, -1, 1]),
                  (7, [-1, -1, -1, -1, -1, -1, -1, 1, -1]),
                  (6, [-1, -1, -1, -1, -1, -1, 1, -1, -1]),
                  (5, [-1, -1, -1, -1, -1, 1, -1, -1, -1]),
                  (4, [-1, -1, -1, -1, 1, -1, -1, -1, -1]),
                  (3, [-1, -1, -1, 1, -1, -1, -1, -1, -1]),
                  (2, [-1, -1, 1, -1, -1, -1, -1, -1, -1]),
                  (1, [-1, 1, -1, -1, -1, -1, -1, -1, -1]),
                  (0, [1, -1, -1, -1, -1, -1, -1, -1, -1])]
        assert move_list == result

    def test_find_best_ratio(self) -> None:

        options = move_options([-1, -1, -1, -1, -1, -1, -1, -1, -1], 9, 1)
        positions_options = list(map(lambda x: x[0], options))
        moves_options = list(map(lambda x: x[1], options))
        highlight_list = list(
            map(highlights, repeat(sa), moves_options, positions_options)
        )
        result = find_best_ratio(highlight_list, len(highlight_list))
        assert (4, 80, 20, 4) == result
