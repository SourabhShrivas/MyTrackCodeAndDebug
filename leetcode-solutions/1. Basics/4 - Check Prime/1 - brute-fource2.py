"""https://www.naukri.com/code360/problems/check-prime_624934"""


def countFactor(n: int) -> int:
    result = []
    for i in range(1, (int(n**0.5)) + 1):  # O(sqrt(n)
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)

    return len(result)


def checkPrime(n: int) -> str:
    if countFactor(n) == 2:
        return "YES"
    else:
        return "NO"


print(checkPrime(5))

"""
TC - O(SQRT (n)) where n is input integer
SC - O(SQRT (n)) - it creates a list result to store factors, 
     which could grow up to approximately 2√n elements in the worst case.
"""
