"""Q7. Python program to find the size of a Dictionary. Basically print how
many total key-value pair are there."""

from typing import Dict


# def checkDictionarySize(dictionary: Dict) -> int:
#     size = 0

#     for k in dictionary.keys():
#         size = size + 1
#     return size


def checkDictionarySize(dictionary: Dict) -> int:
    return len(dictionary.keys())


my_dict = dict()
marks = {
    "Physics": 70,
    "Chemistory": 75,
    "Math": 80,
    "Hindi": 20,
}
print(checkDictionarySize(my_dict))
print(checkDictionarySize(marks))
