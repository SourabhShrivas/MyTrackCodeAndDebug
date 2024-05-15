"""
https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279
"""


# Methos 1
def largestElement_1(arr: [], n: int) -> int:
    # maxi = arr[0]
    maxi = float("-inf")

    for i in range(n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi


n = 5
arr = [1, 2, -100, 4.7, 5]
print(largestElement_1(arr, n))

"""
TC - O(n) - where n is number of elemets
SC - O(1) - using constant space
"""


# Methos 2
def largestElement_2(arr: [], n: int) -> int:
    # maxi = arr[0]
    maxi = float("-inf")

    for i in range(n):
        if arr[i] > maxi:
            maxi = max(maxi, arr[i])

    return maxi


n = 5
arr = [1, 2, -100, 4.7, 5]
print(largestElement_2(arr, n))
"""
TC - O(n) - where n is number of elemets
SC - O(1) - using constant space
"""
