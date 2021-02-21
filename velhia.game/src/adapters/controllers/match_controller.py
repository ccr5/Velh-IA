from typing import Tuple, Union, List, NoReturn
from datetime import datetime
from entities.match.match import Match
from entities.match.play import Play
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.agent.agent_use_cases import get_valid_agents
from usecases.agent.agent_database import get_by_id, get_by_progenitor
from usecases.agent.agent_adapter_type import AgentAdapter
from usecases.mas.mas_dto import convert_mas
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.mas.mas_use_cases import add_new_match, complete_mas, create_mas, update_mas
from usecases.sa.sa_dto import sa_to_entity, sa_to_adapter
from usecases.sa.sa_use_cases import get_valid_sa, alter_sa
from usecases.sa.sa_database import update_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.match.match_use_cases import create_new_match
from usecases.match.match_database import get_current_match, get_last
from usecases.match.match_dto import match_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from shared.list import merge_list
from shared.objects import create_object
from shared.types.game_status import GameStatus


def complete_match(algorithm_db: DatabaseRepositoryType, family_db: DatabaseRepositoryType,
                   education_db: DatabaseRepositoryType, religion_db: DatabaseRepositoryType,
                   match: Match) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

    sa: StatisticalAlgorithmAdapter = sa_to_adapter(
        get_valid_sa(algorithm_db)
    )

    mas: MultiAgentSystemAdapter = complete_mas(
        family_db, religion_db,
        education_db, match, 'repository'
    )

    return (match, sa, mas)


def create_match(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
                 family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
                 religion_db: DatabaseRepositoryType) -> Tuple[
                     Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

    sa: StatisticalAlgorithmAdapter = sa_to_adapter(get_valid_sa(algorithm_db))
    mas: MultiAgentSystemAdapter = convert_mas(
        create_mas(family_db, religion_db, education_db),
        'adapter'
    )
    match: Match = create_new_match(match_db, sa, mas)
    updated_sa: StatisticalAlgorithmAdapter = alter_sa('add')(
        sa, 'matchs', 1
    )
    updated_mas: MultiAgentSystemAdapter = add_new_match(mas, match)
    update_sa(algorithm_db, sa_to_entity(updated_sa))
    update_mas(family_db, religion_db, education_db,
               convert_mas(updated_mas, 'agent'))
    return (match, updated_sa, updated_mas)


def start(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
          family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
          religion_db: DatabaseRepositoryType) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:
    """ Prepare all objects to start the game """

    last_match: Union[Match, None] = get_current_match(match_db)

    if last_match is None or last_match['status'] != 'PENDENT':
        return create_match(match_db, algorithm_db, family_db, education_db, religion_db)
    else:
        return complete_match(algorithm_db, family_db, education_db, religion_db, last_match)


def check_win(player: Union[AgentAdapter, StatisticalAlgorithmAdapter],
              moves: List[GameStatus], lenght: int) -> Union[NoReturn, bool]:
    """ Check and return a position to win """

    if lenght > 0:

        index = lenght - 1
        if moves[index] == [player['char'][-1], player['char'][-1], player['char'][-1]]:
            return True
        else:
            return check_win(player, moves, index)

    else:
        pass


def sequence_list(game_status: GameStatus) -> List[Tuple[int, int, int]]:
    """ All sequence to win """

    return [[game_status[0], game_status[1], game_status[2]],
            [game_status[3], game_status[4], game_status[5]],
            [game_status[6], game_status[7], game_status[8]],
            [game_status[0], game_status[3], game_status[6]],
            [game_status[1], game_status[4], game_status[7]],
            [game_status[2], game_status[5], game_status[8]],
            [game_status[0], game_status[4], game_status[8]],
            [game_status[2], game_status[4], game_status[6]]]


def get_sequence(match_db: DatabaseRepositoryType, match: Match) -> List[str]:

    matchs: List[Match] = get_last(match_db, 2)

    if matchs is not None and len(matchs) > 1:
        last_match: Match = matchs[1]
    else:
        last_match = None

    if len(match['plays']) == 0 and last_match is None:
        return ['SA']
    elif len(match['plays']) == 0 and len(matchs) > 1:
        return ['MAS' if last_match['sa']['playerId'] == last_match['plays'][0]['player'] else 'SA']
    else:
        return ['MAS' if match['sa']['playerId'] == match['plays'][-1]['player'] else 'SA']


def current_game_status(match: Match, saId: str):
    """ Return a list with all plays of the match """

    def fill_game_status(plays: List[Play], lenght: int, game: List[int]) -> List[int]:

        if lenght > 0:
            index = lenght - 1
            if plays[index]['player'] == saId:
                position = plays[index]['position']
                return fill_game_status(plays, index, merge_list(
                    game, len(game), position, 1
                ))
            else:
                position = plays[index]['position']
                return fill_game_status(plays, index, merge_list(
                    game, len(game), position, 0
                ))
        else:
            return game

    game_status = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    return fill_game_status(match['plays'], len(match['plays']), game_status)
