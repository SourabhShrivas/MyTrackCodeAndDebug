# Pass by reference, (address)
# Mutable
from typing import List


# def change1(my_list: List):
#     print(f"Mylist = {id(my_list)}")
#     my_list[0] = 100


# xyz = [34, 22, 11, 78, 67, 65]
# print(f"XYZ = {id(xyz)}")
# change1(xyz)
# print(xyz)


# Pass by value -> int,floats,strings


def change(a: int, b: int):
    a = 100
    b = 100


a = 1
b = 1
change(a, b)
print(a)
print(b)
