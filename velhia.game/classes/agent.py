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

    def remember(self, match, game_status):

        if len(self.info['memory'][-1]['choices']) == 0:
            position = r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            return position

        elif self.info['memory'][-1]['matchId'] == match.info['_id']:
            searching = True
            position = -1
            memory_lenght = len(self.info['memory'])

            while searching and memory_lenght != 0:

                for memory in reversed(self.info['memory']):

                    for choices in memory['choices']:

                        if choices['gameStatus'] == game_status:
                            position = choices['position']
                            searching = False

                    memory_lenght -= 1

            if position == -1:
                position = r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
                return position

            else:
                return position
        else:
            raise SystemError

    def memorize(self, match, game_status, start, end, position):

        time = end - start
        time = time.microseconds / 1000000

        self.info['memory'][-1]['choices'].append({
            'dateRequest': start.ctime(),
            'gameStatus': game_status,
            'timeToAct': time,
            'action': position
        })

    def learn(self, match, game_status, position):

        if self.info['memory'][-1]['matchId'] == match.info['_id']:
            start = datetime.now()
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

            self.info['memory'][-1]['choices'].append({
                'dateRequest': start.ctime(),
                'gameStatus': game_status,
                'timeToAct': time,
                'action': position
            })

        else:
            raise SystemError
