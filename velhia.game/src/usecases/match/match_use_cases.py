from datetime import datetime
from typing import Callable
from entities.match.match import Match
from usecases.match.match_database import save_match
from usecases.match.match_handler import add, insert_or_change
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter


def create_new_match(match_db: DatabaseRepositoryType, sa: StatisticalAlgorithmAdapter,
                     mas: MultiAgentSystemAdapter) -> Match:

    empty_match: Match = dict([
        ("begin", datetime.now().ctime()),
        ("time", 0),
        ("sa", {
            "playerId": sa['_id'],
            "symbol": sa['char'][0]
        }),
        ("mas", [
            {"playerId": mas['family_leader']
                ['_id'], "symbol": mas['char'][0]},
            {"playerId": mas['religion_leader']
                ['_id'], "symbol": mas['char'][0]},
            {"playerId": mas['education_leader']
                ['_id'], "symbol": mas['char'][0]}]),
        ("plays", []),
        ("status", "PENDENT")
    ])

    return save_match(match_db, empty_match)


def alter_match(operation: str) -> Callable:

    if operation == 'add':
        return add
    elif operation == 'insert':
        return insert_or_change
    elif operation == 'change':
        return insert_or_change
    else:
        raise SystemError
