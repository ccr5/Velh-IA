import json
from datetime import datetime
from typing import Union, Tuple, List, Dict
from entities.agent.agent import Agent
from usecases.agent.agent_dto import agent_to_entity
from usecases.database.database_types import DatabaseRepositoryType
from shared.objects import create_object


def save_agent(agent_repository: DatabaseRepositoryType, agent: Agent) -> Agent:

    res: Dict = agent_repository['create'](agent).json()
    return agent_to_entity(res)


def get_last(agent_repository: DatabaseRepositoryType, num: int) -> Union[List[Agent], None]:

    res: List = agent_repository['get'](offset=0, limit=num,
                                        sort="createdAt:desc").json()

    if len(res) > 0:
        return list(map(agent_to_entity, res))
    else:
        None


def get_by_id(agent_repository: DatabaseRepositoryType, hash: str) -> Union[Agent, None]:
    obj_id: Dict = {'_id': hash}
    res: List = agent_repository['get'](filters=obj_id).json()

    if len(res) == 1:
        return agent_to_entity(res[0])
    else:
        None


def get_by_progenitor(agent_repository: DatabaseRepositoryType, hash: str) -> Union[Agent, None]:
    obj_id: Dict = {'progenitor': hash}
    res: List = agent_repository['get'](filters=obj_id).json()

    if len(res) == 1:
        return agent_to_entity(res[0])
    else:
        None


def update_agent(agent_repository: DatabaseRepositoryType, obj: Agent) -> bool:

    res: List = agent_repository['update'](obj['_id'], obj).json()

    if res:
        return True
    else:
        return False


def delete_agent(agent_repository: DatabaseRepositoryType, hash: str) -> bool:

    res: List = agent_repository['delete'](hash).json()

    if len(res) == 1:
        return True
    else:
        return False
