"""Q3. Write a function that updates the values of a 
dictionary by multiplying them by a given factor only if the value is an integer."""

from typing import Dict
import copy


def func(d: Dict) -> Dict:
    factor = int(input("Enter a facter you want to multiply : "))
    result_dict = copy.copy(d)
    for key, value in d.items():
        if type(value) == int:
            result_dict[key] = value * factor

    return result_dict


d1 = {"science": 10, "english": 20, "Physics": "20"}
print(func(d1))
