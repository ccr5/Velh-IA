import os
from dotenv import load_dotenv, find_dotenv
from requests import request
from players.statistical_algorithm import StatisticalAlgorithm
from velhia import Velhia


def main():
    """ Velh-IA's Main function """
    try:
        load_dotenv(find_dotenv())
        print('Welcome to Velh-IA Game\nWhere everything happens')
        print('Check all requirements to starting Velh-IA Game')
        response = request('GET', os.getenv('API_ADDRESS'))

        if response.json() == {'message': 'Welcome Velh-IA API'}:
            print('Connected in Velh-IA API')
        else:
            print("Can't connect with Velh-IA API")

        Velhia.play()
    except:
        print('erro')


if __name__ == "__main__":
    main()
