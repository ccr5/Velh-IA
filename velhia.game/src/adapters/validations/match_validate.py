from typing import NoReturn, List
from adapters.controllers.match_controller import check_win
from entities.match.match import Match
from entities.agent.choices import Choices
from usecases.agent.agent_adapter_type import AgentAdapter
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from shared.types.game_status import GameStatus
from shared.errors.validation.validation_error import ValidationError
from shared.errors.validation.match.match_pendent_error import CurrentyMatchIsNotPendent
from shared.errors.validation.match.match_status_error import PreviousMatchHasInvalidStatus
from shared.errors.validation.match.currenty_match_id_error import CurrentyMatchIdIsDifferent
from shared.errors.validation.match.previous_match_id_error import PreviousMatchIdIsDifferent
from shared.errors.validation.match.currenty_match_game_error import CurrentMatchGameIsDifferent
from shared.errors.validation.match.previous_match_game_error import PreviousMatchGameIsDifferent


def check_match_status(match: Match, mas: MultiAgentSystemAdapter, match_type: str, status: List[str]) -> NoReturn:

    if 'WINNER' in status and match['status'] == 'WINNER' and match['winner'] in ['SA', 'MAS'] and match_type == 'previous':
        pass
    elif 'DRAW' in status and match['status'] == 'DRAW' and len(match['plays']) == 9 and match_type == 'previous':
        pass
    elif 'PENDENT' in status and match['status'] == 'PENDENT' and match_type == 'current':
        pass
    else:
        raise SystemError

    if match_type == 'previous':
        status_list = [
            mas['family_leader']['memory'][-2]['environmentReaction'],
            mas['religion_leader']['memory'][-2]['environmentReaction'],
            mas['education_leader']['memory'][-2]['environmentReaction'],
            mas['family_learner']['memory'][-2]['environmentReaction'],
            mas['religion_learner']['memory'][-2]['environmentReaction'],
            mas['education_learner']['memory'][-2]['environmentReaction'],
        ]

        if [
            match['status'], match['status'], match['status'],
            match['status'], match['status'], match['status']
        ] == status_list:
            pass
        else:
            raise PreviousMatchHasInvalidStatus

    elif match_type == 'current':
        status_list = ['environmentReaction' in mas['family_leader']['memory'][-1],
                       'environmentReaction' in mas['religion_leader']['memory'][-1],
                       'environmentReaction' in mas['education_leader']['memory'][-1],
                       'environmentReaction' in mas['family_learner']['memory'][-1],
                       'environmentReaction' in mas['religion_learner']['memory'][-1],
                       'environmentReaction' in mas['education_learner']['memory'][-1]]

        if [False, False, False, False, False, False] == status_list:
            pass
        else:
            raise SystemError

    else:
        raise SystemError


def check_match_id(match: Match, mas: MultiAgentSystemAdapter, match_type: str) -> NoReturn:
    """ Check if all previous objects has the same match id """

    def check_list_func(agent_list: List[AgentAdapter], lenght: int, check_list: List[int] = []) -> List[int]:

        if lenght > 0:
            index: int = lenght - 1

            if 'death' in agent_list[index] and agent_list[index]['life'] <= 0:
                new_check_list: List[int] = check_list + [index]
                return check_list_func(agent_list, index, new_check_list)
            else:
                return check_list_func(agent_list, index, check_list)

        else:
            return check_list

    if match_type == 'previous':
        _id: str = match['_id']
        match_id_list = [_id, _id, _id, _id, _id, _id]
        id_match_list = [mas['family_leader']['memory'][-2]['matchId'],
                         mas['family_learner']['memory'][-2]['matchId'],
                         mas['education_leader']['memory'][-2]['matchId'],
                         mas['education_learner']['memory'][-2]['matchId'],
                         mas['religion_leader']['memory'][-2]['matchId'],
                         mas['religion_learner']['memory'][-2]['matchId']]

        if match_id_list == id_match_list:
            pass
        else:
            new_id_list: List[bool] = [True, True, True, True, True, True]
            updated_id_list: List[bool] = list(
                map(lambda x: new_id_list[x] == False),
                check_list_func([mas['family_leader'], mas['family_learner'],
                                 mas['education_leader'], mas['education_learner'],
                                 mas['religion_leader'], mas['religion_learner']], 6)
            )

            if [
                _id == mas['family_leader']['memory'][-2]['matchId'], _id == mas['family_learner']['memory'][-2]['matchId'],
                _id == mas['education_leader']['memory'][-2]['matchId'], _id == mas['education_learner']['memory'][-2]['matchId'],
                _id == mas['religion_leader']['memory'][-2]['matchId'], _id == mas['religion_learner']['memory'][-2]['matchId']
            ] == updated_id_list:
                pass
            else:
                raise PreviousMatchIdIsDifferent

    elif match_type == 'current':
        id_match_list = [mas['family_leader']['memory'][-1]['matchId'],
                         mas['family_learner']['memory'][-1]['matchId'],
                         mas['education_leader']['memory'][-1]['matchId'],
                         mas['education_learner']['memory'][-1]['matchId'],
                         mas['religion_leader']['memory'][-1]['matchId'],
                         mas['religion_learner']['memory'][-1]['matchId']]

        match_id_list = [match['_id'], match['_id'], match['_id'],
                         match['_id'], match['_id'], match['_id']]

        if match_id_list == id_match_list:
            pass
        else:
            raise CurrentyMatchIdIsDifferent

    else:
        raise SystemError


