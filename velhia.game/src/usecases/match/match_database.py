from typing import Union, List
from entities.match.match import Match
from usecases.match.match_dto import match_to_entity
from usecases.database.database_types import DatabaseRepositoryType


def save_match(match_repository: DatabaseRepositoryType, obj: Match) -> Match:

    res: list = match_repository['create'](obj).json()
    return match_to_entity(res)


def get_current_match(match_repository: DatabaseRepositoryType) -> Union[Match, None]:

    res: list = match_repository['get'](
        offset=0, limit=1, sort="createdAt:desc"
    ).json()

    if len(res) == 1:
        return match_to_entity(res[0])
    else:
        return None


def get_last(match_repository: DatabaseRepositoryType, num: int) -> Union[List[Match], None]:

    res: list = match_repository['get'](offset=0, limit=num,
                                        sort="createdAt:desc").json()

    if len(res) > 0:
        return list(map(match_to_entity, res))
    else:
        None


def update_match(match_repository: DatabaseRepositoryType, obj: Match) -> bool:

    res: list = match_repository['update'](obj['_id'], obj).json()

    if len(res) == 1:
        return True
    else:
        return False


def delete_match(match_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: list = match_repository['delete'](hash).json()

    if len(res) == 1:
        return True
    else:
        return False
