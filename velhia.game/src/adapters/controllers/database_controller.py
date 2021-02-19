import json
from typing import Dict, List, Callable, NoReturn, Union, Tuple
from entities.algorithm.sa import StatisticalAlgorithm
from entities.match.match import Match
from entities.agent.agent import Agent
from usecases.mas.mas_adapter_type import MultiAgentSystemAdapter
from usecases.mas.mas_database import update_mas
from usecases.database.database_types import DatabaseRepositoryType
from usecases.match.match_database import get_current_match, delete_match, update_match
from usecases.sa.sa_database import get_sa, delete_sa, update_sa
from usecases.sa.sa_dto import sa_to_repository
from usecases.agent.agent_database import get_by_id, get_by_progenitor, delete_agent
from usecases.agent.agent_dto import agent_to_entity
from shared.errors.handler.mas.update_mas_error import UpdateMASError


def backup(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
           family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
           religion_db: DatabaseRepositoryType
           ) -> Union[
               Callable[[Match, StatisticalAlgorithm,
                         MultiAgentSystemAdapter], NoReturn],
               Tuple[None, None, None]]:
    """ Get the lastest datas to use in rollback function """

    ret: Union[Match, None] = get_current_match(match_db)

    if ret != None:

        match_backup: Match = ret
        sa_backup: StatisticalAlgorithm = get_sa(algorithm_db)
        mas_backup: MultiAgentSystemAdapter = MultiAgentSystemAdapter({
            'char': ['O', 0],
            'family_leader': agent_to_entity(get_by_id(family_db, match_backup['mas']['family'][-1]['playerId'])),
            'family_learner': agent_to_entity(get_by_progenitor(family_db, match_backup['mas']['family'][-1]['playerId'])),
            'education_leader': agent_to_entity(get_by_id(education_db, match_backup['mas']['education'][-1]['playerId'])),
            'education_learner': agent_to_entity(get_by_progenitor(education_db, match_backup['mas']['education'][-1]['playerId'])),
            'religion_leader': agent_to_entity(get_by_id(religion_db, match_backup['mas']['religion'][-1]['playerId'])),
            'religion_learner': agent_to_entity(get_by_progenitor(religion_db, match_backup['mas']['religion'][-1]['playerId']))
        })

        def rollback(match: Match, sa: StatisticalAlgorithm,
                     mas: MultiAgentSystemAdapter) -> NoReturn:
            """
            Rollback function to restore database object if something is wrong
            :param match: `Match` Match obj
            :param sa: `StatisticalAlgorithm` Statistical Algorithm obj
            :param mas: `MultiAgentSystemAdapter` Multi Agent System obj
            """

            if [None, None, None] != [match_backup, sa_backup, mas_backup]:

                if sa['_id'] != sa_backup['_id']:
                    delete_sa(algorithm_db, sa['_id'])

                if match['_id'] != match_backup['_id']:
                    delete_match(match_db, match['_id'])

                if mas['family_learner']['_id'] != mas_backup['family_learner']['_id']:
                    delete_agent(family_db, mas['family_learner']['_id'])

                if mas['religion_learner']['_id'] != mas_backup['religion_learner']['_id']:
                    delete_agent(religion_db, mas['religion_learner']['_id'])

                if mas['religion_learner']['_id'] != mas_backup['religion_learner']['_id']:
                    delete_agent(education_db, mas['religion_learner']['_id'])

                update_match(match_db, match_backup)
                update_sa(algorithm_db, sa_backup)
                update_mas(family_db, education_db, religion_db, mas_backup)

            else:
                pass

        return rollback

    else:
        return [None, None, None]
