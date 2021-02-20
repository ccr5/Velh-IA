from typing import Tuple, Union
from datetime import datetime
from entities.match.match import Match
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.mas.mas_use_cases import add_new_match
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.mas.mas_database import complete_mas, create_mas, update_mas
from usecases.sa.sa_dto import sa_to_repository
from usecases.sa.sa_database import get_valid_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.database.database_types import DatabaseRepositoryType
from usecases.agent.agent_use_cases import alter
from usecases.agent.agent_database import get_by_id, get_by_progenitor, get_valid_agents
from usecases.agent.agent_dto import agent_to_repository
from usecases.match.match_database import get_current_match, save_match
from shared.objects import create_object
from usecases.match.match_dto import match_to_entity


def start(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
          family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
          religion_db: DatabaseRepositoryType) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:
    """ Prepare all objects to start the game """

    def complete_match(match: Match) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_repository(
            get_valid_sa(algorithm_db)
        )

        mas: MultiAgentSystemAdapter = complete_mas(
            family_db, religion_db,
            education_db, match, 'repository'
        )

        return (match, sa, mas)

    def create_match() -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_repository(
            get_valid_sa(algorithm_db)
        )

        mas: MultiAgentSystemAdapter = create_mas(
            family_db, religion_db, education_db
        )

        match: Match = save_match(
            match_db, create_object(
                [
                    ("begin", datetime.now().ctime()),
                    ("time", 0),
                    ("sa", {
                        "playerId": sa['_id'],
                        "symbol": sa['char'][0]
                    }),
                    ("mas", {"family": {"playerId": mas['family_leader']['_id'], "symbol": mas['char'][0]},
                             "religion": {"playerId": mas['religion_leader']['_id'], "symbol": mas['char'][0]},
                             "education": {"playerId": mas['education_leader']['_id'], "symbol": mas['char'][0]}}),
                    ("plays", []),
                    ("status", "PENDENT")
                ], 6
            )
        )

        updated_mas: MultiAgentSystemAdapter = add_new_match(mas, match)
        update_mas(family_db, religion_db, education_db, updated_mas)

    last_match: Union[Match, None] = get_current_match(match_db)

    if last_match is None or last_match['status'] != 'PENDENT':
        return create_match()
    else:
        return complete_match(last_match)
