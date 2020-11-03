import os
from config.database import Database
from dotenv import load_dotenv, find_dotenv
from requests import request
from velhia import Velhia


def play():
    """ 
    Velh-IA Flow Control.
    Execute each step of Velh-IA workflow and keep Velh-IA works good.
    """
    match_db = Database('v1', 'matchs')
    family_db = Database('v1', 'families')
    education_db = Database('v1', 'educations')
    religion_db = Database('v1', 'religions')
    algorithm_db = Database('v1', 'algorithms')
    vlh = Velhia(match_db, family_db, education_db, religion_db, algorithm_db)

    (match, sa, education_leader, education_learner, religion_leader,
     religion_learner, family_leader, family_learner) = vlh.get_data()

    print(match, sa, education_leader, education_learner, religion_leader,
          religion_learner, family_leader, family_learner)


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

        print('Starting Velh-IA Game')

        while True:
            play()
    except:
        print('Error to starting Velh-IA Game (main.py)')


if __name__ == "__main__":
    main()
