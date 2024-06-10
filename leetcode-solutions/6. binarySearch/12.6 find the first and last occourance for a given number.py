"""
Find the first or last occurrence of a given number in a sorted array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l, h = 0, n - 1
        lb = n
        ub = n

        while l <= h:
            m = (l + h) // 2
            if nums[m] >= target:
                lb = m
                h = m - 1
            else:
                l = m + 1

        while l <= h:
            m = (l + h) // 2
            if nums[m] > target:
                ub = m
                h = m - 1
            else:
                l = m + 1

        return [lb, ub]

        # return result


c = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
# nums = [1, 2, 4, 4, 4, 4, 4, 4, 4, 4, 8, 9, 9, 10]
# target = 4
print(c.searchRange(nums, target))
