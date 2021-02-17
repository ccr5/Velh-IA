from typing import NewType, Tuple


GameStatus = NewType(
    'GameStatus',
    Tuple[int, int, int, int, int, int, int, int, int]
)
