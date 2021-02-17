import json
from typing import Dict, List, Callable, NoReturn
from src.adapters.repository.database import get, create, update, delete
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.entities.match.match import Match
from src.entities.multi_agent_system.agent import Agent
from src.adapters.types.database_types import DatabaseType
from src.shared.objects import merge_objects, remove_objects
from src.shared.errors.handler.mas.update_mas_error import UpdateMASError


def update_mas(family_db: DatabaseType, education_db: DatabaseType,
               religion_db: DatabaseType, mas: MultiAgentSystem):
    """
    Update all multi agent system
    :param vlh: `Velhia` Velhia obj
    :param mas: `Multi Agent System` Multi Agent System obj 
    """

    try:

        family_db.update(
            mas.family_leader.id, json.dumps(mas.family_leader.create_object()))

        family_db.update(
            mas.family_learner.id, json.dumps(mas.family_learner.create_object()))

        religion_db.update(
            mas.religion_leader.id, json.dumps(mas.religion_leader.create_object()))

        religion_db.update(
            mas.religion_learner.id, json.dumps(mas.religion_learner.create_object()))

        education_db.update(
            mas.education_leader.id, json.dumps(mas.education_leader.create_object()))

        education_db.update(
            mas.education_learner.id, json.dumps(mas.education_learner.create_object()))

    except:
        raise UpdateMASError


def backup(match_db: DatabaseType, algorithm_db: DatabaseType,
           family_db: DatabaseType, education_db: DatabaseType,
           religion_db: DatabaseType
           ) -> Callable[[Match, StatisticalAlgorithm, MultiAgentSystem], NoReturn] | List[None, None, None]:
    """ Get the lastest datas to use in rollback function """

    ret: list = get(db=match_db, offset=0, limit=1).json()

    if len(ret) > 0:

        match_backup: Match = ret[0]

        sa_backup: StatisticalAlgorithm = merge_objects(
            get(db=algorithm_db, offset=0, limit=1).json()[0],
            {'char': ['X', 1], 'enemy': ['O', 0], 'empty': ['', -1]},
            StatisticalAlgorithm
        )

        mas_backup: MultiAgentSystem = {
            'char': ['O', 0],
            'family_leader': merge_objects(
                get(db=family_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            ),
            'family_learner': merge_objects(
                get(db=family_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            ),
            'education_leader': merge_objects(
                get(db=education_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            ),
            'education_learner': merge_objects(
                get(db=education_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            ),
            'religion_leader': merge_objects(
                get(db=religion_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            ),
            'religion_learner': merge_objects(
                get(db=religion_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}, Agent
            )
        }

        def rollback(match: Match, sa: StatisticalAlgorithm,
                     mas: MultiAgentSystem) -> Callable | None:
            """
            Rollback function to restore database object if something is wrong
            :param match_backup: `Match` Match obj
            :param sa_backup: `StatisticalAlgorithm` Statistical Algorithm obj
            :param mas_backup: `MultiAgentSystem` Multi Agent System obj
            """

            if [None, None, None] != [match_backup, sa_backup, mas_backup]:

                if sa._id != sa_backup._id:
                    delete(algorithm_db, sa._id)

                if match._id != match_backup._id:
                    delete(match_db, match._id)

                if mas.family_learner._id != mas_backup.family_learner._id:
                    delete(family_db, mas.family_learner._id)

                if mas.religion_learner._id != mas_backup.religion_learner._id:
                    delete(religion_db, mas.religion_learner._id)

                if mas.religion_learner._id != mas_backup.religion_learner._id:
                    delete(education_db, mas.religion_learner._id)

                match_db.update(match_backup._id, match_backup)

                algorithm_db.update(sa_backup._id, remove_objects(
                    sa_backup, ['char', 'enemy', 'empty'], 3))

                update_mas(family_db, education_db, religion_db, mas_backup)

            else:
                pass

        return rollback

    else:
        return [None, None, None]
