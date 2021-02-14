from typing import TypedDict, List


class Choices(TypedDict):

    dateRequest: str
    gameStatus: List[int]
    timeToAct: float
    action: int
