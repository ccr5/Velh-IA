from config.database import Database
from classes.statistical_algorithm import StatisticalAlgorithm
from classes.match import Match
from classes.agent import Agent
from datetime import datetime
import json


class Velhia:
    """ All functions and methods to the game works """

    match_db = Database('v1', 'matchs')
    family_db = Database('v1', 'families')
    education_db = Database('v1', 'educations')
    religion_db = Database('v1', 'religions')
    algorithm_db = Database('v1', 'algorithms')

    def play(self):
        try:
            last_match = self.match_db.get_last(1).json()

            if len(last_match) == 0 or last_match[0]['status'] != 'PENDENT':
                sa = self.get_lastest_sa()
                (education_leader, education_learner) = self.get_latest_agent(
                    self.education_db
                )
                (religion_leader, religion_learner) = self.get_latest_agent(
                    self.religion_db
                )
                (family_leader, family_learner) = self.get_latest_agent(
                    self.family_db
                )
                match = self.create_new_match(
                    sa, family_leader, religion_leader, education_leader
                )
            else:
                pass

        except:
            print('play() error')

    def get_lastest_sa(self):

        if len(self.algorithm_db.get_last(1).json()) == 0:
            sa = StatisticalAlgorithm(self.algorithm_db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "memory": [],
                "matchs": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('X', 1), ('O', 0))
        else:
            sa = StatisticalAlgorithm(
                self.algorithm_db.get_last(1).json()[0],
                ('X', 1), ('O', 0))

        return sa

    def get_latest_agent(self, db):

        if len(db.get_last(2).json()) < 2:
            leader = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": "I'm the first one, bitch ;)",
                "becomeLeader": datetime.now().ctime(),
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))

            learner = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": leader.info['_id'],
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))
        else:
            res = db.get_last(2).json()
            return self.check_life(db, res)

    def create_new_match(self, sa, family, religion, education):

        match = Match(self.match_db.create(json.dumps({
            "begin": datetime.now().ctime(),
            "time": 0,
            "sa": {"playerId": sa.info['_id'], "symbol": sa.char[0]},
            "mas": {"family": {"playerId": family.info['_id'], "symbol": family.char[0]},
                    "religion": {"playerId": religion.info['_id'], "symbol": religion.char[0]},
                    "education": {"playerId": education.info['_id'], "symbol": education.char[0]}},
            "plays": [],
            "status": "PENDENT"})))

        return match

    def check_life(self, db, agents):

        if agents[1]['life'] > 0:
            leader = Agent(agents[1], ('O', 0))
            learner = Agent(agents[0], ('O', 0))
        else:
            agents[1]['death'] = datetime.now().ctime()
            db.update(agents[1]['_id'], agents[1])
            agents[0]['becomeLeader'] = datetime.now().ctime()
            db.update(agents[0]['_id'], agents[0])
            leader = Agent(agents[0], ('O', 0))
            learner = Agent(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "progenitor": leader.info['_id'],
                "life": 100,
                "memory": [],
                "matchsAsLearner": 0,
                "matchsAsLeader": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('O', 0))

        return (leader, learner)


#         ENDGAME = False
#         NEW_GAME = False
#         try:
#             while not ENDGAME:

#                 while not NEW_GAME:
#                     NEW_GAME = Velhia.play_sa(
#                         MOVES, EMPTY, PLAYER1, STATISTICAL)

#                 if NEW_GAME[1] == PLAYER1:
#                     count_player1 += 1
#                 else:
#                     count_player2 += 1

#                 print("\n Player 1: {} \t Player 2: {}".format(
#                     count_player1, count_player2))
#                 NEW_GAME = NEW_GAME[0]

#                 RESULT = input("Do you wanna play again Y/N? ")
#                 RESULT = RESULT.upper()

#                 if RESULT == 'Y':

#                     ENDGAME = False
#                     NEW_GAME = False
#                     Velhia.clean_game(MOVES)

#                 elif RESULT == "N":

