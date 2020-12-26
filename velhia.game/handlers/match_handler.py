import json
from datetime import datetime
from classes.match import Match
from errors.handler.match.new_match_error import NewMatchError
from errors.handler.match.new_memory_error import NewMemoryError
from errors.handler.match.new_player_mas_error import NewPlayerInMASError
from errors.handler.match.sequence_list_error import SequenceListError


def add_new_match(db, sa, mas):
    """
    Create a new match in the database
    :param sa: `StatisticalAlgorithm` a SA obj
    :param family: `Agent` a Family object
    :param religion: `Agent` a Religion object
    :param education: `Agent` a Education object

    Usage
    >>> from velhia import Velhia
    >>> match = velhia.add_new_match(sa, family, religion, education)
    >>> print(match)

    <classes.match.Match object at 0x7fe6de3287d0>
    """

    try:
        ret = db.create(json.dumps({
            "begin": datetime.now().ctime(),
            "time": 0,
            "sa": {"playerId": sa.info['_id'], "symbol": sa.char[0]},
            "mas": {"family": {"playerId": mas.family_leader.info['_id'], "symbol": mas.char[0]},
                    "religion": {"playerId": mas.religion_leader.info['_id'], "symbol": mas.char[0]},
                    "education": {"playerId": mas.education_leader.info['_id'], "symbol": mas.char[0]}},
            "plays": [],
            "status": "PENDENT"}))

        match = Match(json.loads(ret.text))
        return match
    except:
        raise NewMatchError


def add_new_memory(match, sa, mas):
    try:
        sa.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': False,
            'choices': []
        })

        mas.religion_leader.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': False,
            'choices': []
        })

        mas.religion_learner.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': True,
            'choices': []
        })

        mas.education_leader.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': False,
            'choices': []
        })

        mas.education_learner.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': True,
            'choices': []
        })

        mas.family_leader.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': False,
            'choices': []
        })

        mas.family_learner.info['memory'].append({
            'matchId': match.info['_id'],
            'isLearner': True,
            'choices': []
        })
    except:
        raise NewMemoryError


def add_new_mas_player(db, match, old_leader, new_leader):

    try:

        for institution, players in match.info['mas']:

            if players[-1]['playerId'] == old_leader:

                obj = {
                    'playerId': new_leader.info['_id'],
                    'symbol': 'O'
                }

                match.info['mas'][institution].append(obj)
                db.update(match.info['_id'], json.dumps(match.info))

    except:
        raise NewPlayerInMASError


def sequence_list(game_status):
    """
    All sequence to win 
    :param game_status: game status
    :return: `list` matrix

    Usage
    >>> from sa import StatisticalAlgorithm
    >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
    >>> ret = sa.sequence_list([-1,0,1,0,-1,1,0,-1,-1])
    >>> ret
    [
        [-1, 0, 1],     [0, -1, 1], 
        [0, -1, -1],    [-1, 0, 0], 
        [0, -1, -1],    [1, 1, -1],
        [-1, -1, -1],   [1, -1, 0]
    ]
    """
    try:

        return [[game_status[0], game_status[1], game_status[2]],
                [game_status[3], game_status[4], game_status[5]],
                [game_status[6], game_status[7], game_status[8]],
                [game_status[0], game_status[3], game_status[6]],
                [game_status[1], game_status[4], game_status[7]],
                [game_status[2], game_status[5], game_status[8]],
                [game_status[0], game_status[4], game_status[8]],
                [game_status[2], game_status[4], game_status[6]]]

    except:
        raise SequenceListError
