import os
import json
from requests import request, Response
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.entities.match.match import Match
from src.entities.multi_agent_system.agent import Agent
from .database_types import DatabaseType
from errors.database.invalid_response import InvalidResponse


def get(db: DatabaseType, filters: dict = {}, fields: str = '',
        sort: str = '', offset: int = -1, limit: int = -1) -> Response:
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

    complete_url = f'{db['url']}?filters={json.dumps(filters)}'
    complete_url += f'&fields={fields}' if fields != '' else ''
    complete_url += f'&sort={sort}' if sort != '' else ''
    complete_url += f'&offset={str(offset)}&limit={str(limit)}' if str(
        offset) != '-1' and str(limit) != '-1' else ''

    response = request('GET', complete_url)

    if response.status_code is 200:
        return response
    else:
        raise InvalidResponse(response.status_code, 200)


def create(db: DatabaseType, obj: Agent | Match | StatisticalAlgorithm) -> Response:
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
    response = request('POST', db['url'], data=obj, headers=head)

    if response.status_code is 200:
        return response
    else:
        raise InvalidResponse(response.status_code, 200)


def update(db: DatabaseType, object_id: str,
           obj: Agent | Match | StatisticalAlgorithm) -> Response:
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
    response = request('PUT', f'{db['url']}{str(object_id)}',
                       data=obj, headers=head)

    if response.status_code is 200:
        return response
    else:
        raise InvalidResponse(response.status_code, 200)


def delete(db: DatabaseType, object_id: str) -> Response:
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
        'DELETE', f'{db['url']}{str(object_id)}', headers=head)

    if response.status_code is 200:
        return response
    else:
        raise InvalidResponse(response.status_code, 200)
