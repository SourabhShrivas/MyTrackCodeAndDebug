"""https://leetcode.com/problems/sort-colors/description/"""

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        low, mid, high = 0, 0, n - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low = low + 1
                mid = mid + 1
            elif nums[mid] == 1:
                mid = mid + 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high = high - 1


# Input:
# nums = [2, 0, 2, 1, 1, 0]  # this is working as expected/
nums = [2, 0, 1]  # this example is failing - need to check
# Output: [0,0,1,1,2,2]
a = Solution()
a.sortColors(nums)
print(nums)
"""'
TC = O(n)
SC = O(1)
"""
