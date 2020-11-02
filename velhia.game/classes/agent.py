class Agent:
    """
    Agent Class
    :param obj: `IAgent` Agent object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    """

    def __init__(self, obj, my_char):
        self.info = obj
        self.char = my_char
