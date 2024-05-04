import math


def CountDigit(num):
    return int(math.log10(num)) + 1


num = 5397
print(CountDigit(num))


"""
TC = O(1) where ni s the number
SC = O(1) - just storing one space as 
"""
