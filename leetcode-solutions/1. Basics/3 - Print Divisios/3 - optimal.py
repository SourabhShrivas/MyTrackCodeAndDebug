'''"""https://www.naukri.com/code360/problems/print-all-divisors-of-a-number_1164188?leftPanelTabValue=PROBLEM"""
'''

from math import sqrt
from typing import List


def printDivisors(n: int) -> List[int]:
    result = []
    for i in range(1, (int(n**0.5)) + 1):  # O(sqrt(n)
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    result.sort()  # O(n log n)
    return result


"""
TC - O(sqrt(n) + n log n where n is the number
SC - O(sqrt(n)), where n is the number
"""
