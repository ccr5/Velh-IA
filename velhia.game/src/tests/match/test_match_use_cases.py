import os
from datetime import datetime
from adapters.repository.database import database
from entities.match.match import Match
from usecases.match.match_use_cases import create_new_match, alter_match


class TestMatchUseCases:

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
    ])

    # def test_create_new_match(self) -> None:

    #     match_db = database({
    #         'address': os.getenv('API_ADDRESS'),
    #         'version': os.getenv('API_VERSION'),
    #         'collection': 'matchtest',
    #         'url': f"{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/matchtest/"
    #     })

    #     sa = dict([
    #         ('_id': "5ffb08c12f6c302d184c38d2"),
    #         ('birth', '2021-02-21 14:32:09.000Z'),
    #         ('matchs', 0),
    #         ('victories', 0),
    #         ('defeats', 0),
    #         ('draw', 0),
    #         ('char', ['X', 1]),
    #         ('enemy', ['O', 0]),
    #         ('empty', ['O', 0])
    #     ])

    #     mas = dict([

    #     ])

    #     new_match = create_new_match(match_db, sa)

    def test_alter_match(self) -> None:

        field = 'time'
        value = 1
        new_match = alter_match('add')(self.match, field, value)
        check_match = self.match
        check_match['time'] = 1
        assert check_match == new_match
