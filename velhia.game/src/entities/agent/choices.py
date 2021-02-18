from typing import TypedDict
from shared.types.game_status import GameStatus


class Choices(TypedDict):

    dateRequest: str
    gameStatus: GameStatus
    timeToAct: float
    action: int
