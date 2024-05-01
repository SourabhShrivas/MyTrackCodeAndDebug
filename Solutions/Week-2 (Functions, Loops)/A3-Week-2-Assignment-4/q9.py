# Q9. Ask a number from user. Print if that number is prime or not, use functions.
def prime(n: int):
    factor = 0
    for i in range(1, n + 1):
        if n % i == 0:
            factor += 1

    if factor == 2:
        print("Prime")
    else:
        print("Not Prime")


prime(115)
