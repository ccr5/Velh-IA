import random as r


class Agent:
    """
    Agent Class
    :param obj: `IAgent` Agent object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    """

    def __init__(self, obj, my_char):
        self.info = obj
        self.char = my_char

    def play(self, game_status):

        if len(self.info['memory']) == 0:
            return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        else:
            pass

        searching = True
        position = -1
        memory_lenght = len(self.info['memory'])

        while searching and memory_lenght != 0:

            for memory in reversed(self.info['memory']):

                for choices in self.info['choices']:

                    if choices['gameStatus'] == game_status:
                        position = choices['position']
                        searching = False

                memory_lenght -= 1

        if position == -1:
            return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        else:
            return position
