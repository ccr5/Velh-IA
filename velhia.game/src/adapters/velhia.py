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

        last_match = self.match_db.get(
            offset=0, limit=1, sort="createdAt:desc").json()

        if len(last_match) == 0 or last_match[0]['status'] != 'PENDENT':
            sa = get_lastest_sa(self.algorithm_db)
            sa.matchs += 1

            [education_leader, education_learner] = get_latest_agent(
                self.education_db, self.match_db)
            education_leader.matchsAsLeader += 1
            education_learner.matchsAsLearner += 1

            [religion_leader, religion_learner] = get_latest_agent(
                self.religion_db, self.match_db)
            religion_leader.matchsAsLeader += 1
            religion_learner.matchsAsLearner += 1

            [family_leader, family_learner] = get_latest_agent(
                self.family_db, self.match_db)
            family_leader.matchsAsLeader += 1
            family_learner.matchsAsLearner += 1

            mas = MultiAgentSystem(family_leader, family_learner, education_leader,
                                   education_learner, religion_leader, religion_learner)

            match = add_new_match(self.match_db, sa, mas)
            add_new_memory(match, sa, mas)
            update_mas(self, mas)
            self.algorithm_db.update(sa.id, json.dumps(sa.create_object()))

        else:
            match = Match(last_match[0])

            sa = StatisticalAlgorithm(
                self.algorithm_db.get(
                    filters={"_id": match.sa['playerId']}).json()[0],
                ('X', 1), ('O', 0))

            [education_leader, education_learner] = get_latest_agent(
                self.education_db, self.match_db, match, match.mas['education'][-1])
            [religion_leader, religion_learner] = get_latest_agent(
                self.religion_db, self.match_db, match, match.mas['religion'][-1])
            [family_leader, family_learner] = get_latest_agent(
                self.family_db, self.match_db, match, match.mas['family'][-1])

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

        if len(self.match_db.get(offset=0, limit=2).json()) > 1:

            # Previous
            previous_match = Match(self.match_db.get(
                offset=1, limit=1, sort='createdAt:desc').json()[0])
            previous_sa = StatisticalAlgorithm(self.algorithm_db.get(
                filters={"_id": previous_match.sa['playerId']}).json()[0], ['X', 1], ['O', 0])
            previous_family = Agent(self.family_db.get(
                filters={"_id": previous_match.mas['family'][-1]['playerId']}).json()[0], ['O', 0])
            previous_religion = Agent(self.religion_db.get(
                filters={"_id": previous_match.mas['religion'][-1]['playerId']}).json()[0], ['O', 0])
            previous_education = Agent(self.education_db.get(
                filters={"_id": previous_match.mas['education'][-1]['playerId']}).json()[0], ['O', 0])

            check_match_status(previous_match, previous_family,
                               previous_religion, previous_education)
            check_previous_match_id(previous_match, previous_family,
                                    previous_religion, previous_education)
            game_status = self.game_status(
                previous_match, previous_sa.id)
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
            game_status = self.game_status(match, sa.id)
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
            game_status = self.game_status(match, sa.id)
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

        last_match = self.match_db.get(
            offset=0, limit=2, sort='createdAt:desc').json()

        if len(match.plays) == 0 and len(last_match) == 1:
            return ['SA']
        elif len(match.plays) == 0 and len(last_match) > 1:
            return ['MAS' if last_match[1]['sa']['playerId'] == last_match[1]['plays'][0]['player'] else 'SA']
        else:
            return ['MAS' if match.sa['playerId'] == match.plays[-1]['player'] else 'SA']

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

        if len(match.plays) == 9 and match.status == 'PENDENT':
            match.status = 'DRAW'
            match.end = datetime.now().ctime()

            sa.draw += 1

            mas.family_leader.memory[-1]['environmentReaction'] = 'DRAW'
            mas.family_learner.memory[-1]['environmentReaction'] = 'DRAW'
            mas.family_leader.draw += 1

            mas.education_leader.memory[-1]['environmentReaction'] = 'DRAW'
            mas.education_learner.memory[-1]['environmentReaction'] = 'DRAW'
            mas.education_leader.draw += 1

            mas.religion_leader.memory[-1]['environmentReaction'] = 'DRAW'
            mas.religion_learner.memory[-1]['environmentReaction'] = 'DRAW'
            mas.religion_leader.draw += 1

            update_mas(self, mas)
            self.algorithm_db.update(sa.id, json.dumps(sa.create_object()))
            self.match_db.update(match.id, json.dumps(match.create_object()))

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
                match.plays.append({
                    'seq': len(match.plays) + 1,
                    'player': sa.id,
                    'time': time,
                    'position': position
                })

                match.end = datetime.now().ctime()
                match.status = 'WINNER'
                match.winner = 'SA'

                sa.victories += 1

                mas.family_leader.memory[-1]['environmentReaction'] = 'LOSER'
                mas.education_leader.memory[-1]['environmentReaction'] = 'LOSER'
                mas.religion_leader.memory[-1]['environmentReaction'] = 'LOSER'

                mas.family_learner.memory[-1]['environmentReaction'] = 'LOSER'
                mas.education_learner.memory[-1]['environmentReaction'] = 'LOSER'
                mas.religion_learner.memory[-1]['environmentReaction'] = 'LOSER'

                mas.family_leader.defeats += 1
                mas.education_leader.defeats += 1
                mas.religion_leader.defeats += 1

                plays = 5 if match.plays[0]['player'] == 'MAS' else 4

                mas.family_leader.life -= len(
                    mas.family_leader.memory[-1]['choices']) / plays
                mas.education_leader.life -= len(
                    mas.education_leader.memory[-1]['choices']) / plays
                mas.religion_leader.life -= len(
                    mas.religion_leader.memory[-1]['choices']) / plays

                update_mas(self, mas)

            else:
                match.plays.append({
                    'seq': len(match.plays) + 1,
                    'player': sa.id,
                    'time': time,
                    'position': position
                })

            self.algorithm_db.update(sa.id, json.dumps(sa.create_object()))
            self.match_db.update(match.id, json.dumps(match.create_object()))

        elif sequence == 'MAS':
            new_game_status[position] = mas.char[1]
            results = sequence_list(new_game_status)

            if check_win(mas, results):
                match.plays.append({
                    'seq': len(match.plays) + 1,
                    'player': 'MAS',
                    'time': time,
                    'position': position
                })
                match.status = 'WINNER'
                match.winner = 'MAS'

                mas.family_leader.memory[-1]['environmentReaction'] = 'WINNER'
                mas.family_learner.memory[-1]['environmentReaction'] = 'WINNER'
                mas.family_leader.victories += 1

                mas.education_leader.memory[-1]['environmentReaction'] = 'WINNER'
                mas.education_learner.memory[-1]['environmentReaction'] = 'WINNER'
                mas.education_leader.victories += 1

                mas.religion_leader.memory[-1]['environmentReaction'] = 'WINNER'
                mas.religion_learner.memory[-1]['environmentReaction'] = 'WINNER'
                mas.religion_leader.victories += 1

                sa.defeats += 1

                self.algorithm_db.update(
                    sa.id, json.dumps(sa.create_object()))
            else:
                match.plays.append({
                    'seq': len(match.plays) + 1,
                    'player': 'MAS',
                    'time': time,
                    'position': position
                })

            update_mas(self, mas)
            self.match_db.update(match.id, json.dumps(match.create_object()))
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

        for p in match.plays:
            if p['player'] == saId:
                game_status[p['position']] = 1
            else:
                game_status[p['position']] = 0

        return game_status
