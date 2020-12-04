import random as r


class StatisticalAlgorithm:
    """
    Statistical Algorithm Class
    :param obj: `IAlgorithm` Algorithm object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    :param my_enemy: `list` List with its number and symbol ['O', 0]
    """

    def __init__(self, obj, my_char, my_enemy):
        self.info = obj
        self.char = my_char
        self.enemy = my_enemy
        self.empty = ['', 0]

    def play(self, moves):
        """
        Choose a position to play 
        :param moves: game status
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> position = sa.play([-1,0,1,0,-1,-1,-1,-1,-1])
        >>> position
        4
        """
        winner = self.check_win(moves)
        loser = self.check_lose(moves)

        if winner is not None and loser is not None:
            return winner

        elif winner is not None and loser is None:
            return winner

        elif winner is None and loser is not None:
            return loser

        elif winner is None and loser is None:
            position = self.strategy_plan(moves)
            return position
        else:
            return 55

    def strategy_plan(self, moves):
        """
        Find the best position to play using game status
        :param moves: game status
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> position = sa.strategy_plan([-1,1,1,0,0,0,-1,-1,-1])
        >>> position
        0
        """

        best_position = [-1, -10]
        victory = 0
        defeats = 0

        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = self.char[1]
                matrix = self.create_matrix(moves)
                number_victories = self.count_victories(matrix)
                number_defeats = self.count_defeats(matrix)

                if number_defeats == 0:
                    number_defeats = 1
                else:
                    pass

                ratio = (number_victories / number_defeats)

                if best_position[1] > ratio:
                    pass

                elif best_position[1] == ratio:

                    if number_victories > victory:
                        best_position[0] = x
                        best_position[1] = ratio
                        victory = number_victories
                        defeats = number_defeats
                    else:
                        pass

                elif best_position[1] < ratio:
                    best_position[0] = x
                    best_position[1] = ratio
                    victory = number_victories
                    defeats = number_defeats

                else:
                    pass

                moves[x] = -1

            else:
                pass

        return best_position[0]

    def create_matrix(self, moves):
        """
        all possible game variations
        :param moves: game status
        :return: `list` matrix

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
        >>> matrix
        [
            [0,1,1,1,0,0,1,0,1],
            [0,1,1,1,0,0,0,1,1],
            [0,1,1,1,0,0,1,1,0]
        ]
        """
        matrix = []
        empty_position = len([x for x in moves if x == -1])
        who_begin = self.enemy if len([x for x in moves if x == self.enemy[1]]) > len(
            [x for x in moves if x == self.char[1]]) else self.char
        number_variations = 2 ** empty_position

        while len(matrix) != number_variations:
            new_moves = []

            for x in range(0, len(moves)):

                if moves[x] == -1:
                    new_moves.append(r.choice([self.char[1], self.enemy[1]]))
                else:
                    new_moves.append(moves[x])

            if new_moves in matrix:
                del new_moves
            else:
                matrix.append(new_moves)
                del new_moves

        return [move for move in matrix if len([x for x in move if x == who_begin[1]]) == 5 and
                len([o for o in move if o != who_begin[1] and o != -1]) == 4]

    def count_victories(self, matrix):
        """
        Count how many victories has in a matrix of game variation
        :param matrix: matrix of all possible game variations
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
        >>> victories = sa.count_victories(matrix)
        >>> victories
        100
        """
        result = 0

        for x in matrix:
            checklist = self.sequence_list(x)

            for y in checklist:

                if y == [self.char[1], self.char[1], self.char[1]]:
                    result += 1
                else:
                    pass

        return result

    def count_defeats(self, matrix):
        """
        Count how many defeats has in a matrix of game variation
        :param matrix: matrix of all possible game variations
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> matrix = sa.create_matrix([0,1,1,1,0,0,-1,-1,-1])
        >>> defeats = sa.count_defeats(matrix)
        >>> defeats
        3
        """
        result = 0

        for x in matrix:
            checklist = self.sequence_list(x)

            for y in checklist:

                if y == [self.enemy[1], self.enemy[1], self.enemy[1]]:
                    result += 1
                else:
                    pass

        return result

    def check_win(self, moves):
        """
        Check and return a position to win
        :param moves: game status
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> position = sa.check_win([-1,0,1,0,0,1,0,-1,-1])
        >>> position
        8
        """
        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = self.char[1]
                checklist = self.sequence_list(moves)

                for y in checklist:

                    if y == [self.char[1], self.char[1], self.char[1]]:
                        return x
                    else:
                        moves[x] = -1
            else:
                pass

    def check_lose(self, moves):
        """
        Check and return a position to protect itself
        :param moves: game status
        :return: `int` int

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> position = sa.check_lose([-1,0,1,0,-1,1,0,-1,-1])
        >>> position
        0
        """
        for x in range(0, len(moves)):

            if moves[x] == -1:
                moves[x] = self.enemy[1]
                checklist = self.sequence_list(moves)

                for y in checklist:

                    if y == [self.enemy[1], self.enemy[1], self.enemy[1]]:
                        return x
                    else:
                        moves[x] = -1
            else:
                pass

    def sequence_list(self, game_status):
        """
        All sequence to win 
        :param game_status: game status
        :return: `list` matrix

        Usage
        >>> from sa import StatisticalAlgorithm
        >>> sa = StatisticalAlgorithm(obj, ['X', 1], ['O', 0])
        >>> ret = sa.sequence_list([-1,0,1,0,-1,1,0,-1,-1])
        >>> ret
        [
            [-1, 0, 1],     [0, -1, 1], 
            [0, -1, -1],    [-1, 0, 0], 
            [0, -1, -1],    [1, 1, -1],
            [-1, -1, -1],   [1, -1, 0]
        ]
        """
        return [[game_status[0], game_status[1], game_status[2]],
                [game_status[3], game_status[4], game_status[5]],
                [game_status[6], game_status[7], game_status[8]],
                [game_status[0], game_status[3], game_status[6]],
                [game_status[1], game_status[4], game_status[7]],
                [game_status[2], game_status[5], game_status[8]],
                [game_status[0], game_status[4], game_status[8]],
                [game_status[2], game_status[4], game_status[6]]]
