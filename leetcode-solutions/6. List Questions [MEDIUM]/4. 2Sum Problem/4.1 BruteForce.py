"""https://leetcode.com/problems/two-sum/description/"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        for i in range(n):  # O(n)
            for j in range(i + 1, n):  # TS = sum of n naturals number
                if nums[i] + nums[j] == target:
                    return [i, j]


nums = [3, 2, 4]
target = 6
a = Solution()
print(a.twoSum(nums, target))
"""
TC - O(n^2)
SC - O(1)
"""
