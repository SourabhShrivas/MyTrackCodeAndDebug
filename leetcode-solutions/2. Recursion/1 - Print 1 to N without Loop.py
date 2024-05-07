"""https://www.naukri.com/code360/problems/print-1-to-n_628290"""

from typing import List


# def printNos(x: int) -> None:

#     if x > 0:
#         printNos(x - 1)
#         print(x, end=" ")

# printNos(5)


# def printNos(x: int):
#     result_lst = []
#     if x > 0:
#         printNos(x - 1)
#         result = result_lst.append(x)

#         # result_lst
#         print(result_lst)
#         # print(x, end=" ")
#     # return result_lst


# printNos(5)


def printNos(n):
    if n == 1:
        return [1]
    else:
        return printNos(n - 1) + [n]


print(printNos(5))
