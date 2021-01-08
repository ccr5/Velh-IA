import sys
import json
from datetime import datetime
from classes.statistical_algorithm import StatisticalAlgorithm
from errors.handler.sa.get_sa_error import GetStatisticalAlgorithmError


def get_lastest_sa(db):
    """
    Get the lastest statistical algorithm obj in the database
    or create if it not exists

    Usage
    >>> sa = get_lastest_sa()
    >>> print(sa)

    <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de3287d0>
    <classes.statistical_algorithm.StatisticalAlgorithm object at 0x7fe6de3287d0>
    """

    try:

        if len(db.get(offset=0, limit=1).json()) == 0:
            sa = StatisticalAlgorithm(db.create(json.dumps({
                "birth": datetime.now().ctime(),
                "matchs": 0,
                "victories": 0,
                "defeats": 0,
                "draw": 0
            })).json(), ('X', 1), ('O', 0))
        else:
            sa = StatisticalAlgorithm(
                db.get(offset=0, limit=1).json()[0],
                ('X', 1), ('O', 0))

        return sa

    except:
        raise GetStatisticalAlgorithmError
