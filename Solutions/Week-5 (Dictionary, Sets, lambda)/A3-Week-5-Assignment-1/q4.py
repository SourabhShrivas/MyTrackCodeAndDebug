"""Q5. Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x)"""

from typing import Dict


def createDictionary(num: int) -> Dict[int, int]:
    result_dict = dict()

    for number in range(1, num + 1):
        result_dict[number] = number**2

    return result_dict


num = 5
print(createDictionary(num))
