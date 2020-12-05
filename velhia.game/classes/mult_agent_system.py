import random as r


class MultiAgentSystem:

    def __init__(self,
                 family_leader, family_learner,
                 education_leader, education_learner,
                 religion_leader, religion_learner
                 ):
        self.family_leader = family_leader
        self.family_learner = family_learner
        self.education_leader = education_leader
        self.education_learner = education_learner
        self.religion_leader = religion_leader
        self.religion_learner = religion_learner

    def play(self, game_status):

        family_position = self.family_leader.play(game_status)
        self.family_leader.teach(
            self.family_learner, game_status, family_position)

        education_position = self.education_leader.play(game_status)
        self.education_leader.teach(
            self.education_learner, game_status, education_position)

        religion_position = self.religion_leader.play(game_status)
        self.education_leader.teach(
            self.religion_learner, game_status, religion_position)

        if family_position in [education_position, religion_position]:
            return family_position

        if education_position in [family_position, religion_position]:
            return education_position

        if religion_position in [family_position, education_position]:
            return religion_position

        return r.choice([family_position, education_position, religion_position])
