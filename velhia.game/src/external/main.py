import os
import sys
import logging
from src.adapters.repository.database_types import DatabaseType
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from requests import request, exceptions, Response


load_dotenv(find_dotenv())


def play(match_db: DatabaseType, algorithm_db: DatabaseType,
         family_db: DatabaseType, education_db: DatabaseType,
         religion_db: DatabaseType) -> None:
    """
    Velh-IA Flow Control.
    Execute and control each step of Velh-IA workflow.
    """

    try:
        [match_backup, sa_backup, mas_backup] = vlh.backup()
        [match, sa, mas] = vlh.start()
        vlh.validate(match, sa, mas)
        logging.info('All informations was validated')
        sequence = vlh.get_sequence(match)
        game_status = vlh.game_status(match, sa.id)

        if sequence[-1] == 'SA':
            start = datetime.now()
            position = sa.play(game_status)
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000
        else:
            start = datetime.now()
            position = mas.play(match, game_status)
            end = datetime.now()
            time = end - start
            time = time.microseconds / 1000000

        vlh.update_match(match, sa, mas,
                         sequence[-1], game_status, position, time)

        vlh.check_draw(match, sa, mas)

        logging.info(f"match: {match.id}")
        logging.info(f"sa: {match.sa}")
        logging.info(f"family: {match.mas['family']}")
        logging.info(f"education: {match.mas['education']}")
        logging.info(f"religion: {match.mas['religion']}")
        logging.info(f"seq: {len(match.plays)}")
        logging.info(f"game: {game_status}")
        logging.info(f"status: {match.status}")
        logging.info(
            f"winner: {match.winner}") if match.status == "WINNER" else ""

        del match, sa, mas, sequence, game_status, start, position, end, time

    except Exception as e:
        vlh.rollback(match, match_backup, sa, sa_backup, mas, mas_backup)
        logging.info('Rollback function is successfully')
        raise e


def main() -> None:
    """
    Velh-IA's Main function.
    Load environment variables, check requirements and connections before to start the game
    """

    try:
        root_dir: str = os.path.dirname(
            os.path.abspath(__file__)).replace('\\', '/')

        try:
            file_name: str = f'{datetime.now()}.log'
            logging.basicConfig(filename=f'{root_dir}/logs/{file_name}', filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.DEBUG)
            logging.info(f'log file {file_name} was created')
        except:
            if not os.path.exists(f'{root_dir}/logs/app.log'):
                open(f'{root_dir}/logs/app.log', 'x')

            logging.basicConfig(filename=f'{root_dir}/logs/app.log', filemode='w',
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                level=logging.DEBUG)
            logging.info(f'log file app.log was created')

        response: Response = request('GET', os.getenv('API_ADDRESS'))
        logging.info("Connected with Velhia's API")
        logging.info('Check all requirements to starting Velh-IA Game')

        match_db: DatabaseType = {
            'address': os.getenv('API_ADDRESS'),
            'version': os.getenv('API_VERSION'),
            'collection': 'matchs',
            'url': f'{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/matchs/'
        }

        family_db: DatabaseType = {
            'address': os.getenv('API_ADDRESS'),
            'version': os.getenv('API_VERSION'),
            'collection': 'families',
            'url': f'{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/families/'
        }

        education_db: DatabaseType = {
            'address': os.getenv('API_ADDRESS'),
            'version': os.getenv('API_VERSION'),
            'collection': 'educations',
            'url': f'{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/educations/'
        }

        religion_db: DatabaseType = {
            'address': os.getenv('API_ADDRESS'),
            'version': os.getenv('API_VERSION'),
            'collection': 'religions',
            'url': f'{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/religions/'
        }

        algorithm_db: DatabaseType = {
            'address': os.getenv('API_ADDRESS'),
            'version': os.getenv('API_VERSION'),
            'collection': 'algorithms',
            'url': f'{os.getenv('API_ADDRESS')}api/{os.getenv('API_VERSION')}/algorithms/'
        }

        logging.info('Databases was created!')
        del response, file_name, root_dir
        logging.info('Unnecessary datas was deleted!')
        logging.info('Starting Velh-IA Game')

        while True:
            play(match_db, algorithm_db, family_db,
                 education_db, religion_db)

    except exceptions.ConnectionError:
        print("Can't connect with Velh-IA API")
        logging.exception("Can't connect with Velh-IA API")

    except:
        print('Error: ', sys.exc_info())
        logging.exception('Exception occurred')


if __name__ == "__main__":
    main()
