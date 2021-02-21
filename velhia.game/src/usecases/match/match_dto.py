from typing import Dict
from entities.match.match import Match
from shared.objects import create_object


def match_to_entity(obj: Dict) -> Match:

    items: list = list(obj.items())
    return Match(
        create_object(
            items, len(items),
            ['createdAt', 'updatedAt', '__v']
        )
    )
