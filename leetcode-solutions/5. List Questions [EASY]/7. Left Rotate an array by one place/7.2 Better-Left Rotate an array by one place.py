"""
https://www.naukri.com/code360/problems/left-rotate-an-array-by-one_5026278
https://leetcode.com/problems/rotate-array/description/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        rotations = k % len(nums)
        nums[:] = (
            nums[n - rotations :] + nums[0 : n - rotations]
        )  # slicing takes O(n) TC
        print(nums)


a = Solution()
nums = [1, 2, -100, 4.7, 5]
a.rotate(nums, 2)
"""
TC - O(rotations) +O(n-rotations) ~ O(n)
SC - O(1)
"""
