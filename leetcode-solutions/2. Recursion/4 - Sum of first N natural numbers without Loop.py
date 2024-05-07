"""https://www.naukri.com/code360/problems/sum-of-first-n-numbers_8876068
"""

# from typing import List

# better
# def sumFirstN(n: int) -> int:
#     # Write your code here.
#     if n == 1:
#         return 1
#     return n + sumFirstN(n - 1)


# print(sumFirstN(10))
#  '''
#  Time complexity: O(n)
# Space complexity: O(n)
# '''

# better
# def sumFirstN(n: int) -> int:
#     # Write your code here.
#     sum = 0
#     for i in range(1, n + 1):
#         sum = sum + i
#     return sum


# print(sumFirstN(10))
# """
# Time complexity: O(n)
# Space complexity: O(1)
# """


# optimal
def sumFirstN(n: int) -> int:
    return int((n * (n + 1)) / 2)


print(sumFirstN(10))

"""
Time complexity: O(1) - math formulas have O(1) TS most fo the times.
Space complexity: O(1)
"""
