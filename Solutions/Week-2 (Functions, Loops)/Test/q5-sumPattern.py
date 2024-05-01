# Q5. Make a function named sumPattern that takes an integer n as an argument from the user. And then calculate the sum of the following pattern.


def factorial(n: int):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


def sumPattern(num=int(input("Enther a number (enter 0 to finish): "))):
    i = num
    sum = 0
    while i > 0:
        sum = sum + factorial(i)
        i -= 1
    print(sum)


sumPattern()
