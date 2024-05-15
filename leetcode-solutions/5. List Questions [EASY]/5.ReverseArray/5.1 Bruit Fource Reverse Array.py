from typing import List


def reverse_array(nums: List) -> List:
    reverse = []

    for i in range(len(nums) - 1, -1, -1):  # O(n)
        reverse.append(nums[i])  # O(1)

    return reverse


nums = [1, 2, -100, 4.7, 5]
print(reverse_array(nums))

"""
TC - O(n)
SC - O(n)
"""
