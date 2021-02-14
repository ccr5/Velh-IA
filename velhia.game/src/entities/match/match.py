from typing import TypedDict, List
from .mas import MAS
from .player import Player
from .play import Play
from src.shared.types.char import Char


class Match(TypedDict):

    _id: str
    begin: str
    end: str
    time: float
    sa: Player
    mas: MAS
    plays: List[Play]
    status: str
    winner: str
