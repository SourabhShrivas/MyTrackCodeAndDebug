"""https://www.naukri.com/code360/problems/sum-of-all-divisors_8360720?leftPanelTabValue=PROBLEM"""


def sumOfDivisors(n: int) -> int:
    result = 0

    for i in range(1, (int(n**0.5)) + 1):  # O(sqrt(n))
        if n % i == 0:
            result = result + i
            if i != n // i:
                result = result + (n // i)
    return result


def sumOfAllDivisors(n: int) -> int:
    sum_of_devisior = 0

    for i in range(1, n + 1):
        sum_of_devisior = sum_of_devisior + sumOfDivisors(i)
    return sum_of_devisior


"""
TC = O(n) * O(sqrt(n))
SC = O(1) * O(1) 
"""
