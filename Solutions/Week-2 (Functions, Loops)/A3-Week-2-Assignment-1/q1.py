# Q1. Write a Python function to find the Maximum and minimum of three numbers.
# Use 3 parameters. Make 2 different functions named as
# maxi and mini.


def maxi(a: int, b: int, c: int):
    result = max(a, b, c)
    print(f"{result} is the max number")


def mini(a: int, b: int, c: int):
    result = min(a, b, c)
    print(f"{result} is the max number")


maxi(2, 4, 5)
mini(2, 4, 5)
