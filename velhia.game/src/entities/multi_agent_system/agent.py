from typing import TypedDict, List, Optional
from .memory import Memory
from src.shared.types.char import Char


class Agent(TypedDict):

    _id: str
    birth: str
    progenitor: str
    becomeLeader: Optional[str]
    death: Optional[str]
    life: float
    memory: List[Memory]
    matchsAsLearner: int
    matchsAsLeader: int
    victories: int
    defeats: int
    draw: int
    char: Char
