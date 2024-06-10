"""https://leetcode.com/problems/two-sum/description/"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash_map = dict()

        for i in range(n):
            remaining = target - nums[i]
            if remaining in hash_map:
                return [hash_map[remaining], i]
            hash_map[nums[i]] = i


nums = [3, 2, 4]
target = 6
a = Solution()
print(a.twoSum(nums, target))
"""
Time Complexity (TC): O(n)
Space Complexity (SC): O(n)
"""
