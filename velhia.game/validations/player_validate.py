from errors.invalid_match import InvalidMatch


def check_sa_matchs(sa):

    total_matchs = sa.info['victories'] + sa.info['defeats'] + sa.info['draw']
    total_memories = len(sa.info['memory'])
    matchs_info = sa.info['matchs']

    if matchs_info == total_memories == total_matchs + 1:
        pass
    else:
        raise InvalidMatch


def check_agent_matchs(agent):

    total_matchs = agent.info['victories'] + \
        agent.info['defeats'] + agent.info['draw']
    total_memories = len(agent.info['memory'])
    matchs_info = agent.info['matchsAsLeader'] + agent.info['matchsAsLearner']

    if agent.info['life'] > 0:

        if matchs_info == total_memories == total_matchs + 1:
            pass
        else:
            raise InvalidMatch

    else:

        if matchs_info == total_memories == total_matchs:
            pass
        else:
            raise InvalidMatch
