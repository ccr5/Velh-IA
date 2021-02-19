import json
from typing import Union
from usecases.match.match_dto import match_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from entities.match.match import Match


def save_match(match_repository: DatabaseRepositoryType, obj: Match) -> Match:

    return match_to_entity(match_repository['create'](obj).json()[0])


def get_current_match(match_repository: DatabaseRepositoryType) -> Union[Match, None]:

    res: list = match_repository['get'](
        offset=0, limit=1, sort="createdAt:desc"
    ).json()

    if len(res) == 1:
        if isinstance(res[0], Match):
            return match_to_entity(res[0])
        else:
            raise SystemError
    else:
        return None


def update_match(match_repository: DatabaseRepositoryType, obj: Match) -> bool:

    res: list = match_repository['update'](obj['_id'], json.dumps(obj))

    if len(res) == 1 and isinstance(res[0], Match):
        return True
    else:
        return False


def delete_match(match_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: list = match_repository['delete'](hash).json()

    if len(res) == 1 and isinstance(res[0], Match):
        return True
    else:
        return False
