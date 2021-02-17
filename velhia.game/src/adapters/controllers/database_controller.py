import json
from typing import Dict, List, Callable
from src.adapters.repository.database import get, create, update, delete
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.entities.match.match import Match
from src.entities.multi_agent_system.mas import MultiAgentSystem
from src.adapters.types.backup import BackupType
from src.adapters.types.database_types import DatabaseType
from src.shared.objects import merge_objects


def backup(match_db: DatabaseType, algorithm_db: DatabaseType,
           family_db: DatabaseType, education_db: DatabaseType,
           religion_db: DatabaseType) -> BackupType | List[None, None, None]:
    """ Get the lastest datas to use in rollback function """

    ret = get(db=match_db, offset=0, limit=1).json()

    if len(ret) != 0:

        match_backup: Match = ret[0]

        sa_backup: StatisticalAlgorithm = merge_objects(
            get(db=algorithm_db, offset=0, limit=1).json()[0],
            {'char': ['X', 1], 'enemy': ['O', 0], 'empty': ['', -1]}
        )

        mas_backup: MultiAgentSystem = {
            'char': ['O', 0],
            'family_leader': merge_objects(
                get(db=family_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
            ),
            'family_learner': merge_objects(
                get(db=family_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
            ),
            'education_leader': merge_objects(
                get(db=education_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
            ),
            'education_learner': merge_objects(
                get(db=education_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
            ),
            'religion_leader': merge_objects(
                get(db=religion_db, offset=1, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
            ),
            'religion_learner': merge_objects(
                get(db=religion_db, offset=0, limit=1,
                    sort="createdAt:desc").json()[0],
                {'char': ['O', 0]}
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

                if sa['_id'] != sa_backup['_id']:
                    delete(algorithm_db, sa['_id'])

                if match['_id'] != match_backup['_id']:
                    delete(match_db, match['_id'])

                if mas['family_learner']['_id'] != mas_backup['family_learner']['_id']:
                    delete(family_db, mas['family_learner']['_id'])

                if mas['religion_learner']['_id'] != mas_backup['religion_learner']['_id']:
                    delete(religion_db, mas['religion_learner']['_id'])

                if mas['education_learner']['_id'] != mas_backup['education_learner']['_id']:
                    delete(education_db, mas['education_learner']['_id'])

                match_db.update(
                    match_backup['_id'], json.dumps(match_backup.create_object()))

                algorithm_db.update(
                    sa_backup['_id'], json.dumps(sa_backup.create_object()))

                update_mas(self, mas_backup)

            else:
                pass

        return {
            'match_backup': match_backup,
            'sa_backup': sa_backup,
            'mas_backup': mas_backup,
            'rollback': rollback
        }

    else:
        return [None, None, None]
