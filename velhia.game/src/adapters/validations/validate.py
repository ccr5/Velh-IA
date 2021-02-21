from typing import NoReturn, Union, List
from adapters.controllers.match_controller import complete_match, current_game_status
from adapters.validations.match_validate import check_match_status, check_match_id, check_match_game
from adapters.validations.player_validate import check_sa_matchs, check_agent_matchs
from entities.match.match import Match
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.match.match_database import get_last
from usecases.database.database_types import DatabaseRepositoryType


def previous_match_validate(match: Match, sa: StatisticalAlgorithmAdapter,
                            mas: MultiAgentSystemAdapter) -> NoReturn:

    check_match_status(match, mas, 'previous', ['DRAW', 'WINNER'])
    check_match_id(match, mas, 'previous')
    # check_match_game(current_game_status(match, sa['id']),
    #                  match, mas, 'previous')
    check_sa_matchs(sa)
    map(check_agent_matchs, [
        mas['family_leader'], mas['family_learner'],
        mas['religion_leader'], mas['religion_learner'],
        mas['education_leader'], mas['education_learner'],
    ])


def current_match_validate(match: Match, sa: StatisticalAlgorithmAdapter,
                           mas: MultiAgentSystemAdapter) -> NoReturn:

    check_match_status(match, mas, 'current', ['PENDENT'])
    check_match_id(match, mas, 'current')
    # check_match_game(current_game_status(match, sa['id']),
    #                  match, mas, 'current')
    check_sa_matchs(sa)
    map(check_agent_matchs, [
        mas['family_leader'], mas['family_learner'],
        mas['religion_leader'], mas['religion_learner'],
        mas['education_leader'], mas['education_learner'],
    ])


def validate(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
             family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
             religion_db: DatabaseRepositoryType, match: Match, sa: StatisticalAlgorithmAdapter,
             mas: MultiAgentSystemAdapter) -> NoReturn:
    """
    Check if everything ran correctly

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
    """

    matchs: Union[List[Match], None] = get_last(match_db, 2)

    if matchs is None:
        raise SystemError

    elif len(matchs) > 1:
        (previous_match, previous_sa, previous_mas) = complete_match(
            algorithm_db, family_db, education_db, religion_db, matchs[0]
        )

        previous_match_validate(previous_match, previous_sa, previous_mas)
        current_match_validate(match, sa, mas)

    else:
        current_match_validate(match, sa, mas)
