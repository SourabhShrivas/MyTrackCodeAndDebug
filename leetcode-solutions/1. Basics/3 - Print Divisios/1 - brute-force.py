"""https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?leftPanelTabValue=PROBLEM"""

from typing import List


def printDivisors(n: int) -> List[int]:
    # Write your code here
    factor_list = []
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)

    return factor_list


print(printDivisors(5))

"""
Brute Force
TC - O(n), where n is the number
SC - O(d), where d is the number of divisors of the input integer n
"""
