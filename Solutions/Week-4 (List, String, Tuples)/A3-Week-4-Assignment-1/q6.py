# Q6. Write a program to remove the nth index
# element from a list using a function.

l1 = [34, 11, 91, 59, 33, 22]


def removeNth(lst, n):
    result = []
    if n > len(lst) - 1:
        print("Index does not exist")
    else:
        for index in range(0, len(lst)):
            if index != n:
                result.append(lst[index])
        return result


from typing import List


def removeNth(lst: List, n: int) -> None:
    lst.pop(n)


print(removeNth(l1, 67))
