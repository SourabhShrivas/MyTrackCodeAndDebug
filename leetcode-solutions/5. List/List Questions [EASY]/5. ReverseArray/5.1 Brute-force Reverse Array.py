from typing import List


def reverse_array(nums: List) -> List:
    reverse = []

    for i in range(len(nums) - 1, -1, -1):
        reverse.append(nums[i])

    return reverse


nums = [1, 2, -100, 4.7, 5]
print(reverse_array(nums))
