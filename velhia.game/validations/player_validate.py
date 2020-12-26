from errors.validation.validation_error import ValidationError
from errors.validation.player.sa_match_error import SAMatchError
from errors.validation.player.agent_match_error import AgentMatchError


def check_sa_matchs(sa):

    try:

        total_matchs = sa.info['victories'] + \
            sa.info['defeats'] + sa.info['draw']
        total_memories = len(sa.info['memory'])
        matchs_info = sa.info['matchs']

        if matchs_info == total_memories == total_matchs + 1:
            pass
        else:
            raise SAMatchError

    except:
        raise ValidationError


def check_agent_matchs(agent):

    try:

        total_matchs = agent.info['victories'] + \
            agent.info['defeats'] + agent.info['draw']
        total_memories = len(agent.info['memory'])
        matchs_info = agent.info['matchsAsLeader'] + \
            agent.info['matchsAsLearner']

        if agent.info['life'] > 0:

            if matchs_info == total_memories == total_matchs + 1:
                pass
            else:
                raise AgentMatchError

        else:

            if matchs_info == total_memories == total_matchs:
                pass
            else:
                raise AgentMatchError

    except:
        raise ValidationError
