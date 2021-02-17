from typing import TypedDict, Callable
from src.entities.match.match import Match
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.entities.multi_agent_system.mas import MultiAgentSystem


class BackupType(TypedDict):

    match_backup: Match
    sa_backup: StatisticalAlgorithm
    mas_backup: MultiAgentSystem
    rollback: Callable
