import os
import sys
import logging
from dotenv import load_dotenv, find_dotenv
from typing import Callable, NoReturn
from adapters.controllers.database_controller import backup
from adapters.controllers.match_controller import start
from usecases.database.database_types import DatabaseRepositoryType
from system import root_dir, log_file_name, check_dir
from database_config import load_database_entities
from requests import request, exceptions, Response
from adapters.repository.database import database


load_dotenv(find_dotenv())


def play(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
         family_db: DatabaseRepositoryType, education_db: DatabaseRepositoryType,
         religion_db: DatabaseRepositoryType) -> NoReturn:
    """
    Velh-IA Flow Control.\n
    Execute and control each step of Velh-IA workflow.
    """

    try:
        bckp = backup(match_db, algorithm_db, family_db,
                      education_db, religion_db)

        [match, sa, mas] = start(match_db, algorithm_db, family_db,
                                 education_db, religion_db)
#         vlh.validate(match, sa, mas)
#         logging.info('All informations was validated')
#         sequence = vlh.get_sequence(match)
#         game_status = vlh.game_status(match, sa.id)

#         if sequence[-1] == 'SA':
#             start = datetime.now()
#             position = sa.play(game_status)
#             end = datetime.now()
#             time = end - start
#             time = time.microseconds / 1000000
#         else:
#             start = datetime.now()
#             position = mas.play(match, game_status)
#             end = datetime.now()
#             time = end - start
#             time = time.microseconds / 1000000

#         vlh.update_match(match, sa, mas,
#                          sequence[-1], game_status, position, time)

#         vlh.check_draw(match, sa, mas)

#         logging.info(f"match: {match.id}")
#         logging.info(f"sa: {match.sa}")
#         logging.info(f"family: {match.mas['family']}")
#         logging.info(f"education: {match.mas['education']}")
#         logging.info(f"religion: {match.mas['religion']}")
#         logging.info(f"seq: {len(match.plays)}")
#         logging.info(f"game: {game_status}")
#         logging.info(f"status: {match.status}")
#         logging.info(
#             f"winner: {match.winner}") if match.status == "WINNER" else ""

#         del match, sa, mas, sequence, game_status, start, position, end, time

        return play(match_db, algorithm_db, family_db,
                    education_db, religion_db)

    except Exception as e:
        bckp['rollback'](match, sa, mas)
        logging.info('Rollback function is successfully')
        raise e


def main() -> Callable[
    [DatabaseRepositoryType, DatabaseRepositoryType, DatabaseRepositoryType,
     DatabaseRepositoryType, DatabaseRepositoryType], NoReturn]:
    """
    Velh-IA's Main function.\n
    Load environment variables, check requirements and connections before to start the game
    """

    try:

        try:
            log_file = log_file_name()
            logging.basicConfig(filename=f'{root_dir()}/logs/{log_file}', filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.DEBUG)
            logging.info(f'log file {log_file} was created')
        except:
            path = f'{root_dir()}/logs/app.log'

            if not check_dir(path):
                open(path, 'x')

            logging.basicConfig(filename=path, filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.DEBUG)
            logging.info(f'log file app.log was created')

        request('GET', os.getenv('API_ADDRESS'))
        logging.info("Connected with Velhia's API")
        logging.info('Check all requirements to starting Velh-IA Game')

        [match_db, family_db, education_db, religion_db, algorithm_db] = list(map(
            database,
            load_database_entities(
                os.getenv('API_ADDRESS'),
                os.getenv('API_VERSION'),
                os.getenv('COLLECTIONS').split(','))
        ))

        logging.info('Databases was created!')
        logging.info('Starting Velh-IA Game')

        return play(
            match_db, algorithm_db,
            family_db, education_db,
            religion_db
        )

    except exceptions.ConnectionError:
        print("Can't connect with Velh-IA API")
        logging.exception("Can't connect with Velh-IA API")

    except:
        print('Main error: ', sys.exc_info())
        logging.exception('Exception occurred')


if __name__ == "__main__":
    main()
