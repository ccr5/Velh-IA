from errors.invalid_match import InvalidMatch


def check_match_pendent(match):

    if match.info['status'] == 'PENDENT':
        pass
    else:
        raise InvalidMatch


def check_match_status(match, sa, family, religion, education):

    if match.info['status'] == 'WINNER' and match.info['winner'] in ['SA', 'MAS']:
        pass
    elif match.info['status'] == 'DRAW' and len(match.info['plays']) == 9:
        pass

    status_list = [sa.info['memory'][-2]['environmentReaction'],
                   family.info['memory'][-2]['environmentReaction'],
                   religion.info['memory'][-2]['environmentReaction'],
                   education.info['memory'][-2]['environmentReaction']]

    if ['WINNER', 'LOSER', 'LOSER', 'LOSER'] == status_list:
        pass
    elif ['LOSER', 'WINNER', 'WINNER', 'WINNER'] == status_list:
        pass
    elif ['DRAW', 'DRAW', 'DRAW', 'DRAW'] == status_list:
        pass
    else:
        raise InvalidMatch


def check_previous_match_id(match, sa, family, religion, education):

    id_match_list = [sa.info['memory'][-2]['matchId'],
                     family.info['memory'][-2]['matchId'],
                     religion.info['memory'][-2]['matchId'],
                     education.info['memory'][-2]['matchId']]

    if [match.info['_id'], match.info['_id'], match.info['_id'], match.info['_id']] == id_match_list:
        pass
    else:
        raise InvalidMatch


def check_currenty_match_id(match, sa, family, religion, education):

    id_match_list = [sa.info['memory'][-1]['matchId'],
                     family.info['memory'][-1]['matchId'],
                     religion.info['memory'][-1]['matchId'],
                     education.info['memory'][-1]['matchId']]

    if [match.info['_id'], match.info['_id'], match.info['_id'], match.info['_id']] == id_match_list:
        pass
    else:
        raise InvalidMatch


def check_previous_match_game(game_status, sa, family, religion, education):

    game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

    for p in sa.info['memory'][-2]['choices']:
        game[p['action']] = sa.char[1]

    for p in family.info['memory'][-2]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = family.char[1]
        else:
            pass

    for p in religion.info['memory'][-2]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = religion.char[1]
        else:
            pass

    for p in education.info['memory'][-2]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = education.char[1]
        else:
            pass

    if game_status == game:
        pass
    else:
        raise InvalidMatch


def check_currenty_match_game(game_status, sa, family, religion, education):

    game = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

    for p in sa.info['memory'][-1]['choices']:
        game[p['action']] = sa.char[1]

    for p in family.info['memory'][-1]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = family.char[1]
        else:
            pass

    for p in religion.info['memory'][-1]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = religion.char[1]
        else:
            pass

    for p in education.info['memory'][-1]['choices']:

        if game[p['action']] == -1:
            game[p['action']] = education.char[1]
        else:
            pass

    if game_status == game:
        pass
    else:
        raise InvalidMatch
