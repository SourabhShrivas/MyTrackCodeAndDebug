# Q4. Make a function named factorial(), which takes an integer n. Return the factorial of that number.


def factorial(n: int):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    print(result)


factorial(6)
