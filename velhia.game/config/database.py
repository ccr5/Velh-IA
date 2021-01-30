import os
import json
from requests import request
from errors.database.invalid_response import InvalidResponse


class Database:

    def __init__(self, address, api_version, collection):
        self.address = address
        self.version = api_version
        self.collection = collection
        self.url = f'{address}api/{api_version}/{collection}/'

    def get(self, filters={}, fields='', sort='', offset=-1, limit=-1):
        """
        Get objects in a collection
        :param filters: `{<str>:<value>,<str>:<value>}` all filters to find the objects
        :param fields: `<str>,<str>` all fields to take
        :param sort: `<campo>:<asc | desc>` how to order the objects
        :param offset: `int` index to start to get the objects
        :param limit: `int` how many objects get from offset
        :return: `Response` response

        import
        >>> from config.database import Database
        >>> db = Database('http://localhost:3000/', 'v1', 'algorithms')

        get all objects
        >>> res = db.get()
        >>> res.json()

        get by id
        >>> res = db.get(filters="{'_id': 'hash'}")
        >>> res.json()

        get just some fields
        >>> res = db.get(fields="-_id,victories")
        >>> res.json()

        get sorted objects
        >>> res = db.get(sort="createdAt:desc")
        >>> res.json() 

        get a list
        >>> res = db.get(offset=0, limit=2) # from the first one, get more 2 objects
        >>> res.json()
        """

        complete_url = f'{self.url}?filters={json.dumps(filters)}'
        complete_url += f'&fields={fields}' if fields != '' else ''
        complete_url += f'&sort={sort}' if sort != '' else ''
        complete_url += f'&offset={str(offset)}&limit={str(limit)}' if str(
            offset) != '-1' and str(limit) != '-1' else ''

        response = request('GET', complete_url)

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
        >>> db = Database('http://localhost:3000/', 'v1', 'algorithms')
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

        Usage
        >>> from config.database import Database
        >>> db = Database('http://localhost:3000/', 'v1', 'algorithms')
        >>> res = db.update(IAlgorithm id, IAlgorithm object)
        >>> res
        """

        head = {'Content-Type': 'application/json',
                'cache-control': 'no-cache'}
        response = request('PUT', f'{self.url}{str(object_id)}',
                           data=obj, headers=head)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)

    def delete(self, object_id):
        """
        Delete a object in a collection
        :param object_id: `str` ObjectId
        :return: `dict` lastest object version

        Usage
        >>> from config.database import Database
        >>> db = Database('http://localhost:3000/', 'v1', 'algorithms')
        >>> res = db.delete(IAlgorithm id)
        >>> res
        """

        head = {'Content-Type': 'application/json',
                'cache-control': 'no-cache'}
        response = request(
            'DELETE', f'{self.url}{str(object_id)}', headers=head)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)
