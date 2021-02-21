from typing import Union, Any
from datetime import datetime
from entities.algorithm.sa import StatisticalAlgorithm
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_adapter_type import StatisticalAlgorithmAdapter
from usecases.sa.sa_database import save_sa
from shared.objects import create_object, merge_objects
from shared.errors.statistical_algorithm.strategy_plan_error import StrategyPlanError
from shared.errors.statistical_algorithm.sequence_list_error import SequenceListError
from shared.errors.statistical_algorithm.check_error import CheckError
from shared.errors.statistical_algorithm.count_error import CountError
from shared.errors.statistical_algorithm.create_matrix_error import CreateMatrixError


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


def add(sa: Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm], field: str,
        value: Any) -> Union[StatisticalAlgorithmAdapter, StatisticalAlgorithm]:

    current_value = sa[field]
    new_value = current_value + value
    obj = {field: new_value}
    return merge_objects(sa, obj)
