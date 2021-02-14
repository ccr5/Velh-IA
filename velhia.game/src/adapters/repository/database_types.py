from typing import TypedDict


class DatabaseType(TypedDict):

    address = str
    version = str
    collection = str
    url = str
