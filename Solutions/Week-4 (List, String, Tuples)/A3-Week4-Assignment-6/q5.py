"""Q5. Write a function which accepts a String as a 
parameter and return each word being in reverse.
"""


def func(s: str) -> str:
    s_list = s.split(" ")
    temp_list = []

    for word in s_list:
        temp_list.append(word[::-1])

    return " ".join(temp_list)


s = "python is great"
print(func(s))
