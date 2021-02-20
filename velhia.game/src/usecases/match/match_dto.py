from shared.objects import create_object
from entities.match.match import Match


def match_to_entity(obj: Match) -> Match:

    items: list = list(obj.items())
    return Match(
        create_object(
            items, len(items),
            ['createdAt', 'updatedAt', '__v']
        )
    )
