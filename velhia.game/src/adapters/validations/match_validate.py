from typing import NoReturn, List
from adapters.controllers.match_controller import check_win
from entities.match.match import Match
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from shared.errors.validation.validation_error import ValidationError
from shared.errors.validation.match.match_pendent_error import CurrentyMatchIsNotPendent
from shared.errors.validation.match.match_status_error import PreviousMatchHasInvalidStatus
from shared.errors.validation.match.currenty_match_id_error import CurrentyMatchIdIsDifferent
from shared.errors.validation.match.previous_match_id_error import PreviousMatchIdIsDifferent
from shared.errors.validation.match.currenty_match_game_error import CurrentMatchGameIsDifferent
from shared.errors.validation.match.previous_match_game_error import PreviousMatchGameIsDifferent


def check_match_status(match: Match, mas: MultiAgentSystemAdapter,
                       match_type: str, status: List[str]) -> NoReturn:

    if 'WINNER' in status and match['status'] == 'WINNER' and match['winner'] in ['SA', 'MAS'] and match_type == 'previous':
        pass
    elif 'DRAW' in status and match['status'] == 'DRAW' and len(match['plays']) == 9 and match_type == 'previous':
        pass
    elif 'PENDENT' in status and match['status'] == 'PENDENT' and match_type == 'current':
        pass
    else:
        raise PreviousMatchHasInvalidStatus

    if match_type == 'previous':
        status_list = [
            mas['family_leader']['memory'][-2]['environmentReaction'],
            mas['religion_leader']['memory'][-2]['environmentReaction'],
            mas['education_leader']['memory'][-2]['environmentReaction'],
            mas['family_learner']['memory'][-2]['environmentReaction'],
            mas['religion_learner']['memory'][-2]['environmentReaction'],
            mas['education_learner']['memory'][-2]['environmentReaction'],
        ]

        if ['LOSER', 'LOSER', 'LOSER', 'LOSER', 'LOSER', 'LOSER'] == status_list:
            pass
        elif ['WINNER', 'WINNER', 'WINNER', 'WINNER', 'WINNER', 'WINNER'] == status_list:
            pass
        elif ['DRAW', 'DRAW', 'DRAW', 'DRAW', 'DRAW', 'DRAW'] == status_list:
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

    if match_type == 'previous':
        id_match_list = [mas['family_leader']['memory'][-2]['matchId'],
                         mas['family_learner']['memory'][-2]['matchId'],
                         mas['education_leader']['memory'][-2]['matchId'],
                         mas['education_learner']['memory'][-2]['matchId'],
                         mas['religion_leader']['memory'][-2]['matchId'],
                         mas['religion_learner']['memory'][-2]['matchId']]

        match_id_list = [match['_id'], match['_id'], match['_id'],
                         match['_id'], match['_id'], match['_id']]

        if match_id_list == id_match_list:
            pass
        else:
            pass

    elif match_type == 'current':
        pass
    else:
        raise SystemError

    id_match_list = [family.memory[-2]['matchId'],
                     religion.memory[-2]['matchId'],
                     education.memory[-2]['matchId']]

    if [match.id, match.id, match.id] == id_match_list:
        pass
    else:
        check = []

        if '' != family.death and family.life <= 0:
            check.append(0)
        elif '' in religion.death and religion.life <= 0:
            check.append(1)
        elif '' in education.death and education.life <= 0:
            check.append(2)
        else:
            pass

        new_id_list = [True, True, True]

        for i in check:
            new_id_list[i] = False

        if [match.id == family.memory[-2]['matchId'],
                match.id == religion.memory[-2]['matchId'],
                match.id == education.memory[-2]['matchId']] == new_id_list:
            pass
        else:
            raise PreviousMatchIdIsDifferent


def check_match_game(game_status, match, mas, match_type):
    """ Check if all currenty objects has the same match game """

    try:

        game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        new_game = []

        for p in family.memory[-1]['choices']:

            if game[p['action']] == -1:
                game[p['action']] = family.char[1]
            else:
                pass

        for p in religion.memory[-1]['choices']:

            if game[p['action']] == -1:
                game[p['action']] = religion.char[1]
            else:
                pass

        for p in education.memory[-1]['choices']:

            if game[p['action']] == -1:
                game[p['action']] = education.char[1]
            else:
                pass

        for i in range(0, len(game_status)):

            if game_status[i] == 1:
                game_status[i] = -1

        if game_status == game:
            pass
        else:
            raise CurrentMatchGameIsDifferent

    except CurrentMatchGameIsDifferent:
        raise CurrentMatchGameIsDifferent

    except:
        raise ValidationError
