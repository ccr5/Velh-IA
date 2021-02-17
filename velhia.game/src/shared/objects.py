from typing import List, TypedDict, Tuple, Any
from src.shared.types.char import Char


def merge_objects(first_dict: dict, second_dict: dict) -> dict:
    return {**first_dict, **second_dict}


def remove_objects(obj: dict, keys: List[str], nKeys: int) -> dict:
    if nKeys > 0:
        return remove_objects(obj.pop(keys[nKeys - 1], None), keys, nKeys - 1)
    else:
        return obj


def create_object(
        key_list: List[Tuple[Char]], lenght: int,
        filters: List[str] = [], obj: dict = {}) -> dict:

    index: int = lenght - 1

    if lenght > 0:
        if key_list[index][0] in filters:
            return create_object(key_list, index, filters, obj)
        else:
            obj_to_add: dict = {key_list[index][0]: key_list[index][1]}
            return create_object(key_list, index, filters, merge_objects(obj, obj_to_add))
    else:
        return obj
