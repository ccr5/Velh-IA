import random as r
from typing import List, Union, Any, Callable, Tuple
from datetime import datetime, timedelta
from entities.agent.agent import Agent
from entities.agent.choices import Choices
from entities.agent.memory import Memory
from entities.match.match import Match
from usecases.agent.agent_handler import looking_for_memory, create_new_choice, add_new_choices
from usecases.agent.agent_handler import kill_agent, add, promote_leader, update_match_status
from usecases.agent.agent_handler import create_leader, create_learner
from usecases.agent.agent_database import get_last, update_agent
from usecases.agent.agent_adapter_type import AgentAdapter
from usecases.database.database_types import DatabaseRepositoryType
from shared.types.game_status import GameStatus
from shared.errors.agent.remember_error import RememberError
from shared.errors.agent.memorize_error import MemorizeError
from shared.errors.agent.learn_error import LearnError
from shared.errors.handler.agent.check_life_error import CheckLifeError
from shared.errors.handler.agent.get_agent_error import GetAgentError


def get_valid_agents(agent_repository: DatabaseRepositoryType) -> Tuple[Agent, Agent]:
    """
    Get the lastest agent obj in the database or create if it not exists
    If a match and player was passed, it will get the lastest agents as of a match obj in the database
    :param db: `Database` a Database object
    :param match: `Match`a Match object
    :param player: `string` a player ID
    """

    try:
        agents: List[Agent] = get_last(agent_repository, 2)

        if agents is None:
            leader: Agent = create_leader(agent_repository)
            learner: Agent = create_learner(agent_repository, leader['_id'])
        else:
            suitor_leader: Agent = agents[1]
            suitor_learner: Agent = agents[0]

            if check_agent(suitor_leader, 'life'):
                leader: Agent = suitor_leader
                learner: Agent = suitor_learner
            else:
                dead_leader: Agent = alter_agent('kill')(suitor_leader)
                update_agent(agent_repository, dead_leader)
                new_leader: Agent = alter_agent('promote')(suitor_learner)
                update_agent(agent_repository, new_leader)
                leader: Agent = new_leader
                learner: Agent = create_learner(
                    agent_repository, leader['_id'])

        return (leader, learner)

    except:
        raise GetAgentError


def alter_agent(operation: str) -> Callable:

    if operation == 'add':
        return add
    elif operation == 'kill':
        return kill_agent
    elif operation == 'promote':
        return promote_leader
    elif operation == 'match response':
        return update_match_status
    else:
        None


def check_agent(agent: Union[AgentAdapter, Agent], validation: str) -> bool:

    if validation == 'life':
        return agent['life'] > 0


def learn(choice_list: List[Choices], new_choice: Choices) -> List[Choices]:
    """ Add a new choice in the memory """

    try:
        return list([choice_list, new_choice])

    except:
        raise LearnError


def remember(agent: Agent, game_status: GameStatus):
    """ Remember a game when was received a game status like now """

    if len(agent['memory']) > 0:

        if len(agent['memory'][0]['choices']) == 0:
            return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

        else:
            position: int = looking_for_memory(
                agent['memory'],
                len(agent['memory']),
                game_status
            )

            if position == -1:
                return r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])

            else:
                # return r.choice([position, r.choice([0, 1, 2, 3, 4, 5, 6, 7, 8])])
                return position

    else:
        raise RememberError


def memorize(memory: Memory, match: Match,
             game_status: GameStatus,
             time: float, position: int) -> Agent:
    """ Add a new choice in the memory """

    try:

        choice: Choices = create_new_choice(match, game_status,
                                            time, position)

        new_list_choice: List[Choices] = add_new_choices(
            memory['choices'], choice
        )

        return 1

    except:
        raise MemorizeError
