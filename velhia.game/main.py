import os
from dotenv import load_dotenv, find_dotenv
from requests import request
from sa import StatisticalAlgorithm


def main():
    """
    Velh-IA's Main function
    """
    try:
        print('Welcome to Velh-IA Game \nWhere everything happens')
        load_dotenv(find_dotenv())
        response = request('GET', os.getenv('API_ADDRESS'))
        print('Starting to check all requirements to start..')

        if response.json() == {'message': 'Welcome Velh-IA API'}:
            print('Connected in Velh-IA API')
        else:
            print("Can't connect with Velh-IA API")

        print('Creating Statistical Algorithm object..')
    except:
        pass

    # Check all requirements before to start the game
    # Create an instance of all objects to start the game


if __name__ == "__main__":
    main()
