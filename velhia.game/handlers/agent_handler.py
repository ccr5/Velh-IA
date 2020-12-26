import json
from datetime import datetime
from classes.match import Match
from classes.agent import Agent
from handlers.match_handler import add_new_mas_player


def get_latest_agent(db, match_db, match=Match({'_id': ''}), player=''):
    """
    Get the lastest agent obj in the database or create if it not exists
    If a match and player was passed, it will get the lastest agents as of a match obj in the database
    :param db: `Database` a Database object
    :param match: `Match`a Match object
    :param player: `string` a player ID

    Usage
    >>> (leader, learner) = get_lastest_agent(education_db)
    >>> print(leader, learner)

    <classes.agent.Agent object at 0x7fe6de3287d0>
    <classes.agent.Agent object at 0x7fe6de3289a2>
    """

    try:
        res = db.get_last(2).json()

        if len(res) < 2:
            leader = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": "I'm the first one, bitch ;)",
                "becomeLeader": datetime.now().ctime(),
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))

            learner = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": leader.info['_id'],
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))

            return [leader, learner]

        elif match.info['_id'] != '' and player != '':

            if res[1]['_id'] == player['playerId']:
                [leader, learner] = check_life(db, res)

                if leader.info['_id'] == player['playerId']:
                    return [leader, learner]
                else:
                    add_new_mas_player(match_db, match, player, leader)
                    return [leader, learner]

        else:
            return check_life(db, res)
    except:
        raise SystemError


def check_life(db, agents):
    """
    Check if the lastest lider agent has life and create if hasn't
    :param db: `Database` a Database object
    :param agents: `List` a Agent object list

    Usage
    >>> (leader, learner) = check_life(db, [agent1, agent2])
    >>> print(leader, learner)

    <classes.match.Match object at 0x7fe6de3287d0>
    <classes.match.Match object at 0x7fe6de3215a3>
    """

    try:

        if agents[1]['life'] > 0:
            leader = Agent(agents[1], ('O', 0))
            learner = Agent(agents[0], ('O', 0))

        else:
            agents[1]['death'] = datetime.now().ctime()
            db.update(agents[1]['_id'], json.dumps(agents[1]))
            agents[0]['becomeLeader'] = datetime.now().ctime()
            db.update(agents[0]['_id'], json.dumps(agents[0]))
            leader = Agent(agents[0], ('O', 0))
            learner = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": leader.info['_id'],
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))

        return [leader, learner]

    except:
        raise SystemError


def check_win(player, moves):
    """
    Check and return a position to win
    :param moves: game status
    :return: `int` int

    Usage
    >>> position = check_win(obj, list)
    8
    """

    try:
        for y in moves:

            if y == [player.char[-1], player.char[-1], player.char[-1]]:
                return True
            else:
                pass
    except:
        raise SystemError
