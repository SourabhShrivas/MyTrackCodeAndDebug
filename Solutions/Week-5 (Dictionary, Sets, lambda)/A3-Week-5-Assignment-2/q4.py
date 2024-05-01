"""Q4. Write a Python script to print a dictionary where the keys are numbers between 
1 and 15 (both included) and the values are squares of the keys.
"""


def fun():
    result_dict = dict()
    for i in range(1, 15 + 1):
        result_dict[i] = i * i

    return result_dict


print(fun())
