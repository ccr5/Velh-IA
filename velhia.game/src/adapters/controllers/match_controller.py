from typing import Tuple, Union
from datetime import datetime
from entities.match.match import Match
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.agent.agent_use_cases import alter
from usecases.agent.agent_database import get_by_id, get_by_progenitor
from usecases.agent.agent_use_cases import get_valid_agents
from usecases.mas.mas_dto import convert_mas
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.mas.mas_use_cases import add_new_match, complete_mas, create_mas, update_mas
from usecases.sa.sa_dto import sa_to_adapter
from usecases.sa.sa_use_cases import get_valid_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.match.match_use_cases import create_new_match
from usecases.match.match_database import get_current_match
from usecases.match.match_dto import match_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from shared.objects import create_object


def start(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
          family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
          religion_db: DatabaseRepositoryType) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:
    """ Prepare all objects to start the game """

    def complete_match(match: Match) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_adapter(
            get_valid_sa(algorithm_db)
        )

        mas: MultiAgentSystemAdapter = complete_mas(
            family_db, religion_db,
            education_db, match, 'repository'
        )

        return (match, sa, mas)

    def create_match() -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

        sa: StatisticalAlgorithmAdapter = sa_to_adapter(
            get_valid_sa(algorithm_db)
        )

        mas: MultiAgentSystemAdapter = convert_mas(
            create_mas(family_db, religion_db, education_db),
            'repository'
        )

        match: Match = create_new_match(match_db, sa, mas)
        updated_mas: MultiAgentSystemAdapter = add_new_match(mas, match)
        update_mas(family_db, religion_db, education_db, updated_mas)
        return (match, sa, mas)

    last_match: Union[Match, None] = get_current_match(match_db)

    if last_match is None or last_match['status'] != 'PENDENT':
        return create_match()
    else:
        return complete_match(last_match)


def validate(match, sa, mas):
    """
    Check if everything ran correctly
    :param match: `Match` Match obj
    :param sa: `Statistical Algorithm` Statistical Algorithm obj
    :param mas: `Multi Agent System` Multi Agent System obj

        Previous
        1. Check if the previous match has a status in ['WINNER', 'DRAW']
        2. Check if the previous players memory is the previous match
        3. Check if the previous match status is the previous environment status in the previous players memory
        4. Check if the plays in previous match obj is equals previous players memories
        5. Check if the number of players matchs is correctly (victories, defeats, draws)

        Currenty
        1. Check if the currenty match status is pendent
        2. Check if the last match of institutions leaders is equals the currenty match
        3. Check if the plays in match obj is equals players memories
        4. Check if the number of players matchs is correctly (victories, defeats, draws)

    usage
    >>> from velhia import Velhia
    >>> vlh = Velhia(match_db, family_db, education_db, religion_db, algorithm_db)
    >>> vlh.validate_previous_match()
    True or False
    """

    if len(match_db.get(offset=0, limit=2).json()) > 1:

        # Previous
        previous_match = Match(match_db.get(
            offset=1, limit=1, sort='createdAt:desc').json()[0])
        previous_sa = StatisticalAlgorithm(algorithm_db.get(
            filters={"_id": previous_match.sa['playerId']}).json()[0], ['X', 1], ['O', 0])
        previous_family = Agent(family_db.get(
            filters={"_id": previous_match.mas['family'][-1]['playerId']}).json()[0], ['O', 0])
        previous_religion = Agent(religion_db.get(
            filters={"_id": previous_match.mas['religion'][-1]['playerId']}).json()[0], ['O', 0])
        previous_education = Agent(education_db.get(
            filters={"_id": previous_match.mas['education'][-1]['playerId']}).json()[0], ['O', 0])

        check_match_status(previous_match, previous_family,
                           previous_religion, previous_education)
        check_previous_match_id(previous_match, previous_family,
                                previous_religion, previous_education)
        game_status = game_status(
            previous_match, previous_sa.id)
        check_previous_match_game(game_status, previous_match, previous_family,
                                  previous_religion, previous_education)
        check_sa_matchs(previous_sa)
        [check_agent_matchs(x) for x in [previous_family,
                                         previous_religion,
                                         previous_education]]

        # Currenty
        check_match_pendent(match)
        check_currenty_match_id(match, mas.family_leader,
                                mas.religion_leader, mas.education_leader)
        game_status = game_status(match, sa.id)
        check_currenty_match_game(game_status, mas.family_leader,
                                  mas.religion_leader, mas.education_leader)
        check_sa_matchs(sa)
        [check_agent_matchs(x) for x in [mas.family_leader,
                                         mas.religion_leader,
                                         mas.education_leader]]
    else:

        # Currenty
        check_match_pendent(match)
        check_currenty_match_id(match, mas.family_leader,
                                mas.religion_leader, mas.education_leader)
        game_status = game_status(match, sa.id)
        check_currenty_match_game(game_status, mas.family_leader,
                                  mas.religion_leader, mas.education_leader)
        check_sa_matchs(sa)
        [check_agent_matchs(x) for x in [mas.family_leader,
                                         mas.religion_leader,
                                         mas.education_leader]]
