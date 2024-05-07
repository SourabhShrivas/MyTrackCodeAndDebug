"""5 - Find factorial of a number with recursion.py"""


# method 1
def factorial(n: int) -> int:
    if (n == 1) or (n == 0):
        return 1
    else:
        return n * factorial(n - 1)


# print(factorial(5))
"""
Time complexity: O(n)
Space complexity: O(n)
"""
"""-----------------------------------------"""
# method 2
# from typing import

num = 1
ans = []


def factorialNumbers(n: int) -> List[int]:
    def facRecursion(i, nn):
        global num
        global ans
        num = num * i
        if num > n:
            return
        ans.append(num)
        facRecursion(i + 1, nn)

    facRecursion(1, n)
    return ans


print(factorialNumbers(5))
