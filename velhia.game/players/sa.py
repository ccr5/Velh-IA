import random as r


class StatisticalAlgorithm:
    """
    :return He'll play Velh-IA thinking where he win or need to protect himself
    and choose a position when he has more chance to win
    """

    def __init__(self, my_char, my_enemy):
        self.char = my_char
        self.enemy = my_enemy
        self.empty = ['', 0]
        self.moves = [-1, -1, -1, -1, -1, -1, -1, -1, -1]

    def play(self, moves):
        """
        :return: The number that he has more chance to win or not lose
        """
        self.moves = moves

        winner = self.check_win()
        loser = self.check_lose()

        if winner is not None and loser is not None:
            return winner

        elif winner is not None and loser is None:
            return winner

        elif winner is None and loser is not None:
            return loser

        elif winner is None and loser is None:
            play = self.strategy_plan()
            return play

        else:
            return 55

    def strategy_plan(self):
        """
        :return: The best position to play
        """

        best_position = [-1, -10]
        wins = 0
        defeats = 0

        for x in range(0, len(self.moves)):
            if self.moves[x] == -1:
                self.moves[x] = self.char

                matrix = self.create_matrix()
                new_wins = self.count_wins(matrix)
                new_defeats = self.count_defeats(matrix)

                if new_defeats == 0:
                    new_defeats = 1
                else:
                    pass

                ratio = (new_wins / new_defeats)

                if best_position[1] > ratio:
                    pass

                elif best_position[1] == ratio:

                    if new_wins > wins and new_defeats == defeats:
                        best_position[0] = x
                        best_position[1] = ratio
                        wins = new_wins
                        defeats = new_defeats
                    elif new_wins == wins and new_defeats < defeats:
                        best_position[0] = x
                        best_position[1] = ratio
                        wins = new_wins
                        defeats = new_defeats
                    else:
                        pass

                elif best_position[1] < ratio:
                    best_position[0] = x
                    best_position[1] = ratio
                    wins = new_wins
                    defeats = new_defeats

                else:
                    pass

                self.moves[x] = -1

            else:
                pass

        return best_position[0]

    def create_matrix(self):
        """
        :return: all possible variations into the moves received
        """
        matrix = []

        for i in range(0, 100000):
            new_moves = []

            for x in range(0, len(self.moves)):
                if self.moves[x] == -1:
                    new_moves.append(r.choice([0, 1]))
                else:
                    new_moves.append(self.moves[x])

            if new_moves in matrix:
                del new_moves
            else:
                matrix.append(new_moves)
                del new_moves

        return matrix

    def count_wins(self, matrix):
        """
        :return: count some wins he will have if choose this position
        """

        result = 0

        for x in matrix:

            checklist = [[x[0], x[1], x[2]],
                         [x[3], x[4], x[5]],
                         [x[6], x[7], x[8]],
                         [x[0], x[3], x[6]],
                         [x[1], x[4], x[7]],
                         [x[2], x[5], x[8]],
                         [x[0], x[4], x[8]],
                         [x[2], x[4], x[6]]]

            for y in checklist:

                if y == [self.char[1], self.char[1], self.char[1]]:
                    result += 1
                else:
                    pass

        return result

    def count_defeats(self, matrix):
        """
        :return: count some defeats he will have if choose this position
        """

        result = 0

        for x in matrix:

            checklist = [[x[0], x[1], x[2]],
                         [x[3], x[4], x[5]],
                         [x[6], x[7], x[8]],
                         [x[0], x[3], x[6]],
                         [x[1], x[4], x[7]],
                         [x[2], x[5], x[8]],
                         [x[0], x[4], x[8]],
                         [x[2], x[4], x[6]]]

            for y in checklist:

                if y == [self.enemy[1], self.enemy[1], self.enemy[1]]:
                    result += 1
                else:
                    pass

        return result

    def check_win(self):
        """
        :return: True if he win
        """
        for x in range(0, len(self.moves)):
            if self.moves[x] == -1:
                self.moves[x] = self.char[1]
                checklist = [[self.moves[0], self.moves[1], self.moves[2]],
                             [self.moves[3], self.moves[4], self.moves[5]],
                             [self.moves[6], self.moves[7], self.moves[8]],
                             [self.moves[0], self.moves[3], self.moves[6]],
                             [self.moves[1], self.moves[4], self.moves[7]],
                             [self.moves[2], self.moves[5], self.moves[8]],
                             [self.moves[0], self.moves[4], self.moves[8]],
                             [self.moves[2], self.moves[4], self.moves[6]]]
                for y in checklist:
                    if y == [self.char[1], self.char[1], self.char[1]]:
                        return x
                    else:
                        self.moves[x] = -1
            else:
                pass

    def check_lose(self):
        """
        :return: True if he lose
        """
        for x in range(0, len(self.moves)):
            if self.moves[x] == -1:
                self.moves[x] = self.enemy[1]
                checklist = [[self.moves[0], self.moves[1], self.moves[2]],
                             [self.moves[3], self.moves[4], self.moves[5]],
                             [self.moves[6], self.moves[7], self.moves[8]],
                             [self.moves[0], self.moves[3], self.moves[6]],
                             [self.moves[1], self.moves[4], self.moves[7]],
                             [self.moves[2], self.moves[5], self.moves[8]],
                             [self.moves[0], self.moves[4], self.moves[8]],
                             [self.moves[2], self.moves[4], self.moves[6]]]
                for y in checklist:
                    if y == [self.enemy[1], self.enemy[1], self.enemy[1]]:
                        return x
                    else:
                        self.moves[x] = -1
            else:
                pass
