"""Q7. Write a Python function that takes a dictionary as input where the values are lists of integers. 
The function should return a new dictionary 
where the values are lists containing only the even integers from the original lists."""

from typing import Dict


def func(input_dict: Dict) -> dict:
    result_dict = dict()

    for key, value in input_dict.items():
        even_list = []
        for i in value:
            if i % 2 == 0:
                even_list.append(i)

            result_dict[key] = even_list

    return result_dict


input_dict = {"a": [1, 2, 3, 4, 5], "b": [10, 11, 12, 13, 14]}

print(func(input_dict))
