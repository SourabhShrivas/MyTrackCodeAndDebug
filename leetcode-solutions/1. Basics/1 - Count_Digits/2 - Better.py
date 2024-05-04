def CountDigits(num):
    n = num
    count = 0  # SC = O(1)

    while n > 0:
        count = count + 1
        n = n // 10  # TC = O(log 10 n)
    return count


num = 121
print(CountDigits(num))


"""
TC = O(log 10 n) where ni s the number
SC = O(1) - just storing one space as 
"""
