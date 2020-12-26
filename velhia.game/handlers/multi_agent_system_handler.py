import json


def update_mas(vlh, mas):
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
        raise SystemError
