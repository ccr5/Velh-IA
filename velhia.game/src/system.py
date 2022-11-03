import os
from datetime import datetime
from ovomaltino.ovomaltino import Ovomaltino


def root_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


def log_file_name() -> str:
    return f'{datetime.now()}.log'


def check_dir(path: str) -> bool:
    return os.path.exists(path)


def load_mas_object():

    mas = Ovomaltino(os.getenv('OVOMALTINO_API_ADDRESS'),
                     os.getenv('OVOMALTINO_API_PORT'),
                     os.getenv('OVOMALTINO_API_VERSION'))

    mas.load(5, [0, 1, 2, 3, 4, 5, 6, 7, 8], {'WINNER': {'consequence': 0},
                                              'DRAW': {'consequence': 0},
                                              'LOSER': {'consequence': -1}})

    return mas
