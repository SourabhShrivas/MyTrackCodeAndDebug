"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"""

"""remember INPLACE asked in question or else it can be run with """

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        my_dict = dict()  # O(n) SC

        for i in range(n):  # O(n) TC
            my_dict[nums[i]] = 0

        j = 0

        for key in my_dict:  # O(n) TC
            nums[j] = key
            j = j + 1

        return len(my_dict)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
a = Solution()
print(a.removeDuplicates(nums))

"""
TC - O(n) +  O(n) ~  O(2n)
SC - O(n)
"""
