import random as r
from datetime import datetime
from errors.multi_agent_system.play_error import MASPlayError


class MultiAgentSystem:

    def __init__(self,
                 family_leader, family_learner,
                 education_leader, education_learner,
                 religion_leader, religion_learner
                 ):
        self.char = ['O', 0]
        self.family_leader = family_leader
        self.family_learner = family_learner
        self.education_leader = education_leader
        self.education_learner = education_learner
        self.religion_leader = religion_leader
        self.religion_learner = religion_learner

    def play(self, match, game_status):
        """
        Choose a position to play
        :param match: `Match` a Match obj
        :param game_status: game status
        """

        family_start = datetime.now()
        validation = False
        while not validation:
            family_position = self.family_leader.remember(match, game_status)
            validation = True if game_status[family_position] == -1 else False
        family_end = datetime.now()

        education_start = datetime.now()
        validation = False
        while not validation:
            education_position = self.education_leader.remember(
                match, game_status)
            validation = True if game_status[education_position] == -1 else False
        education_end = datetime.now()

        religion_start = datetime.now()
        validation = False
        while not validation:
            religion_position = self.religion_leader.remember(
                match, game_status)
            validation = True if game_status[religion_position] == -1 else False
        religion_end = datetime.now()

        if family_position == education_position == religion_position:
            self.family_leader.memorize(
                match, game_status, family_start, family_end, family_position)
            self.family_learner.learn(match, game_status, family_position)

            self.education_leader.memorize(
                match, game_status, education_start, education_end, education_position)
            self.education_learner.learn(
                match, game_status, education_position)

            self.religion_leader.memorize(
                match, game_status, religion_start, religion_end, religion_position)
            self.religion_learner.learn(
                match, game_status, religion_position)

            return education_position

        elif family_position == education_position:
            self.family_leader.memorize(
                match, game_status, family_start, family_end, family_position)
            self.family_learner.learn(match, game_status, family_position)

            self.education_leader.memorize(
                match, game_status, education_start, education_end, education_position)
            self.education_learner.learn(
                match, game_status, education_position)

            return family_position

        elif family_position == religion_position:
            self.family_leader.memorize(
                match, game_status, family_start, family_end, family_position)
            self.family_learner.learn(match, game_status, family_position)

            self.religion_leader.memorize(
                match, game_status, religion_start, religion_end, religion_position)
            self.religion_learner.learn(
                match, game_status, religion_position)

            return religion_position

        elif education_position == religion_position:
            self.religion_leader.memorize(
                match, game_status, religion_start, religion_end, religion_position)
            self.religion_learner.learn(match, game_status, religion_position)

            self.education_leader.memorize(
                match, game_status, education_start, education_end, education_position)
            self.education_learner.learn(
                match, game_status, education_position)

            return education_position

        else:
            position = r.choice(
                [family_position, education_position, religion_position])

            if position == family_position:
                self.family_leader.memorize(
                    match, game_status, family_start, family_end, family_position)
                self.family_learner.learn(match, game_status, family_position)

            elif position == education_position:
                self.education_leader.memorize(
                    match, game_status, education_start, education_end, education_position)
                self.education_learner.learn(
                    match, game_status, education_position)

            elif position == religion_position:
                self.religion_leader.memorize(
                    match, game_status, religion_start, religion_end, religion_position)
                self.religion_learner.learn(
                    match, game_status, religion_position)
            else:
                raise MASPlayError

            return position
