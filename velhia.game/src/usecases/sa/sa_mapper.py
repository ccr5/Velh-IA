from typing import List
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter


def sa_to_entity(sa_adapter: StatisticalAlgorithmAdapter) -> StatisticalAlgorithm:

    filters: List[str] = ['char', 'enemy', 'empty',
                          'createdAt', 'updatedAt', '__v']
    return {k: v for k, v in sa_adapter.items() if k not in filters}


def sa_to_adapter(sa: StatisticalAlgorithm) -> StatisticalAlgorithmAdapter:

    new_keys = {'char': ['X', 1], 'enemy': ['O', 0], 'empty': ['O', 0]}
    return sa | new_keys
