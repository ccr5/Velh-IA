import sys
import json
from datetime import datetime
from classes.statistical_algorithm import StatisticalAlgorithm
from classes.mult_agent_system import MultiAgentSystem
from classes.match import Match
from classes.agent import Agent
from handlers.statistical_algorithm_handler import get_lastest_sa
from handlers.multi_agent_system_handler import update_mas
from handlers.match_handler import add_new_match, add_new_memory, sequence_list
from handlers.agent_handler import check_win, get_latest_agent
from validations.match_validate import check_match_status, check_match_pendent
from validations.match_validate import check_previous_match_game, check_currenty_match_game
from validations.match_validate import check_previous_match_id, check_currenty_match_id
from validations.player_validate import check_sa_matchs, check_agent_matchs


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

    def backup(self):
        """
        Get the lastest datas to use in rollback function

        usage
        >>> from velhia import Velhia
        >>> vlh = Velhia()
        >>> [match_backup, sa_backup, mas_backup] = vlh.backup()

        <classes.match.Match object at 0x7fe6de3287d0>
        <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de328150>
        <classes.multi_agent_system.MultiAgentSystem object at 0x7fe6de34dd10>
        """

        ret = self.match_db.get_last(1).json()

        if len(ret) != 0:

            match_backup = Match(ret[0])

            sa_backup = StatisticalAlgorithm(
                self.algorithm_db.get_last(1).json()[0],
                ['X', 1], ['O', 0]
            )

            mas_backup = MultiAgentSystem(
                Agent(self.family_db.get_last(2).json()[1], ['O', 0]),
                Agent(self.family_db.get_last(1).json()[0], ['O', 0]),
                Agent(self.education_db.get_last(2).json()[1], ['O', 0]),
                Agent(self.education_db.get_last(1).json()[0], ['O', 0]),
                Agent(self.religion_db.get_last(2).json()[1], ['O', 0]),
                Agent(self.religion_db.get_last(1).json()[0], ['O', 0]),
            )

            return [match_backup, sa_backup, mas_backup]

        else:
            return [None, None, None]

    def start(self):
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

    def validate(self, match, sa, mas):
        """
        Check if everything ran correctly
        :param match: `Match` Match obj
        :param sa: `Statistical Algorithm` Statistical Algorithm obj
        :param mas: `Multi Agent System` Multi Agent System obj 

            Previous
            1. Check if the previous match has a status in ['WINNER', 'DRAW']
            2. Check if the previous players memory is the previous match
            3. Check if the previous match status is the previous environment status in the previous players memory
            4. Check if the plays in previous match obj is equals previous players memories
            5. Check if the number of players matchs is correctly (victories, defeats, draws)

            Currenty
            1. Check if the currenty match status is pendent
            2. Check if the last match of institutions leaders is equals the currenty match
            3. Check if the plays in match obj is equals players memories
            4. Check if the number of players matchs is correctly (victories, defeats, draws)

        usage
        >>> from velhia import Velhia
        >>> vlh = Velhia(match_db, family_db, education_db, religion_db, algorithm_db)
        >>> vlh.validate_previous_match()
        True or False
        """

        if len(self.match_db.get_last(2).json()) > 1:

            # Previous
            previous_match = Match(self.match_db.get_last(2).json()[1])
            previous_sa = StatisticalAlgorithm(self.algorithm_db.get_one(
                previous_match.info['sa']['playerId']).json(), ['X', 1], ['O', 0])
            previous_family = Agent(self.family_db.get_one(
                previous_match.info['mas']['family'][-1]['playerId']).json(), ['O', 0])
            previous_religion = Agent(self.religion_db.get_one(
                previous_match.info['mas']['religion'][-1]['playerId']).json(), ['O', 0])
            previous_education = Agent(self.education_db.get_one(
                previous_match.info['mas']['education'][-1]['playerId']).json(), ['O', 0])

            check_match_status(previous_match, previous_family,
                               previous_religion, previous_education)
            check_previous_match_id(previous_match, previous_family,
                                    previous_religion, previous_education)
            game_status = self.game_status(
                previous_match, previous_sa.info['_id'])
            check_previous_match_game(game_status, previous_match, previous_family,
                                      previous_religion, previous_education)
            check_sa_matchs(previous_sa)
            [check_agent_matchs(x) for x in [previous_family,
                                             previous_religion,
                                             previous_education]]

            # Currenty
            check_match_pendent(match)
            check_currenty_match_id(match, mas.family_leader,
                                    mas.religion_leader, mas.education_leader)
            game_status = self.game_status(match, sa.info['_id'])
            check_currenty_match_game(game_status, mas.family_leader,
                                      mas.religion_leader, mas.education_leader)
            check_sa_matchs(sa)
            [check_agent_matchs(x) for x in [mas.family_leader,
                                             mas.religion_leader,
                                             mas.education_leader]]
        else:

            # Currenty
            check_match_pendent(match)
            check_currenty_match_id(match, mas.family_leader,
                                    mas.religion_leader, mas.education_leader)
            game_status = self.game_status(match, sa.info['_id'])
            check_currenty_match_game(game_status, mas.family_leader,
                                      mas.religion_leader, mas.education_leader)
            check_sa_matchs(sa)
            [check_agent_matchs(x) for x in [mas.family_leader,
                                             mas.religion_leader,
                                             mas.education_leader]]

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

        last_match = self.match_db.get_last(2).json()

        if len(match.info['plays']) == 0 and len(last_match) == 1:
            return ['SA']
        elif len(match.info['plays']) == 0 and len(last_match) > 1:
            return ['MAS' if last_match[1]['sa']['playerId'] == last_match[1]['plays'][0]['player'] else 'SA']
        else:
            return ['MAS' if match.info['sa']['playerId'] == match.info['plays'][-1]['player'] else 'SA']

    def check_draw(self, match, sa, mas):
        """
        Check if the match is draw and update all datas
        :param match: `Match` a Match object
        :param sa: `Statistical Algorithm` a Statistical Algorithm object
        :param mas: `Multi Agent System` a Multi Agent System object

        usage
        >>> from velhia import Velhia
        >>> velhia.check_draw(match, sa, mas) 
        """

        if len(match.info['plays']) == 9 and match.info['status'] == 'PENDENT':
            match.info['status'] = 'DRAW'
            match.info['end'] = datetime.now().ctime()

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

                sa.info['victories'] += 1

                mas.family_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'
                mas.education_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'
                mas.religion_leader.info['memory'][-1]['environmentReaction'] = 'LOSER'

                mas.family_learner.info['memory'][-1]['environmentReaction'] = 'LOSER'
                mas.education_learner.info['memory'][-1]['environmentReaction'] = 'LOSER'
                mas.religion_learner.info['memory'][-1]['environmentReaction'] = 'LOSER'

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
                mas.family_learner.info['memory'][-1]['environmentReaction'] = 'WINNER'
                mas.family_leader.info['victories'] += 1

                mas.education_leader.info['memory'][-1]['environmentReaction'] = 'WINNER'
                mas.education_learner.info['memory'][-1]['environmentReaction'] = 'WINNER'
                mas.education_leader.info['victories'] += 1

                mas.religion_leader.info['memory'][-1]['environmentReaction'] = 'WINNER'
                mas.religion_learner.info['memory'][-1]['environmentReaction'] = 'WINNER'
                mas.religion_leader.info['victories'] += 1

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
            self.match_db.update(match.info['_id'], json.dumps(match.info))
        else:
            raise SystemError

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

        game_status = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

        for p in match.info['plays']:
            if p['player'] == saId:
                game_status[p['position']] = 1
            else:
                game_status[p['position']] = 0

        return game_status

    def rollback(self, match, match_backup, sa, sa_backup, mas, mas_backup):
        """
        Rollback function to restore database object if something is wrong
        :param match_backup: `Match` Match obj
        :param sa_backup: `StatisticalAlgorithm` Statistical Algorithm obj
        :param mas_backup: `MultiAgentSystem` Multi Agent System obj
        """

        if [None, None, None] != [match_backup, sa_backup, mas_backup]:

            if sa.info['_id'] != sa_backup.info['_id']:
                self.algorithm_db.delete(sa.info['_id'])

            if match.info['_id'] != match_backup.info['_id']:
                self.match_db.delete(match.info['_id'])

            if mas.family_learner.info['_id'] != mas_backup.family_learner.info['_id']:
                self.family_db.delete(mas.family_learner.info['_id'])

            if mas.religion_learner.info['_id'] != mas_backup.religion_learner.info['_id']:
                self.religion_db.delete(mas.religion_learner.info['_id'])

            if mas.education_learner.info['_id'] != mas_backup.education_learner.info['_id']:
                self.education_db.delete(mas.education_learner.info['_id'])

            self.match_db.update(
                match_backup.info['_id'], json.dumps(match_backup.info))

            self.algorithm_db.update(
                sa_backup.info['_id'], json.dumps(sa_backup.info))

            update_mas(self, mas_backup)

        else:
            pass
