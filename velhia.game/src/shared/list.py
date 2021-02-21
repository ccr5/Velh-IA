from typing import Any


def merge_list(current_list: list, position: int, value: Any, ret: list = []) -> list:

    if len(ret) < len(current_list):
        if len(ret) == position:
            new_ret: list = ret + [value]
            return merge_list(current_list, position, value, new_ret)
        else:
            new_ret: list = ret + [current_list[len(ret)]]
            return merge_list(current_list, position, value, new_ret)
    else:
        return ret
