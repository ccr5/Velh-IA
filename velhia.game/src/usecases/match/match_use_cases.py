from datetime import datetime
from typing import Callable
from entities.match.match import Match
from usecases.match.match_database import save_match
from usecases.match.match_handler import add, insert, change
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from shared.objects import create_object


def create_new_match(match_db: DatabaseRepositoryType, sa: StatisticalAlgorithmAdapter,
                     mas: MultiAgentSystemAdapter) -> Match:

    return save_match(
        match_db, create_object(
            [
                ("begin", datetime.now().ctime()),
                ("time", 0),
                ("sa", {
                    "playerId": sa['_id'],
                    "symbol": sa['char'][0]
                }),
                ("mas", {"family": [{"playerId": mas['family_leader']['_id'], "symbol": mas['char'][0]}],
                         "religion": [{"playerId": mas['religion_leader']['_id'], "symbol": mas['char'][0]}],
                         "education": [{"playerId": mas['education_leader']['_id'], "symbol": mas['char'][0]}]}),
                ("plays", []),
                ("status", "PENDENT")
            ], 6
        )
    )


def alter_match(operation: str) -> Callable:

    if operation == 'add':
        return add
    elif operation == 'insert':
        return insert
    elif operation == 'change':
        return change
    else:
        raise SystemError
