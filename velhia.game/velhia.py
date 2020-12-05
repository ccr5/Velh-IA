from classes.statistical_algorithm import StatisticalAlgorithm
from classes.mult_agent_system import MultiAgentSystem
from classes.match import Match
from classes.agent import Agent
from datetime import datetime
import json
import sys


class Velhia:
    """
    All functions and methods to the game works
    :param match_db: `Database` Match object
    :param family_db: `Database` Family object
    :param education_db: `Database` Education object
    :param religion_db: `Database` Religion object
    :param algorithm_db: `Database` Statistical Algorithm object
    """

    def __init__(self, match_db, family_db, education_db, religion_db, algorithm_db):
        self.match_db = match_db
        self.family_db = family_db
        self.education_db = education_db
        self.religion_db = religion_db
        self.algorithm_db = algorithm_db

    def get_data(self):
        """
        Prepare all objects to start the game

        Usage
        >>> from velhia import Velhia
        >>> vlh = Velhia(match_db, family_db, education_db, religion_db, algorithm_db)
        >>> (match, sa, education_leader, education_learner, religion_leader,
        >>>  religion_learner, family_leader, family_learner) = vlh.get_data()

        <classes.match.Match object at 0x7fe6de3287d0>
        <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de328150>
        <classes.agent.Agent object at 0x7fe6de34dd10> <classes.agent.Agent object at 0x7fe6de34d150>
        <classes.agent.Agent object at 0x7fe6de34d410> <classes.agent.Agent object at 0x7fe6de34d090>
        <classes.agent.Agent object at 0x7fe6de34df90> <classes.agent.Agent object at 0x7fe6de34de90>
        """

        try:
            last_match = self.match_db.get_last(1).json()

            if len(last_match) == 0 or last_match[0]['status'] != 'PENDENT':
                sa = self.get_lastest_sa()
                [education_leader, education_learner] = self.get_latest_agent(
                    self.education_db)

                [religion_leader, religion_learner] = self.get_latest_agent(
                    self.religion_db)

                [family_leader, family_learner] = self.get_latest_agent(
                    self.family_db)

                match = self.add_new_match(
                    sa, family_leader, religion_leader, education_leader
                )

                mas = MultiAgentSystem(family_leader, family_learner, education_leader,
                                       education_learner, religion_leader, religion_learner)
            else:
                match = Match(last_match[0])

                sa = StatisticalAlgorithm(
                    self.algorithm_db.get_one(
                        match.info['sa']['playerId']).json(),

                    (match.info['sa']['symbol'],
                     1 if match.info['sa']['symbol'] == 'X' else 0),

                    ('O', 0) if match.info['sa']['symbol'] == 'X' else ('X', 1))

                [education_leader, education_learner] = self.get_latest_players(
                    match, match.info['mas']['education'][-1], self.education_db)

                [religion_leader, religion_learner] = self.get_latest_players(
                    match, match.info['mas']['religion'][-1], self.religion_db)

                [family_leader, family_learner] = self.get_latest_players(
                    match, match.info['mas']['family'][-1], self.family_db)

                mas = MultiAgentSystem(family_leader, family_learner, education_leader,
                                       education_learner, religion_leader, religion_learner)

            return [match, sa, mas]
        except:
            print('get_data() error', sys.exc_info())

    def get_lastest_sa(self):
        """
        Get the lastest statistical algorithm obj in the database
        or create if it not exists

        Usage
        >>> from velhia import Velhia
        >>> sa = velhia.get_lastest_sa()
        >>> print(sa)

        <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de3287d0>
        """

        try:
            if len(self.algorithm_db.get_last(1).json()) == 0:
                sa = StatisticalAlgorithm(self.algorithm_db.create(json.dumps({
                    "birth": datetime.now().ctime(),
                    "memory": [],
                    "matchs": 0,
                    "victories": 0,
                    "defeats": 0,
                    "draw": 0
                })).json(), ('X', 1), ('O', 0))
            else:
                sa = StatisticalAlgorithm(
                    self.algorithm_db.get_last(1).json()[0],
                    ('X', 1), ('O', 0))

            return sa
        except:
            print('get_lastest_sa() error', sys.exc_info())

    def get_latest_agent(self, db):
        """
        Get the lastest agent obj in the database
        or create if it not exists
        :param db: `Database` a Database object

        Usage
        >>> from velhia import Velhia
        >>> (leader, learner) = velhia.get_lastest_agent(education_db)
        >>> print(leader, learner)

        <classes.agent.Agent object at 0x7fe6de3287d0>
        <classes.agent.Agent object at 0x7fe6de3289a2>
        """

        try:
            res = len(db.get_last(2).json())
            if res < 2:
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
            else:
                return self.check_life(db, res)
        except:
            print('get_lastest_agent() error', sys.exc_info())

    def get_latest_players(self, match, player, db):
        """
        Get the lastest agents as of a match obj in the database
        :param player: `string` a player ID
        :param db: `Database` a Database object

        Usage
        >>> from velhia import Velhia
        >>> (education_leader, education_learner) = velhia.get_latest_players(
                                                        match.info['mas']['education'][-1],
                                                        self.education_db
                                                    )
        >>> print(education_leader, education_learner)

        <classes.agent.Agent object at 0x7fe6de3287d0>
        <classes.agent.Agent object at 0x7fe6de3289a2>
        """

        try:
            res = db.get_last(2).json()

            if res[1]['_id'] == player['playerId']:
                [leader, learner] = self.check_life(db, res)

                if leader.info['_id'] == player['playerId']:
                    return [leader, learner]
                else:
                    self.add_new_mas_player(match, player, leader)
                    return [leader, learner]

            else:
                raise SystemError()
        except:
            print('get_lastest_players() error', sys.exc_info())

    def get_sequence(self, match):
        """
        Return who plays first
        :param match: `Match` a Match object

        Usage
        >>> from velhia import Velhia
        >>> sequence = velhia.get_sequence(match)
        >>> print(sequence)

        ['SA']
        """

        try:
            last_match = self.match_db.get_last(2).json()

            if match.info['_id'] == last_match[0]['_id']:

                if len(match.info['plays']) == 0:
                    return ['SA']
                else:
                    return ['MAS' if match.info['sa']['playerId'] == match.info['plays'][-1]['player'] else 'SA']

            else:

                if len(match.info['plays']) == 0:
                    return ['SA']
                else:
                    return ['MAS' if last_match[0]['sa']['playerId'] == last_match[0]['plays'][0]['player'] else 'SA']
        except:
            print('get_sequence() error', sys.exc_info())

    def add_new_match(self, sa, family, religion, education):
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
            match = Match(self.match_db.create(json.dumps({
                "begin": datetime.now().ctime(),
                "time": 0,
                "sa": {"playerId": sa.info['_id'], "symbol": sa.char[0]},
                "mas": {"family": {"playerId": family.info['_id'], "symbol": family.char[0]},
                        "religion": {"playerId": religion.info['_id'], "symbol": religion.char[0]},
                        "education": {"playerId": education.info['_id'], "symbol": education.char[0]}},
                "plays": [],
                "status": "PENDENT"})))

            return match
        except:
            print('add_new_match() error', sys.exc_info())

    def add_new_mas_player(self, match, old_leader, new_leader):

        for institution in match.info['mas']:

            if institution[-1] == old_leader:

                obj = {
                    'playerId': new_leader.info['_id'],
                    'symbol': 'O'
                }

                match.info['mas']['family'].append(obj)
                self.match_db.update(match.info['_id'], json.dumps(match.info))

    def check_life(self, db, agents):
        """
        Check if the lastest lider agent has life and create if hasn't
        :param db: `Database` a Database object
        :param agents: `List` a Agent object list

        Usage
        >>> from velhia import Velhia
        >>> (leader, learner) = velhia.check_life(db, [agent1, agent2])
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
                db.update(agents[1]['_id'], agents[1])
                agents[0]['becomeLeader'] = datetime.now().ctime()
                db.update(agents[0]['_id'], agents[0])
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
            print('check_life() error', sys.exc_info())

    def check_win(self, player, moves):
        """
        Check and return a position to win
        :param moves: game status
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> position = sa.check_win([-1,0,1,0,0,1,0,-1,-1])
        >>> position
        8
        """

        try:
            for y in moves:

                if y == [player.char[-1], player.char[-1], player.char[-1]]:
                    return True
                else:
                    pass
        except:
            print('update_sa_match() error', sys.exc_info())

    def update_sa_match(self, match, sa, game_status, position, start, time):
        """
        Update a Statistical Algorithm and Match object after SA choose a position
        :param match: `Match` a Match object
        :param sa: `Statistical Algorithm` a Statistical Algorithm object
        :param game_status: `List` a game status
        :param position: `Int` a position to play
        :param start: `Datetime` a datetime variable
        :param time: `Int` time to play (seconds)

        Usage
        >>> from velhia import Velhia
        >>> velhia.update_sa_match(self, match, sa, game_status, position, start, time)
        """

        try:
            results = self.sequence_list(game_status)

            if self.check_win(sa, results):
                match.info['plays'].append({
                    'seq': len(match.info['plays']) + 1,
                    'player': sa.info['_id'],
                    'time': time,
                    'position': position
                })
                match.info['status'] = 'WINNER'
                match.info['winner'] = 'SA'

                sa.info['memory'].append({
                    'isLearner': False,
                    'choices': sa.info['choices'].append({
                        'dateRequest': start,
                        'gameStatus': game_status,
                        'timeToAct': time,
                        'action': position
                    }),
                    'environmentReaction': 'WINNER'
                })

                sa.info['memory'].append({
                    'isLearner': False,
                    'choices': []
                })

                sa.info['matchs']: sa.info['matchs'] + 1
                sa.info['victories']: sa.info['victories'] + 1

                self.algorithm_db.update(sa.info['_id'], sa.info)
                self.match_db.update(match.info['_id'], match.info)
            else:
                match.info['plays'].append({
                    'seq': len(match.info['plays']) + 1,
                    'player': sa.info['_id'],
                    'time': time,
                    'position': position
                })

                choices = sa.info['memory']['choices'] if len(
                    sa.info['memory']) > 0 else []

                choices.append({
                    'dateRequest': start,
                    'gameStatus': game_status,
                    'timeToAct': time,
                    'action': position
                })

                sa.info['memory'].append({
                    'isLearner': False,
                    'choices': choices
                })

                self.algorithm_db.update(sa.info['_id'], json.dumps(sa.info))
                self.match_db.update(match.info['_id'], json.dumps(match.info))
        except:
            print('update_sa_match() error', sys.exc_info())

    def update_mas_match(self, match, mas, game_status, position, start, time):
        pass

    def game_status(self, match, saId):
        """
        Return a list with all plays of the match
        :param match: `Match` a Match object
        :param saId: `String` a ID of Statistical Algorithm Obj

        Usage
        >>> from velhia import Velhia
        >>> game_status = velhia.game_status(match, '5fcaa7adb2cd0517560bdb5e')
        >>> print(game_status)

        [-1, 0, -1, -1, 1, -1, 0, -1, 1]
        """

        try:
            game_status = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

            for p in match.info['plays']:
                if p['player'] == saId:
                    game_status[p['position']] = 1
                else:
                    game_status[p['position']] = 0

            return game_status

        except:
            print('game_status() error', sys.exc_info())

    def sequence_list(self, game_status):
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
            print('sequence_list() error', sys.exc_info())
