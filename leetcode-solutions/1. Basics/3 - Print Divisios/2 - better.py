from typing import List


def printDivisors(n: int) -> List[int]:
    # Write your code here
    factor_list = []
    for i in range(1, int(n / 2 + 1)):  # O(n/2)
        if n % i == 0:
            factor_list.append(i)
    factor_list.append(n)

    return factor_list


print(printDivisors(36))

"""
Brute Force
TC - O(n/2) = O(n), where n is the number
SC - O(d), where d is the number of divisors of the input integer n
"""
