# Q7. Create a function named as printPrimeFactors that takes an integer n as a argument and print all the prime factors of that number. Example if number = 20
# Then the factors of 20 are 1,2,5,10,20.So prime factors are 2,5 (this is the output)


def check_prime(n: int):
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1
    if factor == 2:
        return True
    else:
        return False


def printPrimeFactors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            if check_prime(i):
                print(i)


printPrimeFactors(7)
