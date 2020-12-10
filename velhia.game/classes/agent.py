import random as r
from datetime import datetime


class Agent:
    """
    Agent Class
    :param obj: `IAgent` Agent object saved in MongoDB
    :param my_char: `list` List with its number and symbol ['X', 1]
    """

    def __init__(self, obj, my_char):
        self.info = obj
        self.char = my_char

    def play(self, match, game_status):

        if len(self.info['memory']) == 0:
            start = datetime.now()
            position = r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

            new_memory = {
                'matchId': match.info['_id'],
                'isLearner': False,
                'choices': [{
                    'dateRequest': start.ctime(),
                    'gameStatus': game_status,
                    'timeToAct': time,
                    'action': position
                }]
            }

            self.info['memory'].append(new_memory)
            return position

        elif self.info['memory'][-1]['matchId'] == match.info['_id']:
            start = datetime.now()
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
                position = r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
                end = datetime.now()
                time = end - start
                time = time.microseconds / 1000000

                new_choices = {
                    'dateRequest': start.ctime(),
                    'gameStatus': game_status,
                    'timeToAct': time,
                    'action': position
                }

                self.info['memory']['choices'].append(new_choices)
                return position

            else:
                end = datetime.now()
                time = end - start
                time = time.microseconds / 1000000

                new_choices = {
                    'dateRequest': start.ctime(),
                    'gameStatus': game_status,
                    'timeToAct': time,
                    'action': position
                }

                self.info['memory']['choices'].append(new_choices)
                return position
        else:
            raise SystemError

    def learn(self, match, game_status, position):

        if len(self.info['memory']) == 0:
            start = datetime.now()
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

            new_memory = {
                'matchId': match.info['_id'],
                'isLearner': True,
                'choices': [{
                    'dateRequest': start.ctime(),
                    'gameStatus': game_status,
                    'timeToAct': time,
                    'action': position
                }]
            }

            self.info['memory'].append(new_memory)

        elif self.info['memory'][-1]['matchId'] == match.info['_id']:
            start = datetime.now()
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

            new_choices = {
                'dateRequest': start.ctime(),
                'gameStatus': game_status,
                'timeToAct': time,
                'action': position
            }

            self.info['memory']['choices'].append(new_choices)

        else:
            raise SystemError
