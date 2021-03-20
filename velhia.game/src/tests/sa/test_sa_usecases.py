from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_use_cases import alter_sa, strategy_plan, check_win, check_lose


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


class TestSAUseCases:

    def test_get_sa(self) -> None:
        pass

    def test_alter_sa(self) -> None:

        field = 'matchs'
        value = 1
        new_sa = alter_sa('add')(sa, field, value)
        check_sa = sa
        check_sa['matchs'] = 1
        assert check_sa == new_sa

    def test_strategy_plan(self) -> None:
        position = strategy_plan(sa, [-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4

    def test_check_win(self) -> None:
        position = check_win(sa, [-1, 0, 1, 0, 0, 1, 0, -1, -1])
        assert position == 8

    def test_check_lose(self) -> None:
        position = check_lose(sa, [-1, 0, 1, 0, -1, 1, 0, -1, -1])
        assert position == 0
