from requests import Response
from typing import TypedDict, Callable, Union
from entities.match.match import Match
from entities.algorithm.sa import StatisticalAlgorithm


class DatabaseType(TypedDict):

    address: str
    version: str
    collection: str
    url: str


class DatabaseRepositoryType(DatabaseType):

    get: Callable[[dict, str, str, int, int], Response]
    create: Callable[[Union[Match, StatisticalAlgorithm]], Response]
    update: Callable[[str, Union[Match, StatisticalAlgorithm]],
                     Response]
    delete: Callable[[str], Response]
