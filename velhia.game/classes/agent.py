import random as r
from datetime import datetime
from errors.agent.remember_error import RememberError
from errors.agent.memorize_error import MemorizeError
from errors.agent.learn_error import LearnError


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

    def remember(self, game_status):
        """
        Remember a game when was received a game status like now
        :param game_status: `List` a game status

        usage
        >>> from classes.agent import Agent
        >>> agt = Agent(obj, ['O', 0])
        >>> game_status = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        >>> position = agt.remember(match, game_status)
        >>> position
        5
        """

        if len(self.memory) > 0:

            if len(self.memory[0]['choices']) == 0:
                return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

            else:
                searching = True
                position = -1
                memory_lenght = len(self.memory)

                while searching and memory_lenght != 0:

                    for memory in reversed(self.memory):

                        for choices in memory['choices']:

                            if choices['gameStatus'] == game_status:
                                position = choices['action']
                                searching = False

                        memory_lenght -= 1

                if position == -1:
                    return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

                else:
                    # return r.choice([position, r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])])
                    return position

        else:
            raise RememberError

    def memorize(self, match, game_status, start, end, position):
        """
        Add a new play in the memory
        :param match: `Match` a Match obj
        :param game_status: `List` a game status
        :param start: `datetime` when this play started
        :param end: `datetime` when this play ended
        :param position: `int` the chosen position

        usage
        >>> from classes.agent import Agent
        >>> agt = Agent(obj, ['O', 0])
        >>> game_status = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        >>> start = datetime.now()
        >>> end = datetime.now()
        >>> position = 5
        >>> agt.memorize(match, game_status, start, end, position)
        """

        try:
            time = end - start
            time = time.microseconds / 1000000

            self.memory[-1]['choices'].append({
                'dateRequest': start.ctime(),
                'gameStatus': game_status,
                'timeToAct': time,
                'action': position
            })

        except:
            raise MemorizeError

    def learn(self, match, game_status, position):
        """
        Learn a play from its progenitor
        :param match: `Match` a Match obj
        :param game_status: `List` a game status
        :param position: `int` the chosen position

        usage
        >>> from classes.agent import Agent
        >>> agt = Agent(obj, ['O', 0])
        >>> game_status = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
        >>> position = 5
        >>> agt.learn(match, game_status, position)
        """

        if self.memory[-1]['matchId'] == match.id:
            start = datetime.now()
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

            self.memory[-1]['choices'].append({
                'dateRequest': start.ctime(),
                'gameStatus': game_status,
                'timeToAct': time,
                'action': position
            })

        else:
            raise LearnError

    def create_object(self):
        """
        Create a full obj to use in database functions
        """

        agent_info = {"_id": self.id,
                      "birth": self.birth,
                      "progenitor": self.progenitor,
                      "life": self.life,
                      "memory": self.memory,
                      "matchsAsLearner": self.matchsAsLearner,
                      "matchsAsLeader": self.matchsAsLeader,
                      "victories": self.victories,
                      "defeats": self.defeats,
                      "draw": self.draw}

        if self.becomeLeader != '':
            agent_info['becomeLeader'] = self.becomeLeader

        if self.death != '':
            agent_info['death'] = self.death

        return agent_info
