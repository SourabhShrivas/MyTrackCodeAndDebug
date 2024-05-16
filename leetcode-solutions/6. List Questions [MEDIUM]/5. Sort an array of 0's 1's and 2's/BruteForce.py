"""https://leetcode.com/problems/sort-colors/description/"""


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()  # O(nlogn)


# Input:
nums = [2, 0, 2, 1, 1, 0]
# Output: [0,0,1,1,2,2]
a = Solution()
print(a.sortColors(nums))
"""'
TC = O(nlogn)
SC = O(1)
"""
