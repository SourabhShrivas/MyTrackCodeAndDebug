# Create a function calculatePrime that
# accepts an List of Integers and print all the prime numbers in that list.


def checkprime(num: int) -> bool:
    factor = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor = factor + 1

    if factor == 2:
        # print(num)
        return True
    else:
        return False


def calculatePrime(lst: list) -> list:
    list_prime_numes = []
    for item in lst:
        if checkprime(item):
            list_prime_numes.append(item)
    return list_prime_numes


lst = [34, 11, 91, 59, 33, 22]
print(calculatePrime(lst))


#  print prime number from 1 to n
def listOfPrimeNums(n: int) -> list:
    result = []
    for i in range(1, n + 1):
        if checkprime(i):
            result.append(i)
    print(f"Prime number from 1 to {n} are : {result}")


listOfPrimeNums(100)
