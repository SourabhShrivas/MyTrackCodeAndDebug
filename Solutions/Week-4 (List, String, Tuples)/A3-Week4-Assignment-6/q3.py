"""
Q3. Write a function which accepts 
a String as a parameter and return the reversed words as a String.
"""


def func(str) -> str:
    return " ".join(str.split(" ")[::-1])


str = "python is great"
print(func(str))