def check_match_game(game_status: GameStatus, match: Match,
                     mas: MultiAgentSystemAdapter, match_type: str) -> NoReturn:
    """ Check if all currenty objects has the same match game """

    def remove_one(game: GameStatus, lenght: int, ret: List[int] = []) -> GameStatus:

        if len(ret) < len(game):
            index: int = lenght - 1

            if game[index] == 1:
                new_ret: List[int] = ret + [-1]
                return remove_one(game, index, new_ret)
            else:
                new_ret: List[int] = ret + [game[index]]
                return remove_one(game, index, new_ret)

        else:
            return ret

    def add_mas_char(agent_choices: List[Choices], lenght: int, game: GameStatus) -> GameStatus:

        if lenght > 0:
            index: int = lenght - 1
            position: int = agent_choices[index]['position']

            if game[position] == -1:
                new_game: GameStatus = merge_list(
                    game, len(game), position, mas['char'])
                return add_mas_char(agent_choices, len(agent_choices), new_game)
            else:
                return add_mas_char(agent_choices, lenght, game)

        else:
            return game

    if match_type == 'previous':
        game: GameStatus = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        game_plus_family: GameStatus = add_mas_char(
            mas['family_leader']['memory'][-2]['choices'],
            len(mas['family_leader']['memory'][-2]['choices']),
            game
        )
        game_plus_religion: GameStatus = add_mas_char(
            mas['religion_leader']['memory'][-2]['choices'],
            len(mas['religion_leader']['memory'][-2]['choices']),
            game_plus_family
        )
        game_plus_education: GameStatus = add_mas_char(
            mas['education_leader']['memory'][-2]['choices'],
            len(mas['education_leader']['memory'][-2]['choices']),
            game_plus_religion
        )
        final_game = remove_one(game_plus_education, len(game_plus_education))

        if game_status == final_game:
            pass
        else:
            raise PreviousMatchGameIsDifferent

    elif match_type == 'current':
        game: GameStatus = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        game_plus_family: GameStatus = add_mas_char(
            mas['family_leader']['memory'][-1]['choices'],
            len(mas['family_leader']['memory'][-1]['choices']),
            game
        )
        game_plus_religion: GameStatus = add_mas_char(
            mas['religion_leader']['memory'][-1]['choices'],
            len(mas['religion_leader']['memory'][-1]['choices']),
            game_plus_family
        )
        game_plus_education: GameStatus = add_mas_char(
            mas['education_leader']['memory'][-1]['choices'],
            len(mas['education_leader']['memory'][-1]['choices']),
            game_plus_religion
        )
        final_game = remove_one(game_plus_education, len(game_plus_education))

        if game_status == final_game:
            pass
        else:
            raise CurrentMatchGameIsDifferent

    else:
        raise SystemError
