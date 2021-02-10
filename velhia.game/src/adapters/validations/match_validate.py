from errors.validation.validation_error import ValidationError
from errors.validation.match.match_pendent_error import CurrentyMatchIsNotPendent
from errors.validation.match.match_status_error import PreviousMatchHasInvalidStatus
from errors.validation.match.currenty_match_id_error import CurrentyMatchIdIsDifferent
from errors.validation.match.previous_match_id_error import PreviousMatchIdIsDifferent
from errors.validation.match.currenty_match_game_error import CurrentMatchGameIsDifferent
from errors.validation.match.previous_match_game_error import PreviousMatchGameIsDifferent


def check_match_pendent(match):
    """
    Check if a status of currenty match is pendent
    :param match: `Match` Match obj

    usage
    >>> from validations.match_validate import check_match_pendent
    >>> match = Match()
    >>> check_match_pendent(match)
    """

    try:

        if match.status == 'PENDENT':
            pass
        else:
            raise CurrentyMatchIsNotPendent

    except CurrentyMatchIsNotPendent:
        raise CurrentyMatchIsNotPendent

    except:
        raise ValidationError


def check_match_status(match, family, religion, education):
    """
    Check if a status of currenty match is pendent
    :param match: `Match` Match obj
    :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
    :param family: `Agent` Agent obj
    :param religion: `Agent` Agent obj
    :param education: `Agent` Agent obj

    usage
    >>> from validations.match_validate import check_match_status
    >>> match = Match()
    >>> sa = StatisticalAlgorithm()
    >>> family = Agent()
    >>> religion = Agent()
    >>> education = Agent()
    >>> check_match_status(match)
    """

    try:

        if match.status == 'WINNER' and match.winner in ['SA', 'MAS']:
            pass
        elif match.status == 'DRAW' and len(match.plays) == 9:
            pass
        else:
            raise PreviousMatchHasInvalidStatus

        status_list = [family.memory[-2]['environmentReaction'],
                       religion.memory[-2]['environmentReaction'],
                       education.memory[-2]['environmentReaction']]

        if ['LOSER', 'LOSER', 'LOSER'] == status_list:
            pass
        elif ['WINNER', 'WINNER', 'WINNER'] == status_list:
            pass
        elif ['DRAW', 'DRAW', 'DRAW'] == status_list:
            pass
        else:
            raise PreviousMatchHasInvalidStatus

    except PreviousMatchHasInvalidStatus:
        raise PreviousMatchHasInvalidStatus

    except:
        raise ValidationError


def check_previous_match_id(match, family, religion, education):
    """
    Check if all previous objects has the same match id
    :param match: `Match` Match obj
    :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
    :param family: `Agent` Agent obj
    :param religion: `Agent` Agent obj
    :param education: `Agent` Agent obj

    usage
    >>> from validations.match_validate import check_previous_match_id
    >>> match = Match()
    >>> sa = StatisticalAlgorithm()
    >>> family = Agent()
    >>> religion = Agent()
    >>> education = Agent()
    >>> check_previous_match_id(match)
    """

    try:

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

    except PreviousMatchIdIsDifferent:
        raise PreviousMatchIdIsDifferent

    except:
        raise ValidationError


def check_currenty_match_id(match, family, religion, education):
    """
    Check if all currenty objects has the same match id
    :param match: `Match` Match obj
    :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
    :param family: `Agent` Agent obj
    :param religion: `Agent` Agent obj
    :param education: `Agent` Agent obj

    usage
    >>> from validations.match_validate import check_currenty_match_id
    >>> match = Match()
    >>> sa = StatisticalAlgorithm()
    >>> family = Agent()
    >>> religion = Agent()
    >>> education = Agent()
    >>> check_currenty_match_id(match)
    """

    try:

        id_match_list = [family.memory[-1]['matchId'],
                         religion.memory[-1]['matchId'],
                         education.memory[-1]['matchId']]

        if [match.id, match.id, match.id] == id_match_list:
            pass
        else:
            raise CurrentyMatchIdIsDifferent

    except CurrentyMatchIdIsDifferent:
        raise CurrentyMatchIdIsDifferent

    except:
        raise ValidationError


def check_previous_match_game(game_status, match, family, religion, education):
    """
    Check if all previous objects has the same match game
    :param match: `Match` Match obj
    :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
    :param family: `Agent` Agent obj
    :param religion: `Agent` Agent obj
    :param education: `Agent` Agent obj

    usage
    >>> from validations.match_validate import check_previous_match_game
    >>> match = Match()
    >>> sa = StatisticalAlgorithm()
    >>> family = Agent()
    >>> religion = Agent()
    >>> education = Agent()
    >>> check_previous_match_game(match)
    """

    try:

        game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

        for p in family.memory[-2]['choices']:

            if game[p['action']] == -1:
                game[p['action']] = family.char[1]
            else:
                pass

        for p in religion.memory[-2]['choices']:

            if game[p['action']] == -1:
                game[p['action']] = religion.char[1]
            else:
                pass

        for p in education.memory[-2]['choices']:

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
            id_match_list = [family.memory[-2]['matchId'],
                             religion.memory[-2]['matchId'],
                             education.memory[-2]['matchId']]

            if [match.id, match.id, match.id] != id_match_list:
                pass
            else:
                raise PreviousMatchGameIsDifferent

    except PreviousMatchGameIsDifferent:
        raise PreviousMatchGameIsDifferent

    except:
        raise ValidationError


def check_currenty_match_game(game_status, family, religion, education):
    """
    Check if all currenty objects has the same match game
    :param match: `Match` Match obj
    :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
    :param family: `Agent` Agent obj
    :param religion: `Agent` Agent obj
    :param education: `Agent` Agent obj

    usage
    >>> from validations.match_validate import check_currenty_match_game
    >>> match = Match()
    >>> sa = StatisticalAlgorithm()
    >>> family = Agent()
    >>> religion = Agent()
    >>> education = Agent()
    >>> check_currenty_match_game(match)
    """

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
