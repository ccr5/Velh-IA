from adapters.controllers.sa_controller import play_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter


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


class TestSAController:

    def test_play(self) -> None:
        position = play_sa(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4
