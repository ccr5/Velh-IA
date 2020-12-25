import os
import sys
import logging
from config.database import Database
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from requests import request, exceptions
from velhia import Velhia


def play(vlh):
    """
    Velh-IA Flow Control.
    Execute each step of Velh-IA workflow and keeps Velh-IA working good.
    """

    print('Taking the necessary data to start another play')
    [match, sa, mas] = vlh.get_data()
    print('All data was taken')

    print('Get the next player')
    sequence = vlh.get_sequence(match)
    print("Next player: " + sequence[-1])

    print('Getting game status')
    game_status = vlh.game_status(match, sa.info['_id'])
    print('the game status was taken', game_status)

    if sequence[-1] == 'SA':
        start = datetime.now()
        print('Started to play at ' + str(start.date()))
        position = sa.play(game_status)
        end = datetime.now()
        print('Ended at ' + str(end.date()))
        time = end - start
        time = time.microseconds / 1000000
        print('time to play: ' + str(time))
        print(f'choose to play in the position { str(position + 1) }')
    else:
        start = datetime.now()
        print('Started to play at ' + str(start.date()))
        position = mas.play(match, game_status)
        end = datetime.now()
        print('Ended at ' + str(end.date()))
        time = end - start
        time = time.microseconds / 1000000
        print('time to play: ' + str(time))
        print(f'choose to play in the position { str(position + 1) }')

    vlh.update_match(match, sa, mas,
                     sequence[-1], game_status, position, time)

    vlh.check_draw(match, sa, mas)
    print('next move')


def main():
    """
    Velh-IA's Main function.
    Load environment variables 
    check requirements and connections
    before to start the game
    """

    try:

        load_dotenv(find_dotenv())
        print('Welcome to Velh-IA Game\nWhere everything happens\n')
        print('Creating log file')
        root_dir = os.path.dirname(os.path.abspath(__file__))
        logging.basicConfig(filename=f'{root_dir}/logs/{datetime.now()}.log', filemode='w',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                            level=logging.DEBUG)
        logging.info('Check all requirements to starting Velh-IA Game')
        print("Check connection with Velhia's API...")
        response = request('GET', os.getenv('API_ADDRESS'))
        logging.info("Connected with Velhia's API")

        print('Creating databases objects...')
        match_db = Database('v1', 'matchs')
        family_db = Database('v1', 'families')
        education_db = Database('v1', 'educations')
        religion_db = Database('v1', 'religions')
        algorithm_db = Database('v1', 'algorithms')
        logging.info('Databases objects was created!')

        print('Creating Velhia object...')
        velhia = Velhia(match_db, family_db, education_db,
                        religion_db, algorithm_db)
        logging.info('Velhia object was created!\n')

        print('Deleting unnecessary datas...')
        del match_db, algorithm_db, family_db, education_db, religion_db
        logging.info('Unnecessary datas was deleted!\n')

        print('Starting Velh-IA Game\n\n')
        logging.info('Starting Velh-IA Game')

        while True:
            play(velhia)

    except exceptions.ConnectionError:
        print("Can't connect with Velh-IA API")
        logging.exception("Can't connect with Velh-IA API")
    except:
        print('Error (main.py): ', sys.exc_info())
        logging.exception('Exception occurred')


if __name__ == "__main__":
    main()
