import os
from requests import request
from errors.database.invalid_response import InvalidResponse


class Database:

    def __init__(self, api_version, collection):
        self.version = api_version
        self.collection = collection
        self.url = 'http://localhost:3000/' + 'api/' + \
            api_version + '/' + collection + '/'

    def get_one(self, object_id):
        """
        Get a object saved in a collection by id
        :param object_id: `str` ObjectId
        :return: `Response` response

        Usage
        >>> from config.database import Database
        >>> db = Database('v1', 'algorithms')
        >>> res = db.get_one('5fa01ed2b24ffc2dfdc9f019')
        >>> res.json()
        """

        response = request('GET', self.url + object_id)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)

    def get_last(self, limit):
        """
        Get the last object saved in a collect
        :param limit: `int` number of obj to get
        :return: `Response` response

        Usage
        >>> from config.database import Database
        >>> db = Database('v1', 'algorithms')
        >>> res = db.get_last('5fa01ed2b24ffc2dfdc9f019')
        >>> res
        """

        response = request('GET', self.url + 'limit/' + str(limit))

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)

    def create(self, obj):
        """
        Insert a object in a collection
        :param obj: `list` List of objects
        :return: `Response` response

        Usage
        >>> from config.database import Database
        >>> db = Database('v1', 'algorithms')
        >>> res = db.create(IAlgorithm)
        >>> res
        """

        head = {'Content-Type': 'application/json',
                'cache-control': 'no-cache'}
        response = request('POST', self.url, data=obj, headers=head)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)

    def update(self, object_id, obj):
        """
        Update a object in a collection
        :param object_id: `str` ObjectId
        :param obj: `dict` Object
        :return: `dict` lastest object version
        """

        head = {'Content-Type': 'application/json',
                'cache-control': 'no-cache'}
        response = request('PUT', self.url + str(object_id),
                           data=obj, headers=head)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)
