from velhia import Velhia
from config.database import Database


class TestVelhia:

    match_test_db = Database('http://localhost:3000/',
                             'v1', 'matchtests')
    family_test_db = Database('http://localhost:3000/',
                              'v1', 'familytests')
    algorithm_test_db = Database('http://localhost:3000/',
                                 'v1', 'algorithmtests')
    education_test_db = Database('http://localhost:3000/',
                                 'v1', 'educationtests')
    religion_test_db = Database('http://localhost:3000/',
                                'v1', 'religiontests')

    velhia = Velhia(match_test_db, family_test_db,
                    education_test_db, religion_test_db,
                    algorithm_test_db)

    def test_play(self):
        sa = StatisticalAlgorithm({}, ('X', 1), ('O', 0))
        position = sa.play([-1, -1, -1, -1, -1, -1, -1, -1, -1])
        assert position == 4
