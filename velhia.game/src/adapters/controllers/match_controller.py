from typing import Tuple, Union, List, NoReturn
from datetime import datetime
from entities.match.match import Match
from entities.match.play import Play
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.agent.agent_use_cases import get_valid_agents, alter_agent, update_match_status
from usecases.agent.agent_database import get_by_id, get_by_progenitor
from usecases.agent.agent_adapter_type import AgentAdapter
from usecases.mas.mas_dto import convert_mas
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.mas.mas_use_cases import add_new_match, complete_mas, create_mas, update_mas, add_match_response
from usecases.sa.sa_mapper import sa_to_entity, sa_to_adapter
from usecases.sa.sa_use_cases import get_valid_sa, alter_sa
from usecases.sa.sa_database import update_sa
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.match.match_use_cases import create_new_match, alter_match
from usecases.match.match_database import get_current_match, get_last, update_match
from usecases.match.match_mapper import match_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from shared.types.game_status import GameStatus
from ovomaltino.ovomaltino import Ovomaltino


def complete_match(algorithm_db: DatabaseRepositoryType, match: Match
                   ) -> Tuple[Match, StatisticalAlgorithmAdapter, MultiAgentSystemAdapter]:

    sa: StatisticalAlgorithmAdapter = sa_to_adapter(
        get_valid_sa(algorithm_db)
    )

    return (match, sa)


def create_match(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
                 mas: Ovomaltino) -> Tuple[Match, StatisticalAlgorithmAdapter]:

    sa: StatisticalAlgorithmAdapter = sa_to_adapter(get_valid_sa(algorithm_db))
    mas_agents: MultiAgentSystemAdapter = {'char': ('O', 0),
                                           'agents': [agent.data['_id'] for agent in mas.get_leaders()]}
    match: Match = create_new_match(match_db, sa, mas_agents)
    updated_sa: StatisticalAlgorithmAdapter = alter_sa('add')(
        sa, 'matchs', 1
    )
    update_sa(algorithm_db, sa_to_entity(updated_sa))
    return (match, updated_sa)


def start(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
          mas: Ovomaltino) -> Tuple[Match, StatisticalAlgorithmAdapter]:
    """ Prepare all objects to start the game """

    last_match: Union[Match, None] = get_current_match(match_db)

    if last_match is None or last_match['status'] != 'PENDENT':
        return create_match(match_db, algorithm_db, mas)
    else:
        return complete_match(algorithm_db, last_match)


def update_current_match(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
                         family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
                         religion_db: DatabaseRepositoryType, match, sa, mas, sequence, game_status, position, time):
    """ Update a Match object after a play """

    if sequence == 'SA':

        results = sequence_list(list(map(
            lambda x: sa['char'][1] if x == position else game_status[x],
            range(0, len(game_status) - 1)
        )))

        if check_win(sa, results, len(results)):

            match_new_play = alter_match('add')(match, 'plays', {
                'seq': len(match['plays']) + 1,
                'player': sa['_id'],
                'time': time,
                'position': position
            })

            match_end = alter_match('add')(
                match_new_play, 'end',
                datetime.now().ctime()
            )

            match_status = alter_match('change')(match_end, 'status', 'WINNER')
            final_match = alter_match('insert')(match_status, 'winner', 'SA')
            updated_sa = alter_sa('add')(sa, 'victories', 1)
            plays = 5 if match.plays[0]['player'] == 'MAS' else 4
            updated_mas = add_match_response(mas, 'loser', plays)
            update_mas(family_db, religion_db, education_db, updated_mas)

        else:
            final_match = alter_match('add')(match, 'plays', {
                'seq': len(match['plays']) + 1,
                'player': sa['_id'],
                'time': time,
                'position': position
            })

        update_sa(algorithm_db, updated_sa)
        update_match(match_db, final_match)

    elif sequence == 'MAS':

        results = sequence_list(list(map(
            lambda x: sa['enemy'][1] if x == position else game_status[x],
            range(0, len(game_status) - 1)
        )))

        if check_win(mas, results, len(results)):

            match_new_play = alter_match('add')(match, 'plays', {
                'seq': len(match['plays']) + 1,
                'player': 'MAS',
                'time': time,
                'position': position
            })

            match_end = alter_match('add')(
                match_new_play, 'end',
                datetime.now().ctime()
            )

            match_status = alter_match('change')(match_end, 'status', 'WINNER')
            final_match = alter_match('insert')(match_status, 'winner', 'MAS')
            updated_sa = alter_sa('add')(sa, 'defeats', 1)
            updated_mas = add_match_response(mas, 'winner', 0)
            update_sa(algorithm_db, updated_sa)

        else:
            final_match = alter_match('add')(match, 'plays', {
                'seq': len(match['plays']) + 1,
                'player': 'MAS',
                'time': time,
                'position': position
            })

        update_mas(family_db, religion_db, education_db, updated_mas)
        update_match(match_db, final_match)

    else:
        raise SystemError


def check_draw(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
               family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
               religion_db: DatabaseRepositoryType, match: Match,
               sa: StatisticalAlgorithmAdapter, mas: MultiAgentSystemAdapter) -> NoReturn:
    """
    Check if the match is draw and update all datas
    :param match: `Match` a Match object
    :param sa: `Statistical Algorithm` a Statistical Algorithm object
    :param mas: `Multi Agent System` a Multi Agent System object

    usage
    >>> from velhia import Velhia
    >>> velhia.check_draw(match, sa, mas)
    """

    if len(match['plays']) == 9 and match['status'] == 'PENDENT':
        match_end = alter_match('add')(
            match, 'end',
            datetime.now().ctime()
        )
        final_match = alter_match('change')(match_end, 'status', 'DRAW')
        updated_sa = alter_sa('add')(sa, 'draw', 1)
        updated_mas = add_match_response(mas, 'draw', 0)
        update_mas(family_db, religion_db, education_db, updated_mas)
        update_sa(algorithm_db, updated_sa)
        update_match(match_db, final_match)

    else:
        pass


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
                new_game = list(map(lambda x: 1 if x == position else game[x],
                                    range(0, len(game) - 1)))
                return fill_game_status(plays, index, new_game)
            else:
                position = plays[index]['position']
                new_game = list(map(lambda x: 0 if x == position else game[x],
                                    range(0, len(game) - 1)))
                return fill_game_status(plays, index, new_game)
        else:
            return game

    game_status = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    return fill_game_status(match['plays'], len(match['plays']), game_status)
