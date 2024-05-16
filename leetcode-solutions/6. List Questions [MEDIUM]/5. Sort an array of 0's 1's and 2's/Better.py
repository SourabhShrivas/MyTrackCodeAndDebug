"""https://leetcode.com/problems/sort-colors/description/"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt0 = nums.count(0)  # O(n)
        cnt1 = nums.count(1)  # O(n)
        cnt2 = nums.count(2)  # O(n)

        for i in range(0, cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1
        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2
        # O(n) for all three loops as it nums only for N times


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
