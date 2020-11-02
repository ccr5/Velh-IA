from statistical_algorithm import StatisticalAlgorithm


class TestStatisticalAlgorithm(unittest.TestCase):

    def test_play(self):
        obj = {}
        my_char = ('X', 1)
        my_enemy = ('O', 0)
        sa = StatisticalAlgorithm(obj, my_char, my_enemy)
        position = sa.play([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        self.assertEqual(position, 4)
