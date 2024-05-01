# Q6. Create a function named sumOfSquares, which takes a single integer as a parameter named n. Return the sum of squares from 1 to n.


def sumOfSquares(n: int):
    sum = 0
    i = n
    while i > 0:
        sum = sum + i**2
        i -= 1
    print(sum)


sumOfSquares(5)
