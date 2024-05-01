"""
Q5. Ask a string from user. 
Replace all the space characters with “-”. 
Do not use replace() method.
"""


def func(str: str) -> str:
    return str.replace(" ", "-", 2)


str = "thank you so much"
print(func(str))
