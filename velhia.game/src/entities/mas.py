class MultiAgentSystem:
    """
    Multi Agent System Class
    :param family_leader: `IAgent` Agent object saved in MongoDB
    :param family_learner: `IAgent` Agent object saved in MongoDB
    :param education_leader: `IAgent` Agent object saved in MongoDB
    :param education_learner: `IAgent` Agent object saved in MongoDB
    :param religion_leader: `IAgent` Agent object saved in MongoDB
    :param religion_learner: `IAgent` Agent object saved in MongoDB
    """

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
