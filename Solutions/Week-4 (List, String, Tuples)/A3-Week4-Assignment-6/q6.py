"""Q6. Write a function which accepts a String and another string 
(which will be a single character) as a parameter. 
Join that string along with that character.
"""


def func(s1: str, ch: str) -> str:
    return ch.join(s1.split(" "))


s1 = "humse dsa ho jayega"
ch = "YES"
print(func(s1, ch))
