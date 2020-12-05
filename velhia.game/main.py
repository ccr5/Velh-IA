import os
import sys
from config.database import Database
from dotenv import load_dotenv, find_dotenv
from datetime import datetime
from requests import request
from velhia import Velhia


def play(file):
    """
    Velh-IA Flow Control.
    Execute each step of Velh-IA workflow and keeps Velh-IA working good.
    """

    try:
        match_db = Database('v1', 'matchs')
        family_db = Database('v1', 'families')
        education_db = Database('v1', 'educations')
        religion_db = Database('v1', 'religions')
        algorithm_db = Database('v1', 'algorithms')
        vlh = Velhia(match_db, family_db, education_db,
                     religion_db, algorithm_db)

        while True:

            print('Taking the necessary data to start another play')
            file.write('Taking the necessary data to start another play')

            [match, sa, mas] = vlh.get_data()
            print('All data was taken', match.info)
            file.write('All data was taken: ' + str(match.info))

            print('Get the next player')
            file.write('Get the next player')

            sequence = vlh.get_sequence(match)
            print("Next player: " + sequence[-1])
            file.write("Next player: " + sequence[-1])

            print('Getting game status')
            file.write('Getting game status')
            game_status = vlh.game_status(match, sa.info['_id'])
            print('the game status was taken', game_status)
            file.write('the game status was taken: ' + str(game_status))

            if sequence[-1] == 'SA':
                start = datetime.now()
                print('Started to play at ' + str(start.date()))
                file.write('Started to play at ' + str(start.ctime()))
                position = sa.play(game_status)
                end = datetime.now()
                print('Ended at ' + str(end.date()))
                file.write('Ended at ' + str(end.ctime()))
                time = end - start
                time = time.microseconds / 1000000
                print('time to play: ' + str(time))
                file.write('time to play: ' + str(time))
                print(f'choose to play in the position { str(position + 1) }')
                file.write(
                    f'choose to play in the position { str(position + 1) }')
                game_status[position] = 1
                print(f'new game status: {game_status}')
                file.write(f'new game status: {str(game_status)}')
                vlh.update_sa_match(match, sa, game_status, position,
                                    start.ctime(), time)
                print('next move')
                file.write('next move')
            else:
                start = datetime.now()
                print('Started to play at ' + str(start.date()))
                file.write('Started to play at ' + str(start.ctime()))
                position = mas.play(game_status)
                end = datetime.now()
                print('Ended at ' + str(end.date()))
                file.write('Ended at ' + str(end.ctime()))
                time = end - start
                time = time.microseconds / 1000000
                print('time to play: ' + str(time))
                file.write('time to play: ' + str(time))
                print(f'choose to play in the position { str(position + 1) }')
                file.write(
                    f'choose to play in the position { str(position + 1) }')
                game_status[position] = 1
                print(f'new game status: {str(game_status)}')
                file.write(f'new game status: {str(game_status)}')
                # vlh.update_mas_match()
                print('next move')
                file.write('next move')
    except:
        print('Play() Error: ', sys.exc_info())


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

        print('Connected in Velh-IA API') if response.json() == {
            'message': 'Welcome Velh-IA API'} else print("Can't connect with Velh-IA API")

        print('Creating log file')
        f = open(f'{datetime.now()}.txt', 'w')

        print('Starting Velh-IA Game')
        print('Today is ' + str(datetime.now()))

        f.write('Today is ' + str(datetime.now()) + '\n')

        play(f)
    except:
        print('Error to starting Velh-IA Game (main.py)', sys.exc_info())


if __name__ == "__main__":
    main()
