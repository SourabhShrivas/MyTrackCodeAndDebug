"""https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/"""

# hint - think abt break point and count then if > then 1 that means it not sorted after even rotating
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        rotation = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotation += 1
                if rotation > 1:
                    return False
        return True


nums = [2, 1, 3, 4]
# Output: true
a = Solution()
print(a.check(nums))
"""
TC - O(n)
Sc - O(1)
"""
