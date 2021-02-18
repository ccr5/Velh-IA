from typing import TypedDict, Callable
from entities.match.match import Match
from entities.algorithm.sa import StatisticalAlgorithm
from entities.agent.agent import Agent
from requests import Response


class DatabaseType(TypedDict):

    address: str
    version: str
    collection: str
    url: str


class DatabaseRepositoryType(DatabaseType):

    get: Callable[[dict, str, str, int, int], Response]
    create: Callable[[Agent, Match, StatisticalAlgorithm], Response]
    update: Callable[[str, Agent, Match, StatisticalAlgorithm], Response]
    delete: Callable[[str], Response]
