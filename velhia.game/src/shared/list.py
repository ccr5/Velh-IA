from typing import Any


def merge_list(current_list: list, lenght: int, position: int,
               value: Any, ret: list = []) -> list:

    if len(ret) < lenght:
        if len(ret) + 1 == position:
            new_ret: list = ret + [value]
            return merge_list(current_list, lenght, position, value, new_ret)
        else:
            new_ret: list = ret + current_list[len(ret) + 1]
            return merge_list(current_list, lenght, position, value, new_ret)
    else:
        return ret
