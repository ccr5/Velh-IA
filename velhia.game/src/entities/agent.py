class Agent:
    """
    Agent Class
    :param obj: `IAgent` Agent object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    """

    def __init__(self, obj, my_char):
        self.id = obj['_id']
        self.birth = obj['birth']
        self.progenitor = obj['progenitor']
        self.becomeLeader = obj['becomeLeader'] if 'becomeLeader' in obj else ''
        self.death = obj['death'] if 'death' in obj else ''
        self.life = obj['life']
        self.memory = obj['memory']
        self.matchsAsLearner = obj['matchsAsLearner']
        self.matchsAsLeader = obj['matchsAsLeader']
        self.victories = obj['victories']
        self.defeats = obj['defeats']
        self.draw = obj['draw']
        self.char = my_char
