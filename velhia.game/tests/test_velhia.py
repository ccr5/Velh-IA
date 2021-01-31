from velhia import Velhia

class TestVelhia:

    def test_play(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.play([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4