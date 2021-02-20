import json
from typing import Union
from datetime import datetime
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.sa.sa_dto import sa_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from shared.objects import create_object


def save_sa(sa_repository: DatabaseRepositoryType, obj: StatisticalAlgorithm) -> StatisticalAlgorithm:

    res: list = sa_repository['create'](obj).json()
    return sa_to_entity(res)


def get_sa(sa_repository: DatabaseRepositoryType) -> Union[StatisticalAlgorithm, None]:

    res: list = sa_repository['get'](offset=0, limit=1).json()

    if len(res) == 1:
        return sa_to_entity(res[0])
    else:
        return None


def update_sa(sa_repository: DatabaseRepositoryType, obj: StatisticalAlgorithm) -> bool:

    res: list = sa_repository['update'](obj['_id'], obj).json()

    if len(res) == 1:
        return True
    else:
        return False


def delete_sa(sa_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: list = sa_repository['delete'](hash).json()

    if len(res) == 1:
        return True
    else:
        return False
