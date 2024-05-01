# Q6. Write a Python code to split a list into two halves using list slicing.
# (Keep the length of list even).


def func(lst) -> list:
    n = len(lst)
    l1 = lst[0 : n // 2]
    l2 = lst[(n // 2) + 1 :]

    return l1, l2


lst = [10, -5, 8, 3, -1, -9, 7, 2]
print(func(lst))
