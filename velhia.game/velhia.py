import os
from tuples.symbols import EMPTY
from tuples.positions import MOVES


class Velhia:
    """
    All functions and methods to the game works
    """

    def __init__(self, previews_data, player1, player2):
        self.data = previews_data
        self.p1 = player1
        self.p2 = player2
        self.empty = EMPTY
        self.moves = MOVES

    def play(self):
        """
        docstring
        """
        ENDGAME = False
        NEW_GAME = False
        try:
            while not ENDGAME:

                while not NEW_GAME:
                    NEW_GAME = Velhia.play_sa(
                        MOVES, EMPTY, PLAYER1, STATISTICAL)

                if NEW_GAME[1] == PLAYER1:
                    count_player1 += 1
                else:
                    count_player2 += 1

                print("\n Player 1: {} \t Player 2: {}".format(
                    count_player1, count_player2))
                NEW_GAME = NEW_GAME[0]

                RESULT = input("Do you wanna play again Y/N? ")
                RESULT = RESULT.upper()

                if RESULT == 'Y':

                    ENDGAME = False
                    NEW_GAME = False
                    Velhia.clean_game(MOVES)

                elif RESULT == "N":

                    ENDGAME = True

                else:
                    pass

                print("Thank you for play!")

        except Exception as e:
            raise e
      # Checar quem é o próximo a jogar
      # Inicia o loop
      # 1 solicita para o primeiro a jogar
      # checa se ganhou
      # 2 solicita para o segundo a jogar
      # checa se ganhou

  @staticmethod
   def play_sa(m, e, p, s):
        """
        This method will call when the player wanna play with s.a (statistical algorithm)
        :param m: moves until now
        :param e: value of empty places
        :param p: value and character's player1
        :param s: value and character's player2
        :return: True when player or s.a win a game
        """
        game = False
        doppler_sa = Doppler10(s, p)

        try:

            while not game:

                Velhia.camp(m, e, p, s)

                if not game:
                    i = Velhia.check_input(m)
                    m[i] = p[1]
                else:
                    pass

                game = Velhia.check_game(m, p, s)
                Velhia.camp(m, e, p, s)

                if not game:
                    i = doppler_sa.doppler_sa(m)
                    m[i] = s[1]

                game = Velhia.check_game(m, p, s)

            return game

        except Exception as e:
            raise e

    @staticmethod
    def play_play(m, e, p, s):
        """
        This method will call when the player wanna play with s.a (statistical algorithm)
        :param m: moves until now
        :param e: value of empty places
        :param p: value and character's player1
        :param s: value and character's player2
        :return: True when player or s.a win a game
        """
        game = False

        try:

            while not game:

                Velhia.camp(m, e, p, s)

                if not game:
                    i = Velhia.check_input(m)
                    m[i] = p[1]
                else:
                    pass

                game = Velhia.check_game(m, p, s)
                Velhia.camp(m, e, p, s)

                if not game:
                    i = Velhia.check_input(m)
                    m[i] = s[1]

                game = Velhia.check_game(m, p, s)

            return game

        except Exception as e:
            raise e

    @staticmethod
    def check_input(m):
        """
        check if the player or s.a choose a correct input
        :param m: moves until now
        :return: the position to add in moves
        """

        try:
            i = -2

            if -1 not in m:
                print('the game is draw!')
                print('Restarting...')
                print('change who will begin the game...')
                Velhia.clean_game(m)
            else:
                pass

            while i not in m:

                i = int(input('Witch position do you wanna play? '))

                if i < 1 or i > 9:
                    print("\n There isn't this position!!!")
                    i = -2
                    continue
                else:
                    if m[i-1] != -1:
                        print('\n this position was chosen!!!')
                        i = -2
                    else:
                        return i - 1

        except Exception as e:
            raise e

    @staticmethod
    def check_game(m, p, s):
        """
        :param m: moves until now
        :param p: value and character's player1
        :param s: value and character's player2
        :return: True and print who won the game
        """
        try:
            checklist = [[m[0], m[1], m[2]],
                         [m[3], m[4], m[5]],
                         [m[6], m[7], m[8]],
                         [m[0], m[3], m[6]],
                         [m[1], m[4], m[7]],
                         [m[2], m[5], m[8]],
                         [m[0], m[4], m[8]],
                         [m[2], m[4], m[6]]]

            for x in checklist:

                if x == [1, 1, 1]:

                    if p[1] == x[0]:
                        print("Player 1 win!")
                        return True, p
                    else:
                        print("Player 2 win!")
                        return True, s

                elif x == [0, 0, 0]:

                    if p[1] == x[0]:
                        print("Player 1 win!")
                        return True, p
                    else:
                        print("Player 2 win!")
                        return True, s

                else:
                    pass

            return False

        except Exception as e:
            raise e

    @staticmethod
    def clean_game(m):
        """
        :param m: moves until now
        :return: a new field to play (only -1 / '')
        """

        for x in range(0, len(m)):
            m[x] = -1
