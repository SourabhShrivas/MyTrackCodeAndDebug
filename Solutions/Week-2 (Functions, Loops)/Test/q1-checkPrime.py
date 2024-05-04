# Q1. Create a function named as checkPrime that takes an integer as an argument.
# Print YES if the number passed is a prime number else print NO.


def check_Prime(n: int):
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1

    if factor == 2:
        print("Yes")
    else:
        print("No")


check_Prime(7)
