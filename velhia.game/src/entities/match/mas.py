from typing import TypedDict, List
from shared.types.char import Char


class MultiAgentSystem(TypedDict):

    symbol: str
    agents: List[str]
