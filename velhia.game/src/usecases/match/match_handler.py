from typing import Any
from entities.match.match import Match
from usecases.match.match_dto import match_to_entity
from shared.objects import merge_objects


def add(match: Match, field: str, value: Any) -> Match:

    current_value = match[field]
    new_value = current_value + value
    obj = {field: new_value}
    return merge_objects(match, obj)


def insert(match: Match, field: str, value: Any) -> Match:

    obj_to_add = {field: value}
    return match_to_entity(merge_objects(match, obj_to_add))


def change(match: Match, field: str, value: Any) -> Match:

    obj_to_add = {field: value}
    return match_to_entity(merge_objects(match, obj_to_add))
