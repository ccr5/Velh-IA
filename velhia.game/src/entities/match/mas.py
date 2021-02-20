from typing import TypedDict, List
from .player import Player


class MAS(TypedDict):

    family: List[Player]
    religion: List[Player]
    education: List[Player]
