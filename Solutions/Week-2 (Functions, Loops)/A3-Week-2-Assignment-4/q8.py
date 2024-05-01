# Q8. Write a function named pattern
# which accepts an integer n as an argument. Then print the following pattern.
# pattern (4)
# 1 4 9 16


def pattern_for(n: int):
    for i in range(1, n + 1):
        print(i**2, end=" ")


# pattern_for(10)


def pattern_while(n: int):
    i = 1
    while i <= n:
        print(i**2, end=" ")
        i += 1


pattern_while(10)
