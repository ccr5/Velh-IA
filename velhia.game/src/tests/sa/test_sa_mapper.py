from datetime import datetime
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_mapper import sa_to_entity, sa_to_adapter

sa_adapter: StatisticalAlgorithmAdapter = dict([
    ('birth', '2021-02-21 14:32:09.000Z'),
    ('matchs', 0),
    ('victories', 0),
    ('defeats', 0),
    ('draw', 0),
    ('char', ['X', 1]),
    ('enemy', ['O', 0]),
    ('empty', ['O', 0])
])

sa_entity: StatisticalAlgorithmAdapter = dict([
    ('birth', '2021-02-21 14:32:09.000Z'),
    ('matchs', 0),
    ('victories', 0),
    ('defeats', 0),
    ('draw', 0)
])


class TestSAMapper:

    def test_sa_to_entity(self) -> None:

        new_sa = sa_to_entity(sa_adapter)
        assert sa_entity == new_sa

    def test_sa_to_adapter(self) -> None:

        new_sa = sa_to_adapter(sa_entity)
        assert sa_adapter == new_sa
