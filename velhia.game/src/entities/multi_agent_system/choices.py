from typing import TypedDict, List
from src.shared.types.game_status import GameStatus


class Choices(TypedDict):

    dateRequest: str
    gameStatus: GameStatus
    timeToAct: float
    action: int
