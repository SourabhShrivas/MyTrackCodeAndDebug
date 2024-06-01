"""
Search Insert Position
https://leetcode.com/problems/search-insert-position/description/
"""

"""intution - find the lower bound and if LB is = or greater then return 
either LB index or an index before"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, h = 0, n - 1
        lb = n

        while l <= h:
            m = (l + h) // 2
            if nums[m] >= target:
                lb = m
                h = m - 1
            else:
                l = m + 1
        return lb


# nums = [1, 3, 5, 6]
# target = 5

# nums = [1, 3, 5, 6]
# target = 2

nums = [1, 1, 3, 3, 3, 3, 5, 5, 6, 6, 6, 7]
target = 6

a = Solution()
print(a.searchInsert(nums, target))
