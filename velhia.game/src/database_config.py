from typing import List
from usecases.database.database_types import DatabaseType


def load_database_entities(address: str,
                           version: str,
                           collections: List[str]) -> List[DatabaseType]:

    return list(map(
        lambda collection: {
                'address': address,
                'version': version,
                'collection': collection,
                'url': f"{address}api/{version}/{collection}/"},
        collections
    ))
