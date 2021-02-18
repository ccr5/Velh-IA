from classes.statistical_algorithm import StatisticalAlgorithm


class TestSA:

    def test_play(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.play([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4

    def test_strategy_plan(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.play([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4

    def test_create_matrix(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        matrix = sa.create_matrix([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert len(matrix) == 126

    def test_count_victories(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        matrix = sa.create_matrix([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        nVictories = sa.count_victories(matrix)
        assert nVictories == 120

    def test_count_defeats(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        matrix = sa.create_matrix([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        nDefeats = sa.count_defeats(matrix)
        assert nDefeats == 48

    def test_check_win(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.check_win([-1, 0, 1, 0, 0, 1, 0, -1, -1])
        assert position == 8

    def test_check_lose(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.check_lose([-1, 0, 1, 0, -1, 1, 0, -1, -1])
        assert position == 0

    def test_sequence_list(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        ret = sa.sequence_list([-1, 0, 1, 0, -1, 1, 0, -1, -1])
        res = [[-1, 0, 1], [0, -1, 1], [0, -1, -1],
               [-1, 0, 0], [0, -1, -1], [1, 1, -1],
               [-1, -1, -1],   [1, -1, 0]]
        assert ret == res
