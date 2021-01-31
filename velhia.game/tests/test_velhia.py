from velhia import Velhia
from config.database import Database


class TestVelhia:

    match_test_db = Database('http://localhost:3000/test/',
                             'v1', 'matchs')
    family_test_db = Database('http://localhost:3000/test/',
                              'v1', 'families')
    algorithm_test_db = Database('http://localhost:3000/test/',
                                 'v1', 'algorithms')
    education_test_db = Database('http://localhost:3000/test/',
                                 'v1', 'educations')
    religion_test_db = Database('http://localhost:3000/test/',
                                'v1', 'religions')

    velhia = Velhia(match_test_db, family_test_db,
                    education_test_db, religion_test_db,
                    algorithm_test_db)

    def test_backup(self):
        ret = self.velhia.backup()
        assert ret == [None, None, None]
        match1 = {}
        match2 = {}
        match3 = {}
