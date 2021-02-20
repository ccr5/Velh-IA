import json
import random as r
from datetime import datetime
from typing import NoReturn, Union, List
from entities.match.match import Match
from entities.agent.agent import Agent
from usecases.agent.agent_use_cases import get_valid_agents
from usecases.agent.agent_database import update_agent, get_by_id, get_by_progenitor
from usecases.agent.agent_dto import agent_to_entity, agent_to_adapter
from usecases.agent.agent_use_cases import alter
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.database.database_types import DatabaseRepositoryType
from shared.objects import create_object
from shared.errors.multi_agent_system.play_error import MASPlayError
from shared.errors.handler.mas.update_mas_error import UpdateMASError


def add_new_match(mas: MultiAgentSystemAdapter, match: Match) -> MultiAgentSystemAdapter:

    add_one_family_leader = alter('add')(
        mas['family_leader'], 'matchsAsLeader', 1
    )

    add_one_family_learner = alter('add')(
        mas['family_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_family_leader = alter('add')(
        add_one_family_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_family_learner = alter('add')(
        add_one_family_learner, 'memory', [{
            'matchId': match['_id'],
            'isLearner': True,
            'choices': []
        }]
    )

    add_one_education_leader = alter('add')(
        mas['education_leader'], 'matchsAsLeader', 1
    )

    add_one_education_learner = alter('add')(
        mas['education_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_education_leader = alter('add')(
        add_one_education_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_education_learner = alter('add')(
        add_one_education_learner, 'memory', [{
            'matchId': match['_id'],
            'isLearner': True,
            'choices': []
        }]
    )

    add_one_religion_leader = alter('add')(
        mas['religion_leader'], 'matchsAsLeader', 1
    )

    add_one_religion_learner = alter('add')(
        mas['religion_learner'], 'matchsAsLearner', 1
    )

    add_empty_memory_religion_leader = alter('add')(
        add_one_religion_leader, 'memory', [{
            'matchId': match['_id'],
            'isLearner': False,
            'choices': []
        }]
    )

    add_empty_memory_religion_learner = alter('add')(
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
    elif agent_type == 'repository':
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


def play(self, match, game_status):
    """
    Choose a position to play
    :param match: `Match` a Match obj
    :param game_status: game status
    """

    family_start = datetime.now()
    validation = False
    while not validation:
        family_position = self.family_leader.remember(game_status)
        validation = True if game_status[family_position] == -1 else False
    family_end = datetime.now()

    education_start = datetime.now()
    validation = False
    while not validation:
        education_position = self.education_leader.remember(game_status)
        validation = True if game_status[education_position] == -1 else False
    education_end = datetime.now()

    religion_start = datetime.now()
    validation = False
    while not validation:
        religion_position = self.religion_leader.remember(game_status)
        validation = True if game_status[religion_position] == -1 else False
    religion_end = datetime.now()

    if family_position == education_position == religion_position:
        self.family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        self.family_learner.learn(match, game_status, family_position)

        self.education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        self.education_learner.learn(
            match, game_status, education_position)

        self.religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        self.religion_learner.learn(
            match, game_status, religion_position)

        return education_position

    elif family_position == education_position:
        self.family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        self.family_learner.learn(match, game_status, family_position)

        self.education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        self.education_learner.learn(
            match, game_status, education_position)

        return family_position

    elif family_position == religion_position:
        self.family_leader.memorize(
            match, game_status, family_start, family_end, family_position)
        self.family_learner.learn(match, game_status, family_position)

        self.religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        self.religion_learner.learn(
            match, game_status, religion_position)

        return religion_position

    elif education_position == religion_position:
        self.religion_leader.memorize(
            match, game_status, religion_start, religion_end, religion_position)
        self.religion_learner.learn(match, game_status, religion_position)

        self.education_leader.memorize(
            match, game_status, education_start, education_end, education_position)
        self.education_learner.learn(
            match, game_status, education_position)

        return education_position

    else:
        position = r.choice(
            [family_position, education_position, religion_position])

        if position == family_position:
            self.family_leader.memorize(
                match, game_status, family_start, family_end, family_position)
            self.family_learner.learn(match, game_status, family_position)

        elif position == education_position:
            self.education_leader.memorize(
                match, game_status, education_start, education_end, education_position)
            self.education_learner.learn(
                match, game_status, education_position)

        elif position == religion_position:
            self.religion_leader.memorize(
                match, game_status, religion_start, religion_end, religion_position)
            self.religion_learner.learn(
                match, game_status, religion_position)
        else:
            raise MASPlayError

        return position
