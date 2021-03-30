import operator as op
from typing import Any
from entities.match.match import Match
from usecases.match.match_mapper import match_to_entity


def add(match: Match, field: str, value: Any) -> Match:

    return match | {field: op.add(match[field], [value])}


def insert_or_change(match: Match, field: str, value: Any) -> Match:

    return match | {field: value}
