import os
import sys
import logging
from errors.invalid_match import InvalidMatch
from config.database import Database
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from requests import request, exceptions
from velhia import Velhia


def play(vlh):
    """
    Velh-IA Flow Control.
    Execute and control each step of Velh-IA workflow.
    """

    [match, sa, mas] = vlh.get_data()
    vlh.validate(match, sa, mas)
    sequence = vlh.get_sequence(match)
    game_status = vlh.game_status(match, sa.info['_id'])

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

    logging.info(f"match: {match.info['_id']}")
    logging.info(f"sa: {match.info['sa']}")
    logging.info(f"family: {match.info['mas']['family']}")
    logging.info(f"education: {match.info['mas']['education']}")
    logging.info(f"religion: {match.info['mas']['religion']}")
    logging.info(f"seq: {len(match.info['plays'])}")
    logging.info(f"game: {game_status}")
    logging.info(f"status: {match.info['status']}")
    logging.info(
        f"winner: {match.info['winner']}") if match.info['status'] == "WINNER" else ""

    del match, sa, mas, sequence, game_status, start, position, end, time


def main():
    """
    Velh-IA's Main function.
    Load environment variables, check requirements and connections before to start the game
    """

    try:

        load_dotenv(find_dotenv())

        root_dir = os.path.dirname(os.path.abspath(__file__))
        logging.basicConfig(filename=f'{root_dir}/logs/{datetime.now()}.log', filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.INFO)

        logging.info('Check all requirements to starting Velh-IA Game')
        response = request('GET', os.getenv('API_ADDRESS'))
        logging.info("Connected with Velhia's API")

        match_db = Database('v1', 'matchs')
        family_db = Database('v1', 'families')
        education_db = Database('v1', 'educations')
        religion_db = Database('v1', 'religions')
        algorithm_db = Database('v1', 'algorithms')
        logging.info('Databases objects was created!')

        velhia = Velhia(match_db, family_db, education_db,
                        religion_db, algorithm_db)
        logging.info('Velhia object was created!')

        del match_db, algorithm_db, family_db, education_db, religion_db, root_dir
        logging.info('Unnecessary datas was deleted!')

        logging.info('Starting Velh-IA Game')

        while True:
            play(velhia)

    except exceptions.ConnectionError:
        print("Can't connect with Velh-IA API")
        logging.exception("Can't connect with Velh-IA API")

    except InvalidMatch:
        print("There's something incongruity in the Velh-IA")
        logging.exception("There's something incongruity in the Velh-IA")

    except:
        print('Error (main.py): ', sys.exc_info())
        logging.exception('Exception occurred')


if __name__ == "__main__":
    main()
