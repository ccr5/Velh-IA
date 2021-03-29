import typing as tp
from shared.types.char import Char


class MultiAgentSystemAdapter(tp.TypedDict):

    char: Char
    agents: tp.List
