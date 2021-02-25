import json
import random as r
from datetime import datetime
from typing import NoReturn, Union, List
from entities.match.match import Match
from entities.agent.agent import Agent
from usecases.agent.agent_use_cases import get_valid_agents
from usecases.agent.agent_database import update_agent, get_by_id, get_by_progenitor
from usecases.agent.agent_dto import agent_to_entity, agent_to_adapter
from usecases.agent.agent_use_cases import alter_agent
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.database.database_types import DatabaseRepositoryType
from shared.objects import create_object
from shared.errors.multi_agent_system.play_error import MASPlayError
from shared.errors.handler.mas.update_mas_error import UpdateMASError


def add_new_match(mas: MultiAgentSystemAdapter, match: Match) -> MultiAgentSystemAdapter:

    add_one_family_leader = alter_agent('add')(
        mas['family_leader'], 'matchsAsLeader', 1
    )

    add_one_family_learner = alter_agent('add')(
        mas['family_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_family_leader = alter_agent('add')(
        add_one_family_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_family_learner = alter_agent('add')(
        add_one_family_learner, 'memory', [{
            'matchId': match['_id'],
            'isLearner': True,
            'choices': []
        }]
    )

    add_one_education_leader = alter_agent('add')(
        mas['education_leader'], 'matchsAsLeader', 1
    )

    add_one_education_learner = alter_agent('add')(
        mas['education_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_education_leader = alter_agent('add')(
        add_one_education_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_education_learner = alter_agent('add')(
        add_one_education_learner, 'memory', [{
            'matchId': match['_id'],
            'isLearner': True,
            'choices': []
        }]
    )

    add_one_religion_leader = alter_agent('add')(
        mas['religion_leader'], 'matchsAsLeader', 1
    )

    add_one_religion_learner = alter_agent('add')(
        mas['religion_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_religion_leader = alter_agent('add')(
        add_one_religion_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_religion_learner = alter_agent('add')(
        add_one_religion_learner, 'memory', [{
            'matchId': match['_id'],
            'isLearner': True,
            'choices': []
        }]
    )

    return MultiAgentSystemAdapter(
        create_object(
            [
                ('char', ('O', 0)),
                ('family_leader', add_empty_memory_family_leader),
                ('family_learner', add_empty_memory_family_learner),
                ('education_leader', add_empty_memory_education_leader),
                ('education_learner', add_empty_memory_education_learner),
                ('religion_leader', add_empty_memory_religion_leader),
                ('religion_learner', add_empty_memory_religion_learner),
            ], 7
        )
    )


def add_match_response(mas: MultiAgentSystemAdapter, response: str, denominator: int) -> MultiAgentSystemAdapter:

    if response == 'winner':
        pass
    elif response == 'loser':
        pass
    elif response == 'draw':
        pass
    else:
        raise SystemError

    mas.family_leader.memory[-1]['environmentReaction'] = 'LOSER'
    mas.education_leader.memory[-1]['environmentReaction'] = 'LOSER'
    mas.religion_leader.memory[-1]['environmentReaction'] = 'LOSER'

    mas.family_learner.memory[-1]['environmentReaction'] = 'LOSER'
    mas.education_learner.memory[-1]['environmentReaction'] = 'LOSER'
    mas.religion_learner.memory[-1]['environmentReaction'] = 'LOSER'

    mas.family_leader.defeats += 1
    mas.education_leader.defeats += 1
    mas.religion_leader.defeats += 1

    mas.family_leader.life -= len(
        mas.family_leader.memory[-1]['choices']) / plays
    mas.education_leader.life -= len(
        mas.education_leader.memory[-1]['choices']) / plays
    mas.religion_leader.life -= len(
        mas.religion_leader.memory[-1]['choices']) / plays

    return MultiAgentSystemAdapter(
        create_object(
            [
                ('char', ('O', 0)),
                ('family_leader', add_empty_memory_family_leader),
                ('family_learner', add_empty_memory_family_learner),
                ('education_leader', add_empty_memory_education_leader),
                ('education_learner', add_empty_memory_education_learner),
                ('religion_leader', add_empty_memory_religion_leader),
                ('religion_learner', add_empty_memory_religion_learner),
            ], 7
        )
    )


def create_mas(family: DatabaseRepositoryType,
               religion: DatabaseRepositoryType,
               education: DatabaseRepositoryType) -> MultiAgentSystemAdapter:

    [family_leader, family_learner] = get_valid_agents(family)
    [education_leader, education_learner] = get_valid_agents(education)
    [religion_leader, religion_learner] = get_valid_agents(religion)

    return MultiAgentSystemAdapter(
        create_object(
            [
                ('char', ('O', 0)),
                ('family_leader', family_leader),
                ('family_learner', family_learner),
                ('education_leader', education_leader),
                ('education_learner', education_learner),
                ('religion_leader', religion_leader),
                ('religion_learner', religion_learner),
            ], 7
        )
    )


def update_mas(family: DatabaseRepositoryType,
               religion: DatabaseRepositoryType,
               education: DatabaseRepositoryType,
               mas: MultiAgentSystemAdapter) -> NoReturn:
    """
    Update all multi agent system
    :param vlh: `Velhia` Velhia obj
    :param mas: `Multi Agent System` Multi Agent System obj 
    """

    def update_all_agents(db_list: List[DatabaseRepositoryType],
                          obj_list: List[Agent], lengh: int) -> NoReturn:

        if lengh > 0:
            index = lengh - 1
            update_agent(db_list[index], obj_list[index])
            return update_all_agents(db_list, obj_list, index)
        else:
            pass

    databases: List[DatabaseRepositoryType] = [
        family, family,
        religion, religion,
        education, education
    ]

    agents: List[Agent] = [
        mas['family_leader'], mas['family_learner'],
        mas['religion_leader'], mas['religion_learner'],
        mas['education_leader'], mas['education_learner']
    ]

    return update_all_agents(databases, agents, 6)


def complete_mas(family: DatabaseRepositoryType,
                 religion: DatabaseRepositoryType,
                 education: DatabaseRepositoryType,
                 match: Match, agent_type: str) -> Union[MultiAgentSystemAdapter, None]:

    if agent_type == 'entity':
        return MultiAgentSystemAdapter(
            create_object(
                [
                    ('char', ('O', 0)),
                    ('family_leader', agent_to_entity(
                        get_by_id(family, match['mas']['family'][-1]['playerId']))),
                    ('family_learner', agent_to_entity(get_by_progenitor(
                        family, match['mas']['family'][-1]['playerId']))),
                    ('education_leader', agent_to_entity(
                        get_by_id(education, match['mas']['education'][-1]['playerId']))),
                    ('education_learner', agent_to_entity(get_by_progenitor(
                        education, match['mas']['education'][-1]['playerId']))),
                    ('religion_leader', agent_to_entity(
                        get_by_id(religion, match['mas']['religion'][-1]['playerId']))),
                    ('religion_learner', agent_to_entity(get_by_progenitor(
                        religion, match['mas']['religion'][-1]['playerId']))),
                ], 7
            )
        )
    elif agent_type == 'adapter':
        return MultiAgentSystemAdapter(
            create_object(
                [
                    ('char', ('O', 0)),
                    ('family_leader', agent_to_adapter(
                        get_by_id(family, match['mas']['family'][-1]['playerId']))),
                    ('family_learner', agent_to_adapter(get_by_progenitor(
                        family, match['mas']['family'][-1]['playerId']))),
                    ('education_leader', agent_to_adapter(
                        get_by_id(education, match['mas']['education'][-1]['playerId']))),
                    ('education_learner', agent_to_adapter(get_by_progenitor(
                        education, match['mas']['education'][-1]['playerId']))),
                    ('religion_leader', agent_to_adapter(
                        get_by_id(religion, match['mas']['religion'][-1]['playerId']))),
                    ('religion_learner', agent_to_adapter(get_by_progenitor(
                        religion, match['mas']['religion'][-1]['playerId']))),
                ], 7
            )
        )
    else:
        return None
