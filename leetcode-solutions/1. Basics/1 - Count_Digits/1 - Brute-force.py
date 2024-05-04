def PrintDigit(n):
    m = str(n)  # O(n)

    for index in range(len(m) - 1, -1, -1):  # O(n)
        print(m[index])


n = 5397
PrintDigit(n)


"""
TC = O(n) + # O(n) = O(2n)
SC = O(n)
"""
