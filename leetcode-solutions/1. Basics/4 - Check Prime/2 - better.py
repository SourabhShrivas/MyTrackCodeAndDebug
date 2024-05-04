"""https://www.naukri.com/code360/problems/check-prime_624934"""


def checkPrime(n: int):
    if n == 1:
        return False

    for i in range(2, int((n**0.5)) + 1):
        if n % i == 0:
            return False
    return True


if checkPrime(int(input())):
    print("YES")
else:
    print("NO")


"""
TC - O(SQRT (n)) where n is input integer
SC - O(1) - it uses a constant amount of additional space, regardless of the size of the input.
"""
