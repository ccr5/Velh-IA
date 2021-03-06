from errors.validation.validation_error import ValidationError
from errors.validation.player.sa_match_error import SAMatchError
from errors.validation.player.agent_match_error import AgentMatchError


def check_sa_matchs(sa):
    """
    Check if the number of matchs, memories and (victories, defeats and draw) is correctly
    :param sa: `Statistical Algorithm` Statistical Algorithm obj

    usage
    >>> from validations.player_validate import check_sa_matchs
    >>> sa = StatisticalAlgorithm()
    >>> check_sa_matchs(sa) 
    """

    try:

        total_matchs = sa.victories + sa.defeats + sa.draw
        matchs_info = sa.matchs

        if matchs_info == total_matchs + 1:
            pass
        else:
            raise SAMatchError

    except:
        raise SAMatchError


def check_agent_matchs(agent):
    """
    Check if the number of matchs, memories and (victories, defeats and draw) is correctly
    :param sa: `Agent` Agent obj

    usage
    >>> from validations.player_validate import check_sa_matchs
    >>> sa = Agent()
    >>> check_agent_matchs(agent) 
    """

    try:

        total_matchs = agent.victories + agent.defeats + agent.draw
        total_memories = len(agent.memory)
        matchs_info = agent.matchsAsLeader + agent.matchsAsLearner

        if agent.life > 0:

            if matchs_info == total_memories == total_matchs + 1:
                pass
            elif matchs_info == total_memories and agent.matchsAsLeader == total_matchs + 1:
                pass
            else:
                raise AgentMatchError

        else:

            if matchs_info == total_memories == total_matchs:
                pass
            elif matchs_info == total_memories and agent.matchsAsLeader == total_matchs:
                pass
            else:
                raise AgentMatchError

    except:
        raise AgentMatchError
