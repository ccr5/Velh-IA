from datetime import datetime
from entities.match.match import Match
from usecases.match.match_mapper import match_to_entity


class TestMatchMapper:

    match: Match = dict([
        ("_id", "5ffb08c12f6c302d184c38d9"),
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
        ("status", "PENDENT"),
        ("__v", 0),
        ("createdAt", datetime.now().ctime()),
        ("updatedAt", datetime.now().ctime())
    ])

    def test_match_to_entity(self) -> None:

        new_match = match_to_entity(self.match)
        check_match = self.match
        del check_match["__v"], check_match["createdAt"], check_match["updatedAt"]
        assert check_match == new_match
