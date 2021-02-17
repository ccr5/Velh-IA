import json
from requests import request, Response
from typing import List
from src.entities.algorithm.sa import StatisticalAlgorithm
from src.entities.match.match import Match
from src.entities.multi_agent_system.agent import Agent
from src.adapters.types.database_types import DatabaseType
from src.shared.errors.database.invalid_response import InvalidResponse


def get(db: DatabaseType, filters: dict = {},
        fields: str = '', sort: str = '',
        offset: int = -1, limit: int = -1) -> Response:
    """
    Get objects in a collection
    :param filters: `{<str>:<value>,<str>:<value>}` all filters to find the objects
    :param fields: `<str>,<str>` all fields to take
    :param sort: `<campo>:<asc | desc>` how to order the objects
    :param offset: `int` index to start to get the objects
    :param limit: `int` how many objects get from offset
    :return: `Response` response

    import
    >>> from config.database import Database\n
    >>> db = Database('http://localhost:3000/', 'v1', 'algorithms')

    get all objects
    >>> res = db.get()\n
    >>> res.json()

    get by id
    >>> res = db.get(filters="{'_id': 'hash'}")\n
    >>> res.json()

    get just some fields
    >>> res = db.get(fields="-_id,victories")\n
    >>> res.json()

    get sorted objects
    >>> res = db.get(sort="createdAt:desc")\n
    >>> res.json() 

    get a list
    >>> res = db.get(offset=0, limit=2) # from the first one, get more 2 objects\n
    >>> res.json()
    """

    def complete_url(splits: List[str], validations: List[bool],
                     nValidations: int, res='') -> str | bool:

        if len(splits) == len(validations) == nValidations:

            if nValidations > 0:

                if validations[nValidations - 1] == True:
                    return complete_url(splits, validations, nValidations - 1,
                                        str(res + splits[nValidations - 1]))
                else:
                    return complete_url(splits, validations, nValidations - 1, res)
            else:
                return res

        else:
            return False

    params: list = [f'&fields={fields}',
                    f'&sort={sort}',
                    f'&offset={str(offset)}&limit={str(limit)}']

    validations: list = [fields != '',
                         sort != '',
                         str(offset) != '-1' and str(limit) != '-1']

    url: str | bool = complete_url(params, validations, len(params),
                                   f'{db["url"]}?filters={json.dumps(filters)}')

    if type(url) == str:
        response: Response = request('GET', url)

        if response.status_code is 200:
            return response
        else:
            raise InvalidResponse(response.status_code, 200)

    else:
        raise SystemError


def create(db: DatabaseType,
           obj: Agent | Match | StatisticalAlgorithm) -> Response:
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

    response: Response = request('POST', db['url'], data=obj, headers=head)

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

    response: Response = request('PUT', f'{db["url"]}{str(object_id)}',
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

    response: Response = request('DELETE',
                                 f'{db["url"]}{str(object_id)}',
                                 headers=head)

    if response.status_code is 200:
        return response
    else:
        raise InvalidResponse(response.status_code, 200)
