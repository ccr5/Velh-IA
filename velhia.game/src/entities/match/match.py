from typing import TypedDict, List, Optional
from .mas import MAS
from .player import Player
from .play import Play


class Match(TypedDict):

    _id: str
    begin: str
    end: Optional[str]
    time: float
    sa: Player
    mas: MAS
    plays: List[Play]
    status: str
    winner: Optional[str]
