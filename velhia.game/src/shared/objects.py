from typing import List, TypedDict


def merge_objects(first_dict: dict, second_dict: dict, tp: TypedDict) -> TypedDict:
    return tp({**first_dict, **second_dict})


def remove_objects(obj: dict, keys: List[str], nKeys: int) -> dict:
    if nKeys > 0:
        return remove_objects(obj.pop(keys[nKeys - 1], None), keys, nKeys - 1)
    else:
        return obj
