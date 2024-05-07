"""https://www.naukri.com/code360/problems/reverse-an-array_8365444"""

from typing import *


# method 1
def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    if n == 0:
        return []
    else:
        if not nums:
            return nums
        return [nums.pop()] + reverseArray(n - 1, nums)


arr = [1, 2, 3, 4]
n = 4
# print(arr)
# print(arr.pop())
# print(arr)
print(reverseArray(n, arr))

"""
TC - O(n)
SC - O(n)
"""
"""-----------------------------------------------------------------"""


# method 2
def reverse_list(lst, start, end):
    if start > end:
        return
    lst[start], lst[end] = lst[end], lst[start]
    reverse_list(lst, start + 1, end - 1)


"""
TC - O(n)
SC - O(n)
"""
"""-----------------------------------------------------------------"""


# method 3
def revAr(arr, ind):
    n = len(arr)
    if ind == n // 2:
        print(arr)
        return
    arr[ind], arr[n - 1 - ind] = arr[n - 1 - ind], arr[ind]
    revAr(arr, ind + 1)


"""
TC - O(n)
SC - O(n)
"""
