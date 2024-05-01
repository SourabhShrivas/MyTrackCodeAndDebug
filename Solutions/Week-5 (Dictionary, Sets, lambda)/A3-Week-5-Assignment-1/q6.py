"""Q6. Write a Python program to check if a dictionary is empty or not."""

from typing import Dict


def checkEmptyDictionary(dictionary: Dict) -> bool:
    if len(dictionary) == 0:
        return True
    else:
        return False


my_dict = dict()
marks = {
    "Physics": 70,
    "Chemistory": 75,
    "Math": 80,
    "Hindi": 20,
}
print(checkEmptyDictionary(my_dict))
print(checkEmptyDictionary(marks))
