from typing import TypedDict, List, Optional
from .choices import Choices


class Memory(TypedDict):

    matchId: str
    isLearner: bool
    choices: List[Choices]
    environmentReaction: Optional[str]
