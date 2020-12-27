import json
from errors.handler.mas.update_mas_error import UpdateMASError


def update_mas(vlh, mas):
    """
    Update all multi agent system
    :param vlh: `Velhia` Velhia obj
    :param mas: `Multi Agent System` Multi Agent System obj 
    """

    try:

        vlh.family_db.update(
            mas.family_leader.info['_id'], json.dumps(mas.family_leader.info))

        vlh.family_db.update(
            mas.family_learner.info['_id'], json.dumps(mas.family_learner.info))

        vlh.religion_db.update(
            mas.religion_leader.info['_id'], json.dumps(mas.religion_leader.info))

        vlh.religion_db.update(
            mas.religion_learner.info['_id'], json.dumps(mas.religion_learner.info))

        vlh.education_db.update(
            mas.education_leader.info['_id'], json.dumps(mas.education_leader.info))

        vlh.education_db.update(
            mas.education_learner.info['_id'], json.dumps(mas.education_learner.info))

    except:
        raise UpdateMASError
