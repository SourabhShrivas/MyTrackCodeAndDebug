"""https://leetcode.com/problems/majority-element/description/"""

from typing import List


def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):  # O(n)
        count = 0
        for j in range(n):
            if nums[i] == nums[j]:
                count = count + 1
                if count > n // 2:
                    return nums[i]
    return -1


nums = [3, 2, 3]
print(majorityElement(nums))

"""
Time Complexity (TC): O(n^2)
Space Complexity (SC): O(1)
"""
