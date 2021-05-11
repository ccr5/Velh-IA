from typing import Dict, List
from entities.match.match import Match


def match_to_entity(obj: Dict) -> Match:

    filters: List[str] = ['createdAt', 'updatedAt', '__v']
    return {k: v for k, v in obj.items() if k not in filters}
