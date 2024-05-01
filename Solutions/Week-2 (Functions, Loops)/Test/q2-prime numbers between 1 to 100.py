# Print all the prime numbers between 1 to 100.


def check_prime(n: int):
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            # print(i)
            factor += 1
    if factor == 2:
        return True
    else:
        return False


for i in range(1, 100 + 1):
    if check_prime(i):
        print(i, end=" ")

# print(check_prime(5))
