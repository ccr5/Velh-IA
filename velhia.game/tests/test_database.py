from config.database import Database
import json


class TestDatabase:

    def test_get_one(self):
        db = Database('v1', 'algorithms')
        obj_id = '5fa04edeb24ffc2dfdc9f01c'
        alg = db.get_one(obj_id)
        assert alg.status_code == 200

    def test_get_last(self):
        db = Database('v1', 'algorithms')
        limit = 1
        alg = db.get_last(limit)
        assert alg.text != '[]'

    def test_create(self):
        db = Database('v1', 'algorithms')
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
        alg = db.create(json.dumps(obj))
        assert alg.status_code == 200

    def test_update(self):
        db = Database('v1', 'algorithms')
        obj_id = '5fa04edeb24ffc2dfdc9f01c'
        obj = {"_id": "5fa04edeb24ffc2dfdc9f01c",
               "birth": "Thu Jan 05 2017 22:12:46 GMT-0100 (CET)",
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
        alg = db.update(obj_id, json.dumps(obj))
        assert alg.status_code == 200
