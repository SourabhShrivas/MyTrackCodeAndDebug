"""
https://leetcode.com/problems/binary-search/description/
- this will apply only in sorted array
- Integer overflow
"""


def func(arr, target):
    n = len(arr)
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


arr = [3, 6, 8, 9, 19, 29, 37]
target = 29
print(func(arr, target))

"""
TC - O(log2N)
SC - O(1)
"""
