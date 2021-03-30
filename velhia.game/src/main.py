import os
import sys
import logging
from itertools import repeat
from datetime import datetime
from requests import request, exceptions, Response
from dotenv import load_dotenv, find_dotenv
from typing import Callable, NoReturn
from system import root_dir, log_file_name, check_dir
from adapters.repository.database import database
from adapters.controllers.database_controller import backup
from adapters.controllers.match_controller import start, get_sequence
from adapters.controllers.match_controller import current_game_status, update_current_match, check_draw
from adapters.controllers.sa_controller import play_sa
from adapters.validations.validate import validate
from usecases.database.database_types import DatabaseRepositoryType
from usecases.sa.sa_database import get_sa
from usecases.sa.sa_mapper import sa_to_adapter
from ovomaltino.ovomaltino import Ovomaltino


load_dotenv(find_dotenv())


def play(match_db: DatabaseRepositoryType, algorithm_db: DatabaseRepositoryType,
         mas: Ovomaltino) -> NoReturn:
    """
    Velh-IA Flow Control.\n
    Execute and control each step of Velh-IA workflow.
    """

    try:
        bckp = backup(match_db, algorithm_db)
        mas.load(5, [0, 1, 2, 3, 4, 5, 6, 7, 8], {'WINNER': {'consequence': 0},
                                                  'DRAW': {'consequence': 0},
                                                  'LOSER': {'consequence': -1}})
        (match, sa, mas_agents) = start(match_db, algorithm_db, mas)
        validate(match_db, algorithm_db, match, sa)

        logging.info('All informations was validated')
        sequence = get_sequence(match_db, match)
        game_status = current_game_status(match, sa['_id'])

        if sequence[-1] == 'SA':
            begin = datetime.now()
            position = play_sa(sa, game_status)
            end = datetime.now()
            time = end - begin
            time = time.microseconds / 1000000
        else:
            begin = datetime.now()
            # position = play_mas(match, game_status)
            end = datetime.now()
            time = end - begin
            time = time.microseconds / 1000000

        update_current_match(match_db, algorithm_db, match, sa,
                             mas_agents, sequence[-1], game_status,
                             position, time)

        check_draw(match_db, algorithm_db, match, sa)

        logging.info(f"match: {match['_id']}")
        logging.info(f"sa: {match['sa']}")
        logging.info(f"seq: {len(match['plays'])}")
        logging.info(f"game: {game_status}")
        logging.info(f"status: {match['status']}")

        if match['status'] == "WINNER":
            logging.info(f"winner: {match['winner']}")

        return play(match_db, algorithm_db, mas)
    except Exception as e:

        if match is None or sa is None or mas is None:
            logging.info('There is no objects to Rollback')
        else:
            bckp(match, sa, mas)
            logging.info('Rollback function is successfully')

        raise e


def main() -> Callable[[DatabaseRepositoryType, DatabaseRepositoryType,
                        Ovomaltino], NoReturn]:
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

        [match_db, algorithm_db] = list(map(
            database,
            list(map(
                lambda address, version, collection: {'address': address,
                                                      'version': version,
                                                      'collection': collection,
                                                      'url': f"{address}api/{version}/{collection}/"},
                repeat(os.getenv('API_ADDRESS')),
                repeat(os.getenv('API_VERSION')),
                os.getenv('COLLECTIONS').split(',')
            ))
        ))

        logging.info('Databases was created!')

        mas = Ovomaltino(os.getenv('OVOMALTINO_API_ADDRESS'),
                         os.getenv('OVOMALTINO_API_PORT'),
                         os.getenv('OVOMALTINO_API_VERSION'))

        if mas.isconnected():
            pass
        else:
            raise SystemError

        logging.info('Ovomaltino is loaded!')
        logging.info('Starting Velh-IA Game')
        return play(match_db, algorithm_db, mas)

    except exceptions.ConnectionError:
        print("Can't connect with Velh-IA API")
        logging.exception("Can't connect with Velh-IA API")

    except:
        print('Main error: ', sys.exc_info())
        logging.exception('Exception occurred')


if __name__ == "__main__":
    main()
