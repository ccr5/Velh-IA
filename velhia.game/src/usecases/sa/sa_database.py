import json
from typing import Union
from usecases.database.database_types import DatabaseRepositoryType
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.sa.sa_dto import sa_to_entity


def get_sa(sa_repository: DatabaseRepositoryType) -> Union[StatisticalAlgorithm, None]:

    res: list = sa_repository['get'](offset=0, limit=1).json()

    if len(res) == 1:
        if isinstance(res[0], StatisticalAlgorithm):
            return sa_to_entity(res[0])
        else:
            raise SystemError
    else:
        return None


def update_sa(sa_repository: DatabaseRepositoryType, obj: StatisticalAlgorithm) -> bool:

    res: list = sa_repository['update'](obj['_id'], json.dumps(obj))

    if len(res) == 1 and isinstance(res[0], StatisticalAlgorithm):
        return True
    else:
        return False


def delete_sa(sa_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: list = sa_repository['delete'](hash).json()

    if len(res) == 1 and isinstance(res[0], StatisticalAlgorithm):
        return True
    else:
        return False
