"""implement lower bound index
find the smallest index such that arr[index] >= target
"""


def func(arr, target):
    n = len(arr)
    l = 0
    h = n - 1
    lb = n

    while l <= h:
        m = (l + h) // 2
        if arr[m] >= target:
            lb = m
            h = m - 1
        else:
            l = m + 1
    return lb


arr = [4, 6, 7, 7, 7, 8, 10, 10, 14, 19]
target = 7
print(func(arr, target))

"""
TC - O(log2N)
SC - O(1)
"""
