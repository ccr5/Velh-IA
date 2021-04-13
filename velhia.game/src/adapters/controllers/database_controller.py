from typing import Callable, NoReturn, Union, Tuple
from entities.algorithm.sa import StatisticalAlgorithm
from entities.match.match import Match
from usecases.database.database_types import DatabaseRepositoryType
from usecases.match.match_database import get_current_match, delete_match, update_match
from usecases.sa.sa_database import get_sa, delete_sa, update_sa
from ovomaltino.ovomaltino import Ovomaltino


def backup(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType
           ) -> Union[Callable[[Match, StatisticalAlgorithm], NoReturn],
                      Tuple[None, None, None]]:
    """ Get the lastest datas to use in rollback function """

    ret: Union[Match, None] = get_current_match(match_db)

    if ret != None:

        match_backup: Match = ret
        sa_backup: StatisticalAlgorithm = get_sa(algorithm_db)

        def rollback(match: Match, sa: StatisticalAlgorithm) -> NoReturn:
            """ Rollback function to restore database object if something is wrong """

            if [None, None] != [match_backup, sa_backup]:

                if sa['_id'] != sa_backup['_id']:
                    delete_sa(algorithm_db, sa['_id'])

                if match['_id'] != match_backup['_id']:
                    delete_match(match_db, match['_id'])

                update_match(match_db, match_backup)
                update_sa(algorithm_db, sa_backup)

            else:
                pass

        return rollback

    else:
        return [None, None, None]
