from typing import List


def reverse_array(nums: List) -> List:
    n = len(nums)
    i, j = 0, n - 1

    while i < j:  # O(n) however technically/preslicely it runs n/2 ~ O(n/2)
        nums[i], nums[j] = nums[j], nums[i]
        i = i + 1
        j = j - 1
    return nums


nums = [1, 2, -100, 4.7, 5]
print(reverse_array(nums))

"""
TC - O(n) however technically/preslicely it runs n/2 ~ O(n/2)
SC - O(1)
"""
