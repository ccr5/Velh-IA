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
