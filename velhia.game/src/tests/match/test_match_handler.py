from datetime import datetime
from entities.match.match import Match
from usecases.match.match_handler import add, insert_or_change


class TestMatchHandler:

    match: Match = dict([
        ("begin", datetime.now().ctime()),
        ("time", 0),
        ("sa", {
            "playerId": "5ffb08c12f6c302d184c38d2",
            "symbol": "X"
        }),
        ("mas", [{"playerId": "5ffb08c12f6c302d184c38d7", "symbol": "O"},
                 {"playerId": "5ffb08c12f6c302d184c38d8", "symbol": "O"},
                 {"playerId": "5ffb08c12f6c302d184c38d9", "symbol": "O"}]),
        ("plays", []),
        ("status", "PENDENT")
    ])

    def test_add(self) -> None:

        field = 'time'
        value = 1
        new_match = add(self.match, field, value)
        check_match = self.match
        check_match['time'] = 1
        assert check_match == new_match

    def test_insert_or_change(self) -> None:

        field = 'death'
        value = datetime.now().ctime()
        new_match = insert_or_change(self.match, field, value)
        check_match = self.match
        check_match[field] = value
        assert check_match == new_match
