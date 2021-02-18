from src.usecases.database.database_types import DatabaseRepositoryType
from src.entities.agent.agent import Agent


def getLeader(agent_repository: DatabaseRepositoryType) -> Agent:

    res: list = agent_repository.get(
        offset=1, limit=1, sort="createdAt:desc"
    ).json()

    if len(res) == 1 and res[0].has_key('becomeLeader') and isinstance(res[0], Agent):
        return res[0]
    else:
        raise SystemError


def getLearner(agent_repository: DatabaseRepositoryType) -> Agent:

    res: list = agent_repository.get(
        offset=0, limit=1, sort="createdAt:desc"
    ).json()

    if len(res) == 1 and not res[0].has_key('becomeLeader') and isinstance(res[0], Agent):
        return res[0]
    else:
        raise SystemError
