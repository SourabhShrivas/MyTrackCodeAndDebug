"""
Q3. Python 
Program to remove all duplicates from a given string.
"""


def func(str: str) -> str:
    result_str = ""
    for ch in str:
        if ch not in result_str:
            result_str = result_str + ch
    return result_str


str = "aakkkkkkkkkkkkkkkkkkkeeeeeeeeeepoiursd"
print(func(str))
