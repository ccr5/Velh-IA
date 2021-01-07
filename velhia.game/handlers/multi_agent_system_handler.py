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
            mas.family_leader.id, json.dumps(mas.family_leader.create_object()))

        vlh.family_db.update(
            mas.family_learner.id, json.dumps(mas.family_learner.create_object()))

        vlh.religion_db.update(
            mas.religion_leader.id, json.dumps(mas.religion_leader.create_object()))

        vlh.religion_db.update(
            mas.religion_learner.id, json.dumps(mas.religion_learner.create_object()))

        vlh.education_db.update(
            mas.education_leader.id, json.dumps(mas.education_leader.create_object()))

        vlh.education_db.update(
            mas.education_learner.id, json.dumps(mas.education_learner.create_object()))

    except:
        raise UpdateMASError
