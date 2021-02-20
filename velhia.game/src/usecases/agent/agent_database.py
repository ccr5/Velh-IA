import json
from datetime import datetime
from typing import Union, Tuple
from usecases.database.database_types import DatabaseRepositoryType
from entities.agent.agent import Agent
from usecases.agent.agent_use_cases import check_agent, alter
from usecases.agent.agent_dto import agent_to_entity
from shared.objects import create_object
from shared.errors.handler.agent.get_agent_error import GetAgentError


def save_agent(agent_repository: DatabaseRepositoryType, agent: Agent) -> Agent:

    res: list = agent_repository['create'](agent).json()
    return agent_to_entity(res)


def get_by_id(agent_repository: DatabaseRepositoryType, hash: str) -> Union[Agent, None]:
    obj_id: dict = {'_id': hash}
    res: list = agent_repository['get'](filters=obj_id).json()

    if len(res) == 1:
        return agent_to_entity(res[0])
    else:
        None


def get_by_progenitor(agent_repository: DatabaseRepositoryType, hash: str) -> Union[Agent, None]:
    obj_id: dict = {'progenitor': hash}
    res: list = agent_repository['get'](filters=obj_id).json()

    if len(res) == 1:
        return agent_to_entity(res[0])
    else:
        None


def get_valid_agents(agent_repository: DatabaseRepositoryType) -> Tuple[Agent, Agent]:
    """
    Get the lastest agent obj in the database or create if it not exists
    If a match and player was passed, it will get the lastest agents as of a match obj in the database
    :param db: `Database` a Database object
    :param match: `Match`a Match object
    :param player: `string` a player ID
    """

    try:
        res: list = agent_repository['get'](offset=0, limit=2,
                                            sort="createdAt:desc").json()

        if len(res) < 2:
            leader: Agent = save_agent(
                agent_repository, create_object(
                    [
                        ('birth', datetime.now().ctime()),
                        ('progenitor', "I'm the first one, bitch ;)"),
                        ("becomeLeader", datetime.now().ctime()),
                        ("life", 100),
                        ("memory", []),
                        ("matchsAsLearner", 0),
                        ("matchsAsLeader", 0),
                        ("victories", 0),
                        ("defeats", 0),
                        ("draw", 0)
                    ], 10
                )
            )

            learner: Agent = save_agent(
                agent_repository, create_object(
                    [
                        ('birth', datetime.now().ctime()),
                        ('progenitor', leader['_id']),
                        ("life", 100),
                        ("memory", []),
                        ("matchsAsLearner", 0),
                        ("matchsAsLeader", 0),
                        ("victories", 0),
                        ("defeats", 0),
                        ("draw", 0)
                    ], 9
                )
            )
        else:
            suitor_leader: Agent = agent_to_entity(res[1])
            suitor_learner: Agent = agent_to_entity(res[0])

            if check_agent(suitor_leader, 'life'):
                leader: Agent = suitor_leader
                learner: Agent = suitor_learner
            else:
                dead_leader: Agent = alter('kill')(suitor_leader)
                update_agent(agent_repository, dead_leader)
                new_leader: Agent = alter('promote')(suitor_learner)
                update_agent(agent_repository, new_leader)
                leader: Agent = new_leader
                learner: Agent = save_agent(
                    agent_repository, create_object(
                        [
                            ('birth', datetime.now().ctime()),
                            ('progenitor', leader['_id']),
                            ("life", 100),
                            ("memory", []),
                            ("matchsAsLearner", 0),
                            ("matchsAsLeader", 0),
                            ("victories", 0),
                            ("defeats", 0),
                            ("draw", 0)
                        ], 10
                    )
                )

        return (leader, learner)

    except:
        raise GetAgentError


def update_agent(agent_repository: DatabaseRepositoryType, obj: Agent) -> bool:

    res: list = agent_repository['update'](obj['_id'], obj).json()

    if res:
        return True
    else:
        return False


def delete_agent(agent_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: list = agent_repository['delete'](hash).json()

    if len(res) == 1:
        return True
    else:
        return False
