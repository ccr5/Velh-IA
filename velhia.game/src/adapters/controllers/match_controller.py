from typing import Tuple, Union
from datetime import datetime
from entities.match.match import Match
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.sa.sa_dto import sa_to_repository
from usecases.sa.sa_database import get_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.database.database_types import DatabaseRepositoryType
from usecases.agent.agent_use_cases import alter
from usecases.agent.agent_database import get_by_id, get_by_progenitor, get_valid_agents
from usecases.agent.agent_dto import agent_to_repository
from usecases.match.match_database import get_current_match, save_match
from shared.objects import create_object


def start(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
          family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
          religion_db: DatabaseRepositoryType) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:
    """ Prepare all objects to start the game """

    def complete_match(match: Match) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_repository(
            get_sa(algorithm_db)
        )

        mas: MultiAgentSystemAdapter = MultiAgentSystemAdapter({
            'char': ['O', 0],
            'family_leader': agent_to_repository(get_by_id(family_db, match['mas']['family'][-1]['playerId'])),
            'family_learner': agent_to_repository(get_by_progenitor(family_db, match['mas']['family'][-1]['playerId'])),
            'education_leader': agent_to_repository(get_by_id(education_db, match['mas']['education'][-1]['playerId'])),
            'education_learner': agent_to_repository(get_by_progenitor(education_db, match['mas']['education'][-1]['playerId'])),
            'religion_leader': agent_to_repository(get_by_id(religion_db, match['mas']['religion'][-1]['playerId'])),
            'religion_learner': agent_to_repository(get_by_progenitor(religion_db, match['mas']['religion'][-1]['playerId']))
        })

        return (match, sa, mas)

    def create_match() -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_repository(
            get_sa(algorithm_db)
        )

        [family_leader, family_learner] = get_valid_agents(family_db)
        [education_leader, education_learner] = get_valid_agents(education_db)
        [religion_leader, religion_learner] = get_valid_agents(religion_db)

        family_leader_match = alter(family_leader, 'matchsAsLeader', 'add', 1)
        family_learner_match = alter(family_learner, 'matchsAsLearner',
                                     'add', 1)

        education_leader_match = alter(education_leader, 'matchsAsLeader',
                                       'add', 1)
        education_learner_match = alter(education_learner, 'matchsAsLearner',
                                        'add', 1)

        religion_leader_match = alter(religion_leader, 'matchsAsLeader',
                                      'add', 1)
        religion_learner_match = alter(religion_learner, 'matchsAsLearner',
                                       'add', 1)

        mas: MultiAgentSystemAdapter = MultiAgentSystemAdapter({
            'char': ['O', 0],
            'family_leader': family_leader_match,
            'family_learner': family_learner_match,
            'education_leader': education_leader_match,
            'education_learner': education_learner_match,
            'religion_leader': religion_leader_match,
            'religion_learner': religion_learner_match
        })

        match: Match = save_match(match_db, create_object(
            [
                ("begin", datetime.now().ctime()),
                ("time", 0),
                ("sa", {"playerId": sa['_id'], "symbol": sa['char'][0]}),
                ("mas", {"family": {"playerId": mas['family_leader']['_id'], "symbol": mas['char'][0]},
                         "religion": {"playerId": mas['religion_leader']['_id'], "symbol": mas['char'][0]},
                         "education": {"playerId": mas['education_leader']['_id'], "symbol": mas['char'][0]}}),
                ("plays", []),
                ("status", "PENDENT")
            ], 6
        ))

    last_match: Union[Match, None] = get_current_match(match_db)

    if last_match is None or last_match[0]['status'] != 'PENDENT':
        return create_match()
    else:
        return complete_match(last_match)
