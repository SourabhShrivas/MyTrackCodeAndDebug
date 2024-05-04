"""https://www.naukri.com/code360/problems/check-prime_624934"""


def primeNumerCheck(n: int):
    factor = 0

    for i in range(1, n + 1):
        if n % i == 0:
            factor = factor + 1

    if factor == 2:
        print("YES")
    else:
        print("NO")


primeNumerCheck(37)

"""
TC - O(n) - This is because the function iterates through numbers from 1 to n to count the factors of n.
SC - O(1) - a constant amount of additional space regardless of the size of the input.
"""
