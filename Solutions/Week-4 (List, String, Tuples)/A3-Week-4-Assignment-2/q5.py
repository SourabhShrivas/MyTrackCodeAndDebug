# Q5. Write a python program to interchange
# first and last elements in a list.


def func(lst) -> list:
    n1 = len(lst)
    lst[n1 - 1], lst[0] = lst[0], lst[n1 - 1]

    return lst


lst = [10, -5, 8, 3, -1, -9, 7, 2]
print(func(lst))
