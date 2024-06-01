"""
Find the first or last occurrence of a given number in a sorted array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""


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

        return lb
