from config.database import Database
import json


class TestDatabase:

    db = Database('v1', 'algorithms')
    obj_id = ''
    obj = {}

    def test_create(self):
        obj = {"birth": "Thu Jan 05 2017 22:12:46 GMT-0100 (CET)",
               "memory": [{
                   "isLearner": True,
                   "choices": [{
                       "dateRequest": "Thu Jan 05 2017 22:12:46 GMT-0100 (CET)",
                       "gameStatus": [1, -1, 0],
                       "timeToAct": 30,
                       "action": 2
                   }],
                   "environmentReaction": "DRAW"
               }],
               "matchs": 1,
               "victories": 0,
               "defeats": 0,
               "draw": 1}
        alg = self.db.create(json.dumps(obj))
        self.obj_id = alg.json()['_id']
        self.obj = alg.json()
        assert alg.status_code == 200

    def test_get_one(self):
        alg = self.db.get_one(self.obj_id)
        assert alg.status_code == 200

    def test_get_last(self):
        limit = 1
        alg = self.db.get_last(limit)
        assert alg.text != '[]'

    def test_update(self):
        alg = self.db.update(object_id=self.obj_id, obj=json.dumps(self.obj))
        assert alg.status_code == 200
