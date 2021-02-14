from typing import TypedDict, List
from .choices import Choices

class Memory(TypedDict):

    matchId: str
    isLearner: bool
    choices: List[Choices]
    environmentReaction: str