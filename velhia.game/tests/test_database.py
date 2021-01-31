from config.database import Database
import json


class TestDatabase:

    db = Database('http://localhost:3000/test/', 'v1', 'algorithms')
    obj = {"birth": "Thu Jan 05 2017 22:12:46 GMT-0100 (CET)",
           "matchs": 1,
           "victories": 0,
           "defeats": 0,
           "draw": 1}

    def test_create(self):
        alg = self.db.create(json.dumps(self.obj))
        assert alg.status_code == 200
        assert alg.json()['matchs'] == self.obj['matchs']
        assert alg.json()['victories'] == self.obj['victories']
        assert alg.json()['defeats'] == self.obj['defeats']
        assert alg.json()['draw'] == self.obj['draw']

    def test_get(self):
        alg = self.db.get(filters={"matchs": self.obj['matchs']})
        assert alg.status_code == 200
        assert alg.json()[0]['matchs'] == self.obj['matchs']
        assert alg.json()[0]['victories'] == self.obj['victories']
        assert alg.json()[0]['defeats'] == self.obj['defeats']
        assert alg.json()[0]['draw'] == self.obj['draw']
        alg = self.db.get(offset=0, limit=1)
        assert alg.text != '[]'
        assert alg.status_code == 200
        assert alg.json()[0]['matchs'] == self.obj['matchs']
        assert alg.json()[0]['victories'] == self.obj['victories']
        assert alg.json()[0]['defeats'] == self.obj['defeats']
        assert alg.json()[0]['draw'] == self.obj['draw']

    def test_update(self):
        alg = self.db.get(filters={"matchs": self.obj['matchs']})
        obj_id = alg.json()[0]['_id']
        alg = self.db.update(object_id=obj_id,
                             obj=json.dumps(self.obj))
        assert alg.status_code == 200
        assert alg.json()['matchs'] == self.obj['matchs']
        assert alg.json()['victories'] == self.obj['victories']
        assert alg.json()['defeats'] == self.obj['defeats']
        assert alg.json()['draw'] == self.obj['draw']

    def test_delete(self):
        alg = self.db.get(filters={"matchs": self.obj['matchs']})
        alg = self.db.delete(object_id=alg.json()[0]['_id'])
        assert alg.status_code == 200
        assert alg.json()['matchs'] == self.obj['matchs']
        assert alg.json()['victories'] == self.obj['victories']
        assert alg.json()['defeats'] == self.obj['defeats']
        assert alg.json()['draw'] == self.obj['draw']
        alg = self.db.get(offset=0, limit=1)
        assert alg.status_code == 200
        assert alg.text == '[]'
