"""Q2. Write a function which accepts a String as a parameter and return the list of words.
"""


def func(str) -> list:
    return str.split("")  # by default it takes white space like \t \n etc


str = "hel\tlo world"
print(func(str))
