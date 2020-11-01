import os
from dotenv import load_dotenv, find_dotenv
from requests import request


def check_requirements():
    errors = []
    load_dotenv(find_dotenv())
    response = request('GET', os.getenv('API_ADDRESS'))
    print('Starting to check all requirements to start..')

    if response.json() == {'message': 'Welcome Velh-IA API'}:
        pass
    else:
        errors.append("Can't connect with Velh-IA API")
