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
        rotations = k % len(nums)
        for i in range(rotations):  # O(k)
            # left rotate
            last = nums.pop()  # O(1)
            nums.insert(0, last)  # O(n)

            # right rotate
            # first = nums.pop(0)  # O(1)
            # nums.insert(len(nums), first)  # O(n)
        print(nums)


a = Solution()
nums = [1, 2, -100, 4.7, 5]
print(nums)
a.rotate(nums, 2)
"""
TC - O(k*n)
SC - O(1)
"""
