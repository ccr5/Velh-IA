import os
from dotenv import load_dotenv, find_dotenv
from requests import request
from players.statistical_algorithm import StatisticalAlgorithm


def main():
    """
    Velh-IA's Main function
    """
    try:
        load_dotenv(find_dotenv())
        print('Welcome to Velh-IA Game \nWhere everything happens')
        print('Check all requirements to starting Velh-IA Game')
        response = request('GET', os.getenv('API_ADDRESS'))

        if response.json() == {'message': 'Welcome Velh-IA API'}:
            print('Connected in Velh-IA API')
        else:
            print("Can't connect with Velh-IA API")
    except:
        print('erro')

    # Check all requirements before to start the game
    # Create an instance of all objects to start the game


if __name__ == "__main__":
    main()
