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
            "sa": {"playerId": sa.id, "symbol": sa.char[0]},
            "mas": {"family": {"playerId": mas.family_leader.id, "symbol": mas.char[0]},
                    "religion": {"playerId": mas.religion_leader.id, "symbol": mas.char[0]},
                    "education": {"playerId": mas.education_leader.id, "symbol": mas.char[0]}},
            "plays": [],
            "status": "PENDENT"}))

        match = Match(json.loads(ret.text))
        return match
    except:
        raise NewMatchError


def add_new_memory(match, sa, mas):
    """
    Add a new empty memory in all players
    :param match: `Match` Match obj
    :param sa: `Statistical Algorithm` Statistical Algorithm obj
    :param mas: `Multi Agent System` Multi Agent System obj
    """

    try:

        mas.religion_leader.memory.append({
            'matchId': match.id,
            'isLearner': False,
            'choices': []
        })

        mas.religion_learner.memory.append({
            'matchId': match.id,
            'isLearner': True,
            'choices': []
        })

        mas.education_leader.memory.append({
            'matchId': match.id,
            'isLearner': False,
            'choices': []
        })

        mas.education_learner.memory.append({
            'matchId': match.id,
            'isLearner': True,
            'choices': []
        })

        mas.family_leader.memory.append({
            'matchId': match.id,
            'isLearner': False,
            'choices': []
        })

        mas.family_learner.memory.append({
            'matchId': match.id,
            'isLearner': True,
            'choices': []
        })

    except:
        raise NewMemoryError


def add_new_mas_player(db, match, old_leader, new_leader):
    """
    Add a new player in the match's mas obj
    :param db: `Database` Database obj
    :param match: `Match` Match obj
    :param old_leader: `String` old leader id
    :param new_leader: `Agent` new Agent leader obj
    """

    try:

        for institution, players in match.mas:

            if players[-1]['playerId'] == old_leader:

                obj = {'playerId': new_leader.id,
                       'symbol': 'O'}

                match.mas[institution].append(obj)
                db.update(match.id, json.dumps(match.create_object()))

    except:
        raise NewPlayerInMASError


def sequence_list(game_status):
    """
    All sequence to win 
    :param game_status: game status
    :return: `list` matrix
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
