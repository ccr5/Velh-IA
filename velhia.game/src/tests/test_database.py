# import os
# from adapters.repository.database import database
# from usecases.database.database_types import DatabaseType, DatabaseRepositoryType
# import json


# db_config = DatabaseType = {
#     'address': os.getenv('API_ADDRESS'),
#     'version': os.getenv('API_VERSION'),
#     'collection': 'algorithms',
#     'url': f"{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/algorithms/"
# }

# db: DatabaseRepositoryType = database(db_config)
# obj_id = ''
# obj = {}


# class TestDatabase:

#     def test_create(self) -> None:
#         obj = {"draw": 0,
#                "defeats": 0,
#                "victories": 0,
#                "matchs": 1,
#                "birth": "2021-02-21T14:32:09.000Z"}
#         alg = db['create'](obj)
#         obj_id = alg.json()['_id']
#         obj = alg.json()
#         assert alg.status_code == 200

#     def test_get_one(self) -> None:
#         alg = db.get_one(obj_id)
#         assert alg.status_code == 200

#     def test_get_last(self) -> None:
#         limit = 1
#         alg = db.get_last(limit)
#         assert alg.text != '[]'

#     def test_update(self) -> None:
#         alg = db.update(object_id=obj_id, obj=json.dumps(obj))
#         assert alg.status_code == 200
