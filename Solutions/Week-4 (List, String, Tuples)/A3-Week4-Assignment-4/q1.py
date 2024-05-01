# Q1. Write a Python program to get the 4th element from the last element of a tuple.


def nthElement(tpl: tuple, n: int) -> None:
    res = tpl[0 : len(tpl) - n + 1][-1]
    print(f"{n}th ellement from last is : {res}")


nthElement((1, 5, 7, 9, 3, 5, 6, 7, 8), 4)
