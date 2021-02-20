from entities.algorithm.sa import StatisticalAlgorithm
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from shared.objects import create_object


def sa_to_entity(sa_adapter: StatisticalAlgorithmAdapter) -> StatisticalAlgorithm:

    items: list = list(sa_adapter.items())
    return StatisticalAlgorithm(
        create_object(
            items, len(items),
            ['char', 'enemy', 'empty', 'createdAt', 'updatedAt', '__v']
        )
    )


def sa_to_adapter(sa: StatisticalAlgorithm) -> StatisticalAlgorithmAdapter:

    items: list = list(sa.items())
    return StatisticalAlgorithmAdapter(
        create_object(
            key_list=items,
            lenght=len(items),
            filters=['createdAt', 'updatedAt', '__v'],
            obj={
                'char': ['X', 1],
                'enemy': ['O', 0],
                'empty': ['O', 0]
            }
        )
    )
