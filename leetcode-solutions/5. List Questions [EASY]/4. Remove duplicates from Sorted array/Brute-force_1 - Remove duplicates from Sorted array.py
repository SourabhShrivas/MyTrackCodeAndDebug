"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"""

"""remember INPLACE asked in question or else it can be run with """

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        reverse_nums = []

        for i in range(n):  # o(n)
            if nums[i] not in reverse_nums:  # O(n)
                reverse_nums.append(nums[i])
        return len(reverse_nums)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
a = Solution()
print(a.removeDuplicates(nums))

"""
TC - O(n) *  O(n) ~  O(n^2)
SC - O(n)
"""
