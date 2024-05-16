"""https://leetcode.com/problems/sort-colors/description/"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


# Input:
nums = [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]
a = Solution()
a.sortColors(nums)
print(nums)
"""'
TC = O(n)
SC = O(3)~O(1)
"""
