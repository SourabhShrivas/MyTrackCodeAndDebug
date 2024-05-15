"""https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/"""

"""intitution is that compare the consecutive elelemt using two pointer. 
when nums[i]=!nums[j] and swap and keep on swaping same element at the end 
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 1
        i = 0
        j = i + 1  # or i = 2
        while j < n:
            if nums[j] != nums[i]:
                i = i + 1
                nums[i], nums[j] = nums[j], nums[i]
            j = j + 1
        return i + 1
        # return nums


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: true
a = Solution()
print(a.removeDuplicates(nums))
