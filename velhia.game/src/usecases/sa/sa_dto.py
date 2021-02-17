from src.shared.objects import create_object
from src.shared.lists import concat_list
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter


def to_entity(sa_adapter: StatisticalAlgorithmAdapter) -> StatisticalAlgorithm:

    items: list = list(sa_adapter.items())
    return StatisticalAlgorithm(
        create_object(
            items, len(items),
            ['char', 'enemy', 'empty']
        )
    )


def to_repository(sa: StatisticalAlgorithm) -> StatisticalAlgorithmAdapter:

    items: list = concat_list(
        sa.items(),
        [('char', ['X', 1]), ('enemy', ['O', 0]), ('empty', ['', -1])]
    )

    return StatisticalAlgorithmAdapter(
        create_object(
            items, len(items)
        )
    )
