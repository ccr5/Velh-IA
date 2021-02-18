import os
from datetime import datetime


def root_dir() -> str:
    return os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')


def log_file_name() -> str:
    return f'{datetime.now()}.log'


def check_dir(path: str) -> bool:
    return os.path.exists(path)
