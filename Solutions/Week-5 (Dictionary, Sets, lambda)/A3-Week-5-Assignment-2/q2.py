"""Q2. Given two dictionaries, write a function to merge them into a new dictionary. 
If there is any overlap of keys, the value from the second dictionary should overwrite the one from the first dictionary."""

import copy

d1 = {
    "science": 78,
    "english": 91,
}

d2 = {
    "science": 99,
    "maths": 56,
    "hindi": 84,
}


def mergedDictionary(d1, d2):
    merged = copy.copy(d1)
    for key, value in d2.items():
        merged[key] = value
    return merged


print(mergedDictionary(d1, d2))

print(
    mergedDictionary(
        {"apple": 3, "banana": 5, "cherry": 7},
        {"banana": 8, "orange": 10, "apple": 9},
    )
)
