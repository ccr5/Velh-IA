import random as r


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

        family_position = self.family_leader.play(match, game_status)
        self.family_learner.learn(match, game_status, family_position)

        education_position = self.education_leader.play(match, game_status)
        self.education_learner.learn(match, game_status, education_position)

        religion_position = self.religion_leader.play(match, game_status)
        self.religion_learner.learn(match, game_status, religion_position)

        if family_position in [education_position, religion_position]:
            return family_position
        elif education_position in [family_position, religion_position]:
            return education_position
        elif religion_position in [family_position, education_position]:
            return religion_position
        else:
            return r.choice([family_position, education_position, religion_position])

    def clear_latest_play(self):

        del(self.family_leader['memory'][-1]['choices'][-1])
        del(self.family_learner['memory'][-1]['choices'][-1])
        del(self.education_leader['memory'][-1]['choices'][-1])
        del(self.education_learner['memory'][-1]['choices'][-1])
        del(self.religion_leader['memory'][-1]['choices'][-1])
        del(self.religion_learner['memory'][-1]['choices'][-1])
