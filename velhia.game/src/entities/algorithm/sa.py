from typing import TypedDict
from src.shared.types.char import Char


class StatisticalAlgorithm(TypedDict):

    _id: str
    birth: str
    matchs: int
    victories: int
    defeats: int
    draw: int
    char: Char
    enemy: Char
    empty: Char
