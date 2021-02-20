from datetime import datetime
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_database import save_sa
from shared.objects import create_object


def create_sa(sa_repository: DatabaseRepositoryType) -> StatisticalAlgorithm:

    return save_sa(sa_repository, create_object(
        [
            ('birth', datetime.now().ctime()),
            ('matchs', 0),
            ('victories', 0),
            ('defeats', 0),
            ('draw', 0)
        ], 5
    ))
