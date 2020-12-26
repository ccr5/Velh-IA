import sys
import json
from datetime import datetime
from errors.invalid_match import InvalidMatch
from classes.statistical_algorithm import StatisticalAlgorithm
from classes.mult_agent_system import MultiAgentSystem
from classes.match import Match
from classes.agent import Agent
from handlers.statistical_algorithm_handler import get_lastest_sa
from handlers.multi_agent_system_handler import update_mas
from handlers.match_handler import add_new_match, add_new_memory, sequence_list
from handlers.agent_handler import check_win, get_latest_agent


class Velhia:
    """
    All functions and methods to use in Velh-IA workflow
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
        >>> (match, sa, mas) = vlh.get_data()

        <classes.match.Match object at 0x7fe6de3287d0>
        <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de328150>
        <classes.multi_agent_system.MultiAgentSystem object at 0x7fe6de34dd10>
        """

        try:

            last_match = self.match_db.get_last(1).json()

            if len(last_match) == 0 or last_match[0]['status'] != 'PENDENT':
                sa = get_lastest_sa(self.algorithm_db)
                sa.info['matchs'] += 1

                [education_leader, education_learner] = get_latest_agent(
                    self.education_db, self.match_db)
                education_leader.info['matchsAsLeader'] += 1
                education_learner.info['matchsAsLearner'] += 1

                [religion_leader, religion_learner] = get_latest_agent(
                    self.religion_db, self.match_db)
                religion_leader.info['matchsAsLeader'] += 1
                religion_learner.info['matchsAsLearner'] += 1

                [family_leader, family_learner] = get_latest_agent(
                    self.family_db, self.match_db)
                family_leader.info['matchsAsLeader'] += 1
                family_learner.info['matchsAsLearner'] += 1

                mas = MultiAgentSystem(family_leader, family_learner, education_leader,
                                       education_learner, religion_leader, religion_learner)

                match = add_new_match(self.match_db, sa, mas)
                add_new_memory(match, sa, mas)
                update_mas(self, mas)
                self.algorithm_db.update(sa.info['_id'], json.dumps(sa.info))

            else:
                match = Match(last_match[0])

                sa = StatisticalAlgorithm(
                    self.algorithm_db.get_one(
                        match.info['sa']['playerId']).json(),
                    ('X', 1), ('O', 0))

                [education_leader, education_learner] = get_latest_agent(
                    self.education_db, self.match_db, match, match.info['mas']['education'][-1])
                [religion_leader, religion_learner] = get_latest_agent(
                    self.religion_db, self.match_db, match, match.info['mas']['religion'][-1])
                [family_leader, family_learner] = get_latest_agent(
                    self.family_db, self.match_db, match, match.info['mas']['family'][-1])

                mas = MultiAgentSystem(family_leader, family_learner, education_leader,
                                       education_learner, religion_leader, religion_learner)

            return [match, sa, mas]
        except:
            raise SystemError

    def validate(self, match, sa, mas):
        """
        Check if everything is running correctly

            1. Check if the latest match has a status
            2. Check if the currenty match is pendent
            3. Check if the lastest leaders match is equals the currenty match
            4. Check if the plays in match obj is equals the in the leaders memories

        usage
        >>> from velhia import Velhia
        >>> vlh = Velhia(match_db, family_db, education_db, religion_db, algorithm_db)
        >>> vlh.validate(match, sa, mas)
        True or False
        """
        try:
            pass
        except:
            raise InvalidMatch

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

            if len(match.info['plays']) == 0 and len(last_match) == 1:
                return ['SA']
            elif len(match.info['plays']) == 0 and len(last_match) > 1:
                return ['MAS' if last_match[1]['sa']['playerId'] == last_match[1]['plays'][0]['player'] else 'SA']
            else:
                return ['MAS' if match.info['sa']['playerId'] == match.info['plays'][-1]['player'] else 'SA']

        except:
            print('get_sequence() error', sys.exc_info())

    def check_draw(self, match, sa, mas):

        if len(match.info['plays']) == 9 and match.info['status'] == 'PENDENT':
            match.info['status'] = 'DRAW'
            match.info['end'] = datetime.now().ctime()

            sa.info['memory'][-1]['environmentReaction'] = 'DRAW'
            sa.info['draw'] += 1

            mas.family_leader.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.family_learner.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.family_leader.info['draw'] += 1

            mas.education_leader.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.education_learner.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.education_leader.info['draw'] += 1

            mas.religion_leader.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.religion_learner.info['memory'][-1]['environmentReaction'] = 'DRAW'
            mas.religion_leader.info['draw'] += 1

            update_mas(self, mas)
            self.algorithm_db.update(sa.info['_id'], json.dumps(sa.info))
            self.match_db.update(match.info['_id'], json.dumps(match.info))

        else:
            pass

    def update_match(self, match, sa, mas, sequence, game_status, position, time):
        """
        Update a Match object after a play
        :param match: `Match` a Match object
        :param sa: `Statistical Algorithm` a Statistical Algorithm object
        :param mas: `Multi Agent System` a Multi Agent System object
        :param game_status: `List` a game status
        :param position: `Int` a position to play
        :param start: `Datetime` a datetime variable
        :param time: `Int` time to play (seconds)

        Usage
        >>> from velhia import Velhia
        >>> velhia.update_sa_match(self, match, sa, game_status, position, start, time)
        """

        try:
            new_game_status = list(game_status)

            if sequence == 'SA':
                new_game_status[position] = sa.char[1]
                results = sequence_list(new_game_status)

                if check_win(sa, results):
                    match.info['plays'].append({
                        'seq': len(match.info['plays']) + 1,
                        'player': sa.info['_id'],
                        'time': time,
                        'position': position
                    })

                    match.info['end'] = datetime.now().ctime()
                    match.info['status'] = 'WINNER'
                    match.info['winner'] = 'SA'

                    sa.info['memory'][-1]['environmentReaction'] = 'WINNER'
                    sa.info['victories'] += 1

                    mas.family_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'
                    mas.education_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'
                    mas.religion_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'

                    mas.family_leader.info['defeats'] += 1
                    mas.education_leader.info['defeats'] += 1
                    mas.religion_leader.info['defeats'] += 1

                    plays = 5 if match.info['plays'][0]['player'] == 'MAS' else 4

                    mas.family_leader.info['life'] -= len(
                        mas.family_leader.info['memory'][-1]['choices']) / plays
                    mas.education_leader.info['life'] -= len(
                        mas.education_leader.info['memory'][-1]['choices']) / plays
                    mas.religion_leader.info['life'] -= len(
                        mas.religion_leader.info['memory'][-1]['choices']) / plays

                    update_mas(self, mas)

                else:
                    match.info['plays'].append({
                        'seq': len(match.info['plays']) + 1,
                        'player': sa.info['_id'],
                        'time': time,
                        'position': position
                    })

                self.algorithm_db.update(sa.info['_id'], json.dumps(sa.info))
                self.match_db.update(match.info['_id'], json.dumps(match.info))

            elif sequence == 'MAS':
                new_game_status[position] = mas.char[1]
                results = sequence_list(new_game_status)

                if check_win(mas, results):
                    match.info['plays'].append({
                        'seq': len(match.info['plays']) + 1,
                        'player': 'MAS',
                        'time': time,
                        'position': position
                    })
                    match.info['status'] = 'WINNER'
                    match.info['winner'] = 'MAS'

                    mas.family_leader.info['memory'][-1]['environmentReaction'] = 'WINNER'
                    mas.family_leader.info['victories'] += 1

                    mas.education_leader.info['memory'][-1]['environmentReaction'] = 'WINNER'
                    mas.education_leader.info['victories'] += 1

                    mas.religion_leader.info['memory'][-1]['environmentReaction'] = 'WINNER'
                    mas.religion_leader.info['victories'] += 1

                    sa.info['memory'][-1]['environmentReaction'] = 'LOSER'
                    sa.info['defeats'] += 1

                    self.algorithm_db.update(
                        sa.info['_id'], json.dumps(sa.info))
                else:
                    match.info['plays'].append({
                        'seq': len(match.info['plays']) + 1,
                        'player': 'MAS',
                        'time': time,
                        'position': position
                    })

                update_mas(self, mas)
                self.match_db.update(
                    match.info['_id'], json.dumps(match.info))
            else:
                raise SystemError
        except:
            print('update_match() error', sys.exc_info())

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
            raise SystemError
