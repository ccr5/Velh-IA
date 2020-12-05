import os
from config.database import Database
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from requests import request
from velhia import Velhia


def play(vlh):
    """
    Velh-IA Flow Control.
    Execute each step of Velh-IA workflow and keep Velh-IA works good.
    """

    print('Getting data...')
    [match, sa, education_leader, education_learner, religion_leader,
     religion_learner, family_leader, family_learner, mas] = vlh.get_data()
    print('All datas was taked!')

    print('Get who has to play now')
    sequence = vlh.get_sequence(match)
    print("It's time to " + sequence[-1] + ' plays')

    print('Getting game status...')
    game_status = vlh.game_status(match, sa.info['_id'])
    print(game_status)

    if sequence[-1] == 'SA':
        start = datetime.now()
        position = sa.play(game_status)
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        print(f'choose to play in the position { str(position + 1) }')
        game_status[position] = 1
        print(f'new game status: {game_status}')
        vlh.update_sa_match(match, sa, game_status, position,
                            start.ctime(), time)
    else:
        start = datetime.now()
        position = mas.play(game_status)
        end = datetime.now()
        time = end - start
        time = time.microseconds / 1000000
        print(f'choose to play in the position { str(position + 1) }')
        game_status[position] = 1
        print(f'new game status: {game_status}')
        vlh.update_mas_match()


def main():
    """
    Velh-IA's Main function.
    Load environment variables, check requirements and connections
    before to start the game
    """
    try:
        load_dotenv(find_dotenv())
        print('Welcome to Velh-IA Game\nWhere everything happens')
        print('Check all requirements to starting Velh-IA Game')

        response = request('GET', os.getenv('API_ADDRESS'))

        if response.json() == {'message': 'Welcome Velh-IA API'}:
            print('Connected in Velh-IA API')
        else:
            print("Can't connect with Velh-IA API")

        match_db = Database('v1', 'matchs')
        family_db = Database('v1', 'families')
        education_db = Database('v1', 'educations')
        religion_db = Database('v1', 'religions')
        algorithm_db = Database('v1', 'algorithms')
        vlh = Velhia(match_db, family_db, education_db,
                     religion_db, algorithm_db)

        print('Database Objects Ok')
        print('Starting Velh-IA Game')

        while True:
            play(vlh)
    except:
        print('Error to starting Velh-IA Game (main.py)')


if __name__ == "__main__":
    main()
