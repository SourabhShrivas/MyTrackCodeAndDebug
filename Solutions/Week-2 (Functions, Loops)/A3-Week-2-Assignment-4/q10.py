# Q10. Ask a number from user n1. From 1 to n1, print how many prime numbers are there.


def count_prime(n1: int):
    factors = 0
    count_prime = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            factors += 1

    if factors == 2:
        count_prime += 1
        print(f"Number of prime number : {count_prime}")
    else:
        print("Prime number not found")


count_prime(100)
