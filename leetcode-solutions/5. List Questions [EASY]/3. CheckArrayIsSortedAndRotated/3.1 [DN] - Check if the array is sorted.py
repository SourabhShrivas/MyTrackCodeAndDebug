"""
https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957
"""

# this optimal
# there no way to reduse TC and SC


def isSorted(n: int, arr: [int]) -> int:
    for i in range(n - 2):  # O(n-1) ~ 0(n)
        # print(arr[i])
        if arr[i] > arr[i + 1]:
            return 0
    return 1


n = 5
arr = [1, 2, 3, 4, 5]
# Output: 1

print(isSorted(n, arr))
"""
Time Complexity (TC): O(n)
Space Complexity (SC): O(1)
"""

"""https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/"""
