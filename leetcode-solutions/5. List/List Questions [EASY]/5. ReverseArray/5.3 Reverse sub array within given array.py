# 5.3 Reverse sun array within given array.py

from typing import List


def reverse_sub_array(nums: List, start: int, end: int) -> List:
    n = len(nums)

    i, j = start, end

    while i < j:  # O(n) however technically/preslicely it runs n/2 ~ O(n/2)
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = j - 1
    return nums


nums = [1, 2, -100, 4.7, 5]
print(nums)
print(reverse_sub_array(nums, 1, 3))

"""
TC - O(n) however technically/preslicely it runs n/2 ~ O(n/2)
SC - O(1)
"""
