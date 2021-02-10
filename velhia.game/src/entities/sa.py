class StatisticalAlgorithm:
    """
    Statistical Algorithm Class
    :param obj: `IAlgorithm` Algorithm object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    :param my_enemy: `list` List with its number and symbol ['O', 0]
    """

    def __init__(self, obj, my_char, my_enemy):
        self.id = obj['_id']
        self.birth = obj['birth']
        self.matchs = obj['matchs']
        self.victories = obj['victories']
        self.defeats = obj['defeats']
        self.draw = obj['draw']
        self.char = my_char
        self.enemy = my_enemy
        self.empty = ['', -1]
