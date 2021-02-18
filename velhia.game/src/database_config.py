from typing import List
from usecases.database.database_types import DatabaseType


def load_database_entities(
        address: str, version: str,
        collections: List[str]) -> List[DatabaseType]:

    def create_database(collection: str) -> DatabaseType:
        return {
            'address': address,
            'version': version,
            'collection': collection,
            'url': f"{address}api/{version}/{collection}/"
        }

    return list(map(create_database, collections))
