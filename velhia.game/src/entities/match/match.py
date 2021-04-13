from typing import TypedDict, List, Optional
from .mas import MultiAgentSystem
from .player import Player
from .play import Play


class Match(TypedDict):

    begin: str
    end: Optional[str]
    time: float
    sa: Player
    mas: MultiAgentSystem
    plays: List[Play]
    status: str
    winner: Optional[str]
