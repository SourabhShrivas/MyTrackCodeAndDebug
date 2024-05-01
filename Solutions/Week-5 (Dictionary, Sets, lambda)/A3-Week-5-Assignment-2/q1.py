"""Q1. Write a function that takes a dictionary and a key,
 and returns True if the key is found in the dictionary, otherwise False."""

from typing import Dict


# def find(d: Dict, k) -> bool:
#     result = False
#     if k in d.keys():
#         result = True

#     else:
#         result = False
#     return result


def find(d: Dict, key) -> bool:
    return key in d.keys()


d = {
    "science": 78,
    "english": 91,
    "maths": 56,
    "hindi": 84,
    "gender": "Male",
    "adult": False,
    "phone_number": [985698, 774455, 4111125],
}

k = "phone_number"

print(find(d, k))
# print(type(d.keys()))