#                     ENDGAME = True

#                 else:
#                     pass

#                 print("Thank you for play!")

#         except Exception as e:
#             raise e

#    def play_sa(self, m, e, p, s):
#         """
#         This method will call when the player wanna play with s.a (statistical algorithm)
#         :param m: moves until now
#         :param e: value of empty places
#         :param p: value and character's player1
#         :param s: value and character's player2
#         :return: True when player or s.a win a game
#         """
#         game = False
#         doppler_sa = Doppler10(s, p)

#         try:

#             while not game:

#                 Velhia.camp(m, e, p, s)

#                 if not game:
#                     i = Velhia.check_input(m)
#                     m[i] = p[1]
#                 else:
#                     pass

#                 game = Velhia.check_game(m, p, s)
#                 Velhia.camp(m, e, p, s)

#                 if not game:
#                     i = doppler_sa.doppler_sa(m)
#                     m[i] = s[1]

#                 game = Velhia.check_game(m, p, s)

#             return game

#         except Exception as e:
#             raise e

#     def play_play(self, m, e, p, s):
#         """
#         This method will call when the player wanna play with s.a (statistical algorithm)
#         :param m: moves until now
#         :param e: value of empty places
#         :param p: value and character's player1
#         :param s: value and character's player2
#         :return: True when player or s.a win a game
#         """
#         game = False

#         try:

#             while not game:

#                 Velhia.camp(m, e, p, s)

#                 if not game:
#                     i = Velhia.check_input(m)
#                     m[i] = p[1]
#                 else:
#                     pass

#                 game = Velhia.check_game(m, p, s)
#                 Velhia.camp(m, e, p, s)

#                 if not game:
#                     i = Velhia.check_input(m)
#                     m[i] = s[1]

#                 game = Velhia.check_game(m, p, s)

#             return game

#         except Exception as e:
#             raise e


#     def check_input(self, m):
#         """
#         check if the player or s.a choose a correct input
#         :param m: moves until now
#         :return: the position to add in moves
#         """

#         try:
#             i = -2

#             if -1 not in m:
#                 print('the game is draw!')
#                 print('Restarting...')
#                 print('change who will begin the game...')
#                 Velhia.clean_game(m)
#             else:
#                 pass

#             while i not in m:

#                 i = int(input('Witch position do you wanna play? '))

#                 if i < 1 or i > 9:
#                     print("\n There isn't this position!!!")
#                     i = -2
#                     continue
#                 else:
#                     if m[i-1] != -1:
#                         print('\n this position was chosen!!!')
#                         i = -2
#                     else:
#                         return i - 1

#         except Exception as e:
#             raise e


#     def check_game(self, m, p, s):
#         """
#         :param m: moves until now
#         :param p: value and character's player1
#         :param s: value and character's player2
#         :return: True and print who won the game
#         """
#         try:
#             checklist = [[m[0], m[1], m[2]],
#                          [m[3], m[4], m[5]],
#                          [m[6], m[7], m[8]],
#                          [m[0], m[3], m[6]],
#                          [m[1], m[4], m[7]],
#                          [m[2], m[5], m[8]],
#                          [m[0], m[4], m[8]],
#                          [m[2], m[4], m[6]]]

#             for x in checklist:

#                 if x == [1, 1, 1]:

#                     if p[1] == x[0]:
#                         print("Player 1 win!")
#                         return True, p
#                     else:
#                         print("Player 2 win!")
#                         return True, s

#                 elif x == [0, 0, 0]:

#                     if p[1] == x[0]:
#                         print("Player 1 win!")
#                         return True, p
#                     else:
#                         print("Player 2 win!")
#                         return True, s

#                 else:
#                     pass

#             return False

#         except Exception as e:
#             raise e


#     def clean_game(self, m):
#         """
#         :param m: moves until now
#         :return: a new field to play (only -1 / '')
#         """

#         for x in range(0, len(m)):
#             m[x] = -1
