"""https://www.naukri.com/code360/problems/n-to-1-without-loop_8357243"""

from typing import List


# def printNos(x: int) -> List[int]:

#     if x > 0:
#         print(x, end=" ")
#         printNos(x - 1)


# printNos(5)


def printNos(n):
    if n == 1:
        return [1]
    else:
        return [n] + printNos(n - 1)


print(printNos(5))
