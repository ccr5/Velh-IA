from typing import NoReturn
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.agent.agent_adapter_type import AgentAdapter
from shared.errors.validation.validation_error import ValidationError
from shared.errors.validation.player.sa_match_error import SAMatchError
from shared.errors.validation.player.agent_match_error import AgentMatchError


def check_sa_matchs(sa: StatisticalAlgorithmAdapter) -> NoReturn:
    """ Check if the number of matchs, memories and (victories, defeats and draw) is correctly """

    total_matchs = sa['victories'] + sa['defeats'] + sa['draw']
    matchs_info = sa['matchs']

    if matchs_info == total_matchs + 1:
        pass
    else:
        raise SAMatchError
